from django import forms

class ImageUploadForm(forms.Form):
   usr_image = forms.FileField()
   
