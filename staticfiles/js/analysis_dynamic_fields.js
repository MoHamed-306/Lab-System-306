// إظهار الحقول الفرعية ديناميكياً عند اختيار نوع التحليل المركب
// يعمل في شاشة إدارة التحليل

document.addEventListener('DOMContentLoaded', function() {
    var testField = document.getElementById('id_test');
    var compositeFields = [
        'hgb', 'rbcs', 'hct', 'hgb_percent', 'mcv', 'mch', 'mchc', 'rdw_cv', 'plt', 'wbc',
        'neutrophils', 'band', 'segmented', 'lymphocytes', 'monocytes', 'eosinophil', 'basophils', 'comment'
    ];
    var compositeTests = ['CBC', 'LFT', 'RFT', 'LIPID', 'THYROID'];

    function toggleCompositeFields(show) {
        compositeFields.forEach(function(field) {
            var row = document.getElementById('id_' + field)?.closest('.form-row');
            if (row) row.style.display = show ? '' : 'none';
        });
        var resultRow = document.getElementById('id_result')?.closest('.form-row');
        if (resultRow) resultRow.style.display = show ? 'none' : '';
    }

    function checkTestType() {
        var selected = testField.options[testField.selectedIndex].text.trim().toUpperCase();
        if (compositeTests.includes(selected)) {
            toggleCompositeFields(true);
        } else {
            toggleCompositeFields(false);
        }
    }

    if (testField) {
        testField.addEventListener('change', checkTestType);
        checkTestType();
    }
});
