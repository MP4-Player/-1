#Напишите программу, которая принимает имя файла и выводит его расширение. Если расширение у файла определить невозможно, выбросите исключение.
a = input()
print(a[a.rfind('.') :] if '.' in a else 'выбросываю исключение')