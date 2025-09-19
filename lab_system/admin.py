from django.contrib import admin
admin.site.site_header = "نظام المختبر"
admin.site.site_title = "لوحة تحكم نظام المختبر"
admin.site.index_title = "إدارة النظام"

# ترتيب التطبيقات والنماذج في القائمة الجانبية حسب الطلب
def _custom_app_list(request):
	"""Return app list with `analyses` first and `patients` immediately after.

	Also reorder models inside `analyses` as:
	1. طلبات التحليل (AnalysisRequest)
	2. تحاليل اليوم (TodaysAnalysis)
	3. التحاليل (Analysis)
	4. كاتالوج التحاليل (TestCatalog)
	5. الاستعلام عن التحليل (AnalysisResultsLink)
	"""
	# Build final app_list: put analyses first, then patients, then others
	final = []
	if analyses_app:
		# reorder models inside analyses app to the desired server-side order
		desired_order = [
			'analysisrequest',
			'todaysanalysis',
			'analysisresultslink',
			'testcatalog',
			'analysis',
		]
		models = analyses_app.get('models', [])
		models_map = {m['object_name'].lower(): m for m in models}
		new_models = []
		for key in desired_order:
			m = models_map.get(key)
			if m:
				new_models.append(m)
		# append any remaining models not specified
		for m in models:
			if m not in new_models:
				new_models.append(m)
		analyses_app['models'] = new_models
		final.append(analyses_app)
	if patients_app:
		final.append(patients_app)
	for app in app_list:
		if app is analyses_app or app is patients_app:
			continue
		final.append(app)

	return final


# keep original get_app_list to call from our custom function
if not hasattr(admin.site, 'get_app_list_original'):
	admin.site.get_app_list_original = admin.site.get_app_list
# restore default behavior: do not override admin.site.get_app_list
admin.site.get_app_list = admin.site.get_app_list_original


# Sometimes admin themes or templates bypass get_app_list; also wrap the index view
# to reorder the `app_list` right before rendering the index page.
if not hasattr(admin.site, 'index_original'):
	admin.site.index_original = admin.site.index

def _custom_index(request, extra_context=None):
	response = admin.site.index_original(request, extra_context=extra_context)
	try:
		# TemplateResponse may not be rendered yet; modify its context_data
		ctx = getattr(response, 'context_data', None)
		if ctx and 'app_list' in ctx:
			app_list = ctx['app_list']
			# reuse our _custom_app_list logic by calling it and passing through
			reordered = _custom_app_list(request)
			ctx['app_list'] = reordered
			response.context_data = ctx
	except Exception:
		pass
	return response

# restore default index view to avoid server-side reordering
if hasattr(admin.site, 'index_original'):
	admin.site.index = admin.site.index_original