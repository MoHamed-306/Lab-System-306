from django.db import models

class Doctor(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='المستخدم', related_name='doctors', null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='اسم الدكتور')
    specialty = models.CharField(max_length=100, verbose_name='التخصص')
    phone = models.CharField(max_length=20, verbose_name='رقم التليفون')
    address = models.CharField(max_length=255, verbose_name='العنوان', blank=True)

    def __str__(self):
        return f"{self.name} - {self.specialty}"

    class Meta:
        verbose_name = 'الطبيب'
        verbose_name_plural = 'الأطباء'
