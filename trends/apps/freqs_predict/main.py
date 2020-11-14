import json
import numpy as np
from sklearn.svm import SVR
from itertools import groupby
import random
import datetime
import os

def normalize_data(DIR):
    with open(os.path.join(DIR, 'data', 'freqs.json'), encoding='utf-8') as json_file:
        freqs = json.load(json_file)
    for freq in freqs:
        freq['count'] = freq['count'].replace(',', '')
        dates = freq['date'].split('/')

        freq['date'] = '/'.join([date if len(date) == 2 else '0' + date for date in dates])

    with open(os.path.join(DIR, 'data', 'freqs_norm.json'), 'w', encoding='utf-8') as json_file:
        json.dump(freqs, json_file, indent=4, ensure_ascii=False)


def grouper(item):
        return item['name']


def predict_data(DIR, months_count, C, epsilon, kernel):
    svr = SVR(kernel=kernel, C=C, epsilon = epsilon)
    with open(os.path.join(DIR, 'data', 'freqs_norm.json'), encoding='utf-8') as json_file:
        freqs = json.load(json_file)

    result_freqs = []
    for name, items in groupby(freqs, key=grouper):
        T = [[i, item['count'], item['date']] for i, item in enumerate(items)]
        X = [val[0] for val in T]
        Y = [int(val[1]) for val in T]


        predicted_X = []
        for i in range(len(X), len(X) + months_count):
            predicted_X.append(i)

        n_X = np.array(X).reshape(-1, 1)
        n_predicted_X = np.array(predicted_X).reshape(-1, 1)


        Y2 = svr.fit(n_X, Y).predict(np.array(X).reshape(-1, 1))
        predicted_Y = svr.predict(n_predicted_X)

        Y_res = []
        X_res = [i for i in X]

        std = np.std(Y)

        for pred in Y:
            Y_res.append(pred)

        for pred in predicted_Y:
            pred += random.random() * std
            Y_res.append(round(pred))

        for pred in predicted_X:
             X_res.append(pred)

        dates = [val[2] for val in T]
        new_dates = []

        for date in dates:
            dates_split = date.split('/')
            year = int('20' + dates_split[2])
            month = int(dates_split[0])
            day = int(dates_split[1])
            new_date = datetime.date(year, month, day)
            new_dates.append(new_date.strftime('%d-%m-%Y'))


        last_date = dates[len(dates)-1]
        dates_split = last_date.split('/')
        year = int('20' + dates_split[2])
        month = int(dates_split[0])
        day = int(dates_split[1])

        t = 0
        for i in range(1, months_count + 1):
            t += 1
            if month + t == 13:
                month = 1
                t = 0
                year += 1
            new_date = datetime.date(year, month + t, day)
            new_dates.append(new_date.strftime('%d-%m-%Y'))


        for i in range(0, len(Y_res)):
            result_freqs.append({
                "name": name,
                "date": new_dates[i],
                "count": Y_res[i],
            })

    with open(os.path.join(DIR, 'data', 'predicted_freqs.json'), 'w', encoding='utf-8') as json_file:
        json.dump(result_freqs, json_file, indent=4, ensure_ascii=False)


def main():
    DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DIR = os.path.join(DIR, "freqs_predict")
    with open(os.path.join(DIR, 'settings.json'), encoding='utf-8') as json_file:
        settings = json.load(json_file)
    normalize_data(DIR)
    predict_data(DIR, settings['months_count'], settings['C'], settings['epsilon'], settings['kernel'])

main()

