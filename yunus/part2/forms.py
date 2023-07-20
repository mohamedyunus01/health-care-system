from django import forms
from .models import *


class AdmissionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdmissionForm,self).__init__(*args, **kwargs)
        TYPE_SELECT=(('Male','Male'),('Female','Female'),('Others','Others'))
        self.fields['gender'] = forms.ChoiceField(choices=TYPE_SELECT,widget=forms.RadioSelect())
      

    class Meta:
        model=admission
        exclude=['phc_id','admission_no','discharge_time','discharge_status','report']



class DischargeForm(forms.ModelForm):
     class Meta:
         model = admission
         fields=['admission_no','discharge_status']