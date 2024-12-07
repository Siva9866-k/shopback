from django.shortcuts import render
from django.http import HttpResponse
from .product import Product
from .category import Category
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .customer import Customer
# Create your views here.
def home(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    categoryId=request.GET.get('category')
    if categoryId:
        products=Product.get_category_id(categoryId)
    else:
        products=Product.objects.all()   
    data={'products':products,'categories':categories}
    return render(request,'index.html',data)

#signup form
def signup(request):
    if request.method=='GET':
        return render(request,"signup.html")
    else:
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

#login page
def login(request):
    if request.method=='GET':
       return render(request,'login.html')
    else:
        email=request.POST['email']
        password=request.POST['password'] 
        #to check email found or not
        users=Customer.getemail(email)
        error_msg=None
        if users:
            #if email found check password
            check=check_password(password,users.password)
            #if password found
            if check:
                return redirect('/')
            else:
                error_msg="passwoord not found"
                msg={'error':error_msg}
                return render(request,'login.html',msg)
        else:
            error_msg="email not found"
            msg={'error':error_msg}
            return render(request,'login.html',msg)    
            
         
        
        
    