from django.shortcuts import render
from django.http import JsonResponse
from .forms import SafetyRiskForm, ComplianceRegulationForm, EquipmentMaintenanceForm
from .models import AnomalyResult
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.preprocessing import StandardScaler


def anomaly_detection(request):
    if request.method == 'POST':
        form = SafetyRiskForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                uploaded_file = request.FILES['file']
                operational_data = pd.read_csv(uploaded_file, parse_dates=['timestamp'])
                operational_data['timestamp'] = operational_data['timestamp'].apply(lambda x: x.timestamp())
            except KeyError:
                # Handle case where 'timestamp' column is missing in the uploaded file
                error_message = "The uploaded file does not contain a 'timestamp' column."
                return render(request, 'dashbord/realtime.html', {'form': form, 'error_message': error_message})
            except Exception as e:
                # Handle other exceptions
                error_message = f"An error occurred while processing the file: {str(e)}"
                return render(request, 'dashbord/realtime.html', {'form': form, 'error_message': error_message})

            # Continue with anomaly detection process
            X_train, X_test = train_test_split(operational_data, test_size=0.2, random_state=42)
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)
            iforest = IsolationForest(contamination=0.1)
            iforest.fit(X_train_scaled)
            anomaly_preds = iforest.predict(X_test_scaled)
            anomaly_results = []
            for index, prediction in enumerate(anomaly_preds):
                if prediction == -1:
                    anomaly_result = {
                        'risk_name': f"Anomaly detected in operational data {X_test.iloc[index].name}",
                        'risk_description': "Anomaly detected in operational data",
                        'risk_level': 1,  # Adjust based on severity
                        'risk_category': "Anomaly",
                    }
                    anomaly_results.append(anomaly_result)
            return render(request, 'dashbord/realtime.html', {'form': form, 'anomaly_results': anomaly_results})
    else:
        form = SafetyRiskForm()
    return render(request, 'dashbord/realtime.html', {'form': form})


from django.shortcuts import render
from .forms import EquipmentMaintenanceForm
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def predictive_maintenance(request):
    if request.method == 'POST':
        form = EquipmentMaintenanceForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                uploaded_file = request.FILES['file']
                equipment_data = pd.read_csv(uploaded_file)
                columns_to_drop = ['UDI', 'Product ID', 'Type']  # Remove non-relevant columns
                X = equipment_data.drop(columns=columns_to_drop, axis=1)
                y = equipment_data['Machine failure']  # Target variable
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
                rf_classifier.fit(X_train, y_train)
                maintenance_preds = rf_classifier.predict(X_test)
                maintenance_results = []
                for index, prediction in enumerate(maintenance_preds):
                    maintenance_result = {
                        'equipment_name': X_test.index[index],
                        'maintenance_schedule': "2024-04-13",
                        'maintenance_description': "Predictive maintenance required" if prediction else "No maintenance required",
                    }
                    maintenance_results.append(maintenance_result)

                # Debugging: Print maintenance results
                print("Maintenance Results:", maintenance_results)

                return render(request, 'dashbord/predict.html',
                              {'form': form, 'maintenance_results': maintenance_results})
            except Exception as e:
                # Error handling: Handle any exceptions
                error_message = f"An error occurred: {str(e)}"
                print("Error:", error_message)
                return render(request, 'dashbord/predict.html', {'form': form, 'error_message': error_message})
    else:
        form = EquipmentMaintenanceForm()

    # Debugging: Print form data
    print("Form:", form)

    return render(request, 'dashbord/predict.html', {'form': form})


def anomaly_results_api(request):
    if request.method == 'POST':
        # Handle POST request to store anomaly results in the database if necessary
        pass
    else:
        # Fetch anomaly detection results from the database
        anomaly_results = AnomalyResult.objects.all().values('label', 'value')
        return JsonResponse(list(anomaly_results), safe=False)





# views.py
from django.shortcuts import render, redirect
from .forms import SafetyRiskForm, ComplianceRegulationForm, EquipmentMaintenanceForm
from .models import SafetyRisk, ComplianceRegulation, EquipmentMaintenance

def real(request):
    safety_risks = SafetyRisk.objects.all()
    compliance_regulations = ComplianceRegulation.objects.all()
    equipment_maintenance = EquipmentMaintenance.objects.all()

    safety_risk_form = SafetyRiskForm(request.POST or None)
    compliance_regulation_form = ComplianceRegulationForm(request.POST or None)
    equipment_maintenance_form = EquipmentMaintenanceForm(request.POST or None)

    if request.method == 'POST':
        if safety_risk_form.is_valid():
            safety_risk_form.save()
            return redirect('realtime:real-url')
        elif compliance_regulation_form.is_valid():
            compliance_regulation_form.save()
            return redirect('realtime:real-url')
        elif equipment_maintenance_form.is_valid():
            equipment_maintenance_form.save()
            return redirect('realtime:real-url')

    context = {
        'safety_risks': safety_risks,
        'compliance_regulations': compliance_regulations,
        'equipment_maintenance': equipment_maintenance,
        'safety_risk_form': safety_risk_form,
        'compliance_regulation_form': compliance_regulation_form,
        'equipment_maintenance_form': equipment_maintenance_form,
    }
    return render(request, 'dashbord/realtime.html', context)