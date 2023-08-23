from django.http import HttpResponse   #to get a response or goto the webpage
from django.template import loader
from django.shortcuts import render
import csv
from members.models import Member
#import mysql.connector

from .FRforms import ImageUploadForm
from django.conf import settings
import face_recognition
import os

#templates are text docs to connect html and django.
#written in html
#Template loaders are responsible for locating templates, loading them, and returning Template objects.

from .models import Member     #member is a database to store all members' info


# Create your views here.

def members(request):
    
    """ Contains all criminals in the database  """
    
    mymembers = Member.objects.all().values()

    
    template = loader.get_template('all_members.html')

    context = { 'mymembers': mymembers,}
    
    print("Member once complete")
    return HttpResponse(template.render(context,request))   #returns this to the webpage
    
#-----------------------------------------------------------------------------------------------


#main page

def main(request):

    '''Main Page'''
    
    #return render(request,'main.html')
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

#-----------------------------------------------------------------------------------------------

def add_criminal(request):

    ''' Adds a criminal to database '''
    
    if request.method == "GET":   #input data
        
        return render(request,'add_criminal.txt')
        #template = loader.get_template('add_criminal.html')
        #return HttpResponse(template.render(request)) 

    elif request.method == 'POST':   #save data to db/csv
        
        cr_firstname=request.POST['crfirstname']
        
        cr_lastname=request.POST['crlastname']
        
        cr_gender=request.POST['crgender']
        
        cr_crime=request.POST['crime']
        
        cr_weapon=request.POST['weapon']
        
        cr_date=request.POST['date']
        

        if request.GET['a'] =='CSV':                     #CSV FILES
            
            print("i am here")
            
            with open('CriminalDetails.csv','a',newline='') as csvfile:
                
                print("i am here 1")
                
                wcs=csv.writer(csvfile)

                #wcs.writerow(['FirstName','LastName','Gender','Crime','Weapon','Date'])
                #wcs.writerow([cr_firstname,cr_lastname,cr_dna])
                wcs.writerow([cr_firstname,cr_lastname,cr_gender,cr_crime,cr_weapon,cr_date])
                
            print("i am here 2")
            
            return render(request,'main.html')
            
        #else:
           #return render (request,'main.html')
        
        
        else:                                           #DATABASE

            s= Member()           #function in models.py
            
            s.cr_firstname=cr_firstname
            s.cr_lastname=cr_lastname
            s.cr_gender=cr_gender
            s.cr_crime=cr_crime
            s.cr_weapon=cr_weapon
            s.cr_date=cr_date
            
            print("i am here")
            
            s.save()
            
            return render(request,'main.html')
        
#-----------------------------------------------------------------------------------------------
        
        
def fetch_criminals(request):

    ''' To fetch all criminals and dsiplay their information '''

    s_list=Member.objects.all()
    
    print(s_list)
    
    return render(request,'criminal.txt', {'s_lst':s_list})
    
#-----------------------------------------------------------------------------------------------

def search_criminals(request):
    if request.method == "GET":   #input the file
        
        return render(request,'fingerprint.txt')

    #elif request.method == 'POST':  #process file

#-----------------------------------------------------------------------------------------------    

def load_known_faces(known_faces_dir):
    known_faces = {}
    for filename in os.listdir(known_faces_dir):       
        name = os.path.splitext(filename)[0]        
        image = face_recognition.load_image_file(os.path.join(known_faces_dir, filename))       
        face_encoding = face_recognition.face_encodings(image)[0]
        if len(face_encoding)>0:
            known_faces[name] = face_encoding
    return known_faces

def recognize_faces_in_image(image_path, known_faces):
    user_image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(user_image)    
    face_encodings = face_recognition.face_encodings(user_image, face_locations)

    if len(face_encodings)>0:
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(list(known_faces.values()), face_encoding)
            name = "Criminal not found in our database"

            face_distances = face_recognition.face_distance(list(known_faces.values()), face_encoding)
            best_match_index = int(face_distances.argmin())
            if matches[best_match_index]:
                name = list(known_faces.keys())[best_match_index]
            print(f"Name: {name}")
        return name
    else:
        return("Face not detected in uploaded image")

def facial_recognition(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user_image = request.FILES['image']            
            known_faces_dir = settings.MEDIA_ROOT/'known_criminals/'
            known_faces = load_known_faces(known_faces_dir)
            match = recognize_faces_in_image(user_image, known_faces)            
            
            return render(request, 'faceRecog_result.html', {
                   'recognized_name': match,
                   } )                   
        
    else:
        form = ImageUploadForm()
    
    return render(request,'facial_recognition.html',{'form': form}) 


        

    
