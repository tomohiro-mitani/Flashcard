import csv
import random


def create_dummy_csv():
    # csv header
    fieldnames = ['vocab', 'desc_en', 'desc_jp', 'desc_ch']

    # csv data
    rows = [{
        'vocab': 'きめつ',
        'desc_en': 'Damon Slayer',
        'desc_jp': '鬼滅',
        'desc_ch': '贵津'
    }, {
        'vocab': 'ひみつ',
        'desc_en': 'Secret',
        'desc_jp': '秘密',
        'desc_ch': '秘密'
    }]

    with open('text.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def random_keyword():
    with open('text.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        db_list = []
        next(reader)
        for row in reader:
            print(row)
            key_dic = {}
            key_dic['vocab']   = row[0]
            key_dic['desc_en'] = row[1]
            key_dic['desc_jp'] = row[2]
            key_dic['desc_ch'] = row[3]
            db_list.append(key_dic)

    return db_list[random.randrange(0, len(db_list))]
