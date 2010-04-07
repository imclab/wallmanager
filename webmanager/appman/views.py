from django.views.generic.list_detail import *
from django.views.generic.create_update import *
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required

from appman.forms import *
from appman.models import *

def application_list(request):
	cs = Application.objects.all()
	return object_list(request, queryset=cs, template_object_name="application")
	
@login_required
def application_add(request):
	form_class = ApplicationForm
	if request.method == 'POST':
		form = form_class(request.POST, request.FILES)
		if form.is_valid():
			app = form.save(commit=False)
			app.owner = request.user
			app.save()
			return HttpResponseRedirect('/app/list/') # Redirect after POST
	else:
		form = form_class()

	return render_to_response('appman/application_form.html', {
		'form': form,
	})
	
@login_required
def application_edit(request, object_id):
    return update_object(request, form_class=ApplicationForm, 
            object_id=object_id, post_save_redirect="/app/list/")