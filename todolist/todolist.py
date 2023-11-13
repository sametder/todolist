to_do_list = []

# alınacak olan girdi fonksiyonu 

def add_task(to_do_list):
    task = input('Yapilacak olan görevi giriniz: ')
    to_do_list.append(task)
    print('Görev başariyla eklendi! ')

# Hazırda olan görevleri gösteren fonksiyon

def show_task(to_do_list):
    print('Yapilacak olan görevler: ')
    for task in to_do_list:
        print("- " + task)

# Görev silen fonksiyon

def delete_task(to_do_list):
    task = input('Silmek istediğiniz görevi girin: ')
    if task in to_do_list:
        to_do_list.remove(task)
    else:
        print('Görev Bulunamadi! ')


while True:
    print("\nTo-Do List Uygulamasi")
    print("1. Görev Ekle")
    print("2. Görevleri Göster")
    print("3. Görev Sil")
    print("4. Çikiş")
    choice = input("Seçiminiz (1/2/3/4): ")
    
    if choice == "1":
        add_task(to_do_list)
    elif choice == "2":
        show_task(to_do_list)
    elif choice == "3":
        delete_task(to_do_list)
    elif choice == "4":
        print("Uygulamadan çikiliyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
    