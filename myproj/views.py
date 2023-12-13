from django.shortcuts import render,redirect
from django.contrib import messages
from myproj.models import members,employee,adminlogin

def trainer_login(request):
    if request.method =='POST':
        e_id=request.POST['e_id']
        password=request.POST['password']

        try:
            if e_id.startswith('e'):
                user=employee.objects.get(e_id=e_id,password=password)
                return redirect('trainer_success',user_id=user.id)
            else:
                messages.error(request,'Invalid Credentials. Please Try Again.')
        except employee.DoesNotExist:
            messages.error(request,'Invalid Credentials. Please Try Again.')

    return render(request,'elogin.html')


def trainer_success(request,user_id):
    try:
        user=employee.objects.get(id=user_id)
        context={'user':user}
        return render(request,'esuccess.html',context)
    except employee.DoesNotExist:
       return render(request,'error_page.html')


def trainer_reset_password_page(request,user_id):
    return render(request,'trainer_reset_password_page.html',{'user_id':user_id})

def reset_password(request,user_id):
    if request.method=='POST':
        new_password=request.POST['new_password']
        confirm_new_password=request.POST['confirm_new_password']

        try:
            user=employee.objects.get(id=user_id)

            if new_password==confirm_new_password:
                user.password=new_password
                user.save()
                messages.success(request,'Password Reset Sucessfully.')
            else:
                messages.error(request,'New Password And Confirm Password Do Not Match. Please Try Again.')
        except employee.DoesNotExist:
            messages.error(request,'User Not Found')
        
    return render(request,'trainer_reset_password_page.html',{'user_id':user_id})
