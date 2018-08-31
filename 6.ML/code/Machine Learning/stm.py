# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import nltk.stem.porter as pt
import nltk.stem.lancaster as lc
import nltk.stem.snowball as sb
words = ['table', 'probably', 'wolves', 'playing', 'is',
         'dog', 'the', 'beaches', 'grounded', 'dreamt',
         'envision']
porter = pt.PorterStemmer()
lancaster = lc.LancasterStemmer()
snowball = sb.SnowballStemmer('english')
for word in words:
    pstem = porter.stem(word)
    lstem = lancaster.stem(word)
    sstem = snowball.stem(word)
    print('{:10} {:10} {:10} {:10}'.format(
        word, pstem, lstem, sstem))
