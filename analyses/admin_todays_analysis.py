from django.contrib import admin
from .models_todays_analysis import TodaysAnalysis
from .models_analysis_request import AnalysisRequest
from .models import Analysis
from django.urls import reverse
from django.utils.html import format_html
from django.utils import timezone
from django.urls import reverse
from django.utils.safestring import mark_safe

@admin.register(TodaysAnalysis)
class TodaysAnalysisAdmin(admin.ModelAdmin):
    change_list_template = "analyses/todays_analysis_changelist.html"
    def get_queryset(self, request):
        import datetime
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        date_str = request.GET.get('date')
        if date_str:
            try:
                current_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            except Exception:
                current_date = timezone.localdate()
        else:
            current_date = timezone.localdate()
        # تصفية حسب اليوم والمستخدم الحالي
        qs = qs.filter(created_at__date=current_date, request__user=request.user).select_related('request__patient', 'request__test', 'request__doctor')
        # ترقيم الصفوف تسلسلي
        for idx, obj in enumerate(qs, 1):
            obj._row_number = idx
        return qs
    def changelist_view(self, request, extra_context=None):
        import datetime
        date_str = request.GET.get('date')
        if date_str:
            try:
                current_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            except Exception:
                current_date = timezone.localdate()
        else:
            current_date = timezone.localdate()

        prev_date = current_date - datetime.timedelta(days=1)
        next_date = current_date + datetime.timedelta(days=1)
        prev_url = f"?date={prev_date}"
        next_url = f"?date={next_date}"

        extra_context = extra_context or {}
        extra_context['current_date'] = current_date
        extra_context['prev_url'] = prev_url
        extra_context['next_url'] = next_url
        extra_context['highlight_done'] = True
        return super().changelist_view(request, extra_context=extra_context)
    def has_add_permission(self, request):
        return False
    def get_row_css(self, obj, index):
        return 'row-is-done' if obj.is_done else ''

    def get_changelist(self, request, **kwargs):
        from django.contrib.admin.views.main import ChangeList
        class CustomChangeList(ChangeList):
            def get_results(self, *args, **kwargs):
                super().get_results(*args, **kwargs)
                for i, result in enumerate(self.result_list):
                    row_class = self.model_admin.get_row_css(result, i)
                    if row_class:
                        if not hasattr(result, 'admin_row_class'):
                            result.admin_row_class = row_class
        return CustomChangeList
    list_display = ('patient', 'test', 'doctor', 'is_done', 'created_at', 'print_pdf')

    # ...existing code...

    def print_pdf(self, obj):
        # رابط طباعة/تنزيل PDF لنفس المريض والتحليل
        try:
            analysis = Analysis.objects.filter(patient=obj.request.patient, test=obj.request.test).latest('date')
            report_url = f"/analyses/analysis/{analysis.id}/report/"
            pdf_url = f"/analyses/analysis/{analysis.id}/pdf/"
            return format_html('<a href="{}" target="_blank">طباعة</a> | <a href="{}" target="_blank">PDF</a>', report_url, pdf_url)
        except Exception:
            return '-'
    print_pdf.short_description = 'طباعة / PDF'
    actions = None
    class Media:
        css = {
            'all': ('analyses/css/todays_analysis_admin.css',)
        }




    list_filter = ('is_done', 'created_at')
    search_fields = ('request__patient__name', 'request__test__name', 'request__doctor__name')
    ordering = ('-created_at',)

    def patient(self, obj):
        # إذا كان هناك تحليل منفذ لهذا المريض وهذا التحليل، يفتح شاشة التعديل (change)، وإلا يفتح شاشة إضافة تحليل
        analysis = Analysis.objects.filter(patient=obj.request.patient, test=obj.request.test).order_by('-date').first()
        if analysis:
            url = reverse('admin:analyses_analysis_change', args=[analysis.id])
            return format_html('<a href="{}">{}</a>', url, obj.request.patient)
        else:
            url = reverse('admin:analyses_analysis_add') + f'?patient={obj.request.patient.id}&test={obj.request.test.id}'
            return format_html('<a href="{}">{}</a>', url, obj.request.patient)
    def test(self, obj):
        return obj.request.test
    def doctor(self, obj):
        return obj.request.doctor


