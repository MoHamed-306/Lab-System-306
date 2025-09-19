from .forms import NationalIDForm
from patients.models import Patient
# شاشة نتائج التحاليل حسب الرقم القومي
def analysis_results(request):
	message = None
	analyses = None
	patient = None
	form = NationalIDForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		national_id = form.cleaned_data['national_id']
		try:
			patient = Patient.objects.get(national_id=national_id, user=request.user)
		except Patient.DoesNotExist:
			message = 'لا يوجد مريض بهذا الرقم القومي، أو ليس لديك صلاحية الوصول إليه.'
			patient = None
		if patient:
			analyses = patient.analyses.filter(user=request.user).order_by('-date')
			if not analyses.exists():
				message = 'لم يتم الانتهاء من أي تحليل لهذا المريض بعد.'
	return render(request, 'analyses/analysis_results.html', {'form': form, 'message': message, 'analyses': analyses, 'patient': patient})

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Analysis
from django.template.loader import render_to_string
import weasyprint
from django.http import JsonResponse
from .models import TestCatalog

# عرض صفحة تقرير التحليل مع زر الطباعة وحفظ PDF
def analysis_report(request, analysis_id):
	analysis = get_object_or_404(Analysis, id=analysis_id)
	return render(request, 'analyses/analysis_report.html', {'analysis': analysis})

# حفظ التقرير كـ PDF
def analysis_pdf(request, analysis_id):
	analysis = get_object_or_404(Analysis, id=analysis_id)
	html = render_to_string('analyses/analysis_report.html', {'analysis': analysis})
	pdf = weasyprint.HTML(string=html).write_pdf()
	response = HttpResponse(pdf, content_type='application/pdf')
	response['Content-Disposition'] = f'attachment; filename="analysis_{analysis_id}.pdf"' 
	return response


def test_price(request, test_id):
	"""Return JSON with the price for a TestCatalog item."""
	try:
		test = TestCatalog.objects.get(id=test_id)
		return JsonResponse({'price': str(test.price)})
	except TestCatalog.DoesNotExist:
		return JsonResponse({'price': None}, status=404)
