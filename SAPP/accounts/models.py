from django.db import models
from django.contrib.auth.models import User




Level = (('A0', 'A0'), ('A0+', 'A0+'),('A1', 'A1'),('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), 
		('C1', 'C1'), ('C2', 'C2')) 

educ_lvl = (('P1', 'P1'), ('P2', 'P2'),('P3', 'P3'),('P4', 'P4'), ('B1', 'B1'), ('P5', 'P5'), 
		('M1', 'M1'), ('M2', 'M2'), ('M3', 'M3'), ('M4', 'M4'), ('S1', 'S1'),
		 ('S2', 'S2'), ('S3', 'S3'))


CATEGORY= (('Kids', 'Kids'),('Primary School', 'Primary School'),
		('Middle School','Middle School'), ('High school','High School'),
		('University Student','University Student'), ('Adult','Adult'))

class S_parent(models.Model):
	name = models.CharField(max_length=200,null= True)
	last_name = models.CharField(max_length=200,null= True)
	phone = models.CharField(max_length = 200, null=True)
	job = models.CharField(max_length = 200, null=True)
	def __str__(self):
		return self.name+' '+self.last_name

	class Meta:
		db_table ='s_parent'
		constraints = [models.UniqueConstraint(fields=['name','last_name','phone'],name = 'unique parent')]
		
class Student (models.Model):

	STATUS= (('Waiting for Test', 'Waiting for Test'),('Waiting for a group', 'Waiting for a group'),
		('Active','Active'), ('Inactive','Inactive'))


	name = models.CharField(max_length = 200, null=True)
	last_name = models.CharField(max_length = 200, null=True)
	birth_date = models.DateField(null=True)
	category = models.CharField(max_length=200, null=True,choices = CATEGORY)
	sex = models.CharField(max_length=30, null=True)
	job = models.CharField(max_length = 200, null=True)
	phone = models.CharField(max_length = 200, null=True)
	email = models.EmailField(max_length = 200, null=True)
	date_applied = models.DateField( null=True)
	address = models.CharField(max_length = 200, null=True)
	status = models.CharField(max_length=200, null=True,choices = STATUS)
	level = models.CharField(max_length=200, null=True,choices = Level, blank = True)
	educ_level = models.CharField(max_length=200, null=True,choices = educ_lvl)
	parent = models.ForeignKey(S_parent, null= True, on_delete = models.CASCADE)
	
	def __str__(self):
		return self.name +' '+self.last_name




class Language (models.Model):
	language = models.CharField(max_length = 200, null=True)

	def __str__(self):
		return self.language


class Teacher (models.Model):
	user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
	name = models.CharField(max_length = 200, null=True)
	last_name = models.CharField(max_length = 200, null=True)
	language = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
	phone = models.CharField(max_length = 200, null=True)
	email = models. EmailField(max_length = 200, null=True)

	def __str__(self):
		return str(self.name) 





class Group (models.Model):

	
	group_name = models.CharField(max_length = 200, null=True)
	N_sessions = models.IntegerField( null=True)
	level = models.CharField(max_length=200, null=True,choices = Level)
	category =  models.CharField(max_length=200, null=True,choices = CATEGORY)
	language = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
	teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)
	students = models.ManyToManyField(Student, through='Enrollment')

	def __str__(self):
		return self.group_name

	class Meta:
		db_table ='accounts_group'
		constraints = [models.UniqueConstraint(fields=['group_name'],name = 'unique group')]



class Enrollment(models.Model):

	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	date_enrolled = models.DateField( null=True)

	class Meta:
		db_table ='accounts_enrollment'
		constraints = [models.UniqueConstraint(fields=['student','group'],name = 'unique enroll')]

	
class Attendance (models.Model):
	student_status = (('Absent','Absent'),('Present','Present')) 

	student_name = models.CharField(max_length = 200, null=True)
	last_name =  models.CharField(max_length = 200, null=True)
	phone = models.CharField(max_length = 200, null=True)
	status = models.CharField(max_length=200, null=True)
	day_attended = models.DateField(auto_now_add = True, null=True)
	
	group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)

class group_sessions(models.Model):
	group_n = models.ForeignKey(Group, on_delete=models.CASCADE)
	session_date = models.DateField(auto_now_add = True, null=True)













