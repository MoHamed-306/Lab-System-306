from analyses.models import TestCatalog

for test in TestCatalog.objects.all():
    print(test.id, test.name)
