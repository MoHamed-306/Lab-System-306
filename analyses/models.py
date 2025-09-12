
from django.db import models
from django.db import models
from patients.models import Patient


# نموذج كتالوج التحاليل
class TestCatalog(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='صاحب التحليل', related_name='testcatalogs')
	name = models.CharField(max_length=100, unique=True, verbose_name='اسم التحليل')
	unit = models.CharField(max_length=20, verbose_name='الوحدة', blank=True)
	reference_range = models.CharField(max_length=50, verbose_name='المدى المرجعي', blank=True)
	description = models.TextField(verbose_name='وصف التحليل', blank=True)
	price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='سعر التحليل', default=0)

	def __str__(self):
		return self.name

# نموذج التحليل المرتبط بالمريض
class Analysis(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='analyses', verbose_name='المريض')
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='المستخدم', related_name='analyses')
	test = models.ForeignKey(TestCatalog, on_delete=models.CASCADE, verbose_name='نوع التحليل')
	result = models.CharField(max_length=255, verbose_name='النتيجة')
	notes = models.TextField(verbose_name='ملاحظات', blank=True)
	date = models.DateTimeField(verbose_name='تاريخ ووقت التحليل', auto_now_add=True)

	# حقول القيم الفرعية لتحليل CBC
	hgb = models.CharField("Hemoglobin (Hgb)", max_length=20, blank=True, null=True)
	rbcs = models.CharField("Red blood cells (RBCs)", max_length=20, blank=True, null=True)
	hct = models.CharField("HCT", max_length=20, blank=True, null=True)
	hgb_percent = models.CharField("Hgb%", max_length=20, blank=True, null=True)
	mcv = models.CharField("MCV", max_length=20, blank=True, null=True)
	mch = models.CharField("MCH", max_length=20, blank=True, null=True)
	mchc = models.CharField("MCHC", max_length=20, blank=True, null=True)
	rdw_cv = models.CharField("RDW-cv", max_length=20, blank=True, null=True)
	plt = models.CharField("Platelets (PLT)", max_length=20, blank=True, null=True)
	wbc = models.CharField("White blood cells (WBCs)", max_length=20, blank=True, null=True)
	# Differential Count
	neutrophils = models.CharField("Neutrophils", max_length=20, blank=True, null=True)
	band = models.CharField("Band", max_length=20, blank=True, null=True)
	segmented = models.CharField("Segmented", max_length=20, blank=True, null=True)
	lymphocytes = models.CharField("Lymphocytes", max_length=20, blank=True, null=True)
	monocytes = models.CharField("Monocytes", max_length=20, blank=True, null=True)
	eosinophil = models.CharField("Eosinophil", max_length=20, blank=True, null=True)
	basophils = models.CharField("Basophils", max_length=20, blank=True, null=True)
	# التعليق
	comment = models.TextField("Comment", blank=True, null=True)

	def __str__(self):
		return f"{self.test.name} - {self.patient.name}"

# موديل وهمي لزر الاستعلام عن التحليل في القائمة الجانبية
class AnalysisResultsLink(models.Model):
    class Meta:
        verbose_name = 'الاستعلام عن التحليل'
        verbose_name_plural = 'الاستعلام عن التحليل'
        managed = False

