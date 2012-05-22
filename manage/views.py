from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, TemplateView, ListView, DetailView, FormView
from classmanage.people.models import *
from classmanage.manage.forms import *

#TODO Restrict all management views to employees with permission
def managementdashboard(request):
	
	return render_to_response("manage_base.html",
							  context_instance=RequestContext(request))
							
# Example of a class-based generic view							
class managementdashboards(TemplateView):
	template_name="manage_base.html"
	
#Create Family Generic View
class createfamily(CreateView):
	model = Family
	template_name = "manage_family_create.html"
	
class listfamily(ListView):
	model = Family
	template_name = "manage_family_list.html"
	
class detailfamily(DetailView):
	model = Family
	template_name = "manage_family_detail.html"
	
class createstudent(FormView):
	model = Student
	template_name = "manage_student_create.html"
	form_class = StudentAddForm

def addstudent(request, family_id):
	if request.POST:
		form = StudentAddForm(family_id, request.POST)
		if form.is_valid():
			family_id = form.save()
			return HttpResponseRedirect(reverse('detailfamily', args=[family_id]))
	else:
		#Send family_id to form, 
		form = StudentAddForm(family_id)
	return render_to_response("manage_student_create.html", {'form' : form, 'form_title' : 'Add Student'}, 
				  context_instance=RequestContext(request))

class liststudent(ListView):
	model = Student
	template_name = "manage_student_list.html"

class detailstudent(DetailView):
	model = Student
	template_name = "manage_student_detail.html"							

