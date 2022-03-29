from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import numpy as np

class Model:
    def __init__(self, df):
        self.X = df.drop(columns='label')
        self.y = df['label']
    
    def criarModel(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, stratify=self.y, random_state=42)
        clf = RandomForestClassifier(max_depth=2, random_state=0)
        clf.fit(X_train, y_train)
        return clf