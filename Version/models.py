from django.db import models

# Create your models here.
class Versions(models.Model):
	names = models.CharField(max_length=100)
	codeBases = models.CharField(max_length=50)
	versions = models.CharField(max_length=10)
	activeStates = models.BooleanField(default=True)
	description = models.TextField(null=True, blank=True, default=None)
	createAt = models.DateTimeField(auto_now_add=True)
	updateAt = models.DateTimeField(auto_now=True)
	deleteAt = models.DateTimeField(null=True, blank=True, default=None)

	def __str__(self):
		return self.names
	
	class Meta:
		db_table = 'Versions'
