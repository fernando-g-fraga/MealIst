<h1 align="Center"> Meal-ist </h1>
<h3 align="Center"> Prep smart, eat well.</h3>


<p align="center">
<img width=400px height=400px src="https://github.com/fernando-g-fraga/MealIst/blob/main/Design%201.png">
</p>


# Meal Planning CLI Application

This project integrates Google Gemini with a ToDoist account to help users plan their meals for the week. The application allows users to input the recipes they want to eat during the week and generates a meal prep plan, including directions and ingredients, as well as a grocery shopping list.

## Features

- **Recipe Collection**: Users can input up to 3 recipes they want to schedule for the week.
- **Meal Plan Creation**: The app uses Google Gemini to create a meal plan with instructions and a grocery list based on the provided recipes.
- **Response Parsing**: The response from Google Gemini is parsed into a class called `Response_Recipe`, which separates the grocery list and recipe instructions.
- **ToDoist Integration**: 
  - **Weekly Meal Tasks**: The app creates a to-do list for the week with ingredients and directions for the provided recipes.
  - **Grocery List Task**: The app creates a grocery list task in ToDoist.

## Usage

1. **Collect Recipes**:
    - The user is prompted to input the names of up to 3 recipes.
    - The user can exit early by entering "0".

2. **Create Meal Plan**:
    - The app calls `CreateRecipe` with the list of recipes to generate a meal plan.

3. **Parse Response**:
    - The response from Google Gemini is parsed using `splitResponse` to separate the recipes and grocery list.

4. **Post to ToDoist**:
    - The app posts the weekly meal tasks and grocery list to ToDoist using `postWeeklyMealTasks` and `postGroceryListTask`.

**Requirements**
- Python 3.x
- google Gemini API access
- ToDoist API access
###  Installation
1. Clone the repository:

``` git clone https://github.com/yourusername/mealplanningCLI.git```
``` cd mealplanningCLI```

2. Install the required dependencies:
```pip install -r requirements.txt```

3. Set up your API keys for Google Gemini and ToDoist.

## Running the App
Run the application using the following command:

```python app.py```
