# 🧠 Crypto Shock Map

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/status-WIP-orange)](#)

> **Clustering financial volatility to visualize how market shocks move between Bitcoin and traditional finance.**

---

## 📌 Overview

This project explores the transmission of market stress across crypto and traditional assets using unsupervised learning techniques. By clustering weekly volatility patterns, we aim to reveal **distinct market regimes**, quantify contagion, and offer a visual map of how shocks propagate in and out of Bitcoin.

---

## 🧪 Methods

- Weekly volatility calculation from daily price data  
- Dimensionality reduction via PCA  
- Clustering with KMeans, DBSCAN, and Hierarchical Clustering  
- Visual analytics of cluster assignments across time and asset types

---

## 📁 Project Structure

```text
crypto-shock-map/
├── data/             # Raw and processed data
│   ├── raw/
│   └── processed/
├── notebooks/        # Jupyter Notebooks
├── src/              # Python scripts and utilities
├── figures/          # Generated plots and visualizations
├── requirements.txt  # Python dependencies
├── README.md
├── .gitignore
└── LICENSE

📜 **License**
Distributed under the MIT License. See LICENSE for more information.

✍️ **Author**
Marco Villagrán – @yourusername