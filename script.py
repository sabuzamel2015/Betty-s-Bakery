import numpy as np

#Created an array
cupcakes = np.array([2, 0.75, 2, 1, 0.5])

#Generated the CSV file
recipes = np.genfromtxt('recipes.csv', delimiter = ',')

#This is used to find the number of eggs used in each recipe
eggs = recipes[:,2]

#Logical statement used to find all recipes that require one egg 
eggs ==1

#This is used to find the recipes to bake the cookies. Yum!
cookies = recipes[2,:]

#Number of each recipe needed in order to make 2 batches of cupcakes
double_batch = cupcakes*2

#Adding the cookies and double batch of cupcakes in order to create a grocery_list 
grocery_list = cookies + double_batch

print(grocery_list)   
   
