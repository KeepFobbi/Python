minutesForSleep = int(input("Введите минуты:\n"))
hoursAtSleep = int(input("Часы:"))
minutesAtSleep = int(input("Минуты:"))

rez = hoursAtSleep * 60 + minutesAtSleep + minutesForSleep

print("Sample Output:\n", rez // 60)
print(rez % 60)