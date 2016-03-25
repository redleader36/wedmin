from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
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
    RELATION_ANSWERS = (
        (0, "Immediate"),
        (1, "Paternal"),
        (2, "Maternal"),
        (3, "Friend")
    )

    first_name = models.CharField(max_length=45, null=True, blank=True)
    last_name = models.CharField(max_length=45, null=True, blank=True)
    first_name_2 = models.CharField(max_length=45, null=True, blank=True)
    last_name_2 = models.CharField(max_length=45, null=True, blank=True)
    attending = models.BooleanField(blank=True)
    primary_email = models.EmailField(max_length=254, null=True, blank=True)
    street_addr = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    event = models.ForeignKey('Event', null=True, blank=True, default=1)
    groom = models.BooleanField(default=False)
    relation = models.PositiveSmallIntegerField(choices=RELATION_ANSWERS)
    invitation = models.ForeignKey('Invitation', blank=True, null=True, on_delete=models.SET_NULL,
        verbose_name=u'Invitation letter guest is assigned')
    def full_name(self):
        x = str('{0} {1}'.format(self.first_name, self.last_name))
        return x
    def __str__(self):  
        return self.full_name()