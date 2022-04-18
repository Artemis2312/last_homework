import numpy as np
from astropy import units as u
import matplotlib.pyplot as plt
#importing necessary things in order to run code
#uploading the information from sed.txt
data=np.loadtxt('/home/atheodoridis/AST4930/HW7/sed.txt', delimiter = ',')
wave= data[:,0] #* u.micron
lum=data[:,1] #* (u.Lsun/u.micron)
#creating wave and data variables to use later on

#using np.where to distinguish between all values that are meant to be excluded and the ones that need to be counted
waves=np.where((wave<=1000) & (wave>=10))
print(waves)

#creating a second version of both variables as new, clean arrays
newWave=np.asarray(wave[waves])
newLum=np.asarray(lum[waves])
#using np. trapz but setting newWave negative in order to make it go from ascending values to descending
FinWave=np.trapz(newLum, x=-newWave)
print(FinWave)

#converting the Finwave Lsun value into astropy units and then converting it into ergs/s 
FinWave *= u.Lsun
Finwave2=FinWave.to(u.erg/u.s)
print(Finwave2)

#plotting the function in log space
plt.plot(wave,lum)
plt.xscale('log')
plt.xlabel("Wavelength")
plt.ylabel("Luminosity")
plt.yscale('log')
plt.savefig('sample.graph1.png')


