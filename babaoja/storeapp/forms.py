from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


from django import forms
from .models import Profile

class ProfilePicForm(forms.ModelForm):
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': '+2348100000'}))
    address = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': '1234 Elm Street'}))
    city = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'Springfield'}))
    state = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'IL'}))
    zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': '62704'}))
    country = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'USA'}))
    
    profile_images = forms.ImageField(label="", widget=forms.FileInput(attrs={'class': 'form-control'}))
    profile_bio = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control input-box', 'placeholder': 'Write a short bio...'}))
    
    homepage_link = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'https://example.com'}))
    facebook_link = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'https://facebook.com/yourprofile'}))
    instagram_link = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'https://instagram.com/yourprofile'}))
    linkedin_link = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'https://linkedin.com/in/yourprofile'}))
    x_link = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'https://x.com/yourprofile'}))

    class Meta:
        model = Profile
        fields = ['phone', 'address', 'city', 'state', 'zipcode', 'country', 'profile_images', 'profile_bio',
                    'homepage_link', 'facebook_link', 'instagram_link', 'linkedin_link', 'x_link']




class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class input-box':'form-control', 'placeholder':'Email Address'}), required=True)
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control input-box', 'placeholder':'First Name'}), required=True)
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control input-box', 'placeholder':'Last Name'}), required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control input-box'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control input-box'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control input-box'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'