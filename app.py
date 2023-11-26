import streamlit as st
import pandas as pd

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
st.title("🥩 Protein Tracker")
st.subheader("Calculate your calories and protein intake from differnt kind of proteins")  

# Create input fields for calories and protein per kg
protein_per_kg = st.number_input("Enter the desired protein intake per kg (g):", step=0.1)
weight_in_kg = st.slider("Enter your weight (in kgs):", step=1, max_value=120)

# Create input fields for weight and protein per kg
tuna_weight = st.number_input("Enter the weight of tuna (g):", step=100)
egg_weight = st.number_input("Enter the weight of eggs (g):", step=100)
steak_weight = st.number_input("Enter the weight of steak (g):", step=100)
chicken_weight = st.number_input("Enter the weight of chicken (g):", step=100)
bresaola_weight = st.number_input("Enter the weight of breasola (g):", step=100)
    
# Calculate the total calories and protein intake
total_calories = tuna_weight * tuna_calories / 100 + egg_weight * egg_calories / 100 + steak_weight * steak_calories / 100 + chicken_weight * chicken_calories / 100 + bresaola_weight * bresaola_calories / 100
total_protein = tuna_weight * tuna_protein / 100 + egg_weight * egg_protein / 100 + steak_weight * steak_protein / 100 + chicken_weight * chicken_protein / 100 + bresaola_weight * bresaola_protein / 100



try:
    protein_percentage = total_protein / (weight_in_kg*protein_per_kg)
except:
    protein_percentage = 0


# Display the percentage of calories from protein
formatted_percentage = '{:.2%}'.format(protein_percentage)
if  protein_percentage <= 0.5:
    st.title(f''':red[You covered {formatted_percentage} of your protein intake and consumed {total_calories}]''')
elif 0.5 <protein_percentage <= 0.7:
    st.title(f''':orange[You covered {formatted_percentage} of your protein intake and consumed {total_calories}]''')
else:
    st.title(f''':green[You covered {formatted_percentage} of your protein intake and consumed {total_calories}]''')


df = pd.DataFrame([protein_percentage])