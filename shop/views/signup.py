from django.shortcuts import render
from django.http import HttpResponse
from shop.models.product import Product
from shop.models.category import Category
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from shop.models.customer import Customer
from django.views import View  # Correct import for class-based views


#class based view
class signup(View):
    def get(self,request):
        return render(request,'signup.html')
        
    def post(self,request):
        fn=request.POST['fn']
        ln=request.POST['ln']
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=request.POST['password']
        password=make_password(password)
        userdata=[fn,ln,email,mobile,password]
        print(userdata)
        uservalues={'fn':fn,'ln':ln,'email':email,'mobile':mobile,'password':password}
        
        #storing object
        customerdata=Customer(first_name=fn,last_name=ln,email=email,mobile=mobile,password=password) #obj=field name from customer.py = variablename
        
        #validation
        error_msg=None
        success_msg=None
        if(not fn):
            error_msg="first name not found"
        elif(not ln):
            error_msg="LAST name not found"
        elif(not email):
            error_msg="email not found"
        elif(not mobile):
            error_msg="mobile not found"
        elif(not password):
            error_msg="password not empty"
        elif(customerdata.isexit()):
            error_msg="email already exists"
        if(not error_msg):
            success_msg="account created successfully"
            customerdata.save()
            msg={'success':success_msg}
            #return render(request,'signup.html',msg)
            return redirect('login')
        else:       
            msg={'error':error_msg,'value':uservalues}                    
            return render(request,'signup.html',msg)
