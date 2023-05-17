from django.shortcuts import render
from .forms import VoteForm


def vote(request):
    vote_form = VoteForm()

    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'success.html', {'form': vote_form})

    return render(request, 'index.html', {'form': vote_form})


def success(request):
    return render(request, 'success.html')
