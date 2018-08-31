# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import matplotlib.pyplot as mp
sample_rate, noised_sigs = wf.read(
    '../../data/noised.wav')
noised_sigs = noised_sigs / 2 ** 15
times = np.arange(
    len(noised_sigs)) / sample_rate
freqs = nf.fftfreq(times.size, d=1 / sample_rate)
noised_ffts = nf.fft(noised_sigs)
noised_pows = np.abs(noised_ffts)
fund_freq = freqs[noised_pows.argmax()]
print(fund_freq)
noised_indices = np.where(
    np.abs(freqs) != fund_freq)
filter_ffts = noised_ffts.copy()
filter_ffts[noised_indices] = 0
filter_pows = np.abs(filter_ffts)
filter_sigs = nf.ifft(filter_ffts).real
wf.write('../../data/filter.wav', sample_rate,
         (filter_sigs * 2 ** 15).astype(np.int16))
mp.figure('Filter', facecolor='lightgray')
mp.subplot(221)
mp.title('Time Domain', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:178], noised_sigs[:178],
        c='orangered', label='Noised')
mp.legend()
mp.subplot(222)
mp.title('Frequency Domain', fontsize=16)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.semilogy(freqs[freqs >= 0],
            noised_pows[freqs >= 0],
            c='limegreen', label='Noised')
mp.legend()
mp.subplot(223)
mp.xlabel('Time', fontsize=12)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:178], filter_sigs[:178],
        c='hotpink', label='Filter')
mp.legend()
mp.subplot(224)
mp.xlabel('Frequency', fontsize=12)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(freqs[freqs >= 0],
        filter_pows[freqs >= 0],
        c='dodgerblue', label='Filter')
mp.legend()
mp.tight_layout()
mp.show()
