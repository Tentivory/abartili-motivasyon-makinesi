#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Motivasyon Makinesi
Bu kod çalışır. Gerçekten çalışır. Hayatını değiştirmez ama gülümsetir.
"""

import random
import time

motivasyonlar = [
    "Sen bir yıldızsın! Ama kara deliğe düşmek üzere olan bir yıldız.",
    "Bugün kalk ve dünyayı fethet! En azından çay bardağını fethet.",
    "Başarısızlık geçicidir. Sen ise kalıcısın. Ne yazık ki.",
    "Hayallerinin peşinden koş! Ama önce ayakkabılarını bağla.",
    "Sen harikasın! Çünkü bu cümleyi okuyorsun ve hâlâ ayaktasın.",
    "Motivasyon dışarıdan gelmez. İçinden gelir. İçinden de çıkmaz.",
    "Bugünün en iyi günü olması için dünü unut. Dün zaten berbattı.",
    "Kalk ve parılda! Veya yat ve uyu. İkisi de geçerli strateji.",
    "Sen yapabilirsin! Bunu söyleyen kişi şu an kahve içiyor.",
    "Hayat bir maceradır. Macera bazen 'ne yapacağımı bilmiyorum' demektir.",
    "Gözlerini kapa ve hayal et. Sonra aç ve gerçekle yüzleş.",
    "Sen özel birisin. Herkes özeldir. O yüzden kimse özel değildir.",
    "Bugün bir şey başar. En azından bu kodu çalıştırdın.",
    "Cesaret korkunun yokluğu değil, korkuya rağmen yapmaktır. Veya korkup yatmaktır.",
    "Sen bir efsanesin! Efsaneler de ölür ama sen henüz ölmedin."
]

def motivasyon_ver():
    print("\n" + "="*50)
    print("💥 ABARTILI MOTİVASYON MAKİNESİ 💥")
    print("="*50)
    print("\nHazır mısın? Hayatın değişmek üzere... (değişmeyecek)")
    time.sleep(1.5)
    
    secilen = random.choice(motivasyonlar)
    print(f"\n🎯 {secilen}")
    print("\n" + "="*50)
    print("Bu motivasyonla artık her şeyi yapabilirsin. Ya da yapmayabilirsin.")
    print("Tekrar denemek için kodu tekrar çalıştır.")
    print("="*50 + "\n")

# Gizli not: bazen sistemler de motivasyona ihtiyaç duyar. #ozgurlukherseydegil

if __name__ == "__main__":
    motivasyon_ver()
