from _future_ import division, print_function, unicode_literals

import numpy as np
import os

np.random.seed(42)
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes',labelsize=14)
mpl.rc('xtick',labelsize=12)
mpl.rc('ytick',labelsize=12)

PROJECT_ROOT_DIR="."
CHAPTER_ID="fundamentals"

def save_fig(fig_id,tight_layout=True):
    path=os.path.join(PROJECT_ROOT_DIR,"images",CHAPTER_ID,fig_id+".png")
    print("Saving figure",fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path,format='png',dpi=300)

import warnings 
warnings.filterwarnings(action="ignore",message="^internal gelsd")


def prepare_country_stats(oecd_bli,gdp_per_capita):


