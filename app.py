from flask import Flask,render_template,request
import pymongo
from pymongo import MongoClient
import json
from bson import json_util
app = Flask(__name__)

cluster = MongoClient('mongodb+srv://talha:talha@cluster0.xvmvm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster["FPR"]
cl = db["Job Requirements"]

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/keyword',methods=["GET", "POST"])
def keyword():
    if request.method == "POST":
       keyw = request.form.get("key")
       no = request.form.get("num")
       high=request.form.get("selectedtext")
       n=int(no)
       key=str(high)
       update(n,key)
    return 'success'   

@app.route('/add')
def add():
    addmongo()
    return 'Entries Added'

@app.route('/update?')
def update():
    #update()
    return 'This is the Main Page'

@app.route('/show')
def show():
    show()
    return 'This is the Main Page'        


def addmongo():
    cl.insert_many([
   { "_id":1,"Title": "Junior Data Scientist", "Requirements" : "Python: 1 year (Preferred).Python Flask and Pytorch: 1 year (Preferred).Machine learning: 1 year (Preferred).Image Classification and Object Detection algorithms: 1 year (Preferred).Data Science: 1 year (Preferred)", "keywords":" "},
   { "_id":2,"Title": "Machine Learning Engineer", "Requirements": "2 - 3 years experience with NLP and/or Computer vision.Understanding of data structures, data modelling and software architecture.Deep knowledge of math, probability, statistics and algorithms.Ability to write robust code in Python.Familiarity with machine learning frameworks (like Keras or PyTorch) and libraries (like scikit-learn) and Tensorflow.Proven background in working with CNN / RNN / LTSM networks.Familiar with cloud platforms, Linux, Git.Excellent communication skills.Ability to work in a teamO.utstanding analytical and problem-solving skills.Bachelors in Computer Science, Mathematics or similar field; Master’s degree is a plus", "keywords":" " },
   { "_id":3,"Title": "AI & ML Developer", "Requirements": "Developers needed in India for artificial intelligence and machine learning. Should be fluent in English, productive and skilled in TensorFlow, Keras, SkLearn, CUDA and other relevant technologies and have at least 1 year experience with ML." , "keywords":" "},
   { "_id":4,"Title": "Data Analyst","Requirements":"1. Strong working knowledge on Database 2. Advanced excel for preparing Dashboards 3. Data Warehouse 4. Data Mining and Modelling 5. Data visualization 6. Business Intelligence 7. Experience in any of the business intelligence tools like Tableau, Power BI, Informatica, cognos etc 8. With 5 plus years of experience in Data ware house and Data Analysis", "keywords":" " },
   { "_id":5,"Title":"Data Scientist", "Requirements":"Subject matter expert of Decision Sciences areas like predictive modelling, data mining, deep-dive strategic analysisAnalytics expertise in Python (preferred) or R, feature engineering experience in SQL/Hive/Spark is a mustSound knowledge in traditional statistical techniques like Survival Analysis, Linear/Logistic regression, Segmentation, Multivariate Analysis etc.Expertise in machine learning techniques like Decision trees, Neural Network, Random Forest, SVM, KNN etc. is an added advantage"}
])

def update(n,kw):
    myquery = { "_id": n }
    newvalues = { "$set": { "keywords":str(kw) } }

    cl.update_one(myquery, newvalues)

def show():
    for x in cl.find():
        print(x)    
           


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
