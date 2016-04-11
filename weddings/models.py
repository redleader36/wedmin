from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    schedule = models.TextField(null=True, blank=True)
    venue = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    date = models.DateTimeField('event date')
    def __str__(self):  
        return self.name

class Invitation(models.Model):
    invite_code = models.CharField(
        help_text="leave it empty, it will be generated automatically on creation of invitation",
        verbose_name=u'invitation code',
        max_length=6)
    def __str__(self):  
        return self.invite_code

class Guest(models.Model): # we create a model for a single guest
    RELATION_OPTIONS = (
        (0, "Immediate"),
        (1, "Paternal"),
        (2, "Maternal"),
        (3, "Friend")
    )
    SIDE_OPTIONS = (
        (True, "Groom"),
        (False, "Bride"),
    )

    first_name = models.CharField(max_length=45, null=True, blank=True)
    last_name = models.CharField(max_length=45, null=True, blank=True)
    first_name_2 = models.CharField(max_length=45, null=True, blank=True)
    last_name_2 = models.CharField(max_length=45, null=True, blank=True)
    primary_email = models.EmailField(max_length=254, null=True, blank=True)
    street_addr = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    event = models.ForeignKey('Event', null=True, blank=True, default=1)
    side = models.BooleanField(choices=SIDE_OPTIONS)
    relation = models.PositiveSmallIntegerField(choices=RELATION_OPTIONS)
    invitation = models.ForeignKey('Invitation', blank=True, null=True, on_delete=models.SET_NULL,
        verbose_name=u'Invitation letter guest is assigned')
    def full_name(self):
        return str('{0} {1}'.format(self.first_name, self.last_name))
    def full_name_2(self):
        if(self.first_name_2):
            return str('{0} {1}'.format(self.first_name_2, self.last_name_2))
    def combined_name(self):
        if(self.first_name_2):
            return '{0} and {1}'.format(self.full_name(), self.full_name_2())
        else:
            return self.full_name()
    def __str__(self):  
        return self.full_name()