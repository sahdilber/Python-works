import random
import time

class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["Trt"],kanal="Trt"):
        
        self.tv_durum=tv_durum
        
        self.tv_ses=tv_ses
        
        self.kanal_listesi=kanal_listesi
        
        self.kanal=kanal
        
    def tv_ac(self):
        
        if(self.tv_durum=="Açık"):
            print("Televizyon zaten açık.")
        else:
            print("Televizyon açılıyor...")
            self.tv_durum="Açık"
    
    def tv_kapat(self):
        if(self.tv_durum=="Kapalı"):
          print("Televizyon zaten kapalı.")
        else:
            print("Televizyon kapatılıyor...")
            self.tv_durum="Kapalı"
    
    def ses_ayarları(self):
        
        while True:
            cevap=input("Sesi Azalt:'<'\nSesi Artır:'>'\nÇıkış:exit\n")
            
            if(cevap=="<"):
                if(self.tv_ses!=0):
                    self.tv_ses-=1
                    print("Ses:",self.tv_ses)
            elif(cevap==">"):
                if(self.tv_ses != 31):
                    self.tv_ses+=1
                    print("Ses:",self.tv_ses)
            else:
                print("Ses Güncellendi:",self.tv_ses)
                break
    
    def kanal_ekle(self,kanal_ismi):
        
        print("kanal ekleniyor...\n")
        time.sleep(1)
        
        self.kanal_listesi.append(kanal_ismi)
        
        print("Kanal eklendi\n")
    
    def rastgele_kanal(self):
        
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        
        self.kanal=self.kanal_listesi[rastgele]
        
        print("Şu anki kanal:",self.kanal)
        
    def __len__(self):
        
        return len(self.kanal_listesi)
    
    def __str__(self): #print fonksiyonunu çağırdığımızda bu fonksiyon çalışır
        
        return "Tv Durumu:{}\nTv Ses:{}\n Kanal Listesi:{}\nŞu anki kanal:{}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
    
kumanda=Kumanda()

print("""
      Televizyon Uygulaması
      
      1-> Tv Aç
      2-> TV Kapat
      3-> Ses Ayarları
      4-> Kanal Ekle
      5-> Kanal Sayısını Öğrenme
      6-> Rastgele Kanala Geçme
      7-> Televizyon Bilgileri
      
      Çıkmak için '0' a basın.
      
      """)

while True:
    
    islem=int(input("İşlemi Seçiniz:\n"))
    
    if(islem==0):
        print("Program sonlandırılıyor...\n")
        time.sleep(1)
        break
    
    elif(islem==1):
        kumanda.tv_ac()

    elif(islem==2):
        kumanda.tv_kapat()
    
    elif(islem==3):
        kumanda.ses_ayarları()
    
    elif(islem==4):
        kanal_isimleri=input("Kanal isimlerini ',' ile ayırarak giriniz:\n") #yeni bir değişken
        
        kanal_listesi=kanal_isimleri.split(",")
        
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
        
    elif(islem==5):
        print("Kanal Sayısı:\n",len(kumanda))    
        
    elif(islem==6):
        kumanda.rastgele_kanal()
    
    elif(islem==7):
        print(kumanda)
        
    else:
        print("Geçersiz İşlem.\n")
        
          
    
    
    
    
    
    