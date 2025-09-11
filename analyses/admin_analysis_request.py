from django.contrib import admin
from .models_analysis_request import AnalysisRequest

@admin.register(AnalysisRequest)
class AnalysisRequestAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'test', 'created_at')
    search_fields = ('patient__name', 'doctor__name', 'test__name')
    autocomplete_fields = ['patient', 'doctor', 'test']
    list_filter = ('created_at',)
    ordering = ('-created_at',)
