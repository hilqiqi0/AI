# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import nltk.stem as ns
words = ['table', 'probably', 'wolves', 'playing', 'is',
         'dog', 'the', 'beaches', 'grounded', 'dreamt',
         'envision']
lmm = ns.WordNetLemmatizer()
for word in words:
    n = lmm.lemmatize(word, pos='n')
    v = lmm.lemmatize(word, pos='v')
    print('{:10} {:10} {:10}'.format(word, n, v))
