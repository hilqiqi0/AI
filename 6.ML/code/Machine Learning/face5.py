# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.datasets as sd
import sklearn.decomposition as dc
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import matplotlib.pyplot as mp
faces = sd.fetch_olivetti_faces('../../data/')
x = faces.data
y = faces.target
model = dc.PCA(n_components=140)
pca_x = model.fit_transform(x)
train_x, test_x, train_y, test_y = ms.train_test_split(
    pca_x, y, test_size=0.2, random_state=7)
model = svm.SVC(class_weight='balanced')
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print((pred_test_y == test_y).sum() / len(pred_test_y))
print(sm.classification_report(test_y, pred_test_y))
cm = sm.confusion_matrix(test_y, pred_test_y)
mp.figure('Confusion Matrix', facecolor='lightgray')
mp.title('Confusion Matrix', fontsize=20)
mp.xlabel('Predicted Class', fontsize=14)
mp.ylabel('True Class', fontsize=14)
mp.tick_params(labelsize=10)
mp.imshow(cm, interpolation='nearest', cmap='gray')
mp.show()
