from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
	user              = models.OneToOneField(User, 
											on_delete=models.CASCADE,
											default = False, 
											unique = True,
											related_name='users')
	slug        = models.SlugField(max_length=200, unique=True)
	avatar            = models.ImageField(null=True, blank=True,upload_to="image/")
	NomPere           = models.CharField(max_length = 20)
	NomMere           = models.CharField(max_length = 20)
	colline           = models.CharField(max_length = 20)
	commune_natal     = models.CharField(max_length = 20)
	province_natal    = models.CharField(max_length = 20)
	anneeDeNaissance  = models.CharField(max_length = 20)
	nationalite       = models.CharField(max_length = 20)
	etatCivil         = models.CharField(max_length = 20)
	profession        = models.CharField(max_length = 20)
	numberId          = models.CharField(max_length = 20)
	date_delivrated   = models.DateField()


	def __str__(self):
		return ("{0} {1}".format(self.user.first_name, self.user.last_name))






class Province(models.Model):
	name     = models.CharField(max_length = 20)
	govner   = models.CharField(max_length = 30)

	def __str__(self):
		return self.name


class Commune(models.Model):
	province        = models.ForeignKey(Province, on_delete=models.CASCADE)
	name            = models.CharField(max_length = 30)
	administrator   = models.CharField(max_length = 30)

	def __str__(self):
		return self.name
	

class Zone(models.Model):
	commune         = models.ForeignKey(Commune, on_delete=models.CASCADE)
	name            = models.CharField(max_length = 30)
	chefZoneLeader  = models.CharField(max_length = 30)

	def __str__(self):
		return self.name


class Quarter(models.Model):
	zone           = models.ForeignKey(Zone, on_delete=models.CASCADE)
	name           = models.CharField(max_length = 30)
	chefQuarter    = models.CharField(max_length = 30)

	def __str__(self):
		return self.name

