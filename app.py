import streamlit as st
import math 

# Define the nutritional information for each food item
tuna_calories = 142
egg_calories = 78
steak_calories = 208
chicken_calories = 165
bresaola_calories = 150


# Define the nutritional information for each food item
tuna_protein = 25
egg_protein = 13

steak_protein = 21
chicken_protein = 31
bresaola_protein = 35


# Create a title and subtitle for the app
st.title("Calorie and Protein Tracker")
st.subheader("Calculate your calorie and protein intake from tuna, eggs, and steak")

# Create input fields for calories and protein per kg
protein_per_kg = st.number_input("Enter the desired protein intake per kg (in grams):")
weight_in_kg = st.number_input("Enter your weight (in kgs):")

# Create input fields for weight and protein per kg
tuna_weight = st.number_input("Enter the weight of tuna (in grams):")
egg_weight = st.number_input("Enter the weight of eggs (in grams):")
steak_weight = st.number_input("Enter the weight of steak (in grams):")
chicken_weight = st.number_input("Enter the weight of chicken (in grams):")
bresaola_weight = st.number_input("Enter the weight of breasola (in grams):")


# Calculate the total calories and protein intake
total_calories = tuna_weight * tuna_calories / 100 + egg_weight * egg_calories / 100 + steak_weight * steak_calories / 100 + chicken_weight * chicken_calories / 100 + bresaola_weight * bresaola_calories / 100
total_protein = tuna_weight * tuna_protein / 100 + egg_weight * egg_protein / 100 + steak_weight * steak_protein / 100 + chicken_weight * chicken_protein / 100 + bresaola_weight * bresaola_protein / 100

# Display the total calories and protein intake
st.subheader("Total Calories:")
st.write(total_calories)
st.subheader("Total Protein:")
st.write(total_protein)

# Calculate the percentage of calories from protein
try:
    protein_percentage = math.floor(total_protein / (weight_in_kg*protein_per_kg))
except ZeroDivisionError:
    protein_percentage = 0

# Display the percentage of calories from protein
st.subheader("Percentage of Calories from Protein:")
st.write(protein_percentage)
