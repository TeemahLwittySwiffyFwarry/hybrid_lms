from django.db import models

# Create your models here.
# Instructor model
class Routes(models.Model):
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.location
    
class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50, default=" ")
    mobile_no = models.CharField(max_length=20)
    LOCATION_CHOICES = (
        ('Ekoro', 'Ekoro'),
        ('Meiran Road', 'Meiran Road'),
        ('Agege', 'Agege'),
        ('Fagba', 'Fagba')        
    )
    location = models.CharField(max_length=20, choices = LOCATION_CHOICES, default = "null")
    
    # QUALIFICATION_CHOICES = (
    #     ('BSC', 'Bachelor of Science'),
    #     ('MSC', 'Master'),
    #     ('BA', 'Bachelor of Arts'),
    #     ('NCE', 'National Certificate Examination'),
    #     ('ND', 'National Diploma'),
    #     ('HND', 'Higher National Diploma')
    # )
    # qualification = models.CharField(max_length=5, choices = QUALIFICATION_CHOICES)
    
    address = models.TextField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=5, choices = GENDER_CHOICES, default = '0')
    
    # location = models.ManyToManyField(Routes, blank=True, null=True, default = "")
    
    class Meta:
        verbose_name_plural = "1. Instructors"

#Course category model    
class CourseCategory(models.Model):
    title = models.CharField(max_length= 150)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "2. CourseCategories"

#Course Model
class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "3. Courses"

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    class_level = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=20)
    address = models.TextField()
    
    class Meta:
        verbose_name_plural = "4. Students"
