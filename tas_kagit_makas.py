import random
import time

print("TAŞ KAĞIT MAKAS")

pc_input_list = ["taş","kağıt","makas"]

user_score = 0
pc_score = 0

while True:
    time.sleep(0.5)
    print("****************\n")
    print(f"senin skor: {user_score}\n"
          f"bilgisayar skor: {pc_score}\n")
    print("****************\n")

    if user_score == 3 or pc_score == 3:
        time.sleep(1)
        break

    pc_choice = pc_input_list[random.randint(0, 2)]
    user_choice = input("--> taş / kağıt / makas ? ")

    if pc_choice == user_choice:
        time.sleep(1)
        print(f"\nikiniz de {pc_choice} yaptınız...")
        time.sleep(0.5)
        continue

    elif pc_choice == "taş" and user_choice == "kağıt":
        time.sleep(1)
        print(f"\nbilgisayar {pc_choice} yaptı")
        time.sleep(0.5)
        print("\nkağıt taşı alır")
        user_score += 1

    elif pc_choice == "kağıt" and user_choice == "makas":
        time.sleep(1)
        print(f"\nbilgisayar {pc_choice} yaptı")
        time.sleep(0.5)
        print("\nmakas kağıtı alır")
        user_score += 1

    elif pc_choice == "makas" and user_choice == "taş":
        time.sleep(1)
        print(f"\nbilgisayar {pc_choice} yaptı")
        time.sleep(0.5)
        print("\ntaş makası alır")
        user_score += 1


    elif user_choice == "taş" and pc_choice == "kağıt":
        time.sleep(1)
        print(f"\nbilgisayar {pc_choice} yaptı")
        time.sleep(0.5)
        print("\nkağıt taşı alır")
        pc_score += 1

    elif user_choice == "kağıt" and pc_choice == "makas":
        time.sleep(1)
        print(f"\nbilgisayar {pc_choice} yaptı")
        time.sleep(0.5)
        print("\nmakas kağıtı alır")
        pc_score += 1

    elif user_choice == "makas" and pc_choice == "taş":
        time.sleep(1)
        print(f"\nbilgisayar {pc_choice} yaptı")
        time.sleep(0.5)
        print("\ntaş makası alır")
        pc_score += 1

if pc_score == 3:
    print("kaybettin.... :(")

elif user_score == 3:
    print("KAZANDIN!!!! AFERİN ")
