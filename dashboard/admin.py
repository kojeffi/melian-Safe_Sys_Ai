from django.contrib import admin
from.models import SafetyIncident,ComplianceRegulation,EquipmentMaintenance

# Register your models here.
admin.site.register(SafetyIncident)
admin.site.register(ComplianceRegulation)
admin.site.register(EquipmentMaintenance)