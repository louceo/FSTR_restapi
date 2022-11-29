from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=254)
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otc = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, unique=True)
    


class Coordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()


class Level_diff(models.Model):
    winter = models.CharField(max_length=2)
    summer = models.CharField(max_length=2)
    autumn = models.CharField(max_length=2)
    spring = models.CharField(max_length=2)


class Img(models.Model):
    data = models.ImageField(
        upload_to='files/images')
    title = models.CharField(max_length=255)


class Pereval_added(models.Model):
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coordinates, on_delete=models.CASCADE)
    level = models.ForeignKey(Level_diff, on_delete=models.CASCADE)
    images = models.ManyToManyField(Img)
    status = models.CharField(max_length=10, choices=status_choices,
                              default=status_choices[0])

