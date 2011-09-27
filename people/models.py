from django.db import models

#Families are used to group together Contacts and Students
class Family(models.Model):
	name = models.CharField(max_length=100)  #Family name (Typically last name of parent)
	registration_date = models.DateField() #Date family was first registered, auto-generated but editable
	primary_phone = PhoneNumberField()
	address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = USStateField()
    zip_code = models.CharField(max_length=5)
	notes = models.CharField(max_length = 5000, blank=True)
	last_updated = models.DateTimeField(blank=True, editable=False)
	date_created = models.DateTimeField(blank=True, editable=False)

#Contacts are people associated with a Family other than students (Parents, Grandparents, Guardians, etc...)	
class Contact(models.Model):
	family = models.ForeignKey(Family, editable=False)
	contact_type = models.models.CharField(max_length=10, choices=CONTACT_TYPE) #Choices should be set in Settings
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(blank=True)
	primary_contact = models.BooleanField("Primary", blank=True)
	pickup_authorized = models.BooleanField("Authorized to pick-up children", blank=True)
	home_phone = PhoneNumberField(blank=True)
	work_phone = PhoneNumberField(blank=True)
	cell_phone = PhoneNumberField(blank=True)
	fax_phone = PhoneNumberField(blank=True)
	other_phone = PhoneNumberField(blank=True)
	address = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = USStateField(, blank=True)
    zip_code = models.CharField(max_length=5, blank=True)
	notes = models.CharField(max_length = 5000, blank=True)
	last_updated = models.DateTimeField(blank=True, editable=False)
	date_created = models.DateTimeField(blank=True, editable=False)
	
	
#Students can be enrolled in classes and belong to a single family
class Student(models.Model):
	family = models.ForeignKey(Family, editable=False)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	gender = models.CharField(choices=GENDERS) #Set GENDERS options
	birth_date = models.DateField(blank=True)
	registration_date = models.DateField(blank=True)
	medications = models.CharField(blank=True)
	disabilities = models.CharField(blank=True)
	special_needs = models.CharField(blank=True)
	allergies = models.CharField(blank=True)
	instructor_feedback = models.CharField(blank=True)
	has_liabilityform = models.BooleanField("Has liability form", blank=True)
	notes = models.CharField(max_length = 5000, blank=True)
	last_updated = models.DateTimeField(blank=True, editable=False)
	date_created = models.DateTimeField(blank=True, editable=False)

#Employees are any kind of Staff (Instructors, Owners, Etc...) Employees can login into the management portal if given permission.
class Employee(models.Model):
	status =  models.CharField(choices=EMPLOYEE_STATUS, default='Active', max_length=30)
	employee_type = models.CharField(choices=EMPLOYEE_TYPE) #Employee type set in Settings
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = USStateField()
    zip_code = models.CharField(max_length=5)
	notes = models.CharField(max_length = 5000)
	last_updated = models.DateTimeField(blank=True, editable=False)
	date_created = models.DateTimeField(blank=True, editable=False)
	
