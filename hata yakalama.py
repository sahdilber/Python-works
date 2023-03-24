"""
liste = ["345","sadas","324a","14","kemal"]

for eleman in liste:
    
    try:
        eleman = int(eleman) #eğer hata ile karşılaşırsak hata verecek
        print(eleman)
    
    except ValueError:
        pass #pass deyimi bloğun hiçbir şey yapmadığı anlamına geliyor
 """
 
def cift_mi(sayi):
    
     if(sayi%2==0):
         return sayi
     else:
         raise ValueError
liste1=[34,2,1,3,33,100,61,1800]

for i in liste1:
    try:
        print(cift_mi(i))
    except ValueError:
        print("tek sayılar yazdırılamaz.")