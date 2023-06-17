from django.contrib import admin
from .models import Member  #imports member database
#from .models import DNA

# Register your models here.

admin.site.register(Member) #registers to display on webpage

#admin.site.register(DNA)
