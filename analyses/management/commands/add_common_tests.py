from django.core.management.base import BaseCommand
from analyses.models import TestCatalog

# قائمة أشهر التحاليل الطبية مع بياناتها
TESTS = [
    # اسم التحليل، الوحدة، المدى المرجعي، الوصف
    ("CBC", "", "حسب العمر والجنس", "صورة دم كاملة"),
    ("FBS", "mg/dL", "70-110", "سكر صائم"),
    ("PPBS", "mg/dL", "<140", "سكر بعد الأكل بساعتين"),
    ("RBS", "mg/dL", "70-140", "سكر عشوائي"),
    ("HbA1c", "%", "4-6", "سكر تراكمي"),
    ("Urea", "mg/dL", "15-45", "يوريا"),
    ("Creatinine", "mg/dL", "0.6-1.3", "كرياتينين"),
    ("Uric Acid", "mg/dL", "3.5-7.2", "حمض اليوريك"),
    ("SGPT (ALT)", "U/L", "7-56", "إنزيم الكبد ALT"),
    ("SGOT (AST)", "U/L", "8-48", "إنزيم الكبد AST"),
    ("ALP", "U/L", "44-147", "الفوسفاتاز القلوي"),
    ("Total Bilirubin", "mg/dL", "0.1-1.2", "بيليروبين كلي"),
    ("Direct Bilirubin", "mg/dL", "0-0.3", "بيليروبين مباشر"),
    ("Albumin", "g/dL", "3.4-5.4", "ألبومين"),
    ("Total Protein", "g/dL", "6-8.3", "بروتين كلي"),
    ("Cholesterol", "mg/dL", "<200", "كوليسترول كلي"),
    ("Triglycerides", "mg/dL", "<150", "دهون ثلاثية"),
    ("HDL", "mg/dL", ">40", "الكوليسترول الجيد"),
    ("LDL", "mg/dL", "<130", "الكوليسترول الضار"),
    ("Calcium", "mg/dL", "8.5-10.2", "كالسيوم"),
    ("Phosphorus", "mg/dL", "2.5-4.5", "فوسفور"),
    ("Sodium", "mmol/L", "135-145", "صوديوم"),
    ("Potassium", "mmol/L", "3.5-5.1", "بوتاسيوم"),
    ("Chloride", "mmol/L", "98-107", "كلوريد"),
    ("TSH", "uIU/mL", "0.4-4.0", "هرمون الغدة الدرقية المحفز"),
    ("T3", "ng/dL", "80-200", "هرمون T3"),
    ("T4", "ug/dL", "5-12", "هرمون T4"),
    ("CRP", "mg/L", "<5", "بروتين سي التفاعلي"),
    ("ESR", "mm/hr", "<20", "سرعة ترسيب الدم"),
    ("Widal Test", "", "سلبي/إيجابي", "اختبار التيفويد"),
    ("ASO Titer", "IU/mL", "<200", "مضاد الستربتوليزين"),
    ("RF", "IU/mL", "<14", "عامل الروماتويد"),
    ("HCV Ab", "", "سلبي/إيجابي", "أجسام مضادة لفيروس سي"),
    ("HBsAg", "", "سلبي/إيجابي", "مستضد التهاب الكبد B"),
    ("Pregnancy Test", "", "سلبي/إيجابي", "اختبار حمل"),
    ("Urine Analysis", "", "", "تحليل بول كامل"),
    ("Stool Analysis", "", "", "تحليل براز كامل"),
    ("Blood Group", "", "A/B/AB/O +ve/-ve", "فصيلة الدم"),
]

class Command(BaseCommand):
    help = 'إضافة أشهر التحاليل الطبية تلقائيًا في TestCatalog'

    def handle(self, *args, **kwargs):
        for name, unit, ref, desc in TESTS:
            obj, created = TestCatalog.objects.get_or_create(
                name=name,
                defaults={
                    'unit': unit,
                    'reference_range': ref,
                    'description': desc,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'تمت إضافة: {name}'))
            else:
                self.stdout.write(f'موجود بالفعل: {name}')
