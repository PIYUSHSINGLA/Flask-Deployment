# Machine Learning Model Deployment using [Flask](https://flask.palletsprojects.com/en/1.1.x/)

### What is Model Deployment?

In a machine learning and deep learning project, we usually start by defining the problem statement followed by data collection and preparation, understanding of the data, and model building, The next important step is making our model available for the end-users. 

Model Deployment is one of the last stages of any machine learning project and can be a little tricky. How do you get your machine learning model to your client/stakeholder? What are the different things you need to take care of when putting your model into production? And how can you even begin to deploy a model?

### What is Flask?

Flask is a web application framework written in Python. It has multiple modules that make it easier for a web developer to write applications without having to worry about the details like protocol management, thread management, etc.

Flask gives is a variety of choices for developing web applications and it gives us the necessary tools and libraries that allow us to build a web application.

``` 
pip install flask 
```

### Which IDE to use?

Different users have different choices when it comes to the type of python IDE they want to use. Some of the popular IDE’s are Spyder, Jupyter Notebook, PyCharm editor or you can just run it on python compiler.

When you want to run line by line and check the output, it’s idle to go with Jupyter notebooks. When you want to run a chunk of code altogether, Spyder is the better choice and if you want your whole project to look organized, has a lot of files and you want to make it look in a structured way, it’s good to go with PyCharm IDE.

### What is [Pickle](https://docs.python.org/3/library/pickle.html)?

Python pickle module is used for serializing and de-serializing a Python object structure. Any object in Python can be pickled so that it can be saved on disk. What pickle does is that it “serializes” the object first before writing it to file. Pickling is a way to convert a python object (list, dict, etc.) into a character stream. The idea is that this character stream contains all the information necessary to reconstruct the object in another python script.

## Setting up a Flask App

The flask code can be explained in three sections:

1. Loading the saved model:

We load the model.pkl file and initialize the flask app.
   
2. Redirecting the API to the home page index.html:

After initializing the app, we have to tell Flask what we want to do when the web page loads. The line @app.route("/", methods = ["GET","POST"]) tells Flask what to do when we load the home page of our website.

We use @app.route(‘/’) to define functions which are used to redirect them into any number of URI with respect to the API. So, when you start the flask server, it redirects to index.html file by default in our case.

3. Redirecting the API to predict the result

'GET' takes the input/arguments from query string in the URL (starting after ?).
'POST' request, it will be reading the input values from request.form.values(). 

Now that we have the input values in the variable, we will convert it into an array and then use the model to predict it.

The {{ prediction_text }} placeholder in the HTML code will be used to hold the results in our index.html file.

4. Starting the flask server

This will call app.run() and run our web page locally, hosted on your computer.

The flask server starts on localhost and default port (5000) making http://127.0.0.1:5000/
Just paste http://127.0.0.1:5000/ (or) http://localhost:5000 on browser and press enter to see the server working.

## Project Structure

The project has four major parts:

1. model.py — This contains code for our Machine Learning model to predict.
2. app.py — This contains Flask APIs that receives details through GUI or API calls, computes the predicted value based on our model and returns it.
3. template — This folder contains the HTML template (index.html) to allow user to enter detail and displays the predicted results.
4. static — This folder contains the css folder with style.css file which has the styling required for out index.html file.
