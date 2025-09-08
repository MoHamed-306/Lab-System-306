from django.contrib import admin
from django.db import models
from .models import Analysis, TestCatalog, AnalysisResultsLink

@admin.register(TestCatalog)
class TestCatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit', 'reference_range', 'description')
    search_fields = ('name',)
    exclude = ('user',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Mohamed306 يرى كل شيء، الباقي يرون العام وتحاليلهم فقط
        return qs.filter(
            models.Q(user=None) |
            models.Q(user__username='Mohamed306') |
            models.Q(user=request.user)
        )

    def save_model(self, request, obj, form, change):
        if not change:
            # إذا كان المستخدم Mohamed306 أو مشرف، التحليل عام
            if request.user.is_superuser or request.user.username == 'Mohamed306':
                obj.user = None
            else:
                obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    list_display = ('test_name', 'patient', 'result', 'unit', 'reference_range', 'date', 'print_actions')
    search_fields = ('test__name', 'patient__name', 'result')
    list_filter = ('date', 'test')
    autocomplete_fields = ['patient', 'test']
    exclude = ('user',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def test_name(self, obj):
        return obj.test.name
    test_name.short_description = 'اسم التحليل'

    def unit(self, obj):
        return obj.test.unit
    unit.short_description = 'الوحدة'

    def reference_range(self, obj):
        return obj.test.reference_range
    reference_range.short_description = 'المدى المرجعي'

    def print_actions(self, obj):
        from django.utils.html import format_html
        report_url = f"/analyses/analysis/{obj.id}/report/"
        pdf_url = f"/analyses/analysis/{obj.id}/pdf/"
        return format_html(
            '<a href="{}" target="_blank">طباعة</a> | <a href="{}" target="_blank">PDF</a>',
            report_url, pdf_url
        )
    print_actions.short_description = 'خيارات الطباعة'

# زر الاستعلام عن التحليل في القائمة الجانبية
@admin.register(AnalysisResultsLink)
class AnalysisResultsLinkAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect('/analyses/results/')

    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
