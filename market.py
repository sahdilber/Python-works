class market():
    
    def __init__(self,product,price,weight,brand):
        self.product=product
        self.price=price
        self.weight=weight
        self.brand=brand
    def bilgileri_göster(self):
        print("""
              {} ürününün özellikleri:
              
              Fiyat : {}tl
              
              Ağırlık: {}g(gram)
              
              Marka/Cinsi : {}
              
              """.format(self.product,self.price,self.weight,self.brand))
        
def switch(lang):
    if lang == "elma":
        return elma.bilgileri_göster()
    elif lang == "armut":
        return armut.bilgileri_göster()
    elif lang == "sakız":
        return sakız.bilgileri_göster()
    elif lang == "çikolata":
        return cikolata.bilgileri_göster()
    elif lang == "kahve":
        return kahve.bilgileri_göster()
    elif lang == "peynir":
        return peynir.bilgileri_göster()
    elif lang == "süt":
        return süt.bilgileri_göster()
    else:
        print("Markette olmayan bir ürün girdiniz.")

elma=market("Elma",18,500,"Kırmızı Elma")
armut=market("Armut",30,500,"Malatya Armudu")
sakız=market("Sakız",3,50,"Falım")
cikolata=market("Çikolata",6,80,"Browni")
kahve=market("Kahve",60,100,"Türk Kahvesi")
peynir=market("Peynir",50,250,"Beyaz Peynir")
süt=market("süt",18,1000,"Pınar")

deger=input("Ürünlerinizin özelliklerini görmek istiyorsanız q'ya basın(alışveriş tutarı için a'ya basıp bekleyiniz.):")
while (deger=="q"):
    product_features=input("Hangi ürününüzün özelliğini görmek istiyorsunuz(çıkmak için x'e basın):")
    if(product_features=="x"):
        print("Alışveriş tutarı hesaplanıyor...")
        break
    switch(product_features)




fiyatlar={elma.price,armut.price,sakız.price,cikolata.price,kahve.price,peynir.price,süt.price}

alisveris_tutari=0

for i in fiyatlar:
    alisveris_tutari+=i

print("Alışveriş tutarı {}tl.\n".format(alisveris_tutari))

while True:
    ödeme=int(input("Ödeme yapacağınız miktarı girin:"))

    para_üstü=ödeme- alisveris_tutari
    
    if para_üstü==0:
        print("Aldıklarınız tam tuttu.\nYine Bekleriz.:)")
        break
    elif para_üstü>0:
        print("Para üstünüz {}tl idir.\nYine bekleriz.:)".format(para_üstü))
        break
    else:
        print("Eksik para verdiniz.:/")
        
 