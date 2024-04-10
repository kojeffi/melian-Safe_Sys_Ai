from django.db import models


class AIDrivenSafetyManagement(models.Model):
    description = models.TextField()
    chart_data = models.JSONField(blank=True, null=True)
    data_entry = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description
