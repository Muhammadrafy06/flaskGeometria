from flask import Flask,render_template,request
import math
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("tre_1.html")

@app.route('/areaRettangolo2', methods=['POST'])
def scelta_calcolo():
        base = int(request.values.get("base"))
        altezza = int(request.values.get("altezza"))
        option = request.form['name']
        if "diagonale" in option:
            option = math.sqrt((base ** 2) + (altezza ** 2))
            return render_template("tre_2.html", option= option)
            
        else:
            option = base * altezza
            return render_template("tre_2.html", option= option)   
        





  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)