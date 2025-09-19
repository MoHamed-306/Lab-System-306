from django.urls import path
from . import views

urlpatterns = [
    path('analysis/<int:analysis_id>/report/', views.analysis_report, name='analysis_report'),
    path('analysis/<int:analysis_id>/pdf/', views.analysis_pdf, name='analysis_pdf'),
    path('results/', views.analysis_results, name='analysis_results'),
    path('test-price/<int:test_id>/', views.test_price, name='test_price'),
]
