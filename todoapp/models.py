from django.db import models
from django.utils import timezone
class TodoItem(models.Model):
	content = models.CharField(max_length=100,verbose_name='Yapılacaklar',)
	date_created = models.DateField(default=timezone.now)
	complete = models.BooleanField(default=False)