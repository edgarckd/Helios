'''Este programa me calcula el voltaje de salida, potencia disipada vs la corriente que circula por el dispositivo.
'''

import numpy as np
import matplotlib.pyplot as plt

Resistors = [1.7,3.3,1,2,0.67,1.33]
current = np.linspace(0.010,75,1000)
i =0
fig, ax = plt.subplots(len(Resistors),2)

for resistencia in Resistors:
    h = 0.001*resistencia*current
    p = h*current
    #Vout.append(h)
    ax[i,0].set_title(f"{resistencia} mOhm", fontsize=8)
    ax[i,0].plot(current, h, label=f"{ str(f'{min(h)*1000 :,.2f}') +'mV' if 0.0010< min(h)< 1 else str(f'{min(h)*1000000:,.2f}') + 'uV'} - {max(h)*1000}mV")
    ax[i,0].set_ylabel("V(i)")
    ax[i,0].legend(loc='best')
    ax[i,0].grid()
    ax[i,0].set_ylim(min(h), max(h))
    ax[i,0].set_xlim(0.01, 75)
    ax[i,0].set_xticks(range(0,75,5), fontsize=2)
    ax[i,0].set_yticks(np.linspace(min(h),max(h),4))

    ax[i,1].set_title(f"{resistencia} mOhm", fontsize=8)
    ax[i,1].plot(current, p,label=f"{str(f'{min(p)*1000 :,.2f}') +'mW' if 0.0010< min(p)< 1 else str(f'{min(h)*1000000:,.2f}') + 'uW'} - {max(p):,.2f}W; {max(p)/300*100 :,.2f}%")
    ax[i,1].set_ylabel("P(i)")
    ax[i,1].legend(loc='best')
    ax[i,1].grid()
    ax[i,1].set_ylim(min(p), max(p))
    ax[i,1].set_xlim(0.01, 75)
    ax[i,1].set_xticks(range(0,75,5))
    ax[i,1].set_yticks(np.linspace(min(p),max(p),4))
    i=i+1
ax[len(Resistors)-1, 0].set_xlabel("Corriente I")
ax[len(Resistors)-1, 1].set_xlabel("Corriente I")

fig.suptitle("Resistencias Shunt SMB fabricante Megatron")

plt.subplots_adjust(left=0.1, 
                    bottom=0.1,  
                    right=0.9,  
                    top=0.9,  
                    wspace=0.4,  
                    hspace=0.4)
plt.show()
