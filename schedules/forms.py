from django import forms
from .models import Appointment, Time


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['day', 'time', 'repeat', ]
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'day' in self.data:
            try:
                day = self.data.get('day')
                self.fields['time'].queryset = Time.objects.exclude(
                    id__in=Appointment.objects.filter(day=day).values_list('time_id', flat=True)
                )
            except (ValueError, TypeError):
                pass
        else:
            self.fields['time'].queryset = Time.objects.none()
