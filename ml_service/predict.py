import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def predict_trend(data):
    df = pd.DataFrame(data)
    X = df[['feature1', 'feature2']]  # Features
    y = df['target']  # Target variable

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    return predictions

# Example usage
if __name__ == "__main__":
    sample_data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [10, 20, 30, 40, 50]
    }
    print(predict_trend(sample_data))
