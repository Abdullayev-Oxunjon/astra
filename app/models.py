from django.core.validators import RegexValidator
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


class RoomImage(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE,
                             related_name='images')
    image = models.ImageField(upload_to='rooms/')

    def __str__(self):
        return self.room.title


class RoomFeatures(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE,
                             related_name='features')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='roomfeatures/')

    def __str__(self):
        return self.room.title


class RoomAmenity(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE,
                             related_name='amenities')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='roomamenities/')
    description = models.TextField(null=True, blank=True)

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


class Service(models.Model):
    image = models.ImageField(upload_to='services/')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE,
                                related_name='features')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='servicefeatures/')

    def __str__(self):
        return self.title


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


class Reviews(models.Model):
    name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


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
