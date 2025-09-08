
from django.db import models


class Patient(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='المستخدم', related_name='patients')
	GENDER_CHOICES = [
		('M', 'ذكر'),
		('F', 'أنثى'),
	]
	name = models.CharField(max_length=100, verbose_name='الاسم')
	age = models.PositiveIntegerField(verbose_name='العمر')
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='النوع')
	from django.core.validators import RegexValidator
	national_id = models.CharField(
		max_length=14,
		verbose_name='الرقم القومي',
		unique=True,
		blank=True,
		null=True,
		help_text='أرقام فقط',
		validators=[RegexValidator(r'^\d+$', 'يجب إدخال أرقام فقط بدون حروف')]
	)
	doctor_name = models.CharField(max_length=100, verbose_name='اسم الدكتور', blank=True)
	phone = models.CharField(max_length=20, verbose_name='رقم الهاتف')
	address = models.CharField(max_length=255, verbose_name='العنوان', blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')

	def __str__(self):
		return self.name
