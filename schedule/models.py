from django.db import models

# Classes are scheduled ongoing-events that students can enroll in.
class Class(models.Model):
	status = models.CharField(choices=CLASS_STATUS, max_length=30) #TODO Set class status options in Settings
	session # Session class belongs to
	start_datetime = models.DateTimeField()
    start_time = models.TimeField()
    end_datetime = models.DateTimeField()
    end_time = models.TimeField()
    weekday = models.IntegerField()
    instructors = models.ManyToManyField(Employee, blank=True)
    description = models.CharField(max_length=1000, blank=True)
	category_1 = models.CharField(options=CLASS_CATEGORY_1, blank=True) #TODO Set category options in settings
	category_2 = models.CharField(options=CLASS_CATEGORY_2, blank=True) #TODO Set class options in settings
	category_3 = models.CharField(options=CLASS_CATEGORY_3, blank=True) #TODO Set class options in settings
	minimum_age = models.PositiveIntegerField()
	maximum_age = models.PositiveIntegerField()
	maximum_size = models.PositiveIntegerField() #Maximum class size in number of students
	registration_startdate = models.DateField()
	display_on_website = models.BooleanField("Display on website", blank=True)
	notes = models.CharField(max_length = 5000, blank=True)
	last_updated = models.DateTimeField(blank=True, editable=False)
	date_created = models.DateTimeField(blank=True, editable=False)

#An enrollment is a students booking for a class or event	
class Enrollment(models.Model):
	last_updated = models.DateTimeField(blank=True, editable=False)
	date_created = models.DateTimeField(blank=True, editable=False)
	
#An absence is recorded if a student does not show up for an enrolled class or event
class Absence(models.Model):
	last_updated = models.DateTimeField(blank=True, editable=False)
	date_created = models.DateTimeField(blank=True, editable=False)
	