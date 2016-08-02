from django.core.urlresolvers import reverse
from django.db import models

from racetrackschedules.racetracks.models import Racetrack


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(null=True, blank=True)
    racetrack = models.ForeignKey(Racetrack, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('events:detail', args=[str(self.id)])
