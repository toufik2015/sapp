from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *





admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Language)
admin.site.register(Enrollment)
admin.site.register(Attendance)
admin.site.register(S_parent)



