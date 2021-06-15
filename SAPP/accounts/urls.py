from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('loginteacher/', views.loginPageT, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    
    path('teacher/',views.teacher, name="teacher"),
    path('add_lang/',views.addLang, name="add_lang"),
    path('create_group/',views.createGroupView, name="create_group"),
    path('Updatestudent/',views.updateStudentView, name="Updatestudent"),

    path('registerteacher/', views.registerPageT, name="registerteacher"),
    path('registerstudent/',views.registerPageS, name="registerstudent"),
    path('assginstudent/<str:pk>',views.assginStudent, name="assginstudent"),
    
    path('teacher_group/<str:pk_g>',views.group, name="teacher_group"),
    path('studentslist/<str:pk_g>',views.groupStudentsAPI), 
    path('student_present/',views.studentPresent), 
    path('student_absent/',views.studentAbsent), 
    path('sub_session/',views.sessionSub), 


    path('student_search/',views.studentSearch, name="student_search"),
     
     
     
     
     
    

    ]