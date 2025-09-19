from django.test import Client
from django.contrib.auth import get_user_model
from bs4 import BeautifulSoup

User = get_user_model()
su = User.objects.filter(is_superuser=True).first()
if not su:
    User.objects.create_superuser('tempadmin','temp@example.com','temppw')
    su = User.objects.get(username='tempadmin')

c = Client()
logged = c.login(username=su.username, password='temppw' if su.username=='tempadmin' else None)
if not logged:
    # try without password (existing user) via force_login
    c.force_login(su)
resp = c.get('/admin/')
html = resp.content.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
# find module headings
modules = []
for mod in soup.select('.app-list, .module, .grp-module'):
    title = mod.get_text(separator=' ', strip=True)[:60]
    modules.append((title, str(mod)[:200]))

# find analyses module specifically and list anchor texts in it
analyses = None
for mod in soup.select('.app-list, .module, .grp-module'):
    text = mod.get_text(separator=' ', strip=True)
    if 'التحاليل' in text or 'Analyses' in text:
        analyses = mod
        break

if analyses:
    anchors = [a.get_text(strip=True) for a in analyses.find_all('a')]
else:
    anchors = []

print('modules found (titles snippet):')
for t,_ in modules:
    print('-', t)
print('\nanalyses anchors:')
for a in anchors:
    print('-', a)
