from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from products.models import Shop, Product, ProductShop


def test(request):
    print("bylem ty")
    return render(request, "shop.html")


def start(request):
    print('Starts')
    return render(request, 'index.html')


def login(request):
    url = request.POST.get('next', '/')
    print("JAka wartos: " + url)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print(HttpResponseRedirect(url))
            return HttpResponseRedirect(url)


        else:
            messages.info(request, 'invalid credentials')
            return render(request, 'login.html')



    else:
        url = request.GET.get('next', '/')
        print(url)
        return render(request, 'login.html', {'next': url})


def register(request):
    print(request.method)
    if request.method == 'POST':

        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if username == '' or password1 == '' or password2 == '' or email == '':
            print('Bylem tutaj')
            messages.info(request, 'Uzupełnij wszystkie pola!')
            return redirect('register')
        elif password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                )

                user.save()

                return redirect('login')
        else:
            messages.info(request, 'Password not maching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def search(request):
    print("Bylem w search")
    query = request.GET.get('q')
    print(query)
    if query is not None:
        results = Product.objects.filter(Q(name__icontains=query))
        test = []
        for p in results:
            product=ProductShop.objects.filter(product=p).order_by('price')
            print(product)
            for t in product:
                test.append(t)


        print(test)
        print(test.__len__())
        return render(request, "shop.html", {'category': test})
    else:
        products = Product.objects.all()
        return render(request, "shop.html", {'category': products})
