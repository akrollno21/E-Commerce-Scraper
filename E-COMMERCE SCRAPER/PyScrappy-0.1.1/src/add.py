
from flask import Flask, request, render_template, jsonify

from scrapper import ECommerceScrapper
import pandas as pd
app = Flask(__name__, static_folder='static')
app = Flask(__name__)

@app.route('/')
def onload_page():
    return render_template('website.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/about')
def aboutus_page():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')
 
@app.route('/price')
def my_form():
    return render_template('price-check.html')
 

@app.route('/price', methods=['POST'])
def my_form_post():
    name = request.form['name']
    ecom = ECommerceScrapper()    
    flipkart_result =ecom.flipkart_scrapper(name,n_pages=1)
    snapdeal_result=ecom.snapdeal_scrapper(name,n_pages=1)
    #print(flipkart_result)
    #print(snapdeal_result)
    print(type(flipkart_result.to_dict()) )
    print(flipkart_result.to_dict() )

    print(type(snapdeal_result.to_dict()) )
    print(snapdeal_result.to_dict() )

    df = pd.DataFrame(flipkart_result.to_dict())
    df1 = pd.DataFrame(snapdeal_result.to_dict())
    # Convert DataFrame to array of objects
    array_of_objects = df.to_records(index=False)
    array_of_objects1 = df1.to_records(index=False)
    
    # Print the array of objects
    print(array_of_objects)
    print(array_of_objects1)
    return render_template('pass.html',n=name,flipkart_result=array_of_objects,snapdeal_result=array_of_objects1)


    
if __name__ == '__main__': 
    app.run(debug=True) 