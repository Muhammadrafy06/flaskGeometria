from flask import Flask,render_template,request
import math
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("quattro_1.html")

@app.route('/areaRettangolo4', methods=['GET', 'POST'])
def scelta_calcolo():
        
        option = request.form.getlist("name")
        if "diagonale" in option and "area" in option:
            base = int(request.values.get("base"))
            altezza = int(request.values.get("altezza"))
            area = base * altezza
            diagonale = math.sqrt((base ** 2) + (altezza ** 2))
            return render_template("quattro_3.html", area = area,diagonale = diagonale) 
        elif "area" in option or "diagonale" in option:
            if "area" in option:
                base = int(request.values.get("base"))
                altezza = int(request.values.get("altezza"))
                res = base * altezza
                return render_template("quattro_2.html", res = res)
            elif "diagonale" in option:
                base = int(request.values.get("base"))
                altezza = int(request.values.get("altezza"))
                res = math.sqrt((base ** 2) + (altezza ** 2))
                return render_template("quattro_2.html", res = res)





        





  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)