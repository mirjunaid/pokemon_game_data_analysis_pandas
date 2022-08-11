#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


# Read the dataset
data = pd.read_csv('pokemon.csv')
data.head()


# In[ ]:


# Clean the dataset
data.isna()

# Replace the NaN values with nill
data = data.fillna('Single Mode Specie')

data.head()        


# # Let's draw some graphs for this dataset

# In[ ]:


# the graph of the collective features of the species of specific generation 
generation = ['1st Gen specie', '2nd Gen Specie', '3rd Gen Specie', '4th Gen Specei', '5th Gen Specie', '6th Gen Specei']
new_colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red', 'maroon', 'gray', 'silver', 'gold', 'brown']

plt.bar(generation, data.groupby('Generation').sum()['Total'], width=0.5, edgecolor='black', color= new_colors)
plt.xticks(generation, rotation='vertical',size=10)
plt.title('Graph of collective features vs Generation of the specie', color='red', size=20)
plt.ylabel('Sum of collective features', color='red', size=16)
plt.xlabel('Generation', color='red', size=20)
plt.show()


# In[ ]:


# Graph to show how many species were added in each generation
first_gen = 0
sec_gen = 0
third_gen = 0
fourth_gen = 0
fifth_gen = 0
sixth_gen = 0
for index, row in data.iterrows():
    if row['Generation'] == 1:
        first_gen += 1
    elif row['Generation'] == 2:
        sec_gen += 1
    elif row['Generation'] == 3:
        third_gen += 1
    elif row['Generation'] == 4:
        fourth_gen += 1
    elif row['Generation'] == 5:
        fifth_gen += 1
    else:
        sixth_gen += 1
            
number_of_species = np.array([first_gen, sec_gen, third_gen, fourth_gen, fifth_gen, sixth_gen])
number_of_species

plt.bar(generation, number_of_species, color=new_colors, width=0.5, edgecolor='black')
plt.xticks(generation, rotation='vertical', size=10)
plt.title('Graph for number of species introduced in each generation', color='red', size=20)
plt.xlabel('Generation', color='blue', size=20)
plt.ylabel('No. of Species', color='blue', size=20)
plt.show()


# In[ ]:


specie_type = data.groupby('Type 1')
strength_level = specie_type.sum()['Total']
specie_type = [pair for pair, df in specie_type]

plt.bar(specie_type, strength_level, color=new_colors, edgecolor='black')
plt.xticks(specie_type, rotation='vertical', size=10)
plt.title('Graph for the strength of each speciality', color='red', size=20)
plt.xlabel('Speciality', color='blue', size=20)
plt.ylabel('Total strength',color='blue', size=20)
plt.show()


# In[ ]:


specie_type = data.groupby('Type 1')
specie_count = specie_type.count()['Name']
specie_type = [pair for pair, df in specie_type]

plt.bar(specie_type, specie_count, color=new_colors, edgecolor='black')
plt.xticks(specie_type, rotation='vertical', size=10)
plt.title('Graph to show speciality vs number of species having it', color='red', size=20)
plt.xlabel('Speciality', color='blue', size=20)
plt.ylabel('No. of species', color='blue', size=18)
plt.show()


# In[ ]:


speed_per_speciality = data.groupby('Type 1')
speed_value = speed_per_speciality.sum()['Speed']
speed_per_speciality = [pair for pair, df in speed_per_speciality]

plt.bar(speed_per_speciality, speed_value, color=new_colors, edgecolor='black')
plt.xticks(speed_per_speciality, rotation='vertical', size=10)
plt.title('Graph for speed of different different specialities for species', color='red', size=20)
plt.xlabel('Speciality', color='blue', size=20)
plt.ylabel('Speed Values', color='blue', size=20)
plt.show()


# In[ ]:


speed_for_defence_speciality = data.groupby('Type 1')
speed_value_in_defence = speed_for_defence_speciality.sum()['Sp. Def']
speed_for_defence_speciality = [pair for pair, df in speed_for_defence_speciality]

plt.bar(speed_for_defence_speciality, speed_value_in_defence, color=new_colors, edgecolor='black')
plt.xticks(speed_for_defence_speciality, rotation='vertical', size=10)
plt.title('Graph for defence speed of different specialities for species', color='red', size=20)
plt.xlabel('Speciality', color='blue', size=20)
plt.ylabel('Defence speed values', color='blue', size=18)
plt.show()


# In[ ]:


speed_while_attacking = data.groupby('Type 1')
speed_attack_values = speed_while_attacking.sum()['Sp. Atk']
speed_while_attacking = [pair for pair, df in speed_while_attacking]

plt.bar(speed_while_attacking, speed_attack_values, color=new_colors, edgecolor='black')
plt.xticks(speed_while_attacking, rotation='vertical', size=10)
plt.title('Graph for attacking speed of differnet specialities of species', color='red', size=20)
plt.xlabel('Speciality', color='blue', size=20)
plt.ylabel('Attacking speed values', color='blue', size=18)
plt.show()


# In[ ]:


attack_speciality = data.groupby('Type 1')
attack_values = attack_speciality.sum()['Attack']
attack_speciality = [pair for pair, df in attack_speciality]

plt.bar(attack_speciality, attack_values, color=new_colors, edgecolor='black')
plt.xticks(attack_speciality, rotation='vertical', size=10)
plt.title('Graph for the attacking capability of different specialities of species', color='red', size=20)
plt.xlabel('Speciality', color='blue', size=20)
plt.ylabel('Attack level values', color='blue', size=18)
plt.show()


# In[ ]:


defence_speciality = data.groupby('Type 1')
defence_level_values = defence_speciality.sum()['Defense']
defence_speciality = [pair for pair, df in defence_speciality]

plt.bar(defence_speciality, defence_level_values, color=new_colors, edgecolor='black')
plt.xticks(defence_speciality, rotation='vertical', size=10)
plt.title('Graph for the defence level of every speciality of the species', color='red', size=20)
plt.xlabel('Speciality', color='blue', size=20)
plt.ylabel('Defence level values')
plt.show()


# In[ ]:


data.head()


# In[ ]:


health_points = data.groupby('Type 1')
health_points_value = health_points.sum()['HP']
health_points = [pair for pair,df in health_points]

plt.bar(health_points, health_points_value, color = new_colors, edgecolor = 'black')
plt.xticks(health_points, rotation='vertical', size=10)
plt.title('Graph to show how much demage can a specie with a particular speciality withstand', color='red', size=20)
plt.xlabel('Speciality', color='blue', size=20)
plt.ylabel('Sum of health points', color='blue', size=18)
plt.show()


# In[18]:


data.to_csv('Updated pokemon data.csv')


# In[ ]:




