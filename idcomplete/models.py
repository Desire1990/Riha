from django.db import models
from django.contrib.auth.models import User
from account.models import*


class IdentiteComplete(models.Model):
	user              = models.OneToOneField(User, 
											on_delete=models.CASCADE,
											default = False, 
											related_name='users')
	Person            = models.ForeignKey(Person, 
											on_delete=models.CASCADE,
											default = False,
											related_name = 'identiteCompletes')
	province          = models.ForeignKey(Province, on_delete=models.CASCADE)
	commune           = models.ForeignKey(Commune, on_delete=models.CASCADE)
	zone              = models.ForeignKey(Zone, on_delete=models.CASCADE)
	quarter           = models.ForeignKey(Quarter, on_delete = models.CASCADE)
	attestionId       = models.CharField(max_length = 30)
	date              = models.DateField()


	
	def __str__(self):
		return ("{0} {1}".format(self.Person.Nom, self.Person.Prenom))

