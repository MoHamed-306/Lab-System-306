from django.test import Client
from django.contrib.auth import get_user_model
from html.parser import HTMLParser

User = get_user_model()
su = User.objects.filter(is_superuser=True).first()
if not su:
    User.objects.create_superuser('tempadmin','temp@example.com','temppw')
    su = User.objects.get(username='tempadmin')

c = Client()
logged = c.login(username=su.username, password='temppw' if su.username=='tempadmin' else None)
if not logged:
    c.force_login(su)
resp = c.get('/admin/')
html = resp.content.decode('utf-8')

# crude parse: find the first occurrence of 'التحاليل' and then extract subsequent <a> tags within the nearest <ul> after it
idx = html.find('التحاليل')
if idx == -1:
    print('analyses heading not found in HTML')
else:
    # find the nearest <ul after idx
    ul_start = html.find('<ul', idx)
    if ul_start == -1:
        print('no ul after analyses heading')
    else:
        ul_end = html.find('</ul>', ul_start)
        fragment = html[ul_start:ul_end+5]
        # extract anchor texts
        class AParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.in_a=False
                self.anchors=[]
                self.current=''
            def handle_starttag(self, tag, attrs):
                if tag=='a': self.in_a=True; self.current=''
            def handle_endtag(self, tag):
                if tag=='a' and self.in_a:
                    self.anchors.append(self.current.strip())
                    self.in_a=False
            def handle_data(self, data):
                if self.in_a: self.current += data
        p = AParser()
        p.feed(fragment)
        print('analyses anchors:')
        for a in p.anchors:
            print('-', a)

# find order of modules by searching for known titles
module_titles = ['التحاليل','المرضى','إدارة المرضى','الأطباء','إدارة المرضى و الأطباء']
found=[]
for t in module_titles:
    if html.find(t) != -1:
        found.append(t)
print('\nmodule titles present (subset):', found)
