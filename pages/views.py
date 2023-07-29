from django.shortcuts import HttpResponse, render

texts = [
    "Текст 1",
    "Текст 2",
    "Текст 3",
]

def index_view(request):
    context = {
        "page_text": "Это главная страница!!!!!!"
    }
    return render(request, "inapptemp.html", context)


def get_users(request, id):
    context = {
        "page_text": texts[id]
    }
    # image = get_image_from_neural(...)
    return render(request, "pages/users.html", context)
