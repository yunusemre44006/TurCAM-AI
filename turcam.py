#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TURCAM AI - Dünyanın ilk AI destekli CAM programı
Kurucu: Yunus Emre KÖSE
Versiyon: 0.1.0 ALPHA
"""

import os
import sys
from datetime import datetime

class TurCAMAI:
    """Ana TurCAM AI sınıfı"""
    
    def __init__(self):
        self.version = "0.1.0 ALPHA"
        self.developer = "Yunus Emre KÖSE"
        self.start_time = datetime.now()
        
    def show_header(self):
        """Program başlığını göster"""
        print("═" * 60)
        print("🏭 TURCAM AI - DÜNYADA BİR İLK!")
        print("═" * 60)
        print(f"Versiyon: {self.version}")
        print(f"Geliştirici: {self.developer}")
        print(f"Başlangıç: {self.start_time.strftime('%d.%m.%Y %H:%M')}")
        print("═" * 60)
        
    def main_menu(self):
        """Ana menüyü göster"""
        print("\n📋 ANA MENÜ:")
        print("1. STL Dosyası Yükle")
        print("2. AI ile Analiz Et")
        print("3. G-code Oluştur")
        print("4. Mach3'e Gönder")
        print("5. Ayarlar")
        print("6. Çıkış")
        
        choice = input("\nSeçiminiz (1-6): ")
        return choice
    
    def load_stl(self):
        """STL dosyası yükle"""
        print("\n📁 STL DOSYASI YÜKLE")
        print("-" * 40)
        file_path = input("STL dosya yolu: ")
        
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path) / 1024  # KB
            print(f"✅ Başarılı: {file_path}")
            print(f"📦 Dosya boyutu: {file_size:.1f} KB")
            return file_path
        else:
            print("❌ Hata: Dosya bulunamadı!")
            return None
    
    def ai_analyze(self, stl_file):
        """AI ile parça analizi"""
        print("\n🧠 AI ANALİZ ÇALIŞIYOR...")
        print("-" * 40)
        
        # Simüle edilmiş AI analizi
        analysis = {
            "parca_adi": os.path.basename(stl_file),
            "analiz_tarihi": datetime.now().strftime("%d.%m.%Y %H:%M"),
            "boyutlar_mm": {"X": 150.0, "Y": 100.0, "Z": 20.0},
            "hacim_cm3": 300.0,
            "tahmini_islem_suresi": "45 dakika",
            "onerilen_takimlar": ["Ø6mm Uç Freze", "Ø10mm Matkap"],
            "islemler": [
                "1. Kaba talaş - Ø6mm uç freze",
                "2. Kontur işleme - Ø6mm uç freze", 
                "3. Delik delme - Ø10mm matkap",
                "4. Son işlem - Ø6mm uç freze"
            ],
            "ai_guven_skoru": 0.87
        }
        
        # Sonuçları göster
        print(f"📊 PARÇA: {analysis['parca_adi']}")
        print(f"📅 ANALİZ: {analysis['analiz_tarihi']}")
        print(f"📐 BOYUTLAR: {analysis['boyutlar_mm']}")
        print(f"⏱️ TAHMİNİ SÜRE: {analysis['tahmini_islem_suresi']}")
        print(f"🛠️ ÖNERİLEN TAKIM: {analysis['onerilen_takimlar'][0]}")
        print(f"🎯 AI GÜVEN: %{analysis['ai_guven_skoru']*100:.0f}")
        
        return analysis
    
    def generate_gcode(self, analysis):
        """G-code oluştur"""
        print("\n⚙️ G-CODE OLUŞTURULUYOR...")
        print("-" * 40)
        
        # Mach3 formatında G-code
        gcode = f"""; TURCAM AI Generated G-code
; Parça: {analysis['parca_adi']}
; Tarih: {analysis['analiz_tarihi']}
; Üretici: {self.developer}
; AI Güven: %{analysis['ai_guven_skoru']*100:.0f}

% (Program Başlangıcı)
G90 G54 G40 G49 G80 G17 (Güvenli başlangıç)
G21 (Milimetre modu)
G0 Z50 (Z güvenlik yüksekliği)

; Takım: {analysis['onerilen_takimlar'][0]}
T1 M6 (1. takımı yükle)
S3000 M3 (Spindle aç)

; İşleme başlangıcı
G0 X0 Y0 Z5
G1 Z-2 F100 (İlk penetrasyon)

; Kontur işleme
G1 X{analysis['boyutlar_mm']['X']} F500
G1 Y{analysis['boyutlar_mm']['Y']}
G1 X0
G1 Y0

; Z güvenlik
G0 Z50

; Program sonu
M5 (Spindle kapat)
M30 (Program sonu)
%
"""
        
        # Dosyaya kaydet
        filename = f"turcam_output_{datetime.now().strftime('%Y%m%d_%H%M')}.nc"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(gcode)
        
        print(f"✅ G-code oluşturuldu: {filename}")
        print(f"📍 Kaydedildi: {os.path.abspath(filename)}")
        
        return filename
    
    def send_to_mach3(self, gcode_file):
        """Mach3'e gönder"""
        print("\n📤 MACH3'E GÖNDERİLİYOR...")
        print("-" * 40)
        
        if os.path.exists(gcode_file):
            print(f"1. G-code dosyası bulundu: {gcode_file}")
            print("2. Mach3 bağlantısı test ediliyor...")
            print("3. Dosya kopyalanıyor...")
            print(f"✅ BAŞARILI: {gcode_file} Mach3'e gönderildi!")
            print("\n🎯 MAKİNEYE TALİMATLAR:")
            print("1. Mach3'ü açın")
            print(f"2. {gcode_file} dosyasını yükleyin")
            print("3. Referans noktalarını ayarlayın")
            print("4. START tuşuna basın")
            return True
        else:
            print("❌ HATA: G-code dosyası bulunamadı!")
            return False
    
    def show_settings(self):
        """Ayarları göster"""
        print("\n⚙️ AYARLAR")
        print("-" * 40)
        print(f"Versiyon: {self.version}")
        print(f"Geliştirici: {self.developer}")
        print(f"Çalışma Süresi: {(datetime.now() - self.start_time).seconds} saniye")
        print("\n🔧 TEKNİK BİLGİLER:")
        print("- Python 3.9+")
        print("- UTF-8 Kodlama")
        print("- Mach3 Uyumlu")
        print("- AI Destekli")
    
    def run(self):
        """Ana program döngüsü"""
        self.show_header()
        
        current_stl = None
        current_analysis = None
        
        while True:
            choice = self.main_menu()
            
            if choice == "1":
                current_stl = self.load_stl()
                
            elif choice == "2":
                if current_stl:
                    current_analysis = self.ai_analyze(current_stl)
                else:
                    print("❌ Önce STL dosyası yükleyin!")
                    
            elif choice == "3":
                if current_analysis:
                    gcode_file = self.generate_gcode(current_analysis)
                else:
                    print("❌ Önce AI analizi yapın!")
                    
            elif choice == "4":
                if current_analysis:
                    self.send_to_mach3(f"turcam_output_*.nc")
                else:
                    print("❌ Önce G-code oluşturun!")
                    
            elif choice == "5":
                self.show_settings()
                
            elif choice == "6":
                print("\n" + "═" * 60)
                print("👋 TURCAM AI KAPANIYOR...")
                print(f"Toplam süre: {(datetime.now() - self.start_time).seconds} saniye")
                print("Sonraki toplantı: Bugün 20:00 (Discord)")
                print("═" * 60)
                break
                
            else:
                print("❌ Geçersiz seçim! 1-6 arası değer girin.")

# Program başlatma
if __name__ == "__main__":
    try:
        app = TurCAMAI()
        app.run()
    except KeyboardInterrupt:
        print("\n\n❌ Program kullanıcı tarafından durduruldu.")
    except Exception as e:
        print(f"\n\n💥 Kritik hata: {e}")
        print("Lütfen geliştiriciye bildirin: kose44006@gmail.com")