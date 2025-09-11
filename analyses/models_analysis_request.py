from django.db import models
from patients.models import Patient
from patients.models_doctor import Doctor
from analyses.models import TestCatalog

class AnalysisRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='المريض', related_name='analysis_requests')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='الدكتور', related_name='analysis_requests')
    test = models.ForeignKey(TestCatalog, on_delete=models.CASCADE, verbose_name='نوع التحليل', related_name='analysis_requests')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الطلب')

    def __str__(self):
        return f"طلب تحليل: {self.patient} - {self.test} - {self.doctor}"
