from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save,sender= User)
def add_group(sender,instance ,created,**kwargs):
    if created:
       pass


