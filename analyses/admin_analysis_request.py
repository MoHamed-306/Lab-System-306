from django.contrib import admin
from .models_analysis_request import AnalysisRequest

@admin.register(AnalysisRequest)
class AnalysisRequestAdmin(admin.ModelAdmin):
    exclude = ('user',)  # إخفاء خانة المستخدم من النموذج
    exclude = ('user',)  # إخفاء خانة المستخدم من النموذج
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
    list_display = ('patient', 'doctor', 'test', 'created_at') # لا يوجد user هنا
    search_fields = ('patient__name', 'doctor__name', 'test__name')
    autocomplete_fields = ['patient', 'doctor', 'test']
    list_filter = ('created_at',)
    ordering = ('-created_at',)
