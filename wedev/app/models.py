from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=55, editable=True, blank=False, null=False)
    lastname = models.CharField(max_length=55, editable=True, blank=False, null=False)
    email = models.EmailField(max_length=70, editable=True, blank=False, null=False)
    state = models.CharField(max_length=2, editable=True, blank=False, null=False)
    city = models.CharField(max_length=30, editable=True, blank=False, null=False)
    address = models.CharField(max_length=70, editable=True, blank=False, null=False)
    phone_number = models.CharField(max_length=11)
    
    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.name,
                                         self.lastname,
                                         self.email,
                                         self.state,
                                         self.city,
                                         self.address,
                                         self.phone_number
                                        )