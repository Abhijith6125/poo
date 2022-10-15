from django.contrib import admin

# Register your models here.
from registration.models import Course, Batch, Student
# Register your models here.
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Student)
