from loyalty_flow.models.loyalty_program import LoyaltyProgram

# Test data
test_customers = [
    {"customer_id": 1, "is_new_customer": 1, "total_purchases": 100},  # New customer with low purchases
    {"customer_id": 2, "is_new_customer": 0, "total_purchases": 500},  # Recurring customer with high purchases
    {"customer_id": 3, "is_new_customer": 1, "total_purchases": 200},  # New customer with medium purchases
    {"customer_id": 4, "is_new_customer": 0, "total_purchases": 300},  # Recurring customer with medium purchases
]

# Initialize the LoyaltyProgram model
loyalty_program = LoyaltyProgram()

# Test the predict_tokens method
for customer in test_customers:
    predicted_tokens = loyalty_program.predict_tokens(customer)
    print(f"Customer {customer['customer_id']}: Predicted Tokens = {predicted_tokens}")