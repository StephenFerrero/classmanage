from django import forms
from classmanage.people.models import Student

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class StudentAddForm(forms.Form):
	def __init__(self, family_id, *args, **kwargs):
		super(StudentAddForm, self).__init__(*args, **kwargs)

		self.family_id = family_id

	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	gender = forms.CharField(max_length = 20) #Set GENDERS options
	birth_date = forms.DateField(required=False)
	registration_date = forms.DateField(required=False)
	medications = forms.CharField(max_length = 1000, required=False)
	disabilities = forms.CharField(max_length = 1000, required=False)
	special_needs = forms.CharField(max_length = 1000, required=False)
	allergies = forms.CharField(max_length = 1000, required=False)
	instructor_feedback = forms.CharField(max_length = 1000, required=False)
	has_liabilityform = forms.BooleanField(required=False)
	notes = forms.CharField(max_length = 1000, required=False)
	last_updated = forms.DateTimeField(required=False)
	date_created = forms.DateTimeField(required=False)
	
	def save(self):
		new_student = Student()
		new_student.family_id = self.family_id
		new_student.first_name = self.cleaned_data['first_name']
		new_student.last_name = self.cleaned_data['last_name']
		new_student.gender = self.cleaned_data['gender']
		new_student.birth_date = self.cleaned_data['birth_date']
		new_student.registration_date = self.cleaned_data['registration_date']
		new_student.last_updated = self.cleaned_data['registration_date']
		new_student.date_created = self.cleaned_data['registration_date']
		#TODO: Only request liabilty form if Admin

		new_student.save()
		
		return new_student.family_id