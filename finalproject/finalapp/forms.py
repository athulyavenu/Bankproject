from django import forms
from .models import Person, Branch, District
from . widgets import DatePickerInput
from django.contrib.auth.forms import UserCreationForm

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'birthdate', 'age', 'gender', 'phone_num', 'mail_id', 'address', 'district', 'branch', 'accounttype', 'creditcard', 'debitcard')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birthdate'] = forms.DateField(widget=DatePickerInput)
        self.fields['gender'] = forms.ChoiceField(choices=[('Male','Male'), ('Female','Female'),('Does not wish to specify','Does not wish to specify')], widget=forms.RadioSelect)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')

