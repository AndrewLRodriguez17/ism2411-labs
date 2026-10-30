#Exercise 1

def calculate_tax(price, rate):
    return price * rate

#calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $250 at 5%: ${calculate_tax(250, 0.05):.2f}")

#Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85  # 20% discount
    elif tier == "silver":
        return price * 0.9 # 10% discount
    elif tier == "bronze":
        return price * 0.95 # 5% discount
    else:
        return price  # no discount

# Calling the function with different tiers
orignial_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(orignial_price, tier):.2f}")

# Exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# Calling the final_price function
print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4

rate = 0.07
orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price}, Tier: {tier}, Total: ${total:.2f}")

# Exercise 6

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)
