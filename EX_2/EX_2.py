"""
kasutaja annab input-i, kui mitu erinevat asja ta näha tahab. (1-6)

Näiteks
kui kasutaja sisestan 4 siis avanevad 4 akent, mis näitavad erinevaid asju.

boonus kui asjad toimuvad randomiga

kui klahvi vajutada siis kustuvad kõik aknad.

"""
import os
import cv2
import random

# Kausta teekond, kust pildid valitakse.
folder_path = "C:\\Users\\Dell\\PycharmProjects\\Pictures"

# Kontrollime, kas kaust eksisteerib.
if not os.path.exists(folder_path):
    print(f"Kaust {folder_path} ei eksisteeri.")
else:
    # Loendi loomine, mis sisaldab kõiki pildifaile kaustas.
    images = [img for img in os.listdir(folder_path) if img.endswith(('.png', '.jpg', '.jpeg'))]

    # Küsime kasutajalt mitu pilti näidata, kuni sisestatakse õige arv.
    while True:
        num_images = int(input("Sisesta, kui palju pilte näha soovid (1-6): "))
        if 1 <= num_images <= 6:
            break
        else:
            print("Sisesta arv vahemikus 1 kuni 6.")

    # Valime juhuslikud pildid vastavalt kasutaja sisestatud arvule.
    selected_images = random.sample(images, num_images)

    # Kuvame iga valitud pildi eraldi aknas.
    for i, img_name in enumerate(selected_images):
        img_path = os.path.join(folder_path, img_name)
        image = cv2.imread(img_path)
        window_name = f"Pilt {i + 1}"
        cv2.imshow(window_name, image)

    # Ootame, kuni kasutaja vajutab klahvi, et kõik aknad sulgeda.
    cv2.waitKey(0)
    cv2.destroyAllWindows()
