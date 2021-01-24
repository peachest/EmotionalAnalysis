# !/usr/bin/env python
# Author Everlearner
# Created 2021/1/22
# User Stephen Zhang
# By PyCharm
# File Encoding Utf-8

import csv
from timelineplotter import *

data_in_times = []
csv_file_1 = open("emotional_words_1.csv", 'r', newline='')
csv_file_2 = open("emotional_words_2.csv", 'r', newline='')
csv_file_3 = open("emotional_words_3.csv", 'r', newline='')
csv_file_4 = open("emotional_words_4.csv", 'r', newline='')

reader_1 = csv.DictReader(csv_file_1)
reader_2 = csv.DictReader(csv_file_2)
reader_3 = csv.DictReader(csv_file_3)
reader_4 = csv.DictReader(csv_file_4)

pair_data = []
for row in reader_1:
    pair = (row["高频词"], int(float(row["TF-IDF"]) * 1000))
    pair_data.append(pair)

data_in_times.append(pair_data)

pair_data = []
for row in reader_2:
    pair = (row["高频词"], int(float(row["TF-IDF"]) * 1000))
    pair_data.append(pair)

data_in_times.append(pair_data)

pair_data = []
for row in reader_3:
    pair = (row["高频词"], int(float(row["TF-IDF"]) * 1000))
    pair_data.append(pair)

data_in_times.append(pair_data)

pair_data = []
for row in reader_4:
    pair = (row["高频词"], int(float(row["TF-IDF"]) * 1000))
    pair_data.append(pair)

data_in_times.append(pair_data)

plot_timeline(data_in_times)
