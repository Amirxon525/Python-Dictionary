data = {"a": 1, "b": 2, "c": 3}
key = input("O‘chirish uchun kalit nomi: ")

if key in data:
    del data[key]
    print(f"{key} o‘chirildi.")
else:
    print("Bunday kalit yo‘q.")

print(data)