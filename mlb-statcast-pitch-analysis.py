import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_name = 'Data_MLB_2025_StatcastPostseason_PitchByPitch_20251102a.csv'

try:
    df = pd.read_csv(file_name)
    print("✅ Data loaded successfully!")

    # Create hit variable using 'events' column
    hit_events = ['single', 'double', 'triple', 'home_run']
    df['hit_label'] = df['events'].apply(lambda x: 1 if x in hit_events else 0)

    # Descriptive Statistics 
    core_cols = ['release_speed', 'release_spin_rate', 'pfx_x', 'pfx_z']
    print("\n--- [Section 1] Descriptive Statistics of Pitch Physics ---")
    print(df[core_cols].describe())

    sns.set_theme(style="whitegrid")

    # Correlation Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[core_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Matrix: Pitch Physics")
    plt.savefig('correlation_heatmap.png')
    print("✅ 1. Correlation heatmap saved")

    # Hit Rate by Pitch Speed (Including Regression)
    # Binning velocity into 2-mph intervals as described in the report
    df['speed_bin'] = pd.cut(df['release_speed'], bins=range(70, 110, 2))
    hit_rate = df.groupby('speed_bin', observed=True)['hit_label'].mean().reset_index()
    hit_rate['speed_mid'] = hit_rate['speed_bin'].apply(lambda x: x.mid)

    plt.figure(figsize=(10, 6))
    sns.regplot(data=hit_rate, x='speed_mid', y='hit_label', color='red')
    plt.title("Pitch Speed vs Hit Probability (Regression)")
    plt.xlabel("Pitch Speed (mph)")
    plt.ylabel("Hit Probability")
    plt.savefig('regression_hit_analysis.png')
    print("✅ 2. Regression analysis plot saved")

    # Strike Zone Risk Density Analysis (KDE)
    hits_only = df[df['hit_label'] == 1]
    g = sns.jointplot(data=hits_only, x='plate_x', y='plate_z', kind="kde", fill=True, cmap='Reds')
    
    # Adding strike zone boundaries for reference
    g.ax_joint.axvline(x=-0.85, color='black', linestyle='--')
    g.ax_joint.axvline(x=0.85, color='black', linestyle='--')
    g.ax_joint.axhline(y=1.5, color='black', linestyle='--')
    g.ax_joint.axhline(y=3.5, color='black', linestyle='--')
    
    plt.suptitle("Spatial Risk Density: Hit Concentration", y=1.02)
    plt.savefig('hit_density_jointplot.png')
    print("✅ 3. Density analysis plot saved")

except Exception as e:
    print(f"❌ Error occurred: {e}")