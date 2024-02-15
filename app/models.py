from django.db import models


class MainSocialNetwork(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='social_networks/')

    def __str__(self):
        return self.name


class Features(models.Model):
    image = models.ImageField(upload_to='features/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Rooms(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(default=1)
    person = models.PositiveIntegerField(default=1, null=True, blank=True)
    size = models.PositiveIntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return self.title


class RoomImage(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE,
                             related_name='images')
    image = models.ImageField(upload_to='rooms/')

    def __str__(self):
        return self.room.title


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


class Service(models.Model):
    image = models.ImageField(upload_to='services/')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Visitors(models.Model):
    visitor_title = models.CharField(max_length=255)
    visitor_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.visitor_title


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
