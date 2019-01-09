from django.db import models

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=100) 					#max length is 100 always
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return 'Question: {}'.format(self.question_text)


class Choice(models.Model): 											#next line for readablility
	question = models.ForeignKey(Question, on_delete=models.CASCADE) 	#Cascade is constant
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)								#default is optional parameter