from django import forms
from .models import Event

from racetrackschedules.common.forms import BaseForm


class EventForm(BaseForm):
    class Meta:
        model = Event
        fields = ['name', 'racetrack']
