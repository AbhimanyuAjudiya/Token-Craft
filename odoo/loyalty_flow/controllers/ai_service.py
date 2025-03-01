from sklearn.linear_model import LinearRegression
import numpy as np
import logging

_logger = logging.getLogger(__name__)

class DiscountAI:
    
    def __init__(self):
        self.model = LinearRegression()
        self.train_model()
    
    def train_model(self):
        try:
            X = np.array([[1], [2], [3], [4], [5]])  # Purchases
            y = np.array([5, 10, 15, 20, 25])        # Discount Amounts
            self.model.fit(X, y)
            _logger.info("AI Model Trained Successfully")
        except Exception as e:
            _logger.error(f"Training Error: {str(e)}")
    
    def predict_discount(self, purchases):
        try:
            prediction = self.model.predict([[purchases]])[0]
            return prediction
        except Exception as e:
            _logger.error(f"Prediction Error: {str(e)}")
            return 0
