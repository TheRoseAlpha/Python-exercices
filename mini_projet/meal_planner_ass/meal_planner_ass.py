import random as rd

breakfast_options = ["Oatmeal with fruits", "Scrambled eggs and toast", "Smoothie bowl", "Greek yogurt with granola"]
lunch_options = ["Grilled chicken salad", "Quinoa with roasted veggies", "Spaghetti with tomato sauce", "Sushi rolls"]
dinner_options = ["Baked salmon with rice", "Vegetable stir-fry", "Chickpea curry", "Tacos with beans and avocado"]

# choicerd = rd.choice(breakfast_options)
# print(choicerd)

print("Welcome to the Meal Planner Assistant! ")
print(f"Breakfast: {rd.choice(breakfast_options)} \n"
      f"Lunch: {rd.choice(lunch_options)} \n"
      f"Dinner: {rd.choice(dinner_options)}")
