from django.contrib import admin
from django.test.client import RequestFactory
from django.contrib.auth import get_user_model
import json

User = get_user_model()
su = User.objects.filter(is_superuser=True).first()
if not su:
    User.objects.create_superuser('tempadmin', 'temp@example.com', 'temppw')
    su = User.objects.get(username='tempadmin')

rf = RequestFactory()
req = rf.get('/admin/')
req.user = su

apps = admin.site.get_app_list(req)
analyses = next((a for a in apps if a['app_label'] == 'analyses'), None)
if not analyses:
    print('analyses app not found')
else:
    models = analyses.get('models', [])
    # print the object_name list and the admin URL for clarity
    out = [{'object_name': m.get('object_name'), 'admin_url': m.get('admin_url')} for m in models]
    print(json.dumps(out, ensure_ascii=False, indent=2))
