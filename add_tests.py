def add_all_lab_tests():
    all_tests = [
        # تحاليل دم
        {"name": "صورة دم كاملة (CBC)", "unit": "", "reference_range": "", "description": "تحليل مكونات الدم"},
        {"name": "هيموجلوبين", "unit": "g/dL", "reference_range": "13-17 (رجال) 12-15 (نساء)", "description": "قياس نسبة الهيموجلوبين"},
        {"name": "عدد كريات الدم البيضاء (WBC)", "unit": "10^3/uL", "reference_range": "4-11", "description": "قياس عدد كريات الدم البيضاء"},
        {"name": "عدد كريات الدم الحمراء (RBC)", "unit": "10^6/uL", "reference_range": "4.5-6.0", "description": "قياس عدد كريات الدم الحمراء"},
        {"name": "الهيماتوكريت (HCT)", "unit": "%", "reference_range": "40-54 (رجال) 36-48 (نساء)", "description": "قياس نسبة الهيماتوكريت"},
        {"name": "الصفائح الدموية (Platelets)", "unit": "10^3/uL", "reference_range": "150-400", "description": "قياس عدد الصفائح الدموية"},
        {"name": "ESR", "unit": "mm/hr", "reference_range": "< 20", "description": "معدل ترسيب كريات الدم الحمراء"},
        {"name": "CRP", "unit": "mg/L", "reference_range": "< 6", "description": "تحليل البروتين التفاعلي C"},
        {"name": "PT", "unit": "sec", "reference_range": "11-13.5", "description": "زمن البروثرومبين"},
        {"name": "INR", "unit": "", "reference_range": "0.8-1.2", "description": "النسبة المعيارية الدولية"},
        {"name": "APTT", "unit": "sec", "reference_range": "25-35", "description": "زمن الثرومبوبلاستين الجزئي"},
        # كيمياء حيوية
        {"name": "سكر صائم", "unit": "mg/dL", "reference_range": "70-110", "description": "قياس مستوى السكر بعد صيام 8 ساعات"},
        {"name": "سكر عشوائي", "unit": "mg/dL", "reference_range": "< 200", "description": "قياس مستوى السكر في أي وقت"},
        {"name": "HBA1C", "unit": "%", "reference_range": "4-6", "description": "تحليل السكر التراكمي"},
        {"name": "الكوليسترول الكلي", "unit": "mg/dL", "reference_range": "< 200", "description": "تحليل الكوليسترول"},
        {"name": "الدهون الثلاثية (Triglycerides)", "unit": "mg/dL", "reference_range": "< 150", "description": "تحليل الدهون الثلاثية"},
        {"name": "HDL", "unit": "mg/dL", "reference_range": "> 40", "description": "تحليل الكوليسترول الجيد"},
        {"name": "LDL", "unit": "mg/dL", "reference_range": "< 130", "description": "تحليل الكوليسترول الضار"},
        {"name": "وظائف كبد (ALT)", "unit": "U/L", "reference_range": "7-56", "description": "تحليل إنزيمات الكبد ALT"},
        {"name": "وظائف كبد (AST)", "unit": "U/L", "reference_range": "10-40", "description": "تحليل إنزيمات الكبد AST"},
        {"name": "GGT", "unit": "U/L", "reference_range": "9-48", "description": "تحليل إنزيم GGT"},
        {"name": "ALP", "unit": "U/L", "reference_range": "44-147", "description": "تحليل إنزيم ALP"},
        {"name": "البيليروبين الكلي", "unit": "mg/dL", "reference_range": "0.3-1.2", "description": "تحليل البيليروبين"},
        {"name": "وظائف كلى (Urea)", "unit": "mg/dL", "reference_range": "15-45", "description": "تحليل اليوريا"},
        {"name": "وظائف كلى (Creatinine)", "unit": "mg/dL", "reference_range": "0.6-1.3", "description": "تحليل الكرياتينين"},
        {"name": "حمض البوليك (Uric Acid)", "unit": "mg/dL", "reference_range": "3.4-7.0", "description": "تحليل حمض البوليك"},
        # أملاح ومعادن
        {"name": "الكالسيوم", "unit": "mg/dL", "reference_range": "8.5-10.5", "description": "قياس مستوى الكالسيوم"},
        {"name": "البوتاسيوم", "unit": "mmol/L", "reference_range": "3.5-5.1", "description": "قياس مستوى البوتاسيوم"},
        {"name": "الصوديوم", "unit": "mmol/L", "reference_range": "135-145", "description": "قياس مستوى الصوديوم"},
        {"name": "الفوسفور", "unit": "mg/dL", "reference_range": "2.5-4.5", "description": "قياس مستوى الفوسفور"},
        {"name": "المغنيسيوم", "unit": "mg/dL", "reference_range": "1.7-2.2", "description": "قياس مستوى المغنيسيوم"},
        # هرمونات
        {"name": "TSH", "unit": "uIU/mL", "reference_range": "0.4-4.0", "description": "تحليل هرمون الغدة الدرقية"},
        {"name": "T3", "unit": "ng/dL", "reference_range": "80-200", "description": "تحليل هرمون T3"},
        {"name": "T4", "unit": "mcg/dL", "reference_range": "5-12", "description": "تحليل هرمون T4"},
        {"name": "FSH", "unit": "mIU/mL", "reference_range": "1.5-12.4", "description": "تحليل هرمون FSH"},
        {"name": "LH", "unit": "mIU/mL", "reference_range": "1.7-8.6", "description": "تحليل هرمون LH"},
        {"name": "Prolactin", "unit": "ng/mL", "reference_range": "4.8-23.3", "description": "تحليل هرمون البرولاكتين"},
        {"name": "E2 (Estradiol)", "unit": "pg/mL", "reference_range": "15-350", "description": "تحليل هرمون الاستراديول"},
        {"name": "Testosterone", "unit": "ng/dL", "reference_range": "300-1000", "description": "تحليل هرمون التستوستيرون"},
        # فيتامينات
        {"name": "فيتامين D", "unit": "ng/mL", "reference_range": "20-50", "description": "قياس مستوى فيتامين D"},
        {"name": "فيتامين B12", "unit": "pg/mL", "reference_range": "200-900", "description": "قياس مستوى فيتامين B12"},
        # تحاليل مناعية وفيروسات
        {"name": "HBsAg", "unit": "", "reference_range": "سلبي/إيجابي", "description": "تحليل فيروس الكبد B"},
        {"name": "HCV Ab", "unit": "", "reference_range": "سلبي/إيجابي", "description": "تحليل فيروس الكبد C"},
        {"name": "HIV Ab", "unit": "", "reference_range": "سلبي/إيجابي", "description": "تحليل فيروس HIV"},
        {"name": "ASO", "unit": "IU/mL", "reference_range": "< 200", "description": "تحليل الأجسام المضادة للستربتوكوكاس"},
        {"name": "RF", "unit": "IU/mL", "reference_range": "< 20", "description": "تحليل عامل الروماتويد"},
        # تحاليل أورام
        {"name": "CEA", "unit": "ng/mL", "reference_range": "< 5", "description": "تحليل دلالات الأورام CEA"},
        {"name": "CA 19-9", "unit": "U/mL", "reference_range": "< 37", "description": "تحليل دلالات الأورام CA 19-9"},
        {"name": "CA 15-3", "unit": "U/mL", "reference_range": "< 30", "description": "تحليل دلالات الأورام CA 15-3"},
        {"name": "AFP", "unit": "ng/mL", "reference_range": "< 10", "description": "تحليل دلالات الأورام AFP"},
        {"name": "PSA", "unit": "ng/mL", "reference_range": "< 4", "description": "تحليل البروستاتا PSA"},
        # تحاليل بول وبراز
        {"name": "البول الكامل", "unit": "", "reference_range": "", "description": "تحليل البول الكامل"},
        {"name": "البراز الكامل", "unit": "", "reference_range": "", "description": "تحليل البراز الكامل"},
        {"name": "تحليل الحمل الرقمي (Beta HCG)", "unit": "mIU/mL", "reference_range": "< 5", "description": "تحليل الحمل الرقمي"},
        {"name": "تحليل البروتين في البول (Proteinuria)", "unit": "mg/dL", "reference_range": "< 150", "description": "قياس البروتين في البول"},
        # تحاليل بكتيريا وطفيليات
        {"name": "تحليل مزرعة بول", "unit": "", "reference_range": "", "description": "تحليل مزرعة البول"},
        {"name": "تحليل مزرعة براز", "unit": "", "reference_range": "", "description": "تحليل مزرعة البراز"},
        {"name": "تحليل مزرعة دم", "unit": "", "reference_range": "", "description": "تحليل مزرعة الدم"},
        # تحاليل أخرى
        {"name": "تحليل الحديد (Serum Iron)", "unit": "mcg/dL", "reference_range": "60-170", "description": "قياس مستوى الحديد في الدم"},
        {"name": "تحليل الفيريتين (Ferritin)", "unit": "ng/mL", "reference_range": "20-500", "description": "قياس مخزون الحديد"},
        {"name": "تحليل الليباز", "unit": "U/L", "reference_range": "0-160", "description": "قياس إنزيم الليباز"},
        {"name": "تحليل الأميليز", "unit": "U/L", "reference_range": "30-110", "description": "قياس إنزيم الأميليز"},
        {"name": "تحليل LDH", "unit": "U/L", "reference_range": "140-280", "description": "قياس إنزيم LDH"},
        {"name": "تحليل CK", "unit": "U/L", "reference_range": "20-200", "description": "قياس إنزيم CK"},
    ]
    for test in all_tests:
        TestCatalog.objects.get_or_create(
            name=test["name"],
            defaults={
                "unit": test["unit"],
                "reference_range": test["reference_range"],
                "description": test["description"]
            }
        )
from analyses.models import TestCatalog

def add_common_tests():
    tests = [
        {"name": "صورة دم كاملة (CBC)", "unit": "", "reference_range": "", "description": "تحليل مكونات الدم"},
        {"name": "سكر صائم", "unit": "mg/dL", "reference_range": "70-110", "description": "قياس مستوى السكر بعد صيام 8 ساعات"},
        {"name": "سكر عشوائي", "unit": "mg/dL", "reference_range": "< 200", "description": "قياس مستوى السكر في أي وقت"},
        {"name": "هيموجلوبين", "unit": "g/dL", "reference_range": "13-17 (رجال) 12-15 (نساء)", "description": "قياس نسبة الهيموجلوبين في الدم"},
        {"name": "وظائف كبد (ALT)", "unit": "U/L", "reference_range": "7-56", "description": "تحليل إنزيمات الكبد ALT"},
        {"name": "وظائف كبد (AST)", "unit": "U/L", "reference_range": "10-40", "description": "تحليل إنزيمات الكبد AST"},
        {"name": "وظائف كلى (Urea)", "unit": "mg/dL", "reference_range": "15-45", "description": "تحليل اليوريا"},
        {"name": "وظائف كلى (Creatinine)", "unit": "mg/dL", "reference_range": "0.6-1.3", "description": "تحليل الكرياتينين"},
        {"name": "حمض البوليك (Uric Acid)", "unit": "mg/dL", "reference_range": "3.4-7.0", "description": "تحليل حمض البوليك"},
        {"name": "الكوليسترول الكلي", "unit": "mg/dL", "reference_range": "< 200", "description": "تحليل الكوليسترول"},
        {"name": "الدهون الثلاثية (Triglycerides)", "unit": "mg/dL", "reference_range": "< 150", "description": "تحليل الدهون الثلاثية"},
        {"name": "TSH", "unit": "uIU/mL", "reference_range": "0.4-4.0", "description": "تحليل هرمون الغدة الدرقية"},
        {"name": "T3", "unit": "ng/dL", "reference_range": "80-200", "description": "تحليل هرمون T3"},
        {"name": "T4", "unit": "mcg/dL", "reference_range": "5-12", "description": "تحليل هرمون T4"},
        {"name": "البول الكامل", "unit": "", "reference_range": "", "description": "تحليل البول الكامل"},
        {"name": "البراز الكامل", "unit": "", "reference_range": "", "description": "تحليل البراز الكامل"},
        {"name": "ESR", "unit": "mm/hr", "reference_range": "< 20", "description": "معدل ترسيب كريات الدم الحمراء"},
        {"name": "CRP", "unit": "mg/L", "reference_range": "< 6", "description": "تحليل البروتين التفاعلي C"},
        {"name": "PT", "unit": "sec", "reference_range": "11-13.5", "description": "زمن البروثرومبين"},
        {"name": "INR", "unit": "", "reference_range": "0.8-1.2", "description": "النسبة المعيارية الدولية"},
    ]
    for test in tests:
        TestCatalog.objects.get_or_create(
            name=test["name"],
            defaults={
                "unit": test["unit"],
                "reference_range": test["reference_range"],
                "description": test["description"]
            }
        )


def add_extra_tests():
    extra_tests = [
        {"name": "تحليل فيتامين D", "unit": "ng/mL", "reference_range": "20-50", "description": "قياس مستوى فيتامين D"},
        {"name": "تحليل فيتامين B12", "unit": "pg/mL", "reference_range": "200-900", "description": "قياس مستوى فيتامين B12"},
        {"name": "تحليل الحديد (Serum Iron)", "unit": "mcg/dL", "reference_range": "60-170", "description": "قياس مستوى الحديد في الدم"},
        {"name": "تحليل الفيريتين (Ferritin)", "unit": "ng/mL", "reference_range": "20-500", "description": "قياس مخزون الحديد"},
        {"name": "تحليل الكالسيوم", "unit": "mg/dL", "reference_range": "8.5-10.5", "description": "قياس مستوى الكالسيوم"},
        {"name": "تحليل البوتاسيوم", "unit": "mmol/L", "reference_range": "3.5-5.1", "description": "قياس مستوى البوتاسيوم"},
        {"name": "تحليل الصوديوم", "unit": "mmol/L", "reference_range": "135-145", "description": "قياس مستوى الصوديوم"},
        {"name": "تحليل الفوسفور", "unit": "mg/dL", "reference_range": "2.5-4.5", "description": "قياس مستوى الفوسفور"},
        {"name": "تحليل المغنيسيوم", "unit": "mg/dL", "reference_range": "1.7-2.2", "description": "قياس مستوى المغنيسيوم"},
        {"name": "تحليل البروتين الكلي", "unit": "g/dL", "reference_range": "6-8.3", "description": "قياس مستوى البروتين الكلي"},
        {"name": "تحليل الألبومين", "unit": "g/dL", "reference_range": "3.5-5.5", "description": "قياس مستوى الألبومين"},
        {"name": "تحليل الجلوبولين", "unit": "g/dL", "reference_range": "2.0-3.5", "description": "قياس مستوى الجلوبولين"},
        {"name": "تحليل الليباز", "unit": "U/L", "reference_range": "0-160", "description": "قياس إنزيم الليباز"},
        {"name": "تحليل الأميليز", "unit": "U/L", "reference_range": "30-110", "description": "قياس إنزيم الأميليز"},
        {"name": "تحليل LDH", "unit": "U/L", "reference_range": "140-280", "description": "قياس إنزيم LDH"},
        {"name": "تحليل CK", "unit": "U/L", "reference_range": "20-200", "description": "قياس إنزيم CK"},
        {"name": "تحليل PSA", "unit": "ng/mL", "reference_range": "< 4", "description": "تحليل البروستاتا PSA"},
        {"name": "تحليل HBA1C", "unit": "%", "reference_range": "4-6", "description": "تحليل السكر التراكمي"},
        {"name": "تحليل الحمل الرقمي (Beta HCG)", "unit": "mIU/mL", "reference_range": "< 5", "description": "تحليل الحمل الرقمي"},
        {"name": "تحليل البروتين في البول (Proteinuria)", "unit": "mg/dL", "reference_range": "< 150", "description": "قياس البروتين في البول"},
    ]
    for test in extra_tests:
        TestCatalog.objects.get_or_create(
            name=test["name"],
            defaults={
                "unit": test["unit"],
                "reference_range": test["reference_range"],
                "description": test["description"]
            }
        )

