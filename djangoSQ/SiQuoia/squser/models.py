from django.db import models
from question import Question

class SQUserInfo(models.Model):
	# associated user
	user = models.OneToOneField(User)
	# total points
	sq_points = models.IntegerField(default=0)
	# user can have one packet at a time
	packet = models.OneToOneField(Packet)

class Packet(models.Model):
	# questions in the packet
	questions = models.ManyToManyField(Question)