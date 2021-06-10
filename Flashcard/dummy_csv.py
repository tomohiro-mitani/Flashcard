import csv
import random


def create_dummy_csv():
    # csv header
    fieldnames = ['item_id', 'word-jp', 'word-en', 'word-zh']

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
    with open('Flashcards_final.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        db_list = []
        next(reader)
        for row in reader:
            print(row)
            key_dic = {}
            key_dic['item_id'] = row[0]
            key_dic['word-jp'] = row[1]
            key_dic['word-en'] = row[2]
            db_list.append(key_dic)

    return db_list[random.randrange(0, len(db_list))]


def check_state():
    # csv header

    with open('state.csv', newline='') as csvfile:
        s_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        s_db_list = []
        next(s_reader)
        for s_row in s_reader:
            print(s_row)
            s_key_dic = {}
            s_key_dic['state'] = s_row[0]
            s_db_list.append(s_key_dic)
        print(s_db_list[0])
    return s_db_list[0]


def update_true():
    # csv header
    fieldnames = ['state']
    # csv data
    rows = [{
        'state': 'true',
    }]
    with open('state.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    f.close()


def update_false():
    # csv header
    fieldnames = ['state']
    # csv data
    rows = [{
        'state': 'false',
    }]
    with open('state.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    f.close()


def save_keyword(keyword):
    # csv header
    fieldnames = ['keyword']
    # csv data
    rows = [{
        'keyword': keyword,
    }]
    with open('keyword.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def lookup_keyword():
    with open('keyword.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        s_db_list = []
        next(reader)
        for row in reader:
            print(row)
            key_dic = {}
            key_dic['keyword'] = row[0]
            s_db_list.append(key_dic)
        keyword = s_db_list[0]['keyword']
        print(keyword)

    with open('test_flashcards.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        db_list = []
        next(reader)
        for row in reader:
            if row[1] == keyword:
                key_dic = {}
                key_dic['item_id'] = row[0]
                key_dic['word-jp'] = row[1]
                key_dic['word-en'] = row[2]
                db_list.append(key_dic)

    return db_list[0]
