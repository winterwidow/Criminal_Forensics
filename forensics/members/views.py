from django.http import HttpResponse   #to get a response or goto the webpage
from django.template import loader
from django.shortcuts import render
import csv
from members.models import Member


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
    

#to display the details like dna  & fingerprints

def details(request, id):

    """ Contains all details of criminals """
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    
    context = {
        'mymember': mymember,
    }
    
    return HttpResponse(template.render(context, request))
    #return render(context, request)

#main page

def main(request):
    #return render(request,'main.html')
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def add_criminal(request):
    if request.method == "GET":
        return render(request,'add_criminal.txt')
        #template = loader.get_template('add_criminal.html')
        #return HttpResponse(template.render(request)) 

    elif request.method == 'POST':
        
        cr_firstname=request.POST['crfirstname']
        cr_lastname=request.POST['crlastname']
        cr_dna=request.POST['crdna']

        if request.GET['a'] =='CSV':                     #CSV FILES
            
            print("i am here")
            
            with open('CriminalDetails.csv','a',newline='') as csvfile:
                
                print("i am here 1")
                
                wcs=csv.writer(csvfile)
                wcs.writerow([cr_firstname,cr_lastname,cr_dna])
                
            print("i am here 2")
            
            return render(request,'main.html')
            
        else:
           return render (request,'main.html')
        
        '''else:                                           #DATABASE

            s= Member()           #function in models.py
            s.cr_firstname=cr_firstname
            s.cr_lastname=cr_lastname
            s.cr_dna=cr_dna
            s.save()
            return render(request,'main.html')
        '''
        
