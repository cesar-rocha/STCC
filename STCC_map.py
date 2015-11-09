import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

class map(object):
    """ a class that represents the Tropical Pacific Basemap object """
    
    def __init__(
        self,
        lonmin=110.,
        lonmax=185,
        latmin=5,
        latmax=40,
        lat_m=-17.,
        proj="mercartor",
        linewidth=.5,
        fontsize=12.,
        fig_label=None,
        fig_title=None):

            self.lonmin = lonmin
            self.lonmax = lonmax
            self.latmin = latmin
            self.latmax = latmax
            self.lat_m = lat_m
            self.proj = proj
            self.lw = linewidth
            self.fs = fontsize
            self.label= fig_label
            self.title = fig_title

            
            self.m = Basemap(projection='merc',llcrnrlat=self.latmin,urcrnrlat=self.latmax,
                    llcrnrlon=self.lonmin,urcrnrlon=lonmax,lat_ts=lat_m,resolution='i')


    def draw_par_mer(self):
        """ draw parallel and meridians """
        self.m.drawparallels(np.arange(int(self.latmin), int(self.latmax), 5),
            labels=[1, 0, 0, 0], linewidth=self.lw, fontsize=self.fs)
        self.m.drawmeridians(np.arange(self.lonmin, self.lonmax+4, 7),
            labels=[0, 0, 0, 1], linewidth=self.lw, fontsize=self.fs)

    def set_label(self,pos=(1650212,1485371)):
        plt.text(pos[0],pos[1], self.label,size=32)

    def set_title(self,pos=(1400212,1495371)):
        plt.text(pos[0],pos[1], self.title, size=25, rotation=0.,
            ha="center", va="center",bbox = dict(boxstyle="round",ec='k',fc='w'))



