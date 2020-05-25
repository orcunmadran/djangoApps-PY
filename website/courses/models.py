from django.db import models

# Create your models here.
class Course(models.Model):
    courseID = models.CharField(max_length=10)
    courseName = models.TextField()
    courseSource = models.TextField(blank=True) #boş bırakılabilir
    courseURL = models.TextField()

# Bu uygulamanın modelinin veritabanında oluşabilmesi için
# py manage.py makemigrations
# py manage.py migrate