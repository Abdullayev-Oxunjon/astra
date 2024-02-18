from PIL import Image
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


# Service Model    ------------------------------------------------------------
class Service(models.Model):
    image = models.ImageField(upload_to='services/')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Call the parent class's save() method
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        max_width = 1600
        max_height = 1400

        if img.width > max_width or img.height > max_height:
            new_size = (max_width, max_height)
            img.thumbnail(new_size, Image.Resampling.LANCZOS)
            img.save(self.image.path)


@receiver(post_delete, sender=Service)
def delete_social_network_image(sender, instance, **kwargs):
    # Delete the image file when the MainSocialNetwork instance is deleted
    instance.image.delete(save=False)


@receiver(pre_save, sender=Service)
def delete_blog_old_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)
        except sender.DoesNotExist:
            pass


# Service End Model    ----------------------------------------------------------


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Visitors(models.Model):
    visitor_title = models.CharField(max_length=255)
    visitor_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.visitor_title


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Reviews(models.Model):
    name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
