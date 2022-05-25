print("\n\"x² + bx + c = 0\" biçiminde yazılan 2.dereceden bir denklemin köklerini bulacağız. b ve c sayılarını girerek denklemi oluşturunuz.\n")
b = int(input("b sayısını giriniz: ")) #b ve c değerlerini girdi olarak alıyoruz.
c = int(input("c sayısını giriniz: "))
print("\nOluşturduğunuz denklem: x² +", b, "x +", c, "= 0")

if b == 0: #eğer b=0 ise yani denklem x² + c = 0 formundaysa ve c <= 0 ise (çünkü c 0'dan büyük olursa karekök x negatif bir sayıya eşit olur bu durumda x reel olmaz) çakışık iki kök vardır ve bunlar c'nin kareköküne eşittir.
    if c <= 0:
        print("\nDenklemin iki çakışık kökü vardır ve bunlar √" + str(-c) + "'e eşittir.")
        exit()

c_carpanlari = [] #c'nin çarpanlarını içeren bir dizi oluşturuyoruz

if c > 0: #c pozitif ise
    for i in range(1, c + 1): # 1'den başlayıp c+1'e kadar olan her sayıyı bir kereliğine i olarak kullan. tüm i değerleri için tekrarla
       if c % i == 0:             #eğer c'nin i'ye bölümünden kalan 0'sa yani i, c'yi tam bölüyorsa i, c'nin bir çarpanıdır demektir
           c_carpanlari.append(i) #i'yi c'nin çarpanları listesine ekle

elif c < 0:#c negatif ise
    for i in range(c,0): #c'den başlayıp 0'a kadar olan her sayıyı bir kereliğine i olarak kullan. tüm i değerleri için tekrarla
            if c % i == 0:              #eğer c'nin i'ye bölümünden kalan 0'sa yani i, c'yi tam bölüyorsa i, c'nin bir çarpanıdır demektir
                c_carpanlari.append(i)  #i'yi c'nin çarpanları listesine ekle

else: #c pozitif de değil, negatif ise şunu yap: (bu durumda 0 demektir.)
    print("\nDenklemin kökleri: x₁ = 0", ",  x₂ = ", -b, "\n") #c=0 ise x² + bx = 0 denklemi ortaya çıkar x parantezine alırsak x.(x+b)=0 olur bir kök 0, diğer kök -b olur.
    exit() #diğer adımlara geçmeden programa son ver.


#buradan sonraki bazı bölümler c'nin negatif olduğu durumlarda çarpanlara ayrılmasının düzgün olması için var.
c_ters_carpanlari = [-x for x in c_carpanlari] #c_ters_carpanlari adında bir dizi oluştur. c_carpanları dizisindeki her eleman için c_ters carpanları dizisinde o elemanın negatifini al.

# burada neden c_1, c_2, c_3, c_4, c_5 ve c_6 var diye soracak olursanız: yukarıda oluşturduğumuz çarpan bulma algoritması pozitif çarpanları sorunsuz buluyor ama negatif sayılarda çarpanları tamamen negatifini buluyor
# negatif ve pozitif tanım aralığını bir arada verince de listede sıralama doğru olmuyor. Bizim istediğimiz sıralamada bir baştan bir sondan alınan çarpanların çarpımının sayıyı vermesi mesela 12 sayısının çarpanları
# dizisini [1, 2, 3, 4, 6, 12] şeklinde sorunsuz buluyor. Burada bir baştan bir sondan alınan elemanların çarpımları 12'yi veriyor. 1-12, 2-6... gibi. Ama örneğimiz -12 olsaydı burada 2 sorun yaşayacaktık. Birincisi -12,+12
# arasında verdiğimiz aralıkta 0 değerini de deneyecekti ve 0'a bölme yapamayacağı için hata verecekti hadi bu sorunu 0'a kadar olan ve 0'dan sonra olan diye iki parçada denettirip o iki listeyi birleştirerek çözdük diyelim,
# elimizdeki liste istediğimiz formatta yani bir baştan bir sondan alınan elemanların çarpımının sayıyı vereceği şekilde olmayacktı. Örneğin -12 sayısına [-12, -6, -4, -3, -2, -1, 1, 2, 3, 4, 6, 12] şeklinde bir dizi oluşturacaktı.
# bu dizide bir baştan bir sondan gibi bir yöntem kullanamayacaktık. Bu nedenle -12'nin [-12, -6...] diye giden carpanları ve bunun tersi olan [12, 6...] diye giden ters işaretli çarpanları adında 2 dizi oluşturdum. Ardından
# normal çarpanlarını içeren diziyi tam ortadan bölerek normal-1, normal-2 gibi iki diziye ayırdım.(Bunlar sayı ile aynı işarette yani - şu an -12 örneği için) ardından c_ters çarpanlarını yine ortadan ikiye bölüp bunlardan 2
# ayrı dizi oluşturdum. ters1, ters2 gibi (bunlar da c ile ters yani + işaretli). Sonra iki yeni dizi daha oluşturup ilkine normal çarpanların ilk yarısı ve ters işaretlilkerin ikinci yarısını ekledim. Burada örneğin ilk yarısında
# aynı işaretli olan -12, ve ikinci yarıda bulunan ama ters işaretli olan +1 ile eşleşti Ve böylece çarpımları -12 yi verdi. Aksi halde -12 ve -1 eşleşip +1 verecekti ve hiç pozitif çarpan olmayacaktı. Yine aynı şekilde ikinci 
# çarpan dizime normal çarpanların ikinci yarısını ve ters işaretli çarpanların ilk yarısını ekledim. böylece mesela -12 ile +1'in (ve diğerlerinin) eşlendiği ve +12 ile -1'in(ve diğerlerinin) eşlendiği iki çarpan dizimiz oluştu.

c_1 = c_carpanlari[:len(c_carpanlari)//2]
c_2 = c_carpanlari[len(c_carpanlari)//2:]

c_3 = c_ters_carpanlari[:len(c_carpanlari)//2]
c_4 = c_ters_carpanlari[len(c_carpanlari)//2:]


c_5 = c_1 + c_4
c_6 = c_3 + c_2


son_carpan_numarasi = len(c_carpanlari) - 1 #son carpan numarası c_carpanları dizisinin uzunluğunu belirten sayıdan 1 eksik. Neden 1 eksik olduğunu soracak olursak dizilerde ilk eleman 1. değil, 0. elemandır. Aksi bizim 1'den
                                            #başlayarak en son saydığımız eleman 0'dan başlayarak saydığımız son elemandan 1 fazla çıkardı.

for i in range(0, len(c_carpanlari) // 2): #i'yi 0'dan c_carpanları dizisinin uzunluğunun yarısı olana kadar tekrarla. (yarısı çünkü bir baştan bir sondan gruplayarak dizi uzunluğunun yarısı kadar gruplama yapıyoruz.)
    if c > 0: #c pozitif ise
        if c_carpanlari[i] + c_carpanlari[son_carpan_numarasi - i] == b : #c_carpanlarının i.elemanı ile c carpanlarının sondan i.elemanının toplamı b'yi veriyorsa:
            kok1 = c_carpanlari[i] * -1                                #carpan1 c_carpanlarının i.elemanının ters işaretlisidir. (örn: x+5=0: x≠5, x=-5)
            kok2 = c_carpanlari[son_carpan_numarasi - i] * -1          #carpan2 ise sondan i.elemanın ters işaretli halidir.
            break                                                         #bu durumlar gerçekleşir yani denklemin köklerini bulursak break kullanarak döngüden çıkacağız.

        elif c_ters_carpanlari[i] + c_ters_carpanlari[son_carpan_numarasi - i] == b : #b'nin bazı durumlarında(b negatifken) c'nin negatif çarpanlarını da incelemek gerekiyor. örn: x² -6x +8 = 0 denkleminde 8'in sadece negatif
            kok1 = c_ters_carpanlari[i] * -1                                          #çarpanlarının toplamı b yi veriyor. (-2 ve -4)                  
            kok2 = c_ters_carpanlari[son_carpan_numarasi - i] * -1          
            break                                                         

        else:                                                             #koşullar sağlanmaz yani baştan ve sondan i. çarpanların toplamı ortadaki b sayısını vermezse aynı döngü içinde artan i'lerle denemeye devam edeceğiz
            continue
    
    elif c < 0: #c negatif ise ilk yarısı ve son yarısı negatif olan iki farklı çarpanlar kümemizi deneyeceğiz
        if c_5[i] + c_5[son_carpan_numarasi - i] == b : #ilk yarısı normal işaretli olan çarpan kümemizde baştan ve sondan i. elemanların toplamının ortadaki b sayısına eşit olup olmadığını kontrol ediyoruz 
            kok1 = c_5[i] * -1                       #b'yi veriyorlarsa kokler olarak kaydedip döngüden çıkıyoruz
            kok2 = c_5[son_carpan_numarasi - i] * -1
            break
        
        elif c_6[i] + c_6[son_carpan_numarasi - i] == b : #aynı işlemleri ilk yarısı ters işaretli olan dizimiz için uyguluyoruz(tabi ilk diziden kök gelmeyip döngünün kırılmadığı durumda)
            kok1 = c_6[i] * -1
            kok2 = c_6[son_carpan_numarasi - i] * -1
            break

        else:
            continue
    

if('kok1' and 'kok2' in locals()): #eğer kok1 ve kok2 adında değişkenler varsa kök bulduk demektir. Kökleri yazdırıyoruz
    print("\nDenklemin kökleri: x₁ = ", kok1, ",  x₂ = ", kok2, "\n")
    
else: #eğer kok1 ve kok2 adında değişkenlerimiz yoksa kök bulamadık demektir.
    print("\nDenklemin reel sayılar kümesinde kökü yoktur.")