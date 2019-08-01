from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

# https://docs.djangoproject.com/zh-hans/2.1/ref/signals/#module-django.db.models.signals
# https://www.django-rest-framework.org/api-guide/authentication/#generating-tokens


@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()
