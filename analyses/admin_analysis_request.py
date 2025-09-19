from django.contrib import admin
from .models import AnalysisRequest

@admin.register(AnalysisRequest)
class AnalysisRequestAdmin(admin.ModelAdmin):
    exclude = ('user',)  # إخفاء خانة المستخدم من النموذج
    # ضع ترتيب الحقول صراحةً ليظهر حقل الدكتور أسفل حقل نوع التحليل
    fields = ('patient', 'test', 'doctor', 'price', 'discount_percent', 'discount_amount', 'total', 'date')
    readonly_fields = ('discount_amount', 'total')  # الحقول المحسوبة للقراءة فقط
    class Media:
        js = ('analyses/auto_fill_price.js',)

    # تم حذف تعيين user حتى لا تظهر خانة اسم المستخدم في شاشة الطلبات
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(patient__user=request.user)
    # عدّل عرض الحقول والتصفية لتطابق حقول AnalysisRequest الفعلية
    list_display = ('patient', 'test', 'price', 'date')
    search_fields = ('patient__name', 'test__name')
    autocomplete_fields = ['patient', 'test']
    list_filter = ('date',)
    ordering = ('-date',)
