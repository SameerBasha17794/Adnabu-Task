from django.db import models

class Adnabu(models.Model):
	email = models.EmailField()
	url = models.URLField()

	def __str__(self):
		return str(self.email)