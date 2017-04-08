from __future__ import division, print_function

import pandas as pd 
import matplotlib.path as mplPath
import numpy as np 

def get_nta_codes(lons_lats,geo):

    nta_codes = np.empty(lons_lats.shape[0],dtype='object')
    nta_codes[:] = ''

    for nta_code in geo:

        pts = geo[nta_code].dropna().values
        pts = pts.reshape((int(pts.shape[0]/2),2))
        nta_Path = mplPath.Path(pts)
        is_in_nta = nta_Path.contains_points(lons_lats)
        nta_codes[is_in_nta] = nta_code

    return nta_codes

def add_pickup_nta_codes(taxi_data,geo):

    lons_lats = taxi_data.loc[:,['pickup_longitude','pickup_latitude']].as_matrix()
    nta_codes = get_nta_codes(lons_lats,geo)
    taxi_data.loc[:,'pickup_NTA_code'] = pd.Series(nta_codes,index=taxi_data.index)

    return None

def add_dropoff_nta_codes(taxi_data,geo):

    lons_lats = taxi_data.loc[:,['dropoff_longitude','dropoff_latitude']].as_matrix()
    nta_codes = get_nta_codes(lons_lats,geo)
    taxi_data.loc[:,'dropoff_NTA_code'] = pd.Series(nta_codes,index=taxi_data.index)

    return None


