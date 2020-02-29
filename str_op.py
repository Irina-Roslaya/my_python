s = "У лукоморья 123 дуб зеленый 456"
position=s.find('я')
if position==-1:
    print('Буква не встречается')
else:
    print('Позиция буквы "я":', position)
frequency = s.count("у")
print('Встречаемость буквы "у": ',frequency)
if s.isalpha()==True:
    None
else:
    s = s.upper()
    print(s)
if len(s) > 4:
    s = s.lower()
    print(s)
s = 'О' + s[1:]
print(s)

