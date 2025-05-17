import tkinter as tk
from tkinter import scrolledtext

bilgi_tabani = {
    "selam": {
        "anahtar_kelimeler": ["merhaba", "selam", "iyi günler", "hello", "hi"],
        "yanit": "Merhaba! Mehmet Akif Ersoy Üniversitesi hakkında size nasıl yardımcı olabilirim? Fakülteler, kayıt işlemleri, kampüs hayatı ve daha fazlası hakkında sorularınızı sorabilirsiniz."
    },
    "fakulteler": {
        "anahtar_kelimeler": ["fakülte", "bölüm", "bölümler", "program", "öğrenim alanı"],
        "yanit": "Mehmet Akif Ersoy Üniversitesi'nde Eğitim Fakültesi, Fen Edebiyat Fakültesi, İktisadi ve İdari Bilimler Fakültesi, Mühendislik-Mimarlık Fakültesi, Veteriner Fakültesi gibi fakülteler vardır. Her fakültede farklı bölümler bulunur. Daha fazla bilgi için üniversitenin web sitesini ziyaret edebilirsiniz."
    },
    "kayit": {
        "anahtar_kelimeler": ["kayıt", "başvuru", "kayıt işlemi", "kabul", "yerleştirme"],
        "yanit": "Üniversite kayıt işlemleri ÖSYM sonuçları açıklandıktan sonra başlar. Gerekli belgeler ve süreç öğrenci işleri tarafından sağlanır. Detaylar için öğrenci işleri web sitesini kontrol edebilirsiniz."
    },
    "kampus_hayati": {
        "anahtar_kelimeler": ["kampüs", "kampüs hayatı", "sosyal hayat", "yaşam"],
        "yanit": "MAKÜ kampüsü yeşil alanlar, sosyal tesisler, spor alanları ve kafeteryalarla öğrencilere rahat bir ortam sunar. Kütüphane, öğrenci kulüpleri ve kültürel etkinliklerle sosyal hayat zengindir."
    },
    "burslar": {
        "anahtar_kelimeler": ["burs", "burslar", "yardım", "destek"],
        "yanit": "Üniversite başarılı ve ihtiyaç sahibi öğrenciler için KYK bursları, başarı bursları gibi çeşitli burs imkanları sunar. Detaylı bilgi burs ofisinden alınabilir."
    },
    "yurt": {
        "anahtar_kelimeler": ["yurt", "konaklama", "barınma", "öğrenci yurdu", "oda"],
        "yanit": "Kampüse yakın devlet ve özel yurtlar mevcuttur. Ayrıca Burdur şehir merkezinde de konaklama seçenekleri bulunur. Yurt başvurusu ve ücret bilgileri KYK ve konaklama biriminden öğrenilebilir."
    },
    "ogrenci_kulupleri": {
        "anahtar_kelimeler": ["kulüp", "öğrenci kulübü", "kulüpler", "etkinlik", "organizasyon", "topluluk"],
        "yanit": "Üniversitede spor, kültür, sanat ve bilim alanlarında birçok öğrenci kulübü vardır. Kulüplerle ilgili bilgi ve etkinlik duyuruları için öğrenci kulüpleri birimiyle iletişim kurulabilir."
    },
    "kutuphane": {
        "anahtar_kelimeler": ["kütüphane", "kitap", "kaynak", "okuma", "sessiz çalışma"],
        "yanit": "Üniversite kütüphanesinde geniş kitap ve dijital kaynak koleksiyonu vardır. Sessiz çalışma alanları ve ödünç kitap hizmeti sunulur. Çalışma saatleri ve hizmetler üniversite kütüphane sayfasında bulunabilir."
    },
    "etkinlikler": {
        "anahtar_kelimeler": ["etkinlik", "festival", "konferans", "panel", "turnuva", "organizasyon"],
        "yanit": "Üniversitede yıl boyunca konferanslar, paneller, festivaller ve spor turnuvaları düzenlenir. Etkinlik duyurularını üniversitenin etkinlik sayfasından takip edebilirsiniz."
    },
    "tesekkur": {
        "anahtar_kelimeler": ["teşekkür", "sağol", "mersi", "thanks", "thank you"],
        "yanit": "Rica ederim! Başka bir konuda yardımcı olabileceğim bir şey olursa sormaktan çekinmeyin."
    },
    "gorusuruz": {
        "anahtar_kelimeler": ["görüşürüz", "hoşça kal", "çıkış", "çık", "bye", "bye bye"],
        "yanit": "Görüşmek üzere! Mehmet Akif Ersoy Üniversitesi hakkında tekrar bilgi almak isterseniz buradayım."
    }
}

def yanit_ver(kullanici_girdi):
    kullanici_girdi = kullanici_girdi.lower()
    for veri in bilgi_tabani.values():
        if any(anahtar in kullanici_girdi for anahtar in veri["anahtar_kelimeler"]):
            return veri["yanit"]
    return "Üzgünüm, bu konuda size yardımcı olamıyorum. Mehmet Akif Ersoy Üniversitesi hakkında başka bir sorunuz varsa lütfen sorun."

def mesaj_gonder(event=None):
    girdi = kullanici_girdi.get().strip()
    if girdi:
        sohbet_alani.config(state=tk.NORMAL)
        sohbet_alani.insert(tk.END, f"Siz: {girdi}\n", "kullanici")
        cevap = yanit_ver(girdi)
        sohbet_alani.insert(tk.END, f"Chatbot: {cevap}\n\n", "bot")
        sohbet_alani.config(state=tk.DISABLED)
        sohbet_alani.see(tk.END)
        kullanici_girdi.delete(0, tk.END)

pencere = tk.Tk()
pencere.title("MAKÜ Chatbot")
pencere.geometry("450x650")
pencere.resizable(False, False)
pencere.config(bg="#f5f5f5")

baslik = tk.Label(pencere, text="MAKÜ Chatbot", font=("Rockwell", 20, "bold"), bg="#4B0082", fg="white", pady=15)
baslik.grid(row=0, column=0, columnspan=2, sticky="nsew")

sohbet_alani = scrolledtext.ScrolledText(pencere, state=tk.DISABLED, wrap=tk.WORD, font=("Rockwell", 13), bg="white", fg="#222222", bd=3, relief="ridge", height=28, width=55)
sohbet_alani.grid(row=1, column=0, columnspan=2, padx=15, pady=15, sticky="nsew")
sohbet_alani.tag_config("kullanici", foreground="#4B0082", font=("Rockwell", 13, "bold"))
sohbet_alani.tag_config("bot", foreground="#333333", font=("Rockwell", 13))

kullanici_girdi = tk.Entry(pencere, font=("Rockwell", 14), bd=3, relief="groove", width=45)
kullanici_girdi.grid(row=2, column=0, padx=(15, 5), pady=10, sticky="w")

gonder_butonu = tk.Button(pencere, text="Gönder", command=mesaj_gonder, bg="#4B0082", fg="white", font=("Rockwell", 13, "bold"), relief="raised", padx=25, pady=7)
gonder_butonu.grid(row=2, column=1, padx=(5, 15), pady=10, sticky="e")

pencere.bind("<Return>", mesaj_gonder)

pencere.grid_rowconfigure(1, weight=1)
pencere.grid_columnconfigure(0, weight=1)

pencere.mainloop()
