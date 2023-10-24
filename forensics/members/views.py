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

    def search_criminals(request):

    ''' Search By fingerprint '''
    
    if request.method == "GET":   #input the file
        
        return render(request,'fingerprint.txt')

    elif request.method == 'POST':  #process file

        sample=cv2.imread("  ")

    #sample=cv2.resize(sample, None, fx=2.5,fy=2.5)
    #cv2.imshow("sample",sample)
    #cv2.waitKey(0)


    best_score=0
    image=filename=None
    kp1,kp2,mp=None,None,None

    l=[file for file in os.listdir("SOCOFing/Real")]

    counter=0
    
    for file in l[:1000]:
        
        if counter%50==0:
            
            print(counter)
            
        counter+=1
        fingerprint_image=cv2.imread("SOCOFing/Real/"+file)
        sift=cv2.SIFT_create()

        keypoints1, descriptors1=sift.detectAndCompute(sample,None)
        keypoints2, descriptors2=sift.detectAndCompute(fingerprint_image,None)

        matches=cv2.FlannBasedMatcher({'algorithm':1,'trees':10},{}).knnMatch(descriptors1,descriptors2,k=2)


        match_points=[]

        for p,q in matches:
            
            if p.distance<0.1*q.distance:
                
                match_points.append(p)


        keypoints=0

        if len(keypoints1)<len(keypoints2):
            
            keypoints=len(keypoints1)
            
        else:
            
            keypoints=len(keypoints2)


        if len(match_points)/keypoints * 100 >best_score:
            
            best_score=len(match_points)/keypoints * 100

            filename=file
            image=fingerprint_image
            kp1=keypoints1
            kp2=keypoints2
            mp=match_points


    #print("best match:"+filename)
    #print("score:"+str(round(best_score,3)))

    result=cv2.drawMatches(sample, kp1, image,kp2,mp,None)
    result=cv2.resize(result,None, fx=4,fy=4)
    #cv2.imshow("Result",result)
    cv2.waitKey(0)

    #return render(request, 'fingerprint-result.html')

#-----------------------------------------------------------------------------------------------    

# Loads the images of known faces from directory , extracts the facial encodings and stores in a dictionary  
    
def load_known_faces(known_faces_dir):
    known_faces = {}  
    
    for filename in os.listdir(known_faces_dir):       
        name = os.path.splitext(filename)[0]        

        # Returns 'image', a numpy array with image file contents
        image = face_recognition.load_image_file(os.path.join(known_faces_dir, filename))

        # Get the face encodings
        face_encoding = face_recognition.face_encodings(image)[0]        
        
        # Dictionary 'known_faces' has filename as key and facial encodings as value   
        if len(face_encoding)>0:
            known_faces[name] = face_encoding
    return known_faces

def recognize_faces_in_image(user_image_name, known_faces):

    # Returns 'user_image', a numpy array with image file contents
    user_image = face_recognition.load_image_file(user_image_name)    

    # Returns 'user_face_locations', a list of tuples of found face locations in (top, right, bottom, left) order    
    user_face_locations = face_recognition.face_locations(user_image)   

    # Returns 'face_encodings', a list of 128-dimensional face encodings (one for each face in the image)
    user_face_encodings = face_recognition.face_encodings(user_image, user_face_locations)
    
    if len(user_face_encodings)>0: # Check if face is present in image

        for face_encoding in user_face_encodings:
            
            # Compare the known list of face encodings against user image encoding to see if they match
            # Returns 'matches', a list of True/False values indicating which known_face_encodings match
            # the user image face encoding. 
            matches = face_recognition.compare_faces(list(known_faces.values()), face_encoding)
            

            # Compare user face encoding with every known face encoding and get a euclidean distance for
            # each comparison. The distance shows how similar the faces are.
            # Returns 'face_distances', a numpy ndarray.         
            face_distances = face_recognition.face_distance(list(known_faces.values()), face_encoding)
            
            best_match_index = int(face_distances.argmin()) # Returns the index of the minimum value           
            
            if matches[best_match_index]: 
                name = list(known_faces.keys())[best_match_index] # From the index get the name of the known face
            else:
                name = "1" # For criminal not found
            
        return name
    else:
        return("0") # For face not detected in uploaded image

def facial_recognition(request):
    
    if request.method == 'POST': 
        
        # create a form instance and populate it with data from the request:
        myForm = ImageUploadForm(request.POST, request.FILES)

        
        if myForm.is_valid(): #Process the data and redirect to result page
            
            imageName = request.FILES['usr_image']  # User uploaded image name          
            known_faces_dir = settings.MEDIA_ROOT/'known_criminals/' # Directory where images are stored
            
            # Returns 'known_faces', a dictionary with filename as key and facial encodings as value
            known_faces = load_known_faces(known_faces_dir)

            # Compares facial encodings of user uploaded image with known facial encodings dictionary
            match = recognize_faces_in_image(imageName, known_faces)          

            error=""
            mymember=""
            
            if (match=="1"):
                error = "Criminal not found in our database"
            elif(match=="0"):
                error = "Face not detected in uploaded image"
            else:    
                img = 'known_criminals/'+ match +'.jpg' # Construct image path as stored in db                          
                mymember = Member.objects.get(cr_image=img) # Use image path to get details
                print(mymember.cr_firstname)               

            return render(request,'criminal_details.html',{'mymember': mymember,'error': error})
            
        
    else: # If GET request create an empty form. Called first time we visit the url.
        myForm = ImageUploadForm()

    # Returns the form to the template html file to render.
    # An empty form is rendered if coming here from GET    
    # A populated form with previously entered data is rendered
    # if coming here from is_valid()=False    

    return render(request,'facial_recognition.html',{'form': myForm}) 


        

    
