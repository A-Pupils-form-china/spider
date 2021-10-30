import json
import os


data = dict(json.load(open("../整活/data.txt", 'r')))


def main():
    for i in data.items():
        if i[0] == 'album':
            continue
        for j in i[1].values():
            os.system("cd txt")
            os.system("mkdir txt\\%s" % i[0].replace(' ', ''))
            print(j)
            with open("origin/%s/%s.html" % (
                    i[0].replace(' ', ''),
                    j.replace(' ', '') if not j.__contains__('?') else j.replace(' ', '').replace('?', '')),
                      'r',
                      encoding='utf8') as r:
                with open("txt/%s/%s.txt" % (
                        i[0].replace(' ', ''),
                        j.replace(' ', '') if not j.__contains__('?') else j.replace(' ', '').replace('?', '')),
                          'w',
                          encoding='utf8') as w:
                    temp = r.read().split('\n')
                    is_active = False
                    lyric = ''
                    r = '[’!"#$%&\'()*+,.-/:;<=>?@[\\]^_`{|}~。！，]+'
                    for sentence in temp:
                        if sentence.__contains__(
                                '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'):
                            is_active = True
                            continue
                        if sentence.__contains__('<!-- MxM banner -->'):
                            break
                        if is_active:
                            # line = re.sub(r, '', text)
                            lyric += (" " + sentence + ' \n').replace('<br>', '').replace('</div>', '').replace(
                                '&quot;', '').lower()
                    w.write(lyric)


def test():
    with open("origin/Red/Red.html",
              'r',
              encoding='utf8') as r:
        with open("txt/Red.txt",
                  'w',
                  encoding='utf8') as w:
            temp = r.read().split('\n')
            is_active = False
            lyric = ''
            for sentence in temp:
                if sentence.__contains__(
                        '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'):
                    is_active = True
                    continue
                if sentence.__contains__('<!-- MxM banner -->'):
                    break
                if is_active:
                    lyric += (sentence + '\n').replace('<br>', '').replace('</div>', '')
            w.write(lyric)


main()
