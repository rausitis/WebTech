from .models import Code
from django.db.models.signals import post_save
from django.dispatch import receiver
from TwoFAUserApp.models import TwoFAUser


@receiver(post_save, sender=TwoFAUser)
def post_save_generate_code(sender, instance, created, *args, **kwargs):
    if created:
        Code.objects.create(user=instance)
