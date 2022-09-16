
from django.shortcuts import render
from FLT import form
from django.http import HttpResponseRedirect, HttpResponse
from FLT.models import FLIGHT


#Put the template directory path in Template['Dir'] in setting to be loaded by get_template

def searchInfo(request):

    '''
    Search in FLIGHT table for the given flight number.

    Returns:
       return HttpResponse for get & post request
    Exception:
       Throws exception if flight entry isn\'t in database table
    '''
    
    if request.method == 'POST':
        sf = form.SearchForm(request.POST)
        if sf.is_valid():
            try:
                flight = FLIGHT.objects.filter(flight_num = int(request.POST['flight_num']))
                return render(request, 'showRes.txt', {'flights': flight, 'obj':'Search Result'})
            except Exception as e:
                return HttpResponse('Alas!, There\'s no entry with given flight number : '+str(e))
        else:
            return render(request, 'searchInfo.txt', {'form':sf, 'obj':'Search Info'})            
    else:
        frm = form.SearchForm()
        return render(request, 'searchInfo.txt', {'form':frm, 'obj':'Search Info'})


def updateInfo(request):

    '''
    Update the entry in FLIGHT table for the given flight number.

    Returns
       return HttpResponse for get & post request for update & search page res.
    '''
    
    
    if request.method == 'POST':
        sf = form.SearchForm(request.POST)
        if sf.is_valid():
            try:
                flight = FLIGHT.objects.get(flight_num = int(request.POST['flight_num']))
                #Creating with preexisting values
                rc = request.POST.copy()
                rc['dest'] = flight.dest
                rc['dist'] = flight.dist
                rc['quant'] = flight.quant
                nf = form.FlightForm(rc , instance = flight) 
                return render(request, 'update12.txt', {'form': nf, 'obj':'Flight update', 'flight_num':flight.flight_num})
            except Exception as e:
                #Infer that entry is not there in table
                return HttpResponse('Alas!, There\'s no entry with given flight number : '+str(e))
        else:
            return render(request, 'searchInfo.txt', {'form':sf, 'obj':'Search Info'})            
    else:
        frm = form.SearchForm()
        return render(request, 'searchInfo.txt', {'form':frm, 'obj':'Search Info'})


def storeUpdate(request, fn):

    '''
    Updates the flight entry in FLIGHT table.

    Returns:
      return HttpResponseRedirect on successful updation.
             else return render with same page with showing exception

    '''
    
    if request.method == 'POST':
        flight = FLIGHT.objects.get(flight_num = int(fn))
        ff = form.FlightForm(request.POST, instance = flight)
        if ff.is_valid():
            #Valid, so save it
            ff.save()
            return HttpResponseRedirect('/flightInfo/SHOWINFO/')
        else:
            return render(request, 'update.txt', {'flights': ff, 'obj':'Flight update', 'flight_num':flight.flight_num})
    else:
        pass            
            
            
        

def showInfo(request):

    '''
    Display entries in FLIGHT table.

    Returns:
       render the page for displaying all entries
    '''

    #Retreiving all the entries in the table
    flights = FLIGHT.objects.all()
    return render(request, 'showRes.txt', {'flights': flights, 'obj': 'Flights Info'})
