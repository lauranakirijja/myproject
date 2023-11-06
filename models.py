class Recipe:
    def __init__(self, recipe_name, steps, ingredients):
        self.recipe_name = recipe_name
        self.steps = steps
        self.ingredients = ingredients

    def __str__(self):
        return f"recipe: {self.recipe_name}"
    

class Category:
    def __init__(self, name):
        self.name = name
        self.recipes = []


    def __str__(self):
        recipes_info = "\n".join([f"Recipe: {recipe.recipe_name}\nSteps: {recipe.steps}\nIngredients: {recipe.ingredients}" for recipe in self.recipes])
        return f"Category: {self.name}\n{recipes_info}"
    
    def add_recipe(self, recipe_name, steps, ingredients):
        
        recipe = Recipe(recipe_name, steps, ingredients)
        self.recipes.append(recipe)
        return recipe
    

class User:
    def __init__(self, fullname, username, email, password, confirm_password):
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.categories = []
    
    def __str__(self):
        return f"username: {self.username}"

    def create_category(self, name):
        category = Category(name)
        self.categories.append(category)
        return category
    



