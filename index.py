print('I am Sleepy')
print('Mbappe TO MADRID HERE WE GO')

def grams_to_pounds(grams):
    pounds = grams * 0.00220462
    return pounds

# User input
grams = float(input("Enter the weight in grams: "))
pounds = grams_to_pounds(grams)
print(f"{grams} grams is equal to {pounds:.4f} pounds.")

