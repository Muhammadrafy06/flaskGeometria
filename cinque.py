from flask import Flask,render_template,request
import math
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("quattro_1.html")

@app.route('/areaRettangolo4', methods=['GET', 'POST'])
def scelta_calcolo():

        return render_template("quattro_2.html", res = res)





        





  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)