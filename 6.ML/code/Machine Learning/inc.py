# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.naive_bayes as nb


class DigitEncoder():

    def fit_transform(self, y):
        return y.astype(int)

    def transform(self, y):
        return y.astype(int)

    def inverse_transform(self, y):
        return y.astype(str)


num_less, num_more, max_each = 0, 0, 7500
data = []
with open('../../data/adult.txt', 'r') as f:
    for line in f.readlines():
        line_data = line[:-1].split(', ')
        if line_data[-1] == '<=50K' and \
                num_less < max_each:
            data.append(line_data)
            num_less += 1
        elif line_data[-1] == '>50K' and \
                num_more < max_each:
            data.append(line_data)
            num_more += 1
        if num_less >= max_each and \
                num_more >= max_each:
            break
data = np.array(data).T
encoders, x = [], []
for row in range(len(data)):
    if data[row, 0].isdigit():
        encoder = DigitEncoder()
    else:
        encoder = sp.LabelEncoder()
    if row < len(data) - 1:
        x.append(encoder.fit_transform(data[row]))
    else:
        y = encoder.fit_transform(data[row])
    encoders.append(encoder)
x = np.array(x).T
train_x, test_x, train_y, test_y = ms.train_test_split(
    x, y, test_size=0.25, random_state=7)
model = nb.GaussianNB()
print(ms.cross_val_score(model, x, y, cv=10,
                         scoring='f1_weighted').mean())
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print((pred_test_y == test_y).sum() / pred_test_y.size)
data = [[
    '39', 'State-gov', '77516', 'Bachelors', '13',
    'Never-married', 'Adm-clerical', 'Not-in-family',
    'White', 'Male', '2174', '0', '40',
    'United-States']]
data = np.array(data).T
x = []
for row in range(len(data)):
    encoder = encoders[row]
    x.append(encoder.transform(data[row]))
x = np.array(x).T
pred_y = model.predict(x)
print(encoders[-1].inverse_transform(pred_y))
