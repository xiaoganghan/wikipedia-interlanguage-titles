import csv
import argparse


def find_records(line):
    records_str = line.partition('` VALUES ')[2]
    records_str = records_str.strip()[1:-2]
    records = records_str.split('),(')
    return records


def get_pages(page_sql_file):
    all_records = []
    for line in open(page_sql_file).readlines():
        if line.startswith('INSERT INTO '):
            all_records += find_records(line)

    pages = {}
    for record in all_records:
        reader = csv.reader([record], delimiter=',', doublequote=False, escapechar='\\', quotechar="'", strict=True)
        for columns in reader:
            page_id, page_title = int(columns[0]), columns[2]
            pages[page_id] = page_title
    return pages


def get_links(langlinks_sql_file, lang_code):
    all_records = []
    for line in open(langlinks_sql_file).readlines():
        if line.startswith('INSERT INTO '):
            all_records += find_records(line)

    pageid_titles = {}
    for record in all_records:
        reader = csv.reader([record], delimiter=',', doublequote=False, escapechar='\\', quotechar="'", strict=True)
        for columns in reader:
            ll_from, ll_lang, ll_title = columns
            if ll_lang == lang_code:
                pageid_titles[int(ll_from)] = ll_title
    return pageid_titles


def match_titles(page_file, langlinks_file, lang_code, output_file):
    pages = get_pages(page_file)
    pageid_titles = get_links(langlinks_file, lang_code)

    translations = []
    for ind, (page_id, ori_title) in enumerate(pages.items()):
        if page_id in pageid_titles:
            tar_title = pageid_titles[page_id]
            translations.append((page_id, ori_title, tar_title))

    with open(output_file, 'w') as f:
        for page_id, ori_title, tar_title in translations:
            f.write('{}\t{}\t{}\n'.format(page_id, ori_title, tar_title))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='wikipedia-interlanguage-titles: matching all the titles from two different languages on wikipedia')
    parser.add_argument('-p', '--page_file', help='page sql file, e.g. zhwiki-20160305-page.sql', required=True)
    parser.add_argument('-l', '--langlinks_file', help='langlinks sql file, e.g. zhwiki-20160305-langlinks.sql', required=True)
    parser.add_argument('-c', '--lang_code', help='target language code, e.g. en', required=True)
    parser.add_argument('-o', '--output_file', help='output file, e.g. translations.txt', required=True)
    args = vars(parser.parse_args())
    match_titles(**args)
