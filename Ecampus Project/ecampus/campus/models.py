from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Batch(models.Model):
    batchId = models.IntegerField(primary_key=True)
    courseId = models.ForeignKey('campus.Course',on_delete=models.CASCADE, blank=True, null=True)
    batchName = models.CharField(max_length=50)
    batchdescription = models.CharField(max_length=50)
    #facultyId = models.ForeignKey('faculty.Faculty',on_delete=models.CASCADE)
    batchStartDate = models.DateField()
    batchEndDate = models.DateField()
    class Meta: 
        verbose_name_plural = "Batch"

class BatchDetail(models.Model):
    batch_detail_id = models.IntegerField(primary_key=True)
    batchId = models.OneToOneField(Batch, on_delete=models.CASCADE, blank=True, null=True)
    #studentId = models.ForeignKey('student.Student',on_delete=models.CASCADE)
    class Meta: 
        verbose_name_plural = "BatchDetails"
    
class BatchTime(models.Model):
    batchTimeId = models.IntegerField(primary_key=True)
    batchId = models.ManyToManyField('campus.Batch')
    batchDay = models.DateField()
    BatchTime = models.TimeField()
    BatchDuration = models.DurationField()
    class Meta: 
        verbose_name_plural = "BatchTime"

class Course(models.Model):
    courseId = models.IntegerField(primary_key=True)
    courseName = models.CharField(max_length=50)
    courseDescription = models.TextField()
    INACTIVE = 0
    ACTIVE = 1
    STATUS = (
        (INACTIVE, _('Inactive')),
        (ACTIVE, _('Active')),
    )  
    
    active = models.IntegerField(default=0, choices=STATUS)
    class Meta: 
        verbose_name_plural = "Course"

class StudentCourse(models.Model):
    studentCourseId = models.IntegerField(primary_key=True)
    courseId = models.ForeignKey('campus.Course',on_delete=models.CASCADE)
    #UserId = models.ForeignKey('user.User',on_delete=models.CASCADE)
    class Meta: 
        verbose_name_plural = "StudentCourse"

class Material(models.Model):
    batchId = models.ManyToManyField('campus.Batch')
    courseId = models.ForeignKey('campus.Course', on_delete=models.CASCADE, blank= True, null=True)
    materialTitle = models.CharField(max_length=50, null=True)
    materialDescription = models.TextField(null=True)
    INACTIVE = 0
    ACTIVE = 1
    STATUS = (
        (INACTIVE, _('Inactive')),
        (ACTIVE, _('Active')),
    )  
    
    active = models.IntegerField(default=0, choices=STATUS)
    materialURL = models.URLField(null=True)
    class Meta: 
        verbose_name_plural = "Material"

class Attendance(models.Model):
    attendanceId = models.IntegerField(primary_key=True)
    batchId = models.ForeignKey('campus.Batch', on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta: 
        verbose_name_plural = "Attendance"