# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import neurolab as nl
import matplotlib.pyplot as mp
charset = 'omandig'
x, y = [], []
with open('../../data/ocrdb.dat', 'r') as f:
    for line in f.readlines():
        items = line.split('\t')
        char, image = items[1], items[6:-1]
        if char in charset:
            code = np.zeros(len(charset), dtype=int)
            code[charset.index(char)] = 1
            y.append(code)
            x.append(np.array(image, dtype=int))
            if len(x) >= 30:
                break
x = np.array(x)
y = np.array(y)
train_size = int(len(x) * 0.8)
train_x, test_x = x[:train_size], x[train_size:]
train_y, test_y = y[:train_size], y[train_size:]
input_ranges = []
for _ in x.T:
    input_ranges.append([0, 1])
model = nl.net.newff(input_ranges, [128, 16, y.shape[1]])
model.trainf = nl.train.train_gd
error = model.train(train_x, train_y, epochs=10000,
                    show=100, goal=0.01)
pred_test_y = model.sim(test_x)


def decode(codes):
    return ''.join(
        charset[code.argmax()] for code in codes)


true_string = decode(test_y)
pred_string = decode(pred_test_y)
print(true_string, '->', pred_string)
axes = mp.subplots(1, len(test_x), num='OCR',
                   facecolor='lightgray')[1]
for ax, char_image, true_char, pred_char in zip(
        axes, test_x, true_string, pred_string):
    ax.matshow(char_image.reshape(16, 8), cmap='brg')
    ax.set_title('{}{}{}'.format(
        true_char,
        '==' if true_char == pred_char else '!=',
        pred_char), fontsize=14, color='dodgerblue'
        if true_char == pred_char else 'orangered')
    ax.set_xticks(())
    ax.set_yticks(())
mp.figure('Training Process', facecolor='lightgray')
mp.title('Training Process', fontsize=20)
mp.xlabel('Epoch', fontsize=14)
mp.ylabel('Error', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(error, c='orangered', label='Error')
mp.legend()
mp.show()
