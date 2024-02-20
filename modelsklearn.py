import argparse
import os
import numpy as np
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import joblib
import mlflow
import mlflow.sklearn

def main():
    parser = argparse.ArgumentParser('--kernel', type=str, default='linear', help='kernel type to be used in the algorithm')
    parser.add_argument()

    mlflow.start_run()
    mlflow.sklearn.autolog()

    args = parser.parse_args

