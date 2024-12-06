import lifetimes
from lifetimes import BetaGeoFitter, GammaGammaFitter
from lifetimes.utils import *
from lifetimes.plotting import *
from sklearn.metrics import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_holdout_purchase_vs_prob_alive(calibration_holdout_matrix, bgf):
    data = calibration_holdout_matrix.copy().reset_index()
    data['prob_alive'] = bgf.conditional_probability_alive(
        data['frequency_cal'], 
        data['recency_cal'], 
        data['T_cal']).round(1)
    data['have_purchased'] = data['frequency_holdout'].apply(lambda x: 'yes' if x > 0 else 'no')

    plot_data = data.groupby(['prob_alive', 'have_purchased']).size() / data.groupby('prob_alive').size()
    plot_data = plot_data.reset_index(name='ratio')

    ax = sns.barplot(data=plot_data, x='prob_alive', y='ratio', hue='have_purchased')
    ax.set_title('Probability of Alive vs Ratio of Customers Who Have Actual Purchase')
    ax.set_xlabel('Probability of Alive')
    ax.set_ylabel('Ratio of Customers')

    return ax