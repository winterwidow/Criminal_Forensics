from django.http import HttpResponse   #to get a response or goto the webpage
from django.template import loader
from django.shortcuts import render
import csv

#templates are text docs to connect html and django.
#written in django template lang
#Template loaders are responsible for locating templates, loading them, and returning Template objects.

from .models import Member     #member is a database to store all members' info
#from .models import DNA

# Create your views here.
def members(request):
    
    mymembers = Member.objects.all().values()

    #my_dna_mem= DNA.objects.all().values()
    template = loader.get_template('all_members.html')

    context = { 'mymembers': mymembers,}
    #context2= {'dnamembers' : my_dna_mem,}
    
    return HttpResponse(template.render(context,request))   #returns this to the webpage
    #return render(context,request)

#to display the details like dna  & fingerprints

def details(request, id):
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

'''#new from here: 03/06/23
def add_criminal(request):
    if request.method=="GET":
        return render(request,'add_criminal.html')
        #template = loader.get_template('add_criminal.html')
        #return HttpResponse(template.render(request)) 

    elif request.method=='POST':
        cr_firstname=request.POST['crfirstname']
        cr_lastname=request.POST['crlastname']
        cr_dna=request.POST['crdna']
        
        #template = loader.get_template('main.html')
        
        if request.GET['a'] =='csv':
            with open('criminalDetails.csv','a') as csvfile:
                wcs=csv.writer(csvfile)
                wcs.writerow([cr_firstname,cr_lastname,cr_dna])
            return render(request, 'main.html')
            #template=loader.get_template('main.html')
            #return HttpResponse(template.render(request))

        else:
            return render(request, 'main.html')
            #template=loader.get_template('main.html')
            #return HttpResponse(template.render(request))        
'''
