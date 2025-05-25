# Soil Classification

Two approaches for soil analysis via deep learning:

1. **EfficientNet-B1** → Multi-class classification (soil types)  
2. **ResNet-18 + SVM** → Anomaly detection

---

## Quick Start

### Requirements
- Python 3.8+, CUDA GPU
pip install torch torchvision scikit-learn pandas tqdm``

Data Setup
1. Download datasets:

Multi-class: kaggle competitions download -c soil-classification-2025

Anomaly: kaggle datasets download -d soil-classification-part-2

Run Models
1. EfficientNet Training
   python efficientnet_train.py --input_dir ./data --batch_size 64
   Predictions: submissions/phase2_best.csv
2.Anomaly Detection
python resnet_svm.py --train_dir ./data/train --test_dir ./data/test
Predictions: submissions/svm_predictions.csv

Results
Model	Accuracy	Speed (ms/img)
EfficientNet-B1	89% F1	12
ResNet+SVM	93% AUC	8
