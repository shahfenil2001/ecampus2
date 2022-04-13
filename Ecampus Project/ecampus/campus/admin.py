from django.contrib import admin
from .models import Batch, BatchDetail, BatchTime, Course, StudentCourse, Material, Attendance

# Register your models here.

admin.site.register(Batch)
admin.site.register(BatchDetail)
admin.site.register(BatchTime)
admin.site.register(Course)
admin.site.register(StudentCourse)
admin.site.register(Material)
admin.site.register(Attendance)