from django.shortcuts import render
from datastruct import views

# Create your views here.
def hello(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        check = 0
        user = request.POST['user'] 
        password = request.POST['password'] 
        f = open('file/login.txt', 'r', encoding='utf8')
        s = f.readline()
        # spliting line to key and value
        d = s.split()
        realuser = d[0]
        realpassword = d[1]
        f.close()
        if user == realuser:
            if password == realpassword:
                check = 1
        if check == 1:
            stinfor = views.Stack()
            f = open('file/username.txt', 'r', encoding='utf8')
            while True:
                s = f.readline()
                if s == '': # check file end
                    break
                # spliting line to key and value
                d = s.rstrip()
                stinfor.push(d)
            f.close()
            if stinfor.size() == 0:
                return render(request,'inforuser.html',{'press' : 0})
            return render(request,'inforuser.html',{
            'infor' : stinfor.lststack(),
            'press' : 1})
        else:
            return render(request,'login.html',{'check' : check})
    return render(request,'login.html')

def searchroom(request):
    press = 0
    if request.method == 'POST':
        notfound = ''
        press = 1
        userphone = request.POST['userphone']
        stuser = views.Stack()
        stphone = views.Stack()
        stroom = views.Stack()
        stnumroom = views.Stack()
        stdayin = views.Stack()
        stdayout = views.Stack()
        f = open('file/username.txt', 'r', encoding='utf8')
        while True:
            s = f.readline()
            if s == '': # check file end
                break
            # spliting line to key and value
            d = s.rstrip().split()
            stuser.push(d[1])
            stphone.push(d[3])
            stroom.push(d[5])
            stnumroom.push(d[7])
            stdayin.push(d[9])
            stdayout.push(d[11])
        f.close()
        count = 0
        for i in stphone.lststack():
            if i == userphone: 
                return render(request,'searchroom.html',
                {'user' : stuser.find(count) , 
                'userphone' : userphone , 
                'press' : press , 
                'typeroom' : stroom.find(count),
                'numroom' : stnumroom.find(count),
                'dayin' : stdayin.find(count),
                'dayout' : stdayout.find(count)
                })
            count+=1
        press = 2
        notfound = 'ไม่พบข้อมูล'
        return render(request,'searchroom.html',{'notfound' : notfound,'press' : press})
    return render(request,'searchroom.html',{'press' : press})

def reserved(request):
    return render(request,'reserved.html')

def singleroom(request):
    return render(request,'singleroom.html')

def suitroom(request):
    return render(request,'suitroom.html')

def cabin(request):
    return render(request,'cabin.html')

def checkout(request):
    press = 3
    Qinfor = views.Queue()
    f = open('file/username.txt', 'r', encoding='utf8')
    while True:
        s = f.readline()
        if s == '': # check file end
            break
        # spliting line to key and value
        d = s.rstrip()
        Qinfor.enQ(d)
    f.close()
    if Qinfor.size() == 0:
        return render(request,'inforuser.html',{'press' : 0})
    sorting = views.sorting()
    sorting.sortcheckout(Qinfor.show())
    cur = Qinfor.top().split()
    numroom = cur[7]
    for i in numroom:
        firstnum = i
        break
    Qinfor.deQ()
    f = open('file/username.txt', 'w', encoding='utf8')
    for i in Qinfor.show():
        f.write(str(i) + '\n')
    f.close()
    print(numroom)
    print(firstnum)
    if firstnum == '0':
        f = open('file/cabin.txt', 'a', encoding='utf8')
        f.write(str(numroom) + '\n')
        f.close()
    elif firstnum == '1':
        f = open('file/singleroom.txt', 'a', encoding='utf8')
        f.write(str(numroom) + '\n')
        f.close()
    elif firstnum == '2':
        f = open('file/suitroom.txt', 'a', encoding='utf8')
        f.write(str(numroom) + '\n')
        f.close()
    return render(request,'inforuser.html',{'fin' : Qinfor.show(),'press' : press})

def sort(request):
    if request.method == 'POST':
        sortday = request.POST['sortday']
        stinfor = views.Stack()
        f = open('file/username.txt', 'r', encoding='utf8')
        while True:
            s = f.readline()
            if s == '': # check file end
                break
            # spliting line to key and value
            d = s.rstrip()
            stinfor.push(d)
        f.close()
        sorting = views.sorting()
        if stinfor.size() == 0:
            return render(request,'inforuser.html',{'press' : 0})
        elif sortday == 'sortin':
            return render(request,'inforuser.html',{'fin' : sorting.sortcheckin(stinfor.lststack()),'press' : 2})
        elif sortday == 'sortout':
            return render(request,'inforuser.html',{'fin' : sorting.sortcheckout(stinfor.lststack()),'press' : 2})
        else:
            return render(request,'inforuser.html',{
            'infor' : stinfor.lststack(),
            'press' : 1})
    return render(request,'inforuser.html',{'press' : 1})

def addForm(request):
    if request.method == 'POST':
        username = request.POST['username']
        phone = request.POST['phone']
        typeroom = request.POST['typeroom']

        dayin = request.POST['dayin']
        dayout = request.POST['dayout']
        month = request.POST['month']
        year = request.POST['year']

        Qsingleroom = views.Queue()
        Qsuitroom = views.Queue()
        Qcabin = views.Queue()

        if typeroom == 'ห้องเดี่ยว':
            f = open('file/singleroom.txt', 'r', encoding='utf8')
            while True:
                s = f.readline()
                if s == '': # check file end
                    break
                # spliting line to key and value
                d = s.rstrip()
                Qsingleroom.enQ(d)
            f.close()
            numroom = Qsingleroom.deQ()
            f = open('file/singleroom.txt', 'w', encoding='utf8')
            for i in Qsingleroom.show():
                f.write(str(i) + '\n')
            f.close()

        elif typeroom == 'ห้องสูท':
            f = open('file/suitroom.txt', 'r', encoding='utf8')
            while True:
                s = f.readline()
                if s == '': # check file end
                    break
                # spliting line to key and value
                d = s.rstrip()
                Qsuitroom.enQ(d)
            f.close()
            numroom = Qsuitroom.deQ()
            f = open('file/singleroom.txt', 'w', encoding='utf8')
            for i in Qsuitroom.show():
                f.write(str(i) + '\n')
            f.close()
        elif typeroom == 'บ้านพัก':
            f = open('file/cabin.txt', 'r', encoding='utf8')
            while True:
                s = f.readline()
                if s == '': # check file end
                    break
                # spliting line to key and value
                d = s.rstrip()
                Qcabin.enQ(d)
            f.close()
            numroom = Qcabin.deQ()
            f = open('file/cabin.txt', 'w', encoding='utf8')
            for i in Qcabin.show():
                f.write(str(i) + '\n')
            f.close()
            
        fl = open('file/username.txt', 'a', encoding='utf8')
        fl.write('Username ' + username + ' Phone ' + phone + ' typeroom ' + typeroom + 
        ' หมายเลขห้องพัก ' + str(numroom) +
        ' วันเช็คอิน ' + dayin + '/' + month + '/' + year + ' วันเช็คเอ้าท์ ' + dayout + '/' + month + '/' + year + '\n')
        print("hi from file")
        fl.close()
        return render(request,'thankuser.html')
    return render(request,'addForm.html')


