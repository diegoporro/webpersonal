from django import forms


class Contact(forms.Form):
    First_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name...', }))
    Last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name...', }))
    Email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email@...', }))
    Phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1 222 58 47', }))

    def clean(self):
        First_name = self.cleaned_data.get("First_name")
        Last_name = self.cleaned_data.get("Last_name")
        Email = self.cleaned_data.get("Email")
        Phone_number = self.cleaned_data.get("Phone_number")

        return super(Contact, self).clean()
