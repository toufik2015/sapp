from django.shortcuts import render, redirect
from django.http import JsonResponse

from .filters import *
from .decorators import unauthenticated_user, allowed_users,admin_only
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group as Groupg

from django.forms import modelformset_factory
from .forms import CreateUserForm, rgisterS,LangForm,CreateGroupForm
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib import messages






@unauthenticated_user
def loginPageT(request):

	if request.method == 'POST':

		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request,username= username, password=password )

		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			messages.info(request,'username or password is incorrect')		

	context = {}
	return render(request, 'accounts/login.html', context)

#@unauthenticated_user
@allowed_users(allowed_roles=['Admin','Staff'])
def registerPageT(request):


	form = CreateUserForm()
	if  request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			
			group = Groupg.objects.get(name='Teacher')
			user.groups.add(group)
			Teacher.objects.create(
				user = user, name= user.first_name, last_name=user.last_name,email= user.email,phone=user.phone

				)
		
	context = {'form':form}
	return render(request, 'accounts/register.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')



@login_required(login_url = 'login')

@admin_only
def dashboard (request):
	students = Student.objects.all()

	Total_students = students.count()
	active_students = students.filter(status='Active').count()
	group_students = students.filter(status='Waiting for a group ').count()
	test_students = students.filter(status='Waiting for test').count()

	print(Total_students)
	context = {'Total_students':Total_students,'active_students':active_students,'group_students':group_students,'test_students':test_students}
	return render(request,'accounts/home.html',context)




@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Admin','Teacher'])
def teacher (request):
	teacher = request.user.teacher
	teacher_groups = teacher.group_set.all() 
	context = {'teacher':teacher, 'teacher_groups':teacher_groups}
	return render(request,'accounts/teacher.html', context)




@login_required(login_url = 'login')
@allowed_users(allowed_roles=['Admin','Teacher'])
def group (request, pk_g):

	

	group = Group.objects.get(id=pk_g)
		
	students = group.students.all()

	context = {'group':group, 'students':students,}

	return render(request,'accounts/teacher_group.html', context)





def groupStudentsAPI(request,pk_g):

	group = Group.objects.get(id=pk_g)
		
	students = group.students.all()


	studentList =[]

	for s in students:

		studentList.append({'name':s.name+" "+s.last_name, 'phone': s.phone, 'id': s.id})

	return JsonResponse(studentList, safe= False)


def addLang(request):
	form = LangForm()
	if request.method == 'POST':
		form = LangForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form':form}
	return render(request,'accounts/add-language.html',context)




@csrf_exempt
def studentPresent(request):

	id_s = request.POST.get('id')
	student = Student.objects.get(id = id_s)
	name = student.name
	last_name = student.last_name
	phone = student.phone
	status = 'Present'

	Attendance.objects.create(
		student_name = name,
		last_name = last_name,
		phone = phone,
		status = status
		)
	return JsonResponse('Checked!', safe = False)




@csrf_exempt
def studentAbsent(request):

	id_s = request.POST.get('id')
	student = Student.objects.get(id = id_s)
	name = student.name
	last_name = student.last_name
	phone = student.phone

	status = 'Absent'

	Attendance.objects.create(
		student_name = name,
		last_name = last_name,
		phone = phone,
		status = status
		)
	return JsonResponse('Checked!', safe = False)


@csrf_exempt
def sessionSub(request):
	id_g = request.POST.get('id_g')
	print(id_g)


	return JsonResponse('Checked!', safe = False)




def studentSearch(request):
	students = Student.objects.all()
	filtered_students = StudentFilter(request.GET, queryset = students)
	students = filtered_students.qs
	studentList =[]

	for s in students:

		studentList.append({'name':s.name ,'last_name':s.last_name, 'phone': s.phone, 'id': s.id, 'category':s.category, 'level':s.level,
			'sex':s.sex, 'job':s.job,'status':s.status,'date_applied':s.date_applied})

	context = {'filtered_students':filtered_students,'studentList':studentList}

	return render(request,'accounts/StaffAtt.html', context)








def registerPageS (request):
	form = rgisterS()
	if request.method == 'POST':
	 	form = rgisterS(request.POST)
	 	if form.is_valid():
	 		student = form.clean()
	 		parent = S_parent.objects.create(name=student['parent'], last_name=student['parent_last'], phone=student['parent_phone'], job=student['job'])
	 		Student.objects.create(name = student['name'],last_name= student['last_name'],birth_date=student['birth_date'],
	 			category=student['category'], sex=student['sex'], job=student['job'],phone=student['phone'],email = student['email'],date_applied = student['date_applied'],
	 			address=student['address'],status=student['status'],level=student['level'],
	 			)

	context={'form':form}
	return render(request, 'accounts/registerstudent.html', context)


def assginStudent (request, pk):
	EnrollmentFormSet = inlineformset_factory(Student, Enrollment,fields = ('student','group','date_enrolled'))
	student = Student.objects.get(id = pk)
	formset = EnrollmentFormSet(instance= student)
	if request.method == 'POST':
		formset = EnrollmentFormSet(request.POST,instance= student)
	
		if formset.is_valid():
			student.status = "Active"
			print(student.status) 
			formset.save()
			
			
	context = {'formset':formset, 'student':student}
	return render(request, 'accounts/assignStudent.html',context)




def updateStudentView(request):
	
	return render (request, 'accounts/updateStudent.html')

def createGroupView(request):
	form = CreateGroupForm()
	if request.method == 'POST':
		form = CreateGroupForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form': form}
	return render(request,'accounts/createGroup.html', context)








