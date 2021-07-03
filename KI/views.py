from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required


def test_response(request):

    all = Book.objects.all()
    return render(request, "index.html", {'book': all})

def nowa_ksiazka(request):
    form = BookForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(test_response)
    return render(request, 'ksiazka_form.html', {'form': form})

@login_required
def edytuj_ksiazke(request, id):
    book = get_object_or_404(Book, pk=id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect(test_response)

    return render(request, 'ksiazka_form.html', {'form': form})

@login_required
def usun_ksiazke(request, id):
    book = get_object_or_404(Book, pk=id)

    if request.method == 'POST':
        book.delete()
        return redirect(test_response)

    return render(request, 'potwierdz.html', {'book': book})




# Create your views here.
