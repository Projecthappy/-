import numpy as np
import pylab as pl
import matplotlib.font_manager as fm
myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\ARIALN.TTF')
t = np.arange(0.0, 2.0*np.pi, 0.01)
s = np.sin(t)
z = np.cos(t*t)
pl.plot(t, s,'r',label='sin(x)')
pl.plot(t, z,'b--',label='cos(x^2)')
pl.xlabel('times(s)', fontproperties='simhei', fontsize=18)
pl.ylabel('Volt', fontproperties='simhei', fontsize=18)
pl.title('Sin and Cos figure using pyplot', fontproperties='simhei', fontsize=24)
pl.legend(prop=myfont)
pl.show()