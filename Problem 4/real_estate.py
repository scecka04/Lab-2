
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    
    price_change = current_price - last_month_price
    est_monthly_mort_payment = current_price * 0.051 / 12

    print(f'This house is ${current_price}. The change is ${price_change} since last month.')
    print(f'The estimated monthly mortgage is ${est_monthly_mort_payment:.2f}.')

    # Your code goes here
if __name__ == "__main__":
    real_estate()