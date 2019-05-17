from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

@python_2_unicode_compatible
class Todo(models.Model):
	title = models.CharField('TITLE', max_length=50)
	description = models.TextField('DESCRIPTION', blank=True, null=True)
	priority = models.IntegerField(
			'PRIORITY',
			default=0,
			validators=[MaxValueValidator(3), MinValueValidator(0)]
			)
	due = models.DateTimeField('DUE')
	done = models.BooleanField('DONE', default=False)

	class Meta:
		ordering = ('-done', '-due',)

	def __str__(self):
		return self.title

