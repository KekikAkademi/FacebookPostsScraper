# FacebookPostsScraper

```python
from FacebookPostsScraper import FacebookPostsScraper as FPS
from json import dumps

def main():
    email    = 'YOUR_EMAIL'
    password = 'YOUR_PASSWORD'

    facebook = FPS(email, password, post_url_text='Daha Fazla')

    profiles = [
        'https://www.facebook.com/groups/202783390107516',
        "https://www.facebook.com/groups/1590438354504559"

    ]
    data = facebook.get_posts_from_list(profiles)
    str_data = dumps(data, indent=2, ensure_ascii=False, sort_keys=False)

    print(str_data)

    with open("posts.json", "w", encoding="utf8") as f:
        f.write(str_data)

if __name__ == '__main__':
    main()
```

```json
[
  [
    {
      "paylasim": "2 saat",
      "metin": "Değerli arkadaşlar bu raporu dün aldım, İngiltere'de bı arkadaşım bana cihaz göndereceğini söyledi, kulak arkasında yada içinde hangisini isteyebilirim marka model numara varmı ,,,,bu konuda yardımcı olursanız sevinirim ...ilk defa alacağım hiç bir bilgim yok",
      "link": "https://facebook.com/groups/202783390107516/permalink/1570914819961026"
    },
    {
      "paylasim": "3 saat",
      "metin": "Merhabalar.Widex evoke 110 kullanıpta memnun olmayan var mı?Hoparlörü kulak içinde🦻",
      "link": "https://facebook.com/groups/202783390107516/permalink/1571039093281932"
    },
    {
      "paylasim": "1 Mart, 22:00",
      "metin": "Son günlerde televizyon ve internet üzerinden tüketiciyi aldatıcı, yanıltıcı tanıtımlarla ses yükseltici adı altında işitme cihazı satıldığı tespit edilmiştir. İşitme sorunu yaşayan hastalarımızın tecrübe ve bilgi noksanlıkları istismar edilerek aynı zamanda sağlıkları hiçe sayılarak, doğrudan satış...",
      "link": "https://facebook.com/groups/202783390107516/permalink/1569056103480231"
    },
    {
      "paylasim": "27 Aralık 2021, 17:33",
      "metin": "Oticon ve Beltone cihazları hakkında bilgisi olan dostlardan bilgi alabilirmiyim. Çok araştırdım bu iki cihazdan birisini almayı düşünüyorum. Yorumlarınızda cihaz ve sonraki bakım ve firma alakası I bildirirseniz memnun olurum. Teşekkürler.",
      "link": "https://facebook.com/groups/202783390107516/permalink/1524649277920914"
    },
    {
      "paylasim": "3 Mart, 16:45",
      "metin": "Merhaba ben teknisyenim İşitme kaybım ve cihaz kullanım raporum bu şekilde Benim gibi işitme kaybı olup bunu ehliyetine islettiren servis yada esnaf arkadaş var mı. Aracım otomobil ruhsatlı Dacia lodgy Personel taşımıyorum yalnızca oğlum ile çalışıyorum.aracin arkasında takımların ve yedek parçalar...",
      "link": "https://facebook.com/groups/202783390107516/permalink/1570222000030308"
    },
    {
      "paylasim": "1 Mart, 19:45",
      "metin": "Ileri derece isitme kaybi icin ve zor bi karisik isitme kaybi icin signia ,oticon,resaund hangisini tavsiye edersiniz?",
      "link": "https://facebook.com/groups/202783390107516/permalink/1568934570159051"
    },
    {
      "paylasim": "3 Mart, 16:43",
      "metin": "Merhaba arkadaşlar. Ankara da işitme cihazı tamiri yapan yer varmı güvenilir. Tamire çok para isteniyor. Aldığım yer.",
      "link": "https://facebook.com/groups/202783390107516/permalink/1570232746695900"
    },
    {
      "paylasim": "3 Mart, 14:26",
      "metin": "Bir kulağı hiç duymayan diğerinde orta derece işitme kaybı olupta çift cihaz kullanan var mı duymayan kulakta işe yarıyor mu",
      "link": "https://facebook.com/groups/1590438354504559/permalink/3042290972652616"
    },
    {
      "paylasim": "2 Mart, 23:04",
      "metin": "Arkadaşlar  babama isitme cihazı  alacağız.Odyolog babanıza kulak içi olmaz  yankı yapar diyor.Tavsiyeniz nedir.",
      "link": "https://facebook.com/groups/1590438354504559/permalink/3041870556027991"
    },
    {
      "paylasim": "3 Mart, 18:28",
      "metin": "Merhaba ileri derece yuzde 95lerde kayip icin hangi cihazlari onerirsiniz.phonax  var.siemens ince hortumlu var.beltone var.Birde oticon.Hangileri dogal ses ve ise yarar?",
      "link": "https://facebook.com/groups/1590438354504559/permalink/3042456829302697"
    },
    {
      "paylasim": "8 saat",
      "metin": "Ileri derece kayıplarda bluthos ozellikli ince hortum olmayan hangi modeller tavsiyeniz?",
      "link": "https://facebook.com/groups/1590438354504559/permalink/3043056875909359"
    },
    {
      "paylasim": "13 saat",
      "metin": "Yeni ambalajımızla tanışın! 💫\n Taşıma çantalarımız artık daha cep dostu ve işitme cihazlarınızı koruyarak su ve partiküllere karşı dirençliyken güvenli bir şekilde yerinde tutuyor ⭐\n #İşitmeCihazı #Yıldırımİşitme #İşitmeKaybı #İşitmeTesti",
      "link": "https://facebook.com/groups/1590438354504559/permalink/3042940709254309"
    },
    {
      "paylasim": "2 Mart, 16:01",
      "metin": "Selâm İyi günler resimdeki gördüğünüz bernafon markası işitme Cihazı öğretmenler tarafından bana hediye almışlar bir şey diyeceğim İzmir'de hangi işitme Cihazı şirketi bakıyor yardımcı olur musunuz ses ayarısı yaptırmak istiyorum nereden ama?",
      "link": "https://facebook.com/groups/1590438354504559/permalink/3041636179384762"
    },
    {
      "paylasim": "2 Mart, 21:54",
      "metin": "İşitme kaybı yaşayan kişiler işitme kaybına uygun cihaz arayışında iken hele ki konuya biraz uzak ise nereden başlayacağını bilemiyor olabilirler. Doğru bir bilgilendirme yerine ısrarla gönderi altına marka yorumu yazan uzman arkadaşlarımdan ricam önerdiğiniz markayı neden önerdiğinizi de yazabilir misiniz? Önerdiğiniz markalarda olup diğer markalarda olmayan önerme sebepleriniz nelerdir öğrenmiş olalım. Şöyle bir ekleme yapayım ben bu cihazı sattığım için bunu biliyorum şeklinde açıklamalarınız...",
      "link": "https://facebook.com/groups/1590438354504559/permalink/3041836286031418"
    }
  ],
  [
    {
      "paylasim": "2 saat",
      "metin": "Değerli arkadaşlar bu raporu dün aldım, İngiltere'de bı arkadaşım bana cihaz göndereceğini söyledi, kulak arkasında yada içinde hangisini isteyebilirim marka model numara varmı ,,,,bu konuda yardımcı olursanız sevinirim ...ilk defa alacağım hiç bir bilgim yok",
      "link": "https://facebook.com/groups/202783390107516/permalink/1570914819961026"
    },
    {
      "paylasim": "3 saat",
      "metin": "Merhabalar.Widex evoke 110 kullanıpta memnun olmayan var mı?Hoparlörü kulak içinde🦻",
      "link": "https://facebook.com/groups/202783390107516/permalink/1571039093281932"
    },
    {
      "paylasim": "1 Mart, 22:00",
      "metin": "Son günlerde televizyon ve internet üzerinden tüketiciyi aldatıcı, yanıltıcı tanıtımlarla ses yükseltici adı altında işitme cihazı satıldığı tespit edilmiştir. İşitme sorunu yaşayan hastalarımızın tecrübe ve bilgi noksanlıkları istismar edilerek aynı zamanda sağlıkları hiçe sayılarak, doğrudan satış...",
      "link": "https://facebook.com/groups/202783390107516/permalink/1569056103480231"
    },
    {
      "paylasim": "27 Aralık 2021, 17:33",
      "metin": "Oticon ve Beltone cihazları hakkında bilgisi olan dostlardan bilgi alabilirmiyim. Çok araştırdım bu iki cihazdan birisini almayı düşünüyorum. Yorumlarınızda cihaz ve sonraki bakım ve firma alakası I bildirirseniz memnun olurum. Teşekkürler.",
      "link": "https://facebook.com/groups/202783390107516/permalink/1524649277920914"
    },
    {
      "paylasim": "3 Mart, 16:45",
      "metin": "Merhaba ben teknisyenim İşitme kaybım ve cihaz kullanım raporum bu şekilde Benim gibi işitme kaybı olup bunu ehliyetine islettiren servis yada esnaf arkadaş var mı. Aracım otomobil ruhsatlı Dacia lodgy Personel taşımıyorum yalnızca oğlum ile çalışıyorum.aracin arkasında takımların ve yedek parçalar...",
      "link": "https://facebook.com/groups/202783390107516/permalink/1570222000030308"
    },
    {
      "paylasim": "1 Mart, 19:45",
      "metin": "Ileri derece isitme kaybi icin ve zor bi karisik isitme kaybi icin signia ,oticon,resaund hangisini tavsiye edersiniz?",
      "link": "https://facebook.com/groups/202783390107516/permalink/1568934570159051"
    },
    {
      "paylasim": "3 Mart, 16:43",
      "metin": "Merhaba arkadaşlar. Ankara da işitme cihazı tamiri yapan yer varmı güvenilir. Tamire çok para isteniyor. Aldığım yer.",
      "link": "https://facebook.com/groups/202783390107516/permalink/1570232746695900"
    },
    {
      "paylasim": "3 Mart, 14:26",
      "metin": "Bir kulağı hiç duymayan diğerinde orta derece işitme kaybı olupta çift cihaz kullanan var mı duymayan kulakta işe yarıyor mu",
      "link": "https://facebook.com/groups/1590438354504559/permalink/3042290972652616"
    },
    {
      "paylasim": "2 Mart, 23:04",
      "metin": "Arkadaşlar  babama isitme cihazı  alacağız.Odyolog babanıza kulak içi olmaz  yankı yapar diyor.Tavsiyeniz nedir.",
      "link": "https://facebook.com/groups/1590438354504559/permalink/3041870556027991"
    },
    {
      "paylasim": "3 Mart, 18:28",
      "metin": "Merhaba ileri derece yuzde 95lerde kayip icin hangi cihazlari onerirsiniz.phonax  var.siemens ince hortumlu var.beltone var.Birde oticon.Hangileri dogal ses ve ise yarar?",
      "link": "https://facebook.com/groups/1590438354504559/permalink/3042456829302697"
    },
    {
      "paylasim": "8 saat",
      "metin": "Ileri derece kayıplarda bluthos ozellikli ince hortum olmayan hangi modeller tavsiyeniz?",
      "link": "https://facebook.com/groups/1590438354504559/permalink/3043056875909359"
    },
    {
      "paylasim": "13 saat",
      "metin": "Yeni ambalajımızla tanışın! 💫\n Taşıma çantalarımız artık daha cep dostu ve işitme cihazlarınızı koruyarak su ve partiküllere karşı dirençliyken güvenli bir şekilde yerinde tutuyor ⭐\n #İşitmeCihazı #Yıldırımİşitme #İşitmeKaybı #İşitmeTesti",
      "link": "https://facebook.com/groups/1590438354504559/permalink/3042940709254309"
    },
    {
      "paylasim": "2 Mart, 16:01",
      "metin": "Selâm İyi günler resimdeki gördüğünüz bernafon markası işitme Cihazı öğretmenler tarafından bana hediye almışlar bir şey diyeceğim İzmir'de hangi işitme Cihazı şirketi bakıyor yardımcı olur musunuz ses ayarısı yaptırmak istiyorum nereden ama?",
      "link": "https://facebook.com/groups/1590438354504559/permalink/3041636179384762"
    },
    {
      "paylasim": "2 Mart, 21:54",
      "metin": "İşitme kaybı yaşayan kişiler işitme kaybına uygun cihaz arayışında iken hele ki konuya biraz uzak ise nereden başlayacağını bilemiyor olabilirler. Doğru bir bilgilendirme yerine ısrarla gönderi altına marka yorumu yazan uzman arkadaşlarımdan ricam önerdiğiniz markayı neden önerdiğinizi de yazabilir misiniz? Önerdiğiniz markalarda olup diğer markalarda olmayan önerme sebepleriniz nelerdir öğrenmiş olalım. Şöyle bir ekleme yapayım ben bu cihazı sattığım için bunu biliyorum şeklinde açıklamalarınız...",
      "link": "https://facebook.com/groups/1590438354504559/permalink/3041836286031418"
    }
  ]
]
```
