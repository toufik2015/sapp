import django_filters
from django_filters import DateFilter
from django.forms.widgets import TextInput, DateInput,Select
from django import forms
from .models import *


job_list = (('Worker','Worker'), ('Jobless','Jobless'))

CATEGORY= (('Kids', 'Kids'),('Primary School', 'Primary School'),
		('Middle School','Middle School'), ('High school','High School'),
		('University Student','University Student'), ('Adult','Adult'))

Level = (('A0', 'A0'), ('A0+', 'A0+'),('A1', 'A1'),('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), 
		('C1', 'C1'), ('C2', 'C2')) 

sex_list = (('Male','Male'), ('Female','Female'))

educ_lvl = (('P1', 'P1'), ('P2', 'P2'),('P3', 'P3'),('P4', 'P4'), ('B1', 'B1'), ('P5', 'P5'), 
		('M1', 'M1'), ('M2', 'M2'), ('M3', 'M3'), ('M4', 'M4'), ('S1', 'S1'),
		('S2', 'S2'), ('S3', 'S3'))


STATUS= (('Waiting for Test', 'Waiting for Test'),('Waiting for a group', 'Waiting for a group'),
		('Active','Active'), ('Inactive','Inactive'))



class DateInput(forms.DateInput):
	input_type ='date'


class StudentFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(field_name='name',  widget=TextInput(attrs={'placeholder': 'Name...' , 'class':'form-control ml-3 mr-3' }))
	last_name = django_filters.CharFilter(field_name='last_name',  widget=TextInput(attrs={'placeholder': 'Last Name...' , 'class':'form-control ml-3 mr-3' }))
	
	category = django_filters.ChoiceFilter(choices = CATEGORY,field_name='category',  widget=Select(attrs={'placeholder': 'category' , 'class':'form-control ml-3 mr-3' }))
	level = django_filters.ChoiceFilter(choices = Level,field_name='level',  widget=Select(attrs={'placeholder': 'Level' , 'class':'form-control   mr-3' }))
	job = django_filters.ChoiceFilter(choices = job_list,field_name='job',  widget=Select(attrs={'placeholder': 'Job' , 'class':'form-control mt-3 mr-3' }))
	sex = django_filters.ChoiceFilter(choices = sex_list,field_name='sex',  widget=Select(attrs={'placeholder': 'Gender' , 'class':'form-control ml-3 mr-3' }))
	status = django_filters.ChoiceFilter(choices = STATUS,field_name='sex',  widget=Select(attrs={'placeholder': 'Status' , 'class':'form-control ml-3 mr-3' }))
	phone = django_filters.CharFilter(field_name='phone',  widget=TextInput(attrs={'placeholder': 'Phone...' , 'class':'form-control ml-3 mr-3' }))
	email = django_filters.CharFilter(field_name='email',  widget=TextInput(attrs={'placeholder': 'Email...' , 'class':'form-control ml-3 mr-3' }))
	date_applied_gte =DateFilter(field_name='date_applied',  widget= DateInput(attrs={ 'class':'form-control ml-3 mr-3' }), lookup_expr = 'gte')
	date_applied_lte =DateFilter(field_name='date_applied',  widget= DateInput(attrs={ 'class':'form-control ml-3 mr-3' }), lookup_expr = 'lte')
	educ_level = django_filters.ChoiceFilter(choices = educ_lvl,field_name='educ_level',  widget=Select(attrs={'placeholder': 'educ_level' , 'class':'form-control ml-3 mr-3' }))

	class Meta:
		model = Student
		fields ='__all__'
		exclude = ['parent','address','birth_date']



	# name last_name  birth_date  category  sex  job  phone  email  date_applied  status level
 