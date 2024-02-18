from PIL import Image
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


class RoomCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Rooms(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(default=1)
    person = models.PositiveIntegerField(default=1, null=True, blank=True)
    size = models.PositiveIntegerField(default=1, null=True, blank=True)
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE,
                                 related_name='rooms')

    def __str__(self):
        return self.title


# RoomIMage Model    ------------------------------------------------------------

class RoomImage(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE,
                             related_name='images')
    image = models.ImageField(upload_to='rooms/')

    def __str__(self):
        return self.room.title

    def save(self, *args, **kwargs):
        # Call the parent class's save() method
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        max_width = 1400
        max_height = 1200

        if img.width > max_width or img.height > max_height:
            new_size = (max_width, max_height)
            img.thumbnail(new_size, Image.Resampling.LANCZOS)
            img.save(self.image.path)


@receiver(post_delete, sender=RoomImage)
def delete_social_network_image(sender, instance, **kwargs):
    # Delete the image file when the MainSocialNetwork instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=RoomImage)
def delete_blog_old_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)
        except sender.DoesNotExist:
            pass


# RoomImage End Model    ---------------------------------------------------------------------


# RoomFeatures Model    -------------------------------------------------------------------------
class RoomFeatures(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE,
                             related_name='features')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='roomfeatures/')

    def __str__(self):
        return self.room.title

    def save(self, *args, **kwargs):
        # Call the parent class's save() method
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        max_width = 600
        max_height = 400

        if img.width > max_width or img.height > max_height:
            new_size = (max_width, max_height)
            img.thumbnail(new_size, Image.Resampling.LANCZOS)
            img.save(self.image.path)


@receiver(post_delete, sender=RoomFeatures)
def delete_social_network_image(sender, instance, **kwargs):
    # Delete the image file when the MainSocialNetwork instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=RoomFeatures)
def delete_blog_old_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)
        except sender.DoesNotExist:
            pass


# RoomFeatures End Model    ----------------------------------------------------------------


# RoomAmenity Model    ----------------------------------------------------------------
class RoomAmenity(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE,
                             related_name='amenities')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='roomamenities/')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.room.title

    def save(self, *args, **kwargs):
        # Call the parent class's save() method
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        max_width = 600
        max_height = 400

        if img.width > max_width or img.height > max_height:
            new_size = (max_width, max_height)
            img.thumbnail(new_size, Image.Resampling.LANCZOS)
            img.save(self.image.path)


@receiver(post_delete, sender=RoomAmenity)
def delete_social_network_image(sender, instance, **kwargs):
    # Delete the image file when the MainSocialNetwork instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=RoomAmenity)
def delete_blog_old_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)
        except sender.DoesNotExist:
            pass


# RoomAmenity End Model    -------------------------------------------------------------------
class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_validator = RegexValidator(
        regex=r'^\d{9}$',
        message="Yaroqsiz telefon raqam!"
    )
    phone_number = models.CharField(
        max_length=9,
        validators=[phone_validator]
    )

    def __str__(self):
        return self.last_name
