from django.shortcuts import render
from .forms import ParticipantForm

def register(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'register.html', {
                'success': True,
                'form': ParticipantForm()
            })
    else:
        form = ParticipantForm()
    
    return render(request, 'register.html', {'form': form})