
import time
s = 100000


users = []
d = open("Users.txt","r")
x = d.readlines()

for i in x:
    c = i.split(",") # список из 3- элементов
    #print(c)
    t = {}
    g = {}
    for n in c:
        o = n.split(":") #o[0] = login, o[1] = admin1
        #o[0] = login, code, summa o[1] - admin1, 1234, 2000
       # print(o)
        #l = "\n"
        if o[0] == 'code':
            t[o[0]] = int(o[1])
        elif o[0] == 'summa':
            t[o[0]] = int(o[1].replace('\n', ''))
        else:
            t[o[0]] = o[1]
    #print(t)
    users.append(t)

print(users)
while True:
    time.sleep(2)
    login = input('login:')
    time.sleep(2)
    print(users)
    print(login)
    for i in users:
        print("Wait... ...")
        if login==i['login']:
            time.sleep(2)
            pin = int(input('PIN:'))
            time.sleep(2)
            if pin == i['code']:
                print('ok')
                time.sleep(2)
                z = int(input("Введите сумму "))
                time.sleep(2)
                if z <= s and z <= i['summa']:
                    i["summa"] = i["summa"] - z
                    s = s - z
                    print("Late")
                    time.sleep(3)
                    print("Заберите деньги")
                    time.sleep(2)
                else:
                    print("Не достаточная сумма в банкомате")
                    time.sleep(2)

            else:
                print('Error pin')
                time.sleep(2)
        else:
            print('Error login')
            time.sleep(2)
        continue





