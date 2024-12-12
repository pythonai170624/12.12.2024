import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display

# 4
# Create three Pandas DataFrames, each representing the car inventory of
# three different dealerships (A, B, C). Each dealership should have at least five
# different car models on hand, along with the corresponding amount in stock.
# For example - Dealership A → Has 5 units of Ford Mustang GT in-stock
# 2. Write a Python function that gets a list of cars to buy and for each car check
# where the available dealerships that are selling this car and have it in stock.
# Your function should return for each car a list of the available dealerships and
# decrease the amount in stock for the relevant dealerships.

# * In case there are more than 1 available dealership that sell the requested
# car decrease the stock amount for only one of the available dealerships

dealership_a = pd.DataFrame({
    'Car Model': ['Ford Mustang GT', 'Chevrolet Camaro', 'Dodge Charger', 
                  'Tesla Model S', 'BMW M3'],
    'Stock': [5, 3, 2, 4, 1]
})

# Dealership B inventory
dealership_b = pd.DataFrame({
    'Car Model': ['Ford Mustang GT', 'Chevrolet Corvette', 'Dodge Charger', 
                  'Tesla Model 3', 'Audi R8'],
    'Stock': [2, 1, 3, 5, 2]
})

# Dealership C inventory
dealership_c = pd.DataFrame({
    'Car Model': ['Chevrolet Camaro', 'Chevrolet Corvette', 'Dodge Challenger', 
                  'Tesla Model X', 'BMW M3'],
    'Stock': [4, 2, 1, 3, 2]
})

dealerships = [dealership_a, dealership_b, dealership_c]

def buy_car(cars_list):
    result = dict()
    for car in cars_list:
        # exist in all of the dealerships
        # stock > 0
        # add to dict the results
        if car in dealership_a['Car Model'].values:
            print(car, 'exist in deal a')

car = 'Tesla Model S2'
result = buy_car(['BMW M3', 'Tesla Model X', 'Honda Civic'])
b = car in dealership_a['Car Model'].values
dealership_a #['Tesla Model S']
# any(dealership_a['Car Model'] == car)
# any(dealership_a['Car Model'].isin([car]))
