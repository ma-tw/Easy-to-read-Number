import math
import decimal

print(
    '--------------------------------------------------------------------------\n'
    '数字は半角数字で入力してください。カンマ及びスペースは自動で除去されます。\n'
    '--------------------------------------------------------------------------'
    )
while True:
    try:
        entered_num = input('数字を入力 >> ')
        num = float(entered_num.translate(str.maketrans({
            ',': '',
            ' ': '',
        })))

    except ValueError as err:
        print(f'値"{entered_num}"は不正です。')
        print(err + '\n')

    else:
        break

mes = ['万 ', '億 ', '兆 ', '京 ', '垓 ', '杼 ', '穣 ', '溝 ', '澗 ', '正 ', '載 ', '極 ']

num_integer = math.modf(num)[1]
num_fraction = decimal.Decimal(str(num)) - decimal.Decimal(str(math.modf(num)[1]))

#if math.modf(num)[0] == 0:
def readint(num_integer):
    str_integer = str(int(num_integer))
    l = []

    #4字ごとに区切ってlへ
    for i in range(math.ceil(len(str_integer)/4)):
        l.append(str(int(str_integer[-4*(i+1):len(str_integer)-4*i])))

    #mesを入れる
    for i in range(len(l)-1):
        l.insert(2*i+1, mes[i])

    l.reverse()
    
    #0とそれに続く単位を消す
    for i in range(len(l)):
        if l[i] == '0':
            l[i] = ''
            if i + 1 <= len(l) - 1:
                l[i+1] = ''

    return ''.join(l)

if num_fraction == 0:
    answer = readint(num_integer)
else:
    answer = readint(num_integer) + ' . ' + str(num_fraction).replace('0.', '')

print('\n' + answer + '\n')