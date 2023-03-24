print("Harf Notunu Hesaplama Programına Hoş Geldiniz.")

while True:
    
    vize=int(input("Vize notunu girin:"))
    final=int(input("Final notunu girin:"))

    toplam_not = (vize*0.4)+(final*0.6)

    if toplam_not>=90:
        print("Harf notunuz : AA")
    elif toplam_not>=85:
         print("Harf notunuz : BA")
    elif toplam_not>=80:
        print("Harf notunuz : BB")
    elif toplam_not>=75:
        print("Harf notunuz : CB")
    elif toplam_not>=70:
        print("Harf notunuz : CC")
    elif toplam_not>=65:
        print("Harf notunuz : DC") 
    elif toplam_not>=60:
         print("Harf notunuz : DD") 
    elif toplam_not>=55:
         print("Harf notunuz : FD") 
    else:
        print("Harf notunuz : FF")
        
    exit=input("Çıkmak İstiyorsanız a'ya basın.:")
    if (exit=="a"):
        
        print("programdan çıkılıyor...")
        break