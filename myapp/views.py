from django.shortcuts import render,HttpResponse
from .forms import FormPeople
from .models import People

def index(request):
    people = People.objects.all()
    form = FormPeople
    box = People.objects.filter(sport_section='box').count()
    wrestling = People.objects.filter(sport_section='wrestling').count()
    wushu = People.objects.filter(sport_section='wushu').count()
    places = {"box_max": 10, "wrestling_max": 200, "wushu_max": 10}
    places["box_free"] = places["box_max"] - box
    places["wrestling_free"] = places["wrestling_max"] - wrestling
    places["wushu_free"] = places["wushu_max"] - wushu
    message = ""
    if request.method == "POST":
        flag = True
        message = "Не удалось записаться"
        for el in people:
            if request.POST["phone"] == el.phone:
                flag = False
        if places[request.POST["sport_section"] + '_free'] == 0:
            flag = False
        if flag == True:
            form = FormPeople(request.POST)
            if form.is_valid():
                form.save()

                box = People.objects.filter(sport_section='box').count()
                wrestling = People.objects.filter(sport_section='wrestling').count()
                wushu = People.objects.filter(sport_section='wushu').count()
                places["box_free"] = places["box_max"] - box
                places["wrestling_free"] = places["wrestling_max"] - wrestling
                places["wushu_free"] = places["wushu_max"] - wushu

                message = "Ваша запись сохранена"

    data = {"form": form, "places": places, "message": message}
    users = People.objects.all()

    for user in users:
        print("Имя:", user.name, "Телефон:", user.phone, "Спортивная секция:", user.sport_section)
    print(box, wrestling, wushu)

    return render(request, "index.html", data)
