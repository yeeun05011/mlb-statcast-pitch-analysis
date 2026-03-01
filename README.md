## 📌 Project Overview
This project performs an exploratory data analysis (EDA) and statistical modeling on MLB Statcast data to identify key predictive signals in pitch physics. By analyzing the relationship between pitch metrics (speed, spin rate) and hit probability, this research demonstrates a structured approach to Alpha discovery in a high-dimensional dataset.

## 🚀 Key Research Features
Feature Engineering: Derived binary hit_label from raw event data to perform classification-based analysis.

Correlation Analysis: Conducted a multi-variable correlation study using Seaborn heatmaps to identify collinearity between release speed, spin rate, and movement.

Predictive Regression: Modeled the probability of hits relative to pitch velocity using binned regression analysis, highlighting the performance thresholds of professional pitching.

Spatial Risk Density: Implemented Kernel Density Estimation (KDE) to visualize spatial risk within the strike zone, identifying "hot zones" for hit concentration.

## 📊 Technical Highlights
Python Stack: Pandas for data wrangling, NumPy for numerical computing, and Matplotlib/Seaborn for advanced statistical visualization.

Statistical Rigor: Applied descriptive statistics and probability binning to ensure robust insights from the Statcast postseason dataset.

Error Handling: Implemented robust file I/O and exception handling for reliable data processing pipelines.

## 📂 Visualizations
The analysis generates the following automated reports:

correlation_heatmap.png: Inter-variable relationships of pitch physics.

regression_hit_analysis.png: Hit probability trends across velocity bins.

hit_density_jointplot.png: Spatial concentration of hits in the strike zone.
