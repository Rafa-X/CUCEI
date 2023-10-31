#Generates random data to the project using the library "Faker"
#Faker Documentation: https://faker.readthedocs.io/en/master/

#---Virtual environment (venv) creation and modules installation - This for testing and modification
# cd "myprojectroute"
# python -m venv .venv
# .venv\Scripts\activate
# pip install "module_name"

from flask import Flask, jsonify
from faker import Faker
import itertools

app = Flask(__name__) #name of the application
faker = Faker() #instance to create tha random data

def random_data():
    #itertools.islice() - receive an iterable
    #faker.profile().items(), "X" - gather "X" random characteristics of a person profile
    profiles = [dict(itertools.islice(faker.profile().items(), 6))  for data in range(5)]  #create 5 registers 
                    
    return profiles

@app.route('/create_registers')  #endpoint
def create_profiles():    
    try:
        data_profiles = random_data()  #create the random data
        return jsonify(data_profiles)
    except Exception:
        return {"message":"error in data creation process in faker-service"}
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)