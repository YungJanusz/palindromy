"""wyraz = input(str("Podaj wyraz: "))
licznik = 1
for i in wyraz:
    if i == wyraz[len(wyraz)-licznik]:
        licznik += 1
    else:
        print("Wyraz nie jest palindromem!")
        break

print("Wyraz " + wyraz + " jest palindromem!!!")"""

wyraz = input(str("Podaj wyraz: "))
if wyraz == wyraz[::-1]:
    print("Wyraz jest palindromem")
else:
    print("Wyraz nie jest palindromem")
print(wyraz[::-1])