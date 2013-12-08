from django.db import models

# model for the top most category 
class Category1(models.Model):
	# the category name
	name = models.CharField(max_length=50)
	# the "toString" method
	def __unicode__(self):
		return self.name

# model for the 2nd level sub-category
class Category2(models.Model):
	# super category
	category = models.ForeignKey(Category1)
	# the category name
	name = models.CharField(max_length=50)
	# the "toString" method
	def __unicode__(self):
		return self.name

# model for the 3rd level sub-category
class Category3(models.Model):
	# super category
	category = models.ForeignKey(Category2)
	# the category name
	name = models.CharField(max_length=50)
	# the "toString" method
	def __unicode__(self):
		return self.name		

# model for a single question
class Question(models.Model):
	# the question
	text = models.CharField(max_length=500, blank=False)
	# category it belongs to
	category = models.ForeignKey(Category3)
	# number of times answered right by all users
	num_marked_right = models.IntegerField(default=0)
	# number of times answered wrong by all users
	num_marked_wrong = models.IntegerField(default=0)
	# number of times answered by all users
	def num_answered(self):
		return self.num_marked_right + self.num_marked_wrong
	num_answered.integer = True
	# easiness of the question
	def easiness(self):
		return self.num_marked_right - self.num_marked_wrong;
	easiness.integer = True
	# the "toString" method
	def __unicode__(self):
		return self.text

class Choice(models.Model):
	# the choice text
	text = models.CharField(max_length=200, blank=False)
	# question it belongs to
	question = models.ForeignKey(Question)
	# true only if correct choice
	is_correct = models.BooleanField(blank=False, default=False)
	is_correct.short_description = 'Mark correct answer'
	# the "toString" method
	def __unicode__(self):
		return self.text

