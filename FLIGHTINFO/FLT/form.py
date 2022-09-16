

from django import forms
from FLT import models

class SearchForm(forms.Form):

    '''
    Provides form to get flight number.

    Attributes
    flight_num (int): To hold flight number
    '''

    flight_num = forms.IntegerField()

        

    
class FlightForm(forms.ModelForm):

    '''
    Provides form for FLIGHT model.

    class : Meta
            Contains needed option to be render in form

    '''
            

    class Meta:
        model = models.FLIGHT
        exclude = ('flight_num',)


        
