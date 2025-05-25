# Soil Classification with Outlier Detection
A deep learning solution for soil type classification with built-in outlier detection, achieving **good F1-score** on test data.

## 📌 Problem Statement
Classify soil images into four categories (Alluvial, Black, Clay, Red) while identifying out-of-distribution samples. The model handles:
- 4 known soil classes from training data
- Potential unknown soil types in test data

## 🚀 Key Features
- **ResNet50-based classifier** fine-tuned on soil images
- **Confidence thresholding** for outlier detection
- Data augmentation for improved generalization
- Automated preprocessing pipeline
- GPU-accelerated training/inference
