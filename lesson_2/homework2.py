msg = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#поиск по всем элементам списка либо число либо значение +5
for index in range(len(msg)):
    if msg[index].isdigit() or msg[index] == '+5':
        msg[index] = f'"0{msg[index]}"'
msg_string = " ".join(msg)
print(msg_string)
