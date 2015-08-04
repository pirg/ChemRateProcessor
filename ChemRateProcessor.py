import numpy as np
import pylab as pl
pl.ion()

# Sample data H3+ + CO
data = {}
# data['reaction'] = "H$_3^+$ + CO $\\rightarrow$ HCO$^+$ + H$_2$"
data['reaction'] = "H$_{3}$$^{+}$ + CO $\\rightarrow$ HCO$^+$ + H$_2$"

data['UMIST'] = {}
data['KIDA'] = {}
data['UMIST']['alpha']  = 1.36e-9
data['UMIST']['beta']   = -0.14
data['UMIST']['gamma']  = -3.40
data['UMIST']['F0']     = 1.25
data['UMIST']['trange'] = [10,400]
data['KIDA']['alpha']   = 1.61e-9
data['KIDA']['beta']    = 0
data['KIDA']['gamma']   = 0
data['KIDA']['F0']      = 1.25
data['KIDA']['trange']  = [10,280]

def kooji(alpha, beta, gamma):
    """return rate using the kooji formula
       k(T) = alpha * (beta/300) * exp(-gamma/T)"""
    return alpha * (T/300)**(beta) * np.exp(-gamma/T)

trange = [2,500]
npoint = 1000
T = np.linspace(trange[0],trange[1],npoint)

dblist = ["KIDA", "UMIST"]
rate  = {}
for db in dblist:
    rate[db] = kooji(data[db]['alpha'],data[db]['beta'],data[db]['alpha'])

pl.figure(1)
pl.clf()
for i, db in enumerate(dblist):
    line = pl.plot(T,rate[db],label = "{:>10} $\\alpha$={:.2e}, $\\beta$={:.2e}, $\\gamma$={:.2e}".format(db, data[db]['alpha'], data[db]['beta'], data[db]['gamma']))
    pl.fill_between(T,rate[db]/data[db]['F0'],rate[db]*data[db]['F0'],color=line[0].get_color(),alpha=0.1)
    pl.fill_betweenx(np.array([0.1e-9,0.2e-9])+0.1e-9*i, np.array([1,1])*data[db]['trange'][0], np.array([1,1])*data[db]['trange'][1],color=line[0].get_color() )

pl.ylim(ymin=0.)
pl.xlim(trange)
pl.ylabel('k(T) [$cm^3 s^{-1}$]')
pl.xlabel('T [$K$]')
pl.title(data['reaction'])
pl.savefig('ha/RateProcessor.pdf')

pl.legend()




