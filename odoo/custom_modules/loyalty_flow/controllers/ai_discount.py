from sklearn.linear_model import LinearRegression
import numpy as np

# Training Data
X = np.array([[1], [2], [3], [4], [5]])  # Purchases
y = np.array([5, 10, 15, 20, 25])        # Discount Amounts

model = LinearRegression()
model.fit(X, y)

def predict_discount(purchases):
    return model.predict([[purchases]])[0]
