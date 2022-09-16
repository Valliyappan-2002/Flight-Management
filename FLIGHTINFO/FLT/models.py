

from django.db import models


class FLIGHT(models.Model):

    '''
    Create flight entry in database.

    Attribute:
    flight_num (int)
    dest       (string)
    dist       (string)
    quant      (int)

    Methods:
    __str__ : returns string representation of a class
    flightDet : returns the dict contains attributes & values of the class

    '''
 
    flight_num = models.SmallIntegerField(primary_key = True)
    dest = models.CharField(max_length = 20)
    dist = models.SmallIntegerField()
    quant = models.SmallIntegerField()

    def __str__(self):
        return str(self.flight_num) + ' - ' + str(self.dest) + ' - ' +\
               str(self.dist) + ' - ' + str(self.quant)

    def flightDet(self):
        dct = { 'flight_num': self.flight_num, \
                'dest' : self.dest, \
                'dist': self.dist, \
                'quant': self.quant
                }

        return dct
    


    


    
