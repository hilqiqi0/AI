# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import numpy.fft as nf
import matplotlib.pyplot as mp
times = np.linspace(0, 2 * np.pi, 201)
sigs1 = 4 / (1 * np.pi) * np.sin(1 * times)
sigs2 = 4 / (3 * np.pi) * np.sin(3 * times)
sigs3 = 4 / (5 * np.pi) * np.sin(5 * times)
sigs4 = 4 / (7 * np.pi) * np.sin(7 * times)
sigs5 = 4 / (9 * np.pi) * np.sin(9 * times)
sigs6 = sigs1 + sigs2 + sigs3 + sigs4 + sigs5
freqs = nf.fftfreq(times.size,
                   times[1] - times[0])
ffts = nf.fft(sigs6)
pows = np.abs(ffts)
sigs7 = nf.ifft(ffts)
mp.figure('FFT', facecolor='lightgray')
mp.subplot(121)
mp.title('Time Domain', fontsize=16)
mp.xlabel('Time', fontsize=12)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times, sigs1,
        label='{:.4f}'.format(1 / (2 * np.pi)))
mp.plot(times, sigs2,
        label='{:.4f}'.format(3 / (2 * np.pi)))
mp.plot(times, sigs3,
        label='{:.4f}'.format(5 / (2 * np.pi)))
mp.plot(times, sigs4,
        label='{:.4f}'.format(7 / (2 * np.pi)))
mp.plot(times, sigs5,
        label='{:.4f}'.format(9 / (2 * np.pi)))
mp.plot(times, sigs6,
        label='{:.4f}'.format(1 / (2 * np.pi)))
mp.plot(times, sigs7, linewidth=6, alpha=0.5,
        label='{:.4f}'.format(1 / (2 * np.pi)))
mp.legend()
mp.subplot(122)
mp.title('Frequency Domain', fontsize=16)
mp.xlabel('Frequency', fontsize=12)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(freqs[freqs >= 0], pows[freqs >= 0],
        c='orangered',
        label='Frequency Spectrum')
mp.legend()
mp.tight_layout()
mp.show()
