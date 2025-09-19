from django.contrib import admin
from django.test.client import RequestFactory
from django.contrib.auth import get_user_model

User = get_user_model()
su = User.objects.filter(is_superuser=True).first()
if not su:
    User.objects.create_superuser('tempadmin', 'temp@example.com', 'temppw')
    su = User.objects.get(username='tempadmin')

rf = RequestFactory()
req = rf.get('/admin/')
req.user = su

orig = admin.site.get_app_list_original(req)
analyses = next((a for a in orig if a['app_label']=='analyses'), None)
print('original models order:')
for m in analyses.get('models',[]):
    print(' -', m.get('object_name'))

# apply custom reorder logic here
desired_order = [
    'analysisrequest',
    'todaysanalysis',
    'analysisresultslink',
    'testcatalog',
    'analysis',
]
models = analyses.get('models', [])
models_map = {m['object_name'].lower(): m for m in models}
print('\nmodels_map keys:', list(models_map.keys()))
new_models = []
for key in desired_order:
    m = models_map.get(key)
    print('looking for', key, 'found:', bool(m))
    if m:
        new_models.append(m)
for m in models:
    if m not in new_models:
        new_models.append(m)
print('\nnew order result:')
for m in new_models:
    print(' -', m.get('object_name'))
