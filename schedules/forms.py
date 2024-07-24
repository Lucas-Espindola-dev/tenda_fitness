from django import forms
from .models import Appointment, Time
from datetime import datetime


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['day', 'time', 'repeat', ]
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'initial': datetime.today, },),
            'time': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }
        labels = {
            'day': 'Data',
            'time': 'Horário',
            'repeat': 'Repetir Semanalmente'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'day' in self.data:
            try:
                day = self.data.get('day')
                if day:
                    day = datetime.strptime(day, '%Y-%m-%d').date()
                    self.fields['time'].queryset = Time.objects.exclude(
                        id__in=Appointment.objects.filter(day=day).values_list('time_id', flat=True)
                    )
            except (ValueError, TypeError):
                pass
        else:
            self.fields['time'].queryset = Time.objects.all()
