from django.db import models
from question.models import Question
from django.contrib.auth.models import User

class Packet(models.Model):
	# questions in the packet
	questions = models.ManyToManyField(Question)

class Trial(models.Model):
	question = models.ForeignKey(Question)
	correct = models.BooleanField(default=False)

class Completed(models.Model):
	trial = models.ManyToManyField(Trial)

class SQUserInfo(models.Model):
	# associated user
	user = models.OneToOneField(User)
	# total points
	sq_points = models.IntegerField(default=0)
	# user can have one packet at a time
	packet = models.OneToOneField(Packet)
	trial = models.OneToOneField(Completed)