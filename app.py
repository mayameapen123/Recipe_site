import requests
import pandas as pd 


def get_recipe(x, y):
  
  url = 'https://api.spoonacular.com/recipes/findByIngredients?ingredients='+ x +',+' + y + '&apiKey=f0196254955f48f9bd00523af82fa456'
  r = requests.get(url)
  recipe_dict = r.json()

  names = []
  images = []

  for recipe in recipe_dict:
    name = recipe['title']
    image = recipe['image']

    names.append(name)
    images.append(image)

  recipe_df = pd.DataFrame({'names': names, 'image': images})
  return recipe_df

#df =  get_recipe()


### Build the app here
from flask import Flask, render_template, redirect, request 
app = Flask(__name__)
@app.route('/', methods = ["POST","GET"])
def home():
  if request.method == "POST":
        name = request.form.get('fname')
        name2 = request.form.get('sname')
        df = get_recipe(name, name2)
        #return redirect("http://127.0.0.1:5000/recipes", code=302)
        #return render_template('submitted.html', name=name)
        return render_template('recipes.html', data = df)
        
  return render_template('home.html')



@app.route('/recipes' ,methods = ["POST","GET"])
def recipe():
  return render_template('recipes.html', data = df)


if __name__ == '__main__':
    app.run(debug = True)

