from decimal import Decimal
from django.db import models
from django.utils import timezone
from patients.models import Patient


# نموذج كتالوج التحاليل
class TestCatalog(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='صاحب التحليل',
        related_name='testcatalogs',
    )
    name = models.CharField(max_length=100, unique=True, verbose_name='اسم التحليل')
    unit = models.CharField(max_length=20, verbose_name='الوحدة', blank=True)
    reference_range = models.CharField(max_length=50, verbose_name='المدى المرجعي', blank=True)
    description = models.TextField(verbose_name='وصف التحليل', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='سعر التحليل', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'كاتالوج التحاليل'
        verbose_name_plural = 'كتالوج التحاليل'


# نموذج التحليل المرتبط بالمريض
class Analysis(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='analyses',
        verbose_name='المريض',
    )
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, verbose_name='المستخدم', related_name='analyses'
    )
    test = models.ForeignKey(TestCatalog, on_delete=models.CASCADE, verbose_name='نوع التحليل')
    result = models.CharField(max_length=255, verbose_name='النتيجة')
    notes = models.TextField(verbose_name='ملاحظات', blank=True)
    date = models.DateTimeField(verbose_name='تاريخ ووقت التحليل', auto_now_add=True)

    def __str__(self):
        return f"{self.test.name} - {self.patient.name}"

    class Meta:
        verbose_name = 'التحليل'
        verbose_name_plural = 'التحاليل'


# موديل وهمي لزر الاستعلام عن التحليل في القائمة الجانبية
class AnalysisResultsLink(models.Model):
    class Meta:
        verbose_name = 'الاستعلام عن التحليل'
        verbose_name_plural = 'الاستعلام عن التحليل'
        managed = False


class AnalysisRequest(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='analysis_requests',
        verbose_name='المريض',
    )
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, verbose_name='المستخدم', related_name='analysis_requests'
    )
    test = models.ForeignKey(TestCatalog, on_delete=models.CASCADE, verbose_name='نوع التحليل')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal('0.00'), verbose_name='السعر'
    )
    discount_percent = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal('0.00'), verbose_name='نسبة الخصم'
    )
    discount_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal('0.00'), verbose_name='قيمة الخصم'
    )
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal('0.00'), verbose_name='الإجمالي'
    )
    doctor = models.ForeignKey(
        'patients.Doctor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='الدكتور',
        related_name='analysis_requests'
    )
    date = models.DateTimeField(verbose_name='تاريخ ووقت الطلب', default=timezone.now)

    class Meta:
        verbose_name = 'طلب تحليل'
        verbose_name_plural = 'طلبات التحليل'

    def __str__(self):
        return f"طلب تحليل {self.test.name} - {self.patient.name}"

    def save(self, *args, **kwargs):
        # حساب قيمة الخصم والإجمالي قبل الحفظ
        try:
            self.discount_amount = (
                (self.price * self.discount_percent / Decimal('100.00')).quantize(Decimal('0.01'))
            )
            self.total = (self.price - self.discount_amount).quantize(Decimal('0.01'))
        except Exception:
            self.discount_amount = Decimal('0.00')
            self.total = self.price or Decimal('0.00')
        super().save(*args, **kwargs)

