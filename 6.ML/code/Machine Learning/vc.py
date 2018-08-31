# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms
import matplotlib.pyplot as mp
data = []
with open('../../data/car.txt', 'r') as f:
    for line in f.readlines():
        data.append(line[:-1].split(','))
data = np.array(data).T
encoders, x = [], []
for row in range(len(data)):
    encoder = sp.LabelEncoder()
    if row < len(data) - 1:
        x.append(encoder.fit_transform(
            data[row]))
    else:
        y = encoder.fit_transform(
            data[row])
    encoders.append(encoder)
x = np.array(x).T
model = se.RandomForestClassifier(max_depth=8,
                                  random_state=7)
n_estimators = np.linspace(20, 200, 10).astype(int)
train_scores1, test_scores1 = ms.validation_curve(
    model, x, y, 'n_estimators', n_estimators,
    cv=5)
train_means1 = train_scores1.mean(axis=1)
train_stds1 = train_scores1.std(axis=1)
test_means1 = test_scores1.mean(axis=1)
test_stds1 = test_scores1.std(axis=1)
model = se.RandomForestClassifier(n_estimators=140,
                                  random_state=7)
max_depth = np.linspace(1, 10, 11).astype(int)
train_scores2, test_scores2 = ms.validation_curve(
    model, x, y, 'max_depth', max_depth, cv=5)
train_means2 = train_scores2.mean(axis=1)
train_stds2 = train_scores2.std(axis=1)
test_means2 = test_scores2.mean(axis=1)
test_stds2 = test_scores2.std(axis=1)
mp.figure('Validation Curve', facecolor='lightgray')
mp.subplot(121)
mp.title('Validation Curve', fontsize=16)
mp.xlabel('n_estimators', fontsize=12)
mp.ylabel('F1 Score', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.fill_between(
    n_estimators, train_means1 - train_stds1,
    train_means1 + train_stds1, color='dodgerblue',
    alpha=0.25)
mp.fill_between(
    n_estimators, test_means1 - test_stds1,
    test_means1 + test_stds1, color='orangered',
    alpha=0.25)
mp.plot(n_estimators, train_means1, 'o-',
        c='dodgerblue', label='Training')
mp.plot(n_estimators, test_means1, 'o-',
        c='orangered', label='Testing')
mp.legend()
mp.subplot(122)
mp.title('Validation Curve', fontsize=16)
mp.xlabel('max_depth', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.fill_between(
    max_depth, train_means2 - train_stds2,
    train_means2 + train_stds2, color='dodgerblue',
    alpha=0.25)
mp.fill_between(
    max_depth, test_means2 - test_stds2,
    test_means2 + test_stds2, color='orangered',
    alpha=0.25)
mp.plot(max_depth, train_means2, 'o-',
        c='dodgerblue', label='Training')
mp.plot(max_depth, test_means2, 'o-',
        c='orangered', label='Testing')
mp.legend()
mp.tight_layout()
mp.show()
