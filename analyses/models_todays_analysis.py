from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from analyses.models import AnalysisRequest

class TodaysAnalysis(models.Model):
    request = models.OneToOneField(AnalysisRequest, on_delete=models.CASCADE, verbose_name='طلب التحليل', related_name='todays_analysis')
    is_done = models.BooleanField(default=False, verbose_name='تم التنفيذ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')

    def __str__(self):
        return f"تحليل اليوم: {self.request}"

    class Meta:
        verbose_name = 'تحليل اليوم'
        verbose_name_plural = 'تحاليل اليوم'


# Signal: create TodaysAnalysis automatically when AnalysisRequest is created
@receiver(post_save, sender=AnalysisRequest)
def create_todays_analysis(sender, instance, created, **kwargs):
    from .models_todays_analysis import TodaysAnalysis
    if created:
        # AnalysisRequest no longer has `created_at`; use its `date` field instead for the default
        TodaysAnalysis.objects.get_or_create(request=instance, defaults={"created_at": instance.date})
