# Flight-Management
Simple django powered website to manage flight information.

Do path id change in dir list of FLIGHTINFO/setting.py!!!!  
Steps to follow Put this project folder into the django resident environment in the system. 
In cmd, move into this folder & do execute the below commands 
    -> manage.py makemigrations FLT //generate DB table 
    -> manage.py migrate //create table -> manage.py runserver //run it on local host 
Open broweser and put 
   -> "localhost:8000/flightInfo/SEARCHINFO/" to view flight informations
   -> "localhost:8000/flightInfo/UPDATEINFO/" to update the flight info
   -> "localhost:8000/flightInfo/SHOWINFO/" to show the available flights info
