from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record, Project, Sample, Store

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        
# Create add record form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")
    
    class Meta:
        model = Record
        exclude = ("user",)
        
        
class NewProjectForm(forms.ModelForm):    
    class Meta:
        model = Project
        fields = '__all__'
        
    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['owner_name'].widget.attrs.update({"class": "form-control"})
    #    # or iterate over field to add class for each field
    #    for field in self.fields:
    #        self.fields[field].widget.attrs.update({'class':"form-control"})
    
    
class AddSampleForm(forms.ModelForm):
    sample_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Sample Number", "class":"form-control"}), label="")
    sample_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Sample Name", "class":"form-control"}), label="")
    project_number = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.Select(attrs={'id': 'my-select', "placeholder":"Project Number", "class":"form-control"}), initial='0', label="")
    
    class Meta:
        model = Sample
        exclude = ("sample",)
        
        
class StoreForm(forms.ModelForm):
    sample_id = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Sample ID", "class":"form-control"}), label="")
    fridge_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Fridge Number", "class":"form-control"}), label="")
    rack = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Rack", "class":"form-control"}), label="")
    dore = forms.BooleanField(required=True, widget=forms.widgets.CheckboxInput(), label="Is Door")
    
    class Meta:
        model = Store
        exclude = ("store",)
        
            
from .models import Person, City


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')