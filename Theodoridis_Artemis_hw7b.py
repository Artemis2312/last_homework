import numpy as np
from astropy import units as u
import matplotlib.pyplot as plt

data=np.loadtxt('/home/atheodoridis/AST4930/HW7/sed.txt', delimiter = ',')
wave= data[:,0] #* u.micron
lum=data[:,1] #* (u.Lsun/u.micron)


waves=np.where((wave<=1000) & (wave>=10))
print(waves)

newWave=np.asarray(wave[waves])
newLum=np.asarray(lum[waves])
FinWave=np.trapz(newLum, x=-newWave)
print(FinWave)

FinWave *= u.Lsun
Finwave2=FinWave.to(u.erg/u.s)
print(Finwave2)

plt.plot(wave,lum)
plt.xscale('log')
plt.xlabel("Wavelength")
plt.ylabel("Luminosity")
plt.yscale('log')
plt.savefig('sample.graph1.png')


