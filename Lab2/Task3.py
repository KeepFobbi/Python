num = int(input("Введите число: "))

if  num>=0:
  if num==0:
    print(str(num) + " программистов")
  elif num % 100 >= 10 and num % 100 <= 20:
    print(str(num) + " программистов")
  elif num % 10 == 1:
    print(str(num) + " программист")
  elif num % 10 >= 2 and num % 10 <= 4:
    print(str(num) + " программиста")
  else:
    print(str(num) + " программистов")

# if num == 1:
#     print(num, "програмист")
# elif 2 <= num <= 4:   
#     print(num, "програмиста")
# elif 5 <= num <= 1000 or num == 0:
#     print(num, "програмистов")