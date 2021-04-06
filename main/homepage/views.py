from django.shortcuts import render
from datastruct import views

# Create your views here.
def hello(request):
    return render(request,'home.html')

def searchroom(request):
    press = 0
    if request.method == 'POST':
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
    return render(request,'searchroom.html',{'press' : press})

def reserved(request):
    return render(request,'reserved.html')

def singleroom(request):
    return render(request,'singleroom.html')

def suitroom(request):
    return render(request,'suitroom.html')

def cabin(request):
    return render(request,'cabin.html')

def thankuser(request):
    return render(request,'thankuser.html')
    
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
            

        f = open('file/username.txt', 'a', encoding='utf8')
        f.write('Username ' + username + ' Phone ' + phone + ' typeroom ' + typeroom + 
        ' หมายเลขห้องพัก ' + str(numroom) +
        ' วันเช็คอิน ' + dayin + '/' + month + '/' + year + ' วันเช็คเอ้าท์ ' + dayout + '/' + month + '/' + year + '\n')
        f.close()
        return render(request,'addForm.html')
    return render(request,'addForm.html')


