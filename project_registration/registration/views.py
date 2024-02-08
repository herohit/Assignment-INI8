from django.shortcuts import render,redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404

from . models import Registration
from .forms import RegistrationForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or show success message
            messages.success(request, ('Your data was successfully added!'))
            return redirect('create')
        else:
            messages.error(request, 'Error saving form')
    else:
      form = RegistrationForm()
    context={'form':form}
    return render(request,'registration/createForm.html',context)


def read(request):
    all_data = Registration.objects.all()
    context = {'all_data':all_data}
    return render(request,'registration/homepage.html',context)

def update(request,pk):
    instance = get_object_or_404(Registration, pk=pk)
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your data was successfully updated!')
            return redirect('create')
    else:
        form = RegistrationForm(instance=instance)
        
    context = {'form': form}
    return render(request, 'registration/createForm.html', context)


def delete(request,pk):
    obj = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('read')
    
    # Render a confirmation page for the user to confirm deletion
    return render(request, 'registration/deleteRecord.html', {'obj': obj})