# bot_logic in original

import random


def sifre_olusturucu(sifre_uzunlugu):
    ogeler = "+-/*!&$#?=@<>"
    sifre = ""

    for i in range(sifre_uzunlugu):
        sifre += random.choice(ogeler)

    return sifre


def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)


def yazi_tura():
    para = random.randint(0, 2) 
    if para == 0:
        return "YAZI"
    else:
        return "TURA"
    
def number():
    number = random.randint(1,10)
    return number

def fact():
    facts = [
        "Atlantiğin üstünden uçarak giden ilk kadın Amelia Earhart'dır",
        "Beethoven duyma özelliğini kaybetmesine rağmen besteciliğe devam etti, 9. Semfonisini yazdıktan sonra komple saar oldu",
        "8 saatlik bir uykuda sadece 2 saat rüya görürsün, o 2 saatte en fazla 7 tane rüya görebilirsin",
        "Her 100 yılda bir, 1 gün 1.8 saniye artıyor",
        "İnsanlardan Küçük hayvanlar için zaman daha yavaş geçer",
        "1940 yılında Mike isimli bir tavuk kafasız çekilde 18 ay yaşadı",
        "Uzun Kelimelerden korkmaya verilen isim 'Hippopotomonstrosesquippedaliophobia'dır",
        "Dünyanın en çok yaşayan köpeği 29.5 yıl yaşadı",
        "Dünyanın en çok yaşayan kedisi 38 yıl 3 gün yaşadı",
        "Testereler doğum için icat edilmişti"
    ]
    return random.choice(facts)
    