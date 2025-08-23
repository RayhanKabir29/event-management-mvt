from django import forms
from events.models import Category,Event, Participant


class StyleDFormMixin:
    default_css_class = 'form-control'
    
    def apply_style_widget(self):
        for field_name, field in self.fields.items():
           if isinstance(field.widget, forms.widgets.TextInput) :
               field.widget.attrs.update({
                   'class': self.default_css_class,
                   'placeholder': f'Enter {field.label}'
               })
               
                
                
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'})
        }
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event Description'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Location'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'phone', 'participant_events']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Participant Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Participant Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Participant Phone'}),
            'participant_events': forms.SelectMultiple(attrs={'class': 'form-control'})
        }   
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_style_widget()