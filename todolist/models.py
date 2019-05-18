from __future__ import unicode_literals

from django.urls import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

@python_2_unicode_compatible
class Todo(models.Model):
	title = models.CharField('Title', max_length=50)
	description = models.TextField('Description', blank=True, null=True)
	priority = models.IntegerField(
			'Priority',
			default=0,
			validators=[MaxValueValidator(3), MinValueValidator(0)]
			)
	due = models.DateTimeField('Due', blank=True, null=True)
	done = models.BooleanField('Done', default=False)

	class Meta:
		ordering = ('done', '-priority', 'due',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('todo:todo_detail', args=(self.id,))

