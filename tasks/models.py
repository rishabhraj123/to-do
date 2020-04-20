from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Taskheading(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	heading = models.CharField(max_length=200,default='NA')

	def __str__(self):
		return '{}:{}'.format(self.heading,self.user)

class Task(models.Model):
	heading = models.ForeignKey(Taskheading,on_delete=models.CASCADE,null=True)
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return '{}:{}'.format(self.heading,self.title)