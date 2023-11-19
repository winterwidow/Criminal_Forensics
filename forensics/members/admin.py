from django.contrib import admin
from .models import Member  #imports member database
#from .models import DNA

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("cr_firstname", "cr_lastname", "cr_image", "cr_fprint")

admin.site.register(Member, MemberAdmin) #registers to display on webpage

#admin.site.register(DNA)
