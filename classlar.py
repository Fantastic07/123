
from pickle import TRUE


class Talaba:
    def __init__(self , ism , univer , kurs , yosh , tartib_raqam):
        
        self.ism = ism
        self.univer = univer
        self.kurs = kurs
        self.yosh = yosh
        self.tartib_raqam = tartib_raqam
        
    def __str__(self):
        
        return '\n Talaba tartib raqami : ' + f'{self.tartib_raqam}' + '\n Talaba ismi : ' + self.ism + '\n Universiteti : ' + self.univer + '\n Kursi : ' + f'{self.kurs}' + '\n Yoshi : ' + f'{self.yosh}'
    
    
l = []
tartib_raqam = -1

while True:
    
    print('\tQuyidagilardan birini tanlang : \n')
    
    print('1. Talabani ko\'rish')
    print('2. Talabani qo\'shish')
    print('3. Talabani o\'chirish')
    print('4. Chiqish \n')
    
    raqam = int(input())
    
    if raqam < 0 or raqam > 4:
        print('Narmalniy raqam kirit !!!!!!!!! ')
    
    if raqam == 1 :
        for i in(l):
            print(i)
    
    if raqam == 2 :
        print('Talaba ismini kiriting : ')
        ism = input()
        print('Talabani universitetini kiriting : ')
        univer = input()
        print('Talabani kursini kiriting : ')
        kurs = int(input())
        print( 'Talabaning yoshini kiriting : ')
        yosh = int(input())
        
        tartib_raqam = tartib_raqam + 1
        
        s = Talaba(ism , univer , kurs , yosh , tartib_raqam )
        l.append(s)

    if raqam == 3 :
        print('Qaysi talabani o\'chirmoqchisiz ? (o\'chirish uchun tartib raqamdan foydalaniladi)')
        delete = int(input())
        l.pop(delete)
            
            
    if raqam == 4 :
        break


