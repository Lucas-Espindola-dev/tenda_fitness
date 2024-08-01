from django import forms
from .models import Appointment, Time
from datetime import datetime


class AppointmentForm(forms.ModelForm):
    time = forms.ModelChoiceField(
        queryset=Time.objects.all(),
        widget=forms.RadioSelect,
        required=True,
        label="Horários",
    )

    class Meta:
        model = Appointment
        fields = ['day', 'time', 'repeat', ]
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date'},),
            'repeat': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['time'].queryset = Time.objects.none()

        if 'day' in self.data:
            try:
                day = self.data.get('day')
                self.fields['time'].queryset = Time.objects.filter(day=day).exclude(appointment__day=day)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['time'].queryset = self.instance.time.all()
