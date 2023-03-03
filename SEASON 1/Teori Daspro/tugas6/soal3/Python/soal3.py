bil1 = 0
bil2 = 1
n = bil1 + bil2
jml = 1
print(f"Fibonacci = {bil1}, {bil2}, ", end="")
while n <= 500:
    print(n, end=", ")
    bil1, bil2 = bil2, n
    jml += n
    n = bil1 + bil2
print("Jumlah total = ", jml)
