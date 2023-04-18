from django.db import models


class ListOfCountries(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Regions(models.Model):
    country = models.ForeignKey(ListOfCountries, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Tours(models.Model):
    country = models.ForeignKey(ListOfCountries, on_delete=models.CASCADE)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(upload_to='tours/', default='tours/tours-default.jpg')
    short_desc = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    availability = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    room_desc = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    @staticmethod
    def get_items():
        return Tours.objects.filter(is_active=True).order_by('country', 'region', 'name')

    def __str__(self):
        return f'{self.name} ({self.country.name})'
