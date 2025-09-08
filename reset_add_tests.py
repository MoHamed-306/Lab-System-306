from analyses.models import TestCatalog

try:
    TestCatalog.objects.all().delete()
    tests = [
        {"name": "صورة دم كاملة (CBC)", "unit": "", "reference_range": "", "description": "تحليل مكونات الدم"},
        {"name": "سكر صائم", "unit": "mg/dL", "reference_range": "70-110", "description": "قياس مستوى السكر بعد صيام 8 ساعات"},
        {"name": "سكر عشوائي", "unit": "mg/dL", "reference_range": "< 200", "description": "قياس مستوى السكر في أي وقت"},
        {"name": "هيموجلوبين", "unit": "g/dL", "reference_range": "13-17 (رجال) 12-15 (نساء)", "description": "قياس نسبة الهيموجلوبين في الدم"},
        {"name": "وظائف كبد (ALT)", "unit": "U/L", "reference_range": "7-56", "description": "تحليل إنزيمات الكبد ALT"},
        {"name": "وظائف كبد (AST)", "unit": "U/L", "reference_range": "10-40", "description": "تحليل إنزيمات الكبد AST"},
        {"name": "وظائف كبد (ALP)", "unit": "U/L", "reference_range": "44-147", "description": "تحليل إنزيم الفوسفاتاز القلوي"},
        {"name": "جاما جي تي (GGT)", "unit": "U/L", "reference_range": "9-48", "description": "تحليل إنزيم GGT للكبد"},
        {"name": "البيليروبين الكلي", "unit": "mg/dL", "reference_range": "0.1-1.2", "description": "تحليل البيليروبين الكلي"},
        {"name": "البيليروبين المباشر", "unit": "mg/dL", "reference_range": "0.0-0.3", "description": "تحليل البيليروبين المباشر"},
        {"name": "وظائف كلى (Urea)", "unit": "mg/dL", "reference_range": "15-45", "description": "تحليل اليوريا"},
        {"name": "وظائف كلى (Creatinine)", "unit": "mg/dL", "reference_range": "0.6-1.3", "description": "تحليل الكرياتينين"},
        {"name": "حمض البوليك (Uric Acid)", "unit": "mg/dL", "reference_range": "3.4-7.0", "description": "تحليل حمض البوليك"},
        {"name": "صوديوم (Na)", "unit": "mmol/L", "reference_range": "135-145", "description": "تحليل الصوديوم"},
        {"name": "بوتاسيوم (K)", "unit": "mmol/L", "reference_range": "3.5-5.1", "description": "تحليل البوتاسيوم"},
        {"name": "كالسيوم (Ca)", "unit": "mg/dL", "reference_range": "8.5-10.2", "description": "تحليل الكالسيوم"},
        {"name": "فوسفور (Ph)", "unit": "mg/dL", "reference_range": "2.5-4.5", "description": "تحليل الفوسفور"},
        {"name": "مغنيسيوم (Mg)", "unit": "mg/dL", "reference_range": "1.7-2.2", "description": "تحليل المغنيسيوم"},
        {"name": "الكوليسترول الكلي", "unit": "mg/dL", "reference_range": "< 200", "description": "تحليل الكوليسترول"},
        {"name": "الكوليسترول الضار (LDL)", "unit": "mg/dL", "reference_range": "< 130", "description": "تحليل الكوليسترول الضار"},
        {"name": "الكوليسترول النافع (HDL)", "unit": "mg/dL", "reference_range": "> 40", "description": "تحليل الكوليسترول النافع"},
        {"name": "الدهون الثلاثية (Triglycerides)", "unit": "mg/dL", "reference_range": "< 150", "description": "تحليل الدهون الثلاثية"},
        {"name": "TSH", "unit": "uIU/mL", "reference_range": "0.4-4.0", "description": "تحليل هرمون الغدة الدرقية"},
        {"name": "T3", "unit": "ng/dL", "reference_range": "80-200", "description": "تحليل هرمون T3"},
        {"name": "T4", "unit": "mcg/dL", "reference_range": "5-12", "description": "تحليل هرمون T4"},
        {"name": "هرمون الحليب (Prolactin)", "unit": "ng/mL", "reference_range": "4.0-15.2", "description": "تحليل هرمون البرولاكتين"},
        {"name": "هرمون التستوستيرون", "unit": "ng/dL", "reference_range": "300-1000", "description": "تحليل هرمون الذكورة"},
        {"name": "هرمون الاستروجين (E2)", "unit": "pg/mL", "reference_range": "15-350", "description": "تحليل هرمون الاستروجين"},
        {"name": "هرمون البروجسترون", "unit": "ng/mL", "reference_range": "0.1-25.6", "description": "تحليل هرمون البروجسترون"},
        {"name": "فيتامين د", "unit": "ng/mL", "reference_range": "20-50", "description": "تحليل فيتامين د"},
        {"name": "فيتامين B12", "unit": "pg/mL", "reference_range": "200-900", "description": "تحليل فيتامين B12"},
        {"name": "حمض الفوليك", "unit": "ng/mL", "reference_range": "3-17", "description": "تحليل حمض الفوليك"},
        {"name": "البول الكامل", "unit": "", "reference_range": "", "description": "تحليل البول الكامل"},
        {"name": "البراز الكامل", "unit": "", "reference_range": "", "description": "تحليل البراز الكامل"},
        {"name": "تحليل الحمل (BHCG)", "unit": "mIU/mL", "reference_range": "< 5", "description": "تحليل هرمون الحمل"},
        {"name": "ESR", "unit": "mm/hr", "reference_range": "< 20", "description": "معدل ترسيب كريات الدم الحمراء"},
        {"name": "CRP", "unit": "mg/L", "reference_range": "< 6", "description": "تحليل البروتين التفاعلي C"},
        {"name": "RF", "unit": "IU/mL", "reference_range": "< 14", "description": "عامل الروماتويد"},
        {"name": "ANA", "unit": "", "reference_range": "سلبي/إيجابي", "description": "أجسام مضادة نوية"},
        {"name": "PT", "unit": "sec", "reference_range": "11-13.5", "description": "زمن البروثرومبين"},
        {"name": "INR", "unit": "", "reference_range": "0.8-1.2", "description": "النسبة المعيارية الدولية"},
        {"name": "زمن النزف (BT)", "unit": "دقيقة", "reference_range": "2-7", "description": "اختبار زمن النزف"},
        {"name": "زمن التجلط (CT)", "unit": "دقيقة", "reference_range": "4-10", "description": "اختبار زمن التجلط"},
        {"name": "تحليل الحديد (Iron)", "unit": "mcg/dL", "reference_range": "60-170", "description": "تحليل الحديد"},
        {"name": "تحليل الفيريتين (Ferritin)", "unit": "ng/mL", "reference_range": "12-300", "description": "تحليل الفيريتين"},
        {"name": "تحليل الترانسفيرين (Transferrin)", "unit": "mg/dL", "reference_range": "200-360", "description": "تحليل الترانسفيرين"},
        {"name": "تحليل الرصاص (Lead)", "unit": "mcg/dL", "reference_range": "< 10", "description": "تحليل الرصاص في الدم"},
        {"name": "تحليل الزنك (Zinc)", "unit": "mcg/dL", "reference_range": "70-120", "description": "تحليل الزنك"},
        {"name": "تحليل النحاس (Copper)", "unit": "mcg/dL", "reference_range": "70-140", "description": "تحليل النحاس"},
        {"name": "تحليل الكلوريد (Chloride)", "unit": "mmol/L", "reference_range": "98-107", "description": "تحليل الكلوريد"},
        {"name": "تحليل الألبومين (Albumin)", "unit": "g/dL", "reference_range": "3.4-5.4", "description": "تحليل الألبومين"},
        {"name": "تحليل البروتين الكلي (Total Protein)", "unit": "g/dL", "reference_range": "6.0-8.3", "description": "تحليل البروتين الكلي"},
    ]
    for test in tests:
        obj = TestCatalog.objects.create(
            name=test["name"],
            unit=test["unit"],
            reference_range=test["reference_range"],
            description=test["description"]
        )
        print(f"تمت إضافة: {obj.name}")
    print("تمت إضافة جميع التحاليل بنجاح.")
except Exception as e:
    print(f"حدث خطأ: {e}")
