from django.shortcuts import render,redirect
from django.contrib import messages
from .models import TrackingHistory,CurrentBalance
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,login,logout
from django.contrib.auth.decorators import login_required



def logout_view(request):
    logout(request)
    return redirect('login_page')

# Create your views here.
@login_required(login_url='login_view')
def index(request):
    if request.method=="POST":
        current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
        amount=request.POST.get('amount')
        description=request.POST.get('description')
        expence_type="CREDIT"
        if float(amount) < 0:
            expence_type ="DEBIT"
        if float(amount) == 0:
            messages.success(request, "Amount cannot be zero") 
            return redirect('index')

        tracking_history= TrackingHistory.objects.create(
            current_balance=current_balance,
            expence_type=expence_type,
            amount=amount,
            description=description
        )
        print(amount,description)
        current_balance.current_balance +=float(tracking_history.amount)
        current_balance.save()
        return redirect('index')
    current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
    income=0
    expense=0
    for tracking_history in TrackingHistory.objects.all():
        if tracking_history.expence_type =="CREDIT":
            income += tracking_history.amount
        else:
            expense += tracking_history.amount

    context={'income': income,'expense':expense,'transactions':TrackingHistory.objects.all(),'current_balance':current_balance}
        

    return render(request,'index.html',context)

@login_required(login_url='login_view')
def delete_transaction(request,id):
    tracking_history=TrackingHistory.objects.filter(id=id)
    if tracking_history.exists():
        current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
        tracking_history=tracking_history[0]
        current_balance.current_balance -= tracking_history.amount
        current_balance.save()
    tracking_history.delete()
    return redirect('index')

      
def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.success(request, "user is already taken") 
            return redirect('register_page')
        
        user=User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created") 
        return redirect('register_page')



    

    return render(request,'register.html')


def login_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.filter(username=username)

        if not user.exists():
             messages.success(request, "Username not found") 
             return redirect('login_page')
        
        user=authenticate(username=username,password=password)
        if not user:
             messages.success(request, "Invalid Password") 
             return redirect('login_page')
            
        login(request,user)
        return redirect('index')



    return render(request,'login.html')