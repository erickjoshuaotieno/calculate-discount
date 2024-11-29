# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discounted price
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Prompt the user to enter the original price
original_price = float(input("Enter the original price of the item: "))

# Prompt the user to enter the discount percentage
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price using the function
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price != original_price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The price remains: ${original_price:.2f}")
