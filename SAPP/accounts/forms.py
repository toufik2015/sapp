
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms  
from django.db import models
from .models import *





class UserT(User):
	
	phone = models.CharField(max_length = 200, null=True)
	 
	
class CreateUserForm(UserCreationForm):
	
	class Meta:
		model = UserT
		fields =  ['username','first_name','phone','last_name', 'email', 'password1', 'password2']


class DateInput(forms.DateInput):
	input_type ='date'



class rgisterS(forms.Form):

	job_list = (('Worker','Worker'), ('Jobless','Jobless'))

	Level = (('', ''),('A0', 'A0'), ('A0+', 'A0+'),('A1', 'A1'),('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), 
		('C1', 'C1'), ('C2', 'C2')) 

	CATEGORY= (('Kids', 'Kids'),('Primary School', 'Primary School'),
		('Middle School','Middle School'), ('High school','High School'),
		('University Student','University Student'), ('Adult','Adult'))
	STATUS= (('Waiting for Test', 'Waiting for Test'),('Waiting for a group', 'Waiting for a group'),
		('Active','Active'), ('Inactive','Inactive'))
	sex_list = (('',''),('Male','Male'), ('Female','Female'))


	name 	= forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200)
	birth_date = forms.DateField(widget = DateInput)
	category = forms.ChoiceField(choices = CATEGORY)
	job = forms.ChoiceField( choices = job_list )
	phone = forms.CharField(max_length = 200)
	email = forms.EmailField(max_length = 200)
	date_applied = forms.DateField(widget = DateInput)
	address = forms.CharField(max_length = 200)
	status = forms.ChoiceField(choices = STATUS)
	level = forms.ChoiceField(choices = Level,required=False)
	parent = forms.CharField(max_length = 200,required=False)
	parent_last = forms.CharField(max_length = 200,required=False)
	parent_phone = forms.CharField(max_length = 200,required=False)
	sex = forms.ChoiceField(choices = sex_list) 


class LangForm(forms.ModelForm):
	class Meta:
		model = Language
		fields = ['language']

		widgets = {'language':forms.TextInput(attrs = {'class': 'form-control'})}


class CreateGroupForm(ModelForm):
	class Meta:
		model= Group
		fields ='__all__'
		exclude = ['students']
