def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        return price - discount
    return price

def main():
    try:
        original_price = float(input("Enter the original price: $"))
        discount = float(input("Enter the discount percentage: "))
        
        final_price = calculate_discount(original_price, discount)
        
        if final_price != original_price:
            print(f"Final price after {discount}% discount: ${final_price:.2f}")
        else:
            print(f"No discount applied. Original price: ${original_price:.2f}")
            
    except ValueError:
        print("Please enter valid numbers")

if __name__ == "__main__":
    main()