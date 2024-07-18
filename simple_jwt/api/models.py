from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    ship = models.CharField(max_length=100)


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



# using signal we can easily generate token with this code
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)