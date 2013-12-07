from django.db import models

# model for a single category 
class Category(models.Model):
	# the super category can be null if top level category
	super_category = models.ForeignKey('self', blank=True, null=True)
	# the category name
	name = models.CharField(max_length=50)
	# the "toString" method
	def __unicode__(self):
		return self.name

# model for a single question
class Question(models.Model):
	# the question
	text = models.CharField(max_length=500)
	# category it belongs to
	category = models.ForeignKey(Category)
	# number of times answered right by all users
	num_marked_right = models.IntegerField(default=0)
	# number of times answered wrong by all users
	num_marked_wrong = models.IntegerField(default=0)
	# number of times answered by all users
	def num_answerd(self):
		return self.num_marked_right + self.num_marked_wrong
	# easiness of the question
	def easiness(self):
		return self.num_marked_right - self.num_marked_wrong;
	# the "toString" method
	def __unicode__(self):
		return self.text

class Choice(models.Model):
	# the choice text
	text = models.CharField(max_length=200)
	# question it belongs to
	question = models.ForeignKey(Question)
	# true only if correct choice
	is_correct = models.BooleanField(default=False)
	# the "toString" method
	def __unicode__(self):
		return self.text

