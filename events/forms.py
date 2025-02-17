from django import forms
from events.models import Event, Participant

class StyledFormMixin:
    default_classes = "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-teal-500 focus:ring-teal-500"
    
    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}"
                }) 
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} resize-none",
                    'placeholder': f"Enter {field.label.lower()}",
                    'rows': 5
                })
            elif isinstance(field.widget, forms.DateInput):
                field.widget.attrs.update({
                    "type": "date",
                    "class": self.default_classes
                })
            elif isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({
                    "type": "time",
                    "class": self.default_classes
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': "space-y-2"
                })
            else:
                field.widget.attrs.update({
                    'class': self.default_classes
                })

class EventForm(StyledFormMixin, forms.ModelForm):
    participants = forms.ModelMultipleChoiceField(
        queryset=Participant.objects.all(),  # Fetch all participants
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Select Participants"
    )

    class Meta:
        model = Event
        exclude = ['category']  # Exclude category if not needed in the form
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
