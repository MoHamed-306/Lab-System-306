# debug reorder
import lab_system.admin as la
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
print('orig models:', [m.get('object_name') for m in analyses.get('models',[])])

# show models_map keys
models = analyses.get('models', [])
models_map = {m['object_name'].lower(): m for m in models}
print('models_map keys:', list(models_map.keys()))

# desired order
desired_order = [
    'analysisrequest',
    'todaysanalysis',
    'analysisresultslink',
    'testcatalog',
    'analysis',
]
for key in desired_order:
    print('key', key, 'in map?', key in models_map)
    if key in models_map:
        print(' ->', models_map[key]['object_name'])

# now call custom _custom_app_list
reordered = la._custom_app_list(req)
anal = next((a for a in reordered if a['app_label']=='analyses'), None)
print('\nreordered models:', [m.get('object_name') for m in anal.get('models',[])])
