from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    mobile=models.CharField(max_length=20)
    password=models.CharField(max_length=200)
    
    #checking if email is exiting or not
    def isexit(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
    
    #to check email id is matching or not
    @staticmethod
    def getemail(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return None
            