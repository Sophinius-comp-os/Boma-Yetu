from django import  forms

from skapp.models import Contact, ImageModel, Booking


class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = '__all__'


class BookingForm(forms.ModelForm):
  class Meta:
    model = Booking
    fields = '__all__'


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'

