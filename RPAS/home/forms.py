from django import forms
from .models import User_Profile, Video, PDFNotes

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ['name','profile_pic','message','email','subjects']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter name'})
        self.fields['profile_pic'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Pick Profile Picture'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Write your message'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Add your Email'})
        self.fields['subjects'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Pick your Subject'})



class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title','video_image', 'description', 'video_file']

    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter name'})
        self.fields['video_image'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Pick your Backgraund Image'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Write your Description'})
        self.fields['video_file'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Pick your Video'})


class PDFNotesForm(forms.ModelForm):
    class Meta:
        model = PDFNotes
        fields = ['title', 'pdf_file']

    
    def __init__(self, *args, **kwargs):
        super(PDFNotesForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter name'})
        self.fields['pdf_file'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Pick your pick PDF file'})
       