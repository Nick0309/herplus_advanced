from django.shortcuts import render, get_object_or_404, redirect
from .models import Meal, Order, OrderMeal
from .form import CustomerForm
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

cartlist = []


# Create your views here.

def home(request):
    return render(request,'app/home.html')

def show_menu(request):

    meals = Meal.objects.all()

    return render(request,'app/show_menu.html', locals())

def detail(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    return render(request, 'app/detail.html', locals())

def addcart(request, meal_id):
    global cartlist
    namelist = []
    templist = []
    addition = Meal.objects.get(pk=meal_id)

    for list in cartlist:
        namelist.append(list[0])

    if request.method == 'POST':
        unit = int(request.POST['unit'])
        if addition.name in namelist :
            index = namelist.index(addition.name)
            cartlist[index][2] += unit
        else:
            templist.append(addition.name)
            templist.append(addition.price)
            templist.append(unit)
            cartlist.append(templist)
    request.session['cartlist'] = cartlist

    return redirect('show_menu')

def show_cart(request):
    global cartlist
    cartlist1 = cartlist
    total = 0
    for list in cartlist1:
        total = total + list[1] * list[2]
    return render(request, 'app/show_cart.html', locals())

def update(request, add_id):
    global cartlist
    index = add_id - 1
    cartlist1 = cartlist[index]
    meal = Meal.objects.get(name=cartlist1[0])

    return render(request, 'app/update.html', locals())

def goupdate(request, add_id):
    global cartlist

    if request.method == "POST":
        try:
            if int(request.POST['unit']) > 0:
                cartlist[add_id][2] = int(request.POST['unit'])
            else:
                del cartlist[add_id]
            request.session['cartlist'] = cartlist
            return redirect('show_cart')
        except:
            message = '請輸入數字'
            return render(request, 'app/update.html', locals())

def delete(request, add_id):
    global cartlist
    if request.method == "POST":
        del cartlist[add_id-1]
    request.session['cartlist'] = cartlist
    return redirect('show_cart')

def fill_info(request):
    global cartlist
    cartlist1 = cartlist
    total = 0
    form = CustomerForm()

    for list in cartlist1:
        total = total + list[1] * list[2]

    if cartlist1 :
        return render(request, 'app/fill_info.html', locals())
    else:
        message = '您無點餐內容'
        return render(request, 'app/show_cart.html', locals())

def confirm(request):
    global cartlist
    cartlist1 = cartlist
    total = 0
    content = []
    text = ''
    order_no = ''
    character = list('1234567890')
    for i in range(10):
        order_no += random.choice(character)

    for thelist in cartlist1:
        total = total + thelist[1] * thelist[2]
        content.append(thelist[0])
        content.append(thelist[2])

    for i in range(0, len(content) - 1, 2):
        text = text + '\n' + " "*32 + f'{content[i]} {content[i + 1]}份'
        
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            if len(content) != 0:
                order = Order.objects.create(orderno=order_no, cname = name, cphone = phone, cmail = email, content=content, total_price = total)
                order.save()
                for thelist in cartlist1:
                    ordermeal = OrderMeal.objects.create(order=order, pname=thelist[0], unitprice=thelist[1], unit=thelist[2], subtotal=thelist[1]*thelist[2])
                    ordermeal.save()
                cartlist=[]
                request.session['cartlist'] = cartlist

                msg = f'''
                        您的訂餐內容如下
                        
                        姓名: {name} 
                        電話末三碼: {phone[-3:]} 
                        餐點: {text} 
                        總金額: {total} 元
                        
                        系統寄出請勿直接回覆, 請洽076318627
                        '''
                letter = MIMEMultipart()
                letter["subject"] = f"Her+ 訂單成功通知 單號:{order_no}"
                letter["from"] = "eu201352@gmail.com"
                letter["to"] = email
                letter.attach(MIMEText(msg))

                with smtplib.SMTP(host='smtp.gmail.com', port='587') as smpt:
                    smpt.ehlo()
                    smpt.starttls()
                    smpt.login('eu201352@gmail.com', 'fllrgrgzkmebaazd')
                    smpt.send_message(letter)

                return render(request, 'app/success.html', locals())
            else:
                return redirect('home')

def search(request):
    mealname =[]
    unit = []
    if request.method == 'POST':
        try:
            order_no = request.POST['order_no'].strip()
            order = Order.objects.get(orderno=order_no)
            ordermeal = OrderMeal.objects.filter(order=order)
            content = eval(order.content)
            for i in range(0,len(content)-1, 2):
                mealname.append(content[i])
            for i in range(1, len(content), 2):
                unit.append(content[i])
            content=zip(mealname,unit)
        except:
            message = '查無此訂單'

    return render(request, 'app/search.html', locals())

def check_order(request, order_id):

    order = get_object_or_404(Order, orderno=order_id)
    ordermeal = OrderMeal.objects.filter(order=order) # 使用filter才能得到queryset, templates才能用for loop取出

    return render(request, 'app/check_order.html', locals())


