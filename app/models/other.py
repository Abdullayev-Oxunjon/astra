from PIL import Image
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


# MainSocialNetwork Model    ------------------------------------------------
class MainSocialNetwork(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='social_networks/')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Call the parent class's save() method
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        max_width = 800
        max_height = 600

        if img.width > max_width or img.height > max_height:
            new_size = (max_width, max_height)
            img.thumbnail(new_size, Image.Resampling.LANCZOS)
            img.save(self.image.path)


@receiver(post_delete, sender=MainSocialNetwork)
def delete_social_network_image(sender, instance, **kwargs):
    # Delete the image file when the MainSocialNetwork instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=MainSocialNetwork)
def delete_blog_old_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)
        except sender.DoesNotExist:
            pass


# MainSocialNetwork End Model    ------------------------------------------------


# Features Model    -------------------------------------------------------------
class Features(models.Model):
    image = models.ImageField(upload_to='features/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Call the parent class's save() method
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        max_width = 800
        max_height = 600

        if img.width > max_width or img.height > max_height:
            new_size = (max_width, max_height)
            img.thumbnail(new_size, Image.Resampling.LANCZOS)
            img.save(self.image.path)


@receiver(post_delete, sender=Features)
def delete_social_network_image(sender, instance, **kwargs):
    # Delete the image file when the MainSocialNetwork instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=Features)
def delete_blog_old_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)
        except sender.DoesNotExist:
            pass


# Features End Model    -------------------------------------------------------------


class Contact(models.Model):
    name = models.CharField(max_length=155)
    phone_validator = RegexValidator(
        regex=r'^\d{9}$',
        message="Yaroqsiz telefon raqam!"
    )
    phone_number = models.CharField(
        max_length=9,
        validators=[phone_validator]
    )
    message = models.TextField()

    def __str__(self):
        return self.name
