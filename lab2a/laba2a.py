1. print("First constant", None)
print("First constant",True)
print("First constant", False)

2.a1=(1, "Masha", True, 2)
print(any(a1))

a2=(1, "Masha", False, 123)
print(all(a2))

a3=(1, 4, 1.4, 3.6)
print(sorted(a3))

3. def main():
    x, y = 108, 407

    if (x < y):
        res = "Х менший за У"

    elif (x == y):
        res = "Х дорівнює У"

    else:
        res = "Х більший за У"
    print (res)

if name == "main":
 main()

4. a=100;
while a > 0:
    a = a/2;
    if a <= 1:
        break
    print(a)
print("Далі 'а' менше за одиницю!")

5.arr1 = [5, 8, 4]
try:
    print(arr1[3])
except Exception as err:
    print(err)
finally:
    print("Error found")

6. with open("laba2a.txt", "w") as file:
    file.write("Go out from my territory!")

7. from functools import reduce
arr = [1, 3, 4, 2, 7]
total = reduce(lambda x, y: x+y,arr)
print(f'Сума всіх елементів масиву - {total}')
