from PIL import Image
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


# Blog Model    --------------------------------------------------------------
class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blogs/')
    description = models.TextField()
    mini_image = models.ImageField(upload_to='blogs/')
    short_description = models.TextField()
    author = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Call the parent class's save() method
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        mini_img = Image.open(self.mini_image.path)

        max_width = 1400
        max_height = 1200

        if img.width > max_width or img.height > max_height:
            new_size = (max_width, max_height)
            img.thumbnail(new_size, Image.Resampling.LANCZOS)
            img.save(self.image.path)

        if mini_img.width > max_width or mini_img.height > max_height:
            new_size = (max_width, max_height)
            mini_img.thumbnail(new_size, Image.Resampling.LANCZOS)
            mini_img.save(self.mini_image.path)


@receiver(post_delete, sender=Blog)
def delete_blog_image(sender, instance, **kwargs):
    # Delete the image file when the AboutBanner instance is deleted
    instance.image.delete(save=False)
    instance.mini_image.delete(save=False)


@receiver(pre_save, sender=Blog)
def delete_blog_old_image(sender, instance, **kwargs):
    # Delete the old image file when the AboutBanner instance is updated with a new image
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)
            if old_instance.mini_image != instance.mini_image:
                old_instance.mini_image.delete(save=False)
        except sender.DoesNotExist:
            pass


# Blog Model End  ----------------------------------------------------------------


class BlogComment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,
                             related_name='comments')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
