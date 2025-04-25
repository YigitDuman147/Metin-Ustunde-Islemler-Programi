import time
import tkinter as tk
from tkinter import messagebox, font


def console_menu():
    print("Merhaba Kullanıcı! Ne yapmak istersiniz?\n")
    print("1-) Metinde verilen kelimelerin harlerini alt alta yazdırma")
    print("2-) Girilen metnin orjinalini, Tamamen tersi alınmış halini ve Kelime kelime tersi alınmış halini bulma")
    print("3-) Metin içinde geçen Tüm “a” harflerinin büyük harf “A” haline getirme")
    print("4-) Metin içinde geçen kelimeleri ayrı ayrı yazdırma")
    print("5-) Metnin ayrılan kelimelerini yeniden birleştirme")
    print("6-) Metin içinde kaç tane ünlü harf olduğunu bulma")
    print("7-) Metinin yazı yazma hızını hesaplama\n")


baslangic_zamani = 0


def alt_alta(metin):
    kelimeler = metin.split()
    sonuc = ""
    for kelime in kelimeler:
        for harf in kelime:
            sonuc += harf + "\n"
        sonuc += "\n"
    return sonuc


def metnin_tersi(metin):
    orjinal = metin
    tamamen_ters = metin[::-1]
    kelime_kelime_ters = ' '.join([kelime[::-1] for kelime in metin.split()])
    return f"Orjinal Metin: {orjinal}\nTamamen Tersi: {tamamen_ters}\nKelime kelime ters: {kelime_kelime_ters}"


def kucuk_alar_buyuk_a(metin):
    return metin.replace("a", "A")


def kelimeleri_ayirma(metin):
    return metin.split()


def ayrilari_birlestirme(metin):
    return metin.replace(" ", "")


def kac_tane_unlu(metin):
    unlu_harfler = "aeıioöuüAEIİOÖUÜ"
    sayac = 0
    for harf in metin:
        if harf in unlu_harfler:
            sayac += 1
    return f"Metin içinde geçen ünlü harf sayısı: {sayac}"


def yazma_hizi_hesapla(metin):
    global baslangic_zamani
    bitis_zamani = time.time()
    sure = bitis_zamani - baslangic_zamani
    uzunluk = len(metin)
    hiz = uzunluk / sure
    return f"Geçen süre: {sure} saniye\nMetni yazma hızınız: {hiz} harf/saniye"


def arayuz_baslat():
    def islem_yap(secenek):
        metin = entry.get()
        if secenek == 1:
            sonuc = alt_alta(metin)
        elif secenek == 2:
            sonuc = metnin_tersi(metin)
        elif secenek == 3:
            sonuc = kucuk_alar_buyuk_a(metin)
        elif secenek == 4:
            sonuc = kelimeleri_ayirma(metin)
        elif secenek == 5:
            sonuc = ayrilari_birlestirme(metin)
        elif secenek == 6:
            sonuc = kac_tane_unlu(metin)
        elif secenek == 7:
            sonuc = yazma_hizi_hesapla(metin)
        else:
            sonuc = "Geçersiz seçenek."
        messagebox.showinfo("Sonuç", sonuc)

    def basla():
        global baslangic_zamani
        baslangic_zamani = time.time()
        messagebox.showinfo("Başla", "Yazmaya başlayabilirsiniz.")

    root = tk.Tk()
    root.title("Metin Üzerinde İşlemler Programı")
    root.geometry("800x600")
    root.configure(bg="#f0f8f0")

    baslik_font = font.Font(family="Helvetica", size=16, weight="bold")
    button_font = font.Font(family="Arial", size=12)

    tk.Label(root, text="Metin Üzerinde İşlemler Programı", font=baslik_font, bg="#f0f8f0", fg="#333333").pack(pady=10)

    tk.Label(root, text="Metin Giriniz:", font=button_font, bg="#f0f8f0").pack(pady=10)
    entry = tk.Entry(root, width=50, font=button_font)
    entry.pack(pady=4)

    buton_renk = "#87ceeb"
    buton_renk2 = "#4682b4"
    messagebox.showinfo("Başla", "Yazmaya başlayabilirsiniz.")
    tk.Button(root, text="Başla", font=button_font, bg=buton_renk, command=basla).pack(pady=5)
    tk.Button(root, text="1. Harfleri Alt Alta Yazdır", font=button_font, bg=buton_renk2,
              command=lambda: islem_yap(1)).pack(pady=10)
    tk.Button(root, text="2. Ters Çevirme İşlemi", font=button_font, bg=buton_renk, command=lambda: islem_yap(2)).pack(
        pady=10)
    tk.Button(root, text="3. 'a' Harflerini Büyük Yap", font=button_font, bg=buton_renk2,
              command=lambda: islem_yap(3)).pack(pady=10)
    tk.Button(root, text="4. Kelimeleri Ayır", font=button_font, bg=buton_renk, command=lambda: islem_yap(4)).pack(
        pady=10)
    tk.Button(root, text="5. Kelimeleri Birleştir", font=button_font, bg=buton_renk2,
              command=lambda: islem_yap(5)).pack(pady=10)
    tk.Button(root, text="6. Ünlü Harf Sayısı", font=button_font, bg=buton_renk, command=lambda: islem_yap(6)).pack(
        pady=10)
    tk.Button(root, text="7. Yazma Hızı Hesapla", font=button_font, bg=buton_renk2, command=lambda: islem_yap(7)).pack(
        pady=10)

    tk.Button(root, text="Çıkış", font=button_font, bg="#ff4500", command=root.quit).pack(pady=10)

    root.mainloop()


arayuz_baslat()