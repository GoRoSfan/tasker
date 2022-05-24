from django.db import models

# Create your models here.

class Point(models.Model):

    name = models.CharField(max_length=200, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))

    latitude = models.DecimalField(max_digits=9, decimal_places=6,
                                   verbose_name=_('Latitude'))
    longitude = models.DecimalField(max_digits=9, decimal_places=6,
                                    verbose_name=_('Longitude'))

    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True,
                             related_name='points', verbose_name=_('City'))

    class Meta:
        verbose_name = _('Point')
        verbose_name_plural = _('Points')
        unique_together = ('name', 'city')

    def __str__(self):
        return '{} ({})'.format(self.name, self.city.name)

    def __repr__(self):
        return 'Point({}, {}, {}, {})'.format(
            self.name, self.latitude, self.longitude, self.city.name)


class PointImage(models.Model):
    point = models.ForeignKey(Point, on_delete=models.CASCADE,
                              related_name='images', verbose_name=_('Point'))

    url = models.URLField(verbose_name='URL')

    class Meta:
        verbose_name = _('Point image')
        verbose_name_plural = _('Point images')

    def __str__(self):
        return str(self.pk)

    def __repr__(self):
        return 'PointImage({}, {})'.format(self.point.name, self.url)


class City(models.Model):

    name = models.CharField(max_length=100, verbose_name=_('Name'))

    latitude = models.DecimalField(max_digits=9, decimal_places=6,
                                   verbose_name=_('Latitude'))
    longitude = models.DecimalField(max_digits=9, decimal_places=6,
                                    verbose_name=_('Longitude'))

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'City({}, {}, {})'.format(self.name, self.latitude,
                                         self.longitude)

