"""
E-commerce Customer Retention Analysis
Email: 23f3003311@ds.study.iitm.ac.in
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Quarterly customer retention data
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Retention_Rate': [65.08, 67.72, 76.68, 75.14]
}

df = pd.DataFrame(data)
industry_target = 85
average_retention = df['Retention_Rate'].mean()

print("=" * 60)
print("E-COMMERCE CUSTOMER RETENTION ANALYSIS")
print("=" * 60)
print(f"\nQuarterly Retention Rates:")
for i, row in df.iterrows():
    print(f"  {row['Quarter']}: {row['Retention_Rate']}%")

print(f"\nAverage Retention Rate: {average_retention:.2f}%")
print(f"Industry Target: {industry_target}%")
print(f"Gap to Target: {industry_target - average_retention:.2f}%")
print("=" * 60)

# Calculate percentage change
df['Growth'] = df['Retention_Rate'].pct_change() * 100

print("\nQuarter-over-Quarter Growth:")
for i in range(1, len(df)):
    print(f"  {df.loc[i-1, 'Quarter']} → {df.loc[i, 'Quarter']}: {df.loc[i, 'Growth']:.2f}%")

# Create visualizations
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Line chart with target
ax1.plot(df['Quarter'], df['Retention_Rate'], marker='o', linewidth=2, markersize=8, label='Actual Retention')
ax1.axhline(y=industry_target, color='r', linestyle='--', linewidth=2, label=f'Target ({industry_target}%)')
ax1.axhline(y=average_retention, color='g', linestyle=':', linewidth=2, label=f'Avg ({average_retention:.1f}%)')
ax1.fill_between(df['Quarter'], df['Retention_Rate'], industry_target, where=(df['Retention_Rate'] < industry_target), 
                 color='red', alpha=0.2, label='Below Target')
ax1.set_title('Customer Retention Rate - Quarterly Trend', fontsize=14, fontweight='bold')
ax1.set_xlabel('Quarter', fontsize=12)
ax1.set_ylabel('Retention Rate (%)', fontsize=12)
ax1.legend()
ax1.grid(True, alpha=0.3)

# Plot 2: Bar chart with improvement needed
improvement_needed = industry_target - df['Retention_Rate']
colors = ['red' if rate < industry_target else 'green' for rate in df['Retention_Rate']]

bars = ax2.bar(df['Quarter'], improvement_needed, color=colors, alpha=0.7)
ax2.set_title('Improvement Needed to Reach Target', fontsize=14, fontweight='bold')
ax2.set_xlabel('Quarter', fontsize=12)
ax2.set_ylabel('Gap to Target (%)', fontsize=12)
ax2.axhline(y=0, color='black', linewidth=0.8)

# Add value labels on bars
for bar, value in zip(bars, improvement_needed):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{value:.1f}%', ha='center', va='bottom', fontweight='bold')

ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('retention_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Calculate required improvement
current_rate = df['Retention_Rate'].iloc[-1]
required_improvement = ((industry_target - current_rate) / current_rate) * 100

print("\n" + "=" * 60)
print("ANALYSIS SUMMARY")
print("=" * 60)
print(f"1. Current average retention: {average_retention:.2f}%")
print(f"2. Distance from target: {industry_target - average_retention:.2f}%")
print(f"3. Best performing quarter: Q3 ({df['Retention_Rate'].max()}%)")
print(f"4. Worst performing quarter: Q1 ({df['Retention_Rate'].min()}%)")
print(f"5. Required improvement from Q4: {required_improvement:.1f}%")
print("=" * 60)
