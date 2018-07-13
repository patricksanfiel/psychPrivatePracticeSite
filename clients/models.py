from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Therapist(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    bio = models.TextField()

    def __str__(self):
        return self.name

class Client(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = PhoneNumberField()
    appointment_date = models.DateTimeField(unique=True)
    therapist = models.ForeignKey(Therapist, on_delete = models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
