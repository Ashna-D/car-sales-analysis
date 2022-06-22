#!/usr/bin/env python
# coding: utf-8

# ### Actions:

# #### 1. Calculate revenue 
# #### 2. Calculate corporate  tax 
# #### 3. Price of refuelling
# #### 4. Calculate cost of repainting

# In[1]:


import pandas as pd
car_list= pd.read_csv(r'C:\Users\Ashna\Downloads\archive\Car_sales.csv')
car_list


# In[2]:


#GET UNIQUE VALUES OF A COLUMN 
#GET DATA TYPE

car_list['Vehicle_type'].eq('Passenger').sum()
car_list.Vehicle_type.unique() 


# In[3]:


#Group cars by manufacturer

df=car_list.groupby('Manufacturer').sum()
df


# In[4]:


#sort values in ascending or descending order 
df=df.sort_values(['Sales_in_thousands', '__year_resale_value'], axis=0, ascending=True) #axis=0 is row wise sorting
df1


# #### 1. Revenue of each manufacturer

# In[5]:


import numpy as np
df['Revenue']= df['Sales_in_thousands']*df['Price_in_thousands']
df


# #### 2. Corporate taxes and Profits 

# In[11]:


corp_taxrate= 0.2
df['Corp_tax']= df['Revenue']*corp_taxrate

df['Profit']=df['Revenue']-df['Corp_tax']
df



# #### 3. Plot revenue

# In[ ]:


import matplotlib.pyplot as plt

cars=[car for car, df in car_list.groupby('Manufacturer')]

plt.bar(cars, df['Revenue'], color='orange')

plt.xticks(cars, rotation=90, size=9, color='purple') 


plt.ylabel('Revenue')
plt.xlabel('Manufacturers')
plt.show()


# #### 4. Plot sales

# In[7]:


cars=[car for car, df in car_list.groupby('Manufacturer')]
plt.bar(cars, df['Sales_in_thousands'], color='orange')

plt.xticks(cars, rotation=90, size=9, color='purple') 


plt.ylabel('Sales')
plt.xlabel('Manufacturers')
plt.show()


# #### 5. Refuelling price

# In[8]:


ppl_oil=30
car_list['refuelling_price']=ppl_oil*car_list['Fuel_capacity']
car_list


# In[9]:


car_list.describe()


# #### 6. Cost of repainting 
# 

# In[10]:


length= float(input('length:'))
width= float(input('width:'))
cost=float(input('costs:'))
def repainting_cost(length, width, cost):
    area=length*width
    price=area*cost
    
    return price
print(repainting_cost(length, width, cost))


# In[ ]:





# In[ ]:




