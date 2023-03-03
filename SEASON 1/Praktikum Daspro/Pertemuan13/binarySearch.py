def sorting(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j >= 0 and arr[j - 1]> key:
            arr[j] = arr[j - 1]
            j-=1
            arr[j] = key
    return arr

numbers = [1, 3, 5]
sorting(numbers)
print(f"""{"Program Menggunakan Binary Search".center(50)}
{"="*50}
Daftar Angka : {numbers}\n""")
ask = input("Ingin menambahkan data (Y/t) ? ").lower()
while ask == "y":
    found = False
    add = int(input("\ningin tambah angka berapa ? "))
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == add:
            found = True
            break
        elif numbers[mid] < add:
            left = mid + 1
        else:
            right = mid - 1
    if found:
        print(f"angka {add} sudah ada")
        ask = input("Ingin menambahkan angka yang lain (Y/t) ? ").lower()
    else:
        numbers.append(add)
        sorting(numbers)
        print(f"Angka berhasil ditambahkan : {numbers}")
        ask = input("Ingin menambahkan angka lagi (Y/t) ? ").lower()
print(f"""\n{"="*50}
Data akhir : {numbers}""")
