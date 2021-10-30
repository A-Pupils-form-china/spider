import json

f = open("test.html", 'r')
data_file = open("data.txt", 'w')
data = {'album': {}}
amount = 1
flag = False
album = ''
song_amount = 1
skip = False
for i in f.read().replace(';&amp', 'And').split('\n'):
    if i.__contains__("Fearless"):
        skip = False
    if i.__contains__("Sounds Of The Season: The Taylor Swift Holiday Collection"):
        skip = True
    if skip:
        continue
    if i.__contains__('album:') and not i.__contains__('..'):
        data['album'][amount] = i[i.find("<b>") + 3:i.find("</b>")].replace('\"', '')
        amount += 1
        print(i[i.find("<b>") + 3:i.find("</b>")].replace('\"', ''))
        song_amount = 1
        album = i[i.find("<b>") + 3:i.find("</b>")].replace('\"', '')
        data[album] = {}

    if i.__contains__('_blank') and not album == '':
        data[album][song_amount] = i[i.find("_blank") + 8:i.find('</a>')].replace('&amp;', '')
        if i[i.find("_blank") + 8:i.find('</a>')].replace('&amp;', '').__contains__("You All Over Me"):
            data[album][song_amount] = "You All Over Me"
        song_amount += 1
        print(i[i.find("_blank") + 8:i.find('</a>')])
        if i[i.find("_blank") + 8:i.find('</a>')] == 'Bye Bye Baby (Taylor\'s Version) (From The Vault)':
            break

json.dump(data, data_file)
