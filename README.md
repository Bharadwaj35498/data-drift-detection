# Data Drift Detection (Hyderabad)

This project focuses on detecting **data drift** using simple, reliable statistical methods.
The goal is to understand how data distributions change over time and how those changes can
be identified before they impact machine learning models.

The project is intentionally kept practical and readable, without using heavy frameworks
or automated tools, so that the logic behind drift detection is clearly visible.

---

## Problem Statement

In real-world systems, data rarely stays the same.
Even if a model is trained correctly, changes in incoming data can silently reduce
its performance. This change in data distribution is known as **data drift**.

This project demonstrates:
- How data drift occurs
- How it can be detected statistically
- How drift can be analyzed over time for a single city (Hyderabad)

---

## What This Project Does

- Creates a baseline dataset that represents historical data
- Simulates new incoming data with controlled distribution changes
- Compares baseline and new data using:
  - Visual analysis
  - Statistical tests
- Detects drift across different time windows

The focus is on **understanding**, not automation.

---

## Dataset Description

The data used here is **synthetic**, but designed to resemble real-world sensor or
weather-style data.

**City:** Hyderabad  
**Granularity:** Hourly data  
**Duration:** Multiple months  

Simulated changes include:
- Mean shifts
- Variance changes
- Gradual time-based drift

This setup makes the drift easy to reason about and verify.

---

## Drift Detection Method

### 1. Visual Comparison
- Histogram overlays
- Density-normalized distributions
- Used to build intuition about how data changes

### 2. Statistical Detection
- Kolmogorov–Smirnov (KS) test
- Compares full distributions instead of summary statistics
- Drift is flagged when the p-value falls below a chosen threshold

### 3. Time-Based Drift
- Early data is treated as reference
- Later data is treated as current
- Drift is detected across time windows to observe how it evolves

---

## Project Structure

```text
data-drift-detection/
│
├── notebooks/
│   └── 01_data_drift_baseline.ipynb   # Full analysis and plots
│
├── src/
│   └── drift_utils.py                 # Reusable drift detection logic
│
├── requirements.txt
├── .gitignore
└── README.md
