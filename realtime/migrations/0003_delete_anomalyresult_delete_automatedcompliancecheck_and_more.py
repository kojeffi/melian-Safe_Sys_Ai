# Generated by Django 5.0.4 on 2024-04-27 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtime', '0002_anomalyresult_automatedcompliancecheck_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnomalyResult',
        ),
        migrations.DeleteModel(
            name='AutomatedComplianceCheck',
        ),
        migrations.DeleteModel(
            name='DataMiningAlgorithm',
        ),
        migrations.DeleteModel(
            name='NaturalLanguageProcessing',
        ),
        migrations.DeleteModel(
            name='PatternRecognition',
        ),
        migrations.DeleteModel(
            name='PredictiveMaintenance',
        ),
        migrations.DeleteModel(
            name='RiskPredictionModel',
        ),
    ]
