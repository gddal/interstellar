from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from interstellar.forms import OrderForm


def index(request):
    context = {"title": "Ola"}
    return render(request, "index.html", context)


def create_order(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST)
        breakpoint()
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # se der match ver pedidos, TEMPORARIO
            # redirect to a new URL:
            return render(request, 'templates/preview.html')
        return HttpResponse({'Bad Request': 'Invalid data...'})


    # if a GET (or any other method), TEMPORARIO
    else:
        form = OrderForm()

    return render(request, 'order.html', {'form': form})



