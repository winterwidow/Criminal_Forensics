from .models import Member

class MemberDBRouter:
    def db_for_read (self, model, **hints):
        if(model==Member):
            return 'new'
        return none

    def db_for_write(self,model,**hints):
        if(model == Member):
            return 'new'
        return none
    
