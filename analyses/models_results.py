from django.db import models

class AnalysisResultsEntry(models.Model):
    class Meta:
        verbose_name = 'نتائج التحاليل'
        verbose_name_plural = 'نتائج التحاليل'
        managed = False
