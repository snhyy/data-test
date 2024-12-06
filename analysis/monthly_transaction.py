import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_monthly_transactions(data, year):
    # Convert "InvoiceDate" to datetime format if not already done
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

    # Extract the year and month from the "InvoiceDate" column
    data['YearMonth'] = data['InvoiceDate'].dt.to_period('M')

    # Count the number of rows for each month
    monthly_counts = data.groupby('YearMonth').size()

    # Filter for the specified year
    monthly_counts_year = monthly_counts[monthly_counts.index.year == year]

    print(f"Total transactions: {monthly_counts_year.sum()}")

    # Plotting
    plt.figure(figsize=(12, 6))
    a = sns.barplot(x=monthly_counts_year.index.astype(str), y=monthly_counts_year.values, palette='viridis')
    plt.title(f'Monthly Transactions in {year}', fontsize=16)
    plt.xlabel('Month', fontsize=14)
    plt.ylabel('Number of Transactions', fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add transaction counts on top of the bars
    for p in a.patches:
        a.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha='center', va='bottom', fontsize=10)

    plt.show()