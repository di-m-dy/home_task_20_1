from django.shortcuts import render


def index(request):
    """
    Контроллер для главной страницы
    """
    return render(request, 'catalog/index.html')


def contacts(request):
    """
    Контроллер для страницы контактов
    """
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        context = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }
        return render(request, 'catalog/thanx.html', context)
    return render(request, 'catalog/contacts.html')
