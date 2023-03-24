import time
import random

class bilgisayar():
    
    def __init__(self,pc_durum="Kapalı",pc_parlaklık=0,uygulama_listesi=["Microsoft"],uygulama="Microsoft"):
        
        self.pc_durum=pc_durum
        self.pc_parlaklık=pc_parlaklık
        self.uygulama_listesi=uygulama_listesi
        self.uygulama=uygulama
        
    def pc_ac(self):
        
        if(self.pc_durum=="Açık"):
            print("Bilgisayar zaten açık.\n")
        else:
            print("Bilgisayar açılıyor...")
            self.pc_durum="Açık"
    
    def pc_kapat(self):
        
        if(self.pc_durum=="Kapalı"):
            print("Bilgisayar zaten kapalı.\n")
        else:
            print("Bilgisayar kapatılıyor...")
            self.pc_durum="Kapalı"
    
    def parlaklık_ayarı(self):
        
        while True:
            cevap=input("Azaltmak için '-' tuşuna basın.\nArtırmak için '+' tuşuna basın\nÇıkmak için '0' a basın:\n")

            if(cevap=="-"):
                if(self.pc_parlaklık != 0):
                    self.pc_parlaklık-=1
                    print("Parlaklık:",self.pc_parlaklık)
            
            elif(cevap=="+"):
                if(self.pc_parlaklık!=30):
                    self.pc_parlaklık+=1
                    print("Parlaklık:",self.pc_parlaklık)
            elif(cevap=="0"):
                break
    
    def uygulama_ekle(self,uygulama_ismi):
        
        print("Uygulama Ekleniyor...")
        time.sleep(1)
                     
        self.uygulama_listesi.append(uygulama_ismi)
        
        print("Uygulama Eklendi.")
        
    def rastgele_uygulama(self):
        
        rastgele=random.randint(0,len(self.uygulama_listesi)-1)
        
        self.uygulama=self.uygulama_listesi[rastgele]
        
        print("Şu anki uygulama:",self.uygulama)
        
    def __len__(self):
        return len(self.uygulama_listesi)
    def __str__(self):
        return "PC durumu:{}\nParlaklık:{}\nUygulama Listesi:{}\nŞu Anki uygulama:{}".format(self.pc_durum,self.pc_parlaklık,self.uygulama_listesi,self.uygulama)
    
pc=bilgisayar()

print("""
      
      Televizyon Uygulaması
      
      1-> PC Aç
      2-> PC Kapat
      3-> Parlaklık Ayarları
      4-> Uygulama Ekle
      5-> Uygulama Sayısını Öğrenme
      6-> Rastgele Uygulamaya Geçme
      7-> Uygulama Bilgileri
      
      Çıkmak için '0' a basın.
      """)

while True:
    
    islem=int(input("İşlem Seçiniz:"))
    
    if(islem==0):
        print("Program sonlandırılıyor...")
        break
    
    elif(islem==1):
        pc.pc_ac()
    elif(islem==2):
        pc.pc_kapat()
    elif(islem==3):
        pc.parlaklık_ayarı()
    elif(islem==4):
        uygulama_ismi=input("Uygulamaları ',' ile ayırarak giriniz.")
        
        uygulama_listesi=uygulama_ismi.split(",")
        
        for eklenecekler in uygulama_listesi:
            pc.uygulama_ekle(eklenecekler)
    elif(islem==5):
            print("Kanal Sayısı:",len(pc))
    elif(islem==6):
         pc.rastgele_uygulama()
    elif(islem==7):
            print(pc)
    else:
        print("Geçersiz İşlem.")
            
            
            
            
            
            
            