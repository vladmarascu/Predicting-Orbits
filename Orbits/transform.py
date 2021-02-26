import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
#sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")
%matplotlib inline
from poliastro.core.elements import rv2coe
from poliastro.bodies import Earth, Mars, Sun, Jupiter


# Function

def transform_rv_to_oe(df): # df as input 6dimensional r,v state space
    df_p = []
    df_ecc = []
    df_inc = []
    df_raan = []
    df_argp = []
    df_nu = []
    
    #Iterate all rows of R,V datapoints
    for i in range(0,500):
        
        rrr = np.array([df.x[i],df.y[i],df.z[i]])
        vvv = np.array([df.x_vv[i],df.y_vv[i],df.z_vv[i]])
        p,ecc,inc,raan,argp,nu = rv2coe(k=Earth.k*1e-9, r=rrr, v=vvv)
    
        df_p.append(p)
        df_ecc.append(ecc)
        df_inc.append(inc)
        df_raan.append(raan)
        df_argp.append(argp)
        df_nu.append(nu)
    
    # Write to DF with OE
    df_OE = pd.DataFrame(
        {'p': df_p,
         'ecc': df_ecc,
         'inc': df_inc,
         'raan': df_raan,
         'argp': df_argp,
         'nu': df_nu,
        })
    
    #print(df_OE.head())
    return df_OE # 6 dimensional output dataframe with orbital elements