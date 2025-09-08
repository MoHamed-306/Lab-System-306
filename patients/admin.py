from django.contrib import admin
from .models import Patient
from django.utils.html import format_html
from django.urls import reverse

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
	list_display = ('name', 'age', 'gender_colored', 'national_id', 'doctor_name', 'phone', 'address', 'created_at')
	search_fields = ('name', 'phone', 'address', 'national_id', 'doctor_name')
	list_filter = ('gender', 'created_at')
	ordering = ('-created_at',)
	fieldsets = (
		('البيانات الأساسية', {
			'fields': ('name', 'age', 'gender', 'national_id', 'doctor_name')
		}),
		('معلومات التواصل', {
			'fields': ('phone', 'address')
		}),
		('تاريخ الإنشاء', {
			'fields': ('created_at',),
			'classes': ('collapse',)
		}),
	)
	readonly_fields = ('created_at',)

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(user=request.user)

	def save_model(self, request, obj, form, change):
		if not change:
			obj.user = request.user
		super().save_model(request, obj, form, change)

	def gender_colored(self, obj):
		return dict(obj.GENDER_CHOICES).get(obj.gender, '-')
	gender_colored.short_description = 'النوع'

	def doctor_name(self, obj):
		return obj.doctor_name
	doctor_name.short_description = 'اسم الدكتور'

