from desimalToBiner import desimalToBiner

desimal = int(input("Masukan bilangan desimal : "))
converter = desimalToBiner(desimal)
binary = converter.convert()

print(f"\nHasil konversi bilangan desimal {desimal} ke biner ", end=": ")
for i in range (len(binary)):
    if i % 4 == 0:
        print(" ", end="")
    print(binary[i], end="")

print("\nLangkah-langkah yang dilakukan untuk konversi")
converter.get_explanation()