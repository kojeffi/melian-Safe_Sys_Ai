from django.contrib import admin
from.models import SafetyRisk,EquipmentMaintenance,ComplianceRegulation

# Register your models here.
admin.site.register(SafetyRisk)
admin.site.register(ComplianceRegulation)
admin.site.register(EquipmentMaintenance)