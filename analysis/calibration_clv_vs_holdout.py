def plot_calibration_clv_vs_holdout_clv(calibration_holdout_matrix, n_months):
    data = calibration_holdout_matrix.copy()
    data['clv_cal'] = (
        ((data['frequency_cal'] * data['monetary_value_cal']) / 1000).round(1)
    )
    data['clv_holdout'] = (data['clv_holdout'] / 1000).round(1)
    data[f'exp_clv_next_{n_months}m'] = (data[f'exp_clv_next_{n_months}m'] / 1000).round(1)
    ax = (data
      .groupby('clv_cal')[['clv_holdout', f'exp_clv_next_{n_months}m']].mean()
      .plot(
          xlabel='CLV (thousand of dollar) in Calibration Period', 
          ylabel='Average of CLV (thousand of dollar) in Holdout Period', 
          title='Actual CLV in Holdout Period vs Predicted CLV',
          figsize=(8, 5))
    )
    return ax