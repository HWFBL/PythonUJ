import roman

print('\nzad 3.1')
print('\nponizej poprawny weslug mnie kod')
x, y = 2, 3
if x > y:
    result = x
else:
    result = y

line = 'qwerty'
for i in line:
    if ord(i) < 100:
        print(i)

line = 'axby'
for i in line:
    if ord(i) < 100:
        print(ord(i))
    else:
        print(i)
#3.2
print('\nzad3.2')
L = [3, 5, 4] ; L = L.sort() #w porzadku jednak tablica nam sie nadpisze
x, y = 1, 2, 3 #dwie zmienne trzy wartosci blad przypisania wartosci
X = 1, 2, 3 ; X[1] = 4 #poniewaz jest to krotka to nie mozna uzywac na niej takiej operacji nie bedzie to dzialac
X = [1, 2, 3] ; X[3] = 4 #indeksy liczone od zera wyjscie poza zakres
X = "abc" ; X.append("d") #jest to string wiec taka funkcja nie zadziala
map(pow, range(8)) # funkcja map przyjmuje dwa argumenty funkcja pow nie jest w tym przypadku argumentem
#zad3.3
print('\nzad 3.3')
for i in range(31):
    if i%3 == 0:
        continue
    else:
        print(i)
#zad3.4
print('\nzad 3.4')
x = None
while x != 'stop':
    x = input('Prosze podac liczbe x: ')
    if x.isnumeric():
        x = float(x)
        print('\noto para liczb x i jej trzecia potega\n')
        print(x, x**3)
    elif isinstance(x, str):
        print('Blad! Prosze podac liczbe!')
        continue
#zad3.5
print('zad 3.5')
lenght = int(input('podaj dlugosc miarki'))
lineUp = '|'
lineDown = '0'
for i in range(lenght):
    lineUp += '....|'
    if i < 10:
        lineDown +='    {0}'.format(i+1)
    else:
        lineDown += '   {0}'.format(i+1)
print(lineUp)
print(lineDown)
#zad3.6
try:
    width = int(input('podaj szerokosc: '))
    height = int(input('podaj wysokosc: '))
except ValueError:
    print('prosze podac liczbe!')

pWidth = "+"
kWidth = "---+"
pHeight = "|"
kHeight = "   |"

A = pWidth + width * kWidth + ""
B = pHeight + width * kHeight + ""

result = ""

for x in range (height):
    result = result + A + "\n"
    result = result + B + "\n"

result = result + A + "\n"
print(result)
#zad 3.8
print('zad 3.8')
seq1 = "mielonka"
seq2 = "biedronka"
alist = []
for item in seq1:
    if item in seq2:
        alist.append(item)
print(alist)
result = list(set(seq1+seq2))
print(result)
#zad 3.9
print('zad 3.9')
D = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
result = list(map(sum, D))
print(result)
#zad 3.10
print('zad 3.10')
rom = input("Podaj liczbe rzymska: ")
ara = 0
ara = roman.fromRoman(rom.upper())
print("Liczba w postaci arabskiej: ", ara)







