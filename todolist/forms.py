from django import forms
from tempus_dominus.widgets import DateTimePicker
from .models import Todo

PRIORITY_CHOICES = [
    ('0', 'None'),
    ('1', '★'),
    ('2', '★★'),
	('3', '★★★'),
]


class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ['title','description','priority','due']

	def __init__(self, *args, **kwargs):
		super(TodoForm, self).__init__(*args, **kwargs)
		self.fields['priority'] = forms.ChoiceField(choices=PRIORITY_CHOICES, widget=forms.RadioSelect)	
		self.fields['due'].widget = DateTimePicker(
				options={
					'collapse': False,
					'icon_toggle': False,
				},
				)
