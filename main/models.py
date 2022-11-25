from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=254)
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otc = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, unique=True)


class coordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()


class level_diff(models.Model):
    season = models.CharField(max_length=10)
    difficulty = models.CharField(max_length=2)


class img(models.Model):
    data = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None)
    title = models.CharField(max_length=255)


class pereval_added(models.Model):
    status_choices = [
        ('new', 'new'),
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected')
    ]

    beautyTitle = models.CharField(max_length=50)
    title = models.CharField(max_length=50, unique=True)
    other_titles = models.CharField(max_length=50)
    connect = models.TextField(max_length=255)
    coords = models.ForeignKey(coordinates, on_delete=models.CASCADE)
    level = models.ForeignKey(level_diff, on_delete=models.CASCADE)
    images = models.ForeignKey(img, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=status_choices,
                              default=status_choices[0])
