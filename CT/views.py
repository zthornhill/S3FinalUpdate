from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

now = timezone.now()


def home(request):
    return render(request, 'CT/home.html',
                  {'CT': home})


@login_required
def client_list(request):
    client = Client.objects.filter(created_date__lte=timezone.now())
    return render(request, 'CT/client_list.html',
                  {'clients': client})


@login_required
def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        # update
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.updated_date = timezone.now()
            client.save()
            client = Client.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/client_list.html',
                          {'clients': client})
    else:
        # edit
        form = ClientForm(instance=client)
    return render(request, 'CT/client_edit.html', {'form': form})


@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('CT:client_list')


@login_required
def mealtrack_list(request):
    mealtracks = MealTracker.objects.filter(created_date__lte=timezone.now())
    return render(request, 'CT/mealtrack_list.html', {'mealtracks': mealtracks})


@login_required
def mealtrack_new(request):
    if request.method == "POST":
        form = MealTrackerForm(request.POST)
        if form.is_valid():
            mealtracks = form.save(commit=False)
            mealtracks.created_date = timezone.now()
            mealtracks.save()
            mealtracks = MealTracker.objects.filter(created_date__lte=timezone.now())
            return render(request, 'CT/mealtrack_list.html',
                          {'mealtracks': mealtracks})
    else:
        form = MealTrackerForm()
        # print("Else")
    return render(request, 'CT/mealtrack_new.html', {'form': form})


@login_required
def mealtrack_edit(request, pk):
    mealtrack = get_object_or_404(MealTracker, pk=pk)
    if request.method == "POST":
        form = MealTrackerForm(request.POST, instance=mealtrack)
        if form.is_valid():
            mealtrack = form.save()
            # mealtrack.client = mealtrack.id
            mealtrack.updated_date = timezone.now()
            mealtrack.save()
            mealtracks = MealTracker.objects.filter(created_date__lte=timezone.now())
            return render(request, 'CT/mealtrack_list.html', {'mealtracks': mealtracks})
    else:
        # print("else")
        form = MealTrackerForm(instance=mealtrack)
    return render(request, 'CT/mealtrack_edit.html', {'form': form})


@login_required
def mealtrack_delete(request, pk):
    mealtrack = get_object_or_404(MealTracker, pk=pk)
    mealtrack.delete()
    return redirect('CT:mealtrack_list')
