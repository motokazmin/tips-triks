import numpy as np
import pandas as pd
import re

# clean_name - чистит текс от непечатных символов
def clean_name(name):
    name = re.sub(r'[^\w]', ' ', name)
    name = re.sub(r'[,:._\-\[\]\d]', ' ', name)

    return name.strip()

# get_texts - Парсит текстовую колонку DataFrame и возвращает распаршенные слова в виде Series
# df - DataFrame, колонку которого будем парсить
# label - имя колонки для парсинга
# reset_index - сбрасываем индекс или нет
# drop_nsymbol - минимальное колличество символов в слове, попадающие в результат
# lower_case - переводить в нижний регист или нет
# unique - оставлять только уникальные значения
# sort - сортировать выход или нет
# return Series
def get_texts(df, label, reset_index = True, drop_nsymbol = 0, lower_case = False,
              unique = True, sort = False):
    texts = df[label].str.split().explode()

    if lower_case == True:
        texts = texts.str.lower()
    if unique == True:
        texts = texts.drop_duplicates()
    if sort == True:
        texts = texts.sort_values()
    texts = texts[texts.str.len() > drop_nsymbol]
    if reset_index == True:
        texts = texts.reset_index(drop = True)

    return texts

# get_stat_by_word - возвращает колличество вхождений каждого слова в датасет
# df - DataFrame, колонку которого будем парсить
# label - имя колонки для парсинга
# drop_nsymbol - минимальное колличество символов в слове, попадающие в результат
# lower_case - переводить в нижний регист или нет
# return Series
def get_stat_by_word(df, label, drop_nsymbol = 0, lower_case = False):

    names = get_texts(df, label, reset_index = False, drop_nsymbol = drop_nsymbol,
                      unique = False, lower_case = lower_case)
    words = names.groupby(names).apply(len)
    words.name = 'count'
    return words

# compare_two_text_features - возвращат результат oper над двумя текстовыми колонками одного и того же датасета
# df - DataFrame, колонку которого будем парсить
# label1 - имя первой колонки для парсинга
# label2 - имя второй колонки для парсинга
# oper - логическая операция, применяемая над данными
# drop_nsymbol - минимальное колличество символов в слове, попадающие в результат
# lower_case - переводить в нижний регист или нет
# unique - оставлять только уникальные значения
# return set
def compare_two_text_features(df, label1, label2, oper, drop_nsymbol = 0, lower_case = False, unique = False):
    names1 = set([*get_texts(df, label1, reset_index = False, drop_nsymbol = drop_nsymbol,
                      unique = False, lower_case = lower_case)])
    names2 = set([*get_texts(df, label2, reset_index = False, drop_nsymbol = drop_nsymbol,
                      unique = False, lower_case = lower_case)])

    if oper =='|':
        return names1|names2
    elif oper == '&':
        return names1&names2
    elif oper == 'left':
        return names1.difference(names2)
    elif oper == 'right':
        return names2.difference(names1)

# compare_two_text_features - возвращат результат oper над текстовой колонкой одного и того же датасета,
# но для двух разных значений(val1, val2) другой колонки idx
# df - DataFrame, колонку которого будем парсить
# label - имя колонки для парсинга
# idx - имя колонки, которая определяет условие для фильтрации данных
# val1 - первое значение колонки idx
# val2 - второе значение колонки idx
# oper - логическая операция, применяемая над данными
# drop_nsymbol - минимальное колличество символов в слове, попадающие в результат
# lower_case - переводить в нижний регист или нет
# unique - оставлять только уникальные значения
# return set
def compare_features_two_index(df, label, idx, val1, val2, oper, drop_nsymbol, lower_case = False, unique = False):
    names1 = set([*get_texts(df[df[idx] == val1], label, reset_index = False, drop_nsymbol = drop_nsymbol,
                      unique = unique, lower_case = lower_case)])
    names2 = set([*get_texts(df[df[idx] == val2], label, reset_index = False, drop_nsymbol = drop_nsymbol,
                      unique = unique, lower_case = lower_case)])

    if oper =='|':
        return names1|names2
    elif oper == '&':
        return names1&names2
    elif oper == 'left':
        return names1.difference(names2)
    elif oper == 'right':
        return names2.difference(names1)

def compare_features_all_with_one_index(df, label, idx, val1, oper, drop_nsymbol, lower_case = False, unique = False):
    names1 = set([*get_texts(df[df[idx] == val1], label, reset_index = False, drop_nsymbol = drop_nsymbol,
                      unique = unique, lower_case = lower_case)])
    names2 = set([*get_texts(df[df[idx] != val1], label, reset_index = False, drop_nsymbol = drop_nsymbol,
                      unique = unique, lower_case = lower_case)])

    if oper =='|':
        return names1|names2
    elif oper == '&':
        return names1&names2
    elif oper == 'left':
        return names1.difference(names2)
    elif oper == 'right':
        return names2.difference(names1)

