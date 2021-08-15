
# # A very simple Flask Hello World app for you to get started with...

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello from Flask!'


from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
# from flask_ngrok import run_with_ngrok # Alternatif Ngrok => Heroku / PythonAnywhere / https://labs.play-with-docker.com / AWS / GCP / Azure/ eval_js dari Colab (agak terbatas) / etc
import sqlite3

app = Flask(__name__, static_folder='static')
# run_with_ngrok(app)  # Start ngrok when app is run

# app.debug = False
app.secret_key = 'key_big_data_app'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET", "POST"])
def login():
  # conn = connect_db()
  # db = conn.cursor()
  conn = sqlite3.connect('fga_big_data.db')
  db = conn.cursor()
  msg = ""
  if request.method == "POST":
      mail = request.form["mail"]
      passw = request.form["passw"]

      rs = db.execute("SELECT * FROM user WHERE Mail=\'"+ mail +"\'"+" AND Password=\'"+ passw+"\'" + " LIMIT 1")

      conn.commit()

      hasil = []
      for v_login in rs:
         hasil.append(v_login)

      if hasil:
        session['name'] = v_login[3]
        session['name'] = v_login[3]
        return redirect(url_for("bigdataApps"))
        # return redirect('/bigdataApps')
        # return render_template("bigdataApps.html")
      else:
        msg = "Masukkan Username (Email) dan Password dgn Benar!"

  return render_template("login.html", msg = msg)

@app.route("/register", methods=["GET", "POST"])
def register():
  # conn = connect_db()
  # db = conn.cursor()
  conn = sqlite3.connect('fga_big_data.db')
  db = conn.cursor()
  if request.method == "POST":
      mail = request.form['mail']
      uname = request.form['uname']
      passw = request.form['passw']

      cmd = "insert into user(Mail, Password,Name,Level) values('{}','{}','{}','{}')".format(mail,passw,uname,'1')
      conn.execute(cmd)
      conn.commit()

      # conn = db

      return redirect(url_for("login"))
  return render_template("register.html")


@app.route("/contohfp2_nonspark", methods=["GET", "POST"])
def contohfp2_nonspark():
  # Simple Linear Regression / Klasifikasi / Clustering
  # Importing the libraries
  import numpy as np
  # import matplotlib.pyplot as plt
  import pandas as pd

  # Importing the dataset => ganti sesuai dengan case yg anda usulkan
  # a. Min. 30 Data dari case data simulasi dari yg Anda usulkan
  # b. Min. 30 Data dari real case, sesuai dgn yg Anda usulkan dari tugas minggu ke-3 (dari Kaggle/UCI Repository)
  url = "./Salary_Data.csv"
  dataset = pd.read_csv(url)
  X = dataset.iloc[:, :-1].values
  y = dataset.iloc[:, 1].values

  # Splitting the dataset into the Training set and Test set
  # Lib-nya selain sklearn/ Tensorflow/ Keras/ PyTorch/ etc
  from sklearn.model_selection import train_test_split
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

  # Hitung Mape
  # from sklearn.metrics import mean_absolute_percentage_error

  # Feature Scaling
  """from sklearn.preprocessing import StandardScaler
  sc_X = StandardScaler()
  X_train = sc_X.fit_transform(X_train)
  X_test = sc_X.transform(X_test)
  sc_y = StandardScaler()
  y_train = sc_y.fit_transform(y_train)"""

  # Fitting Simple Linear Regression to the Training set
  from sklearn.linear_model import LinearRegression
  regressor = LinearRegression()
  regressor.fit(X_train, y_train)

  # Predicting the Test set results
  y_pred = regressor.predict(X_test)
  y_pred2 = regressor.predict(X_train)

  # Visualising the Training set results
  # plt.scatter(X_train, y_train, color = 'red')
  # plt.plot(X_train, regressor.predict(X_train), color = 'blue')


  # Visualising the Test set results
  # plt.scatter(X_test, y_test, color = 'red')
  # plt.plot(X_train, regressor.predict(X_train), color = 'blue')
  # plt.title('Salary vs Experience (Test set)')
  # plt.xlabel('Years of Experience')
  # plt.ylabel('Salary')
  # plt.show()

  aktual, predict = y_train, y_pred2
  mape = np.sum(np.abs(((aktual - predict)/aktual)*100))/len(predict)

  # return render_template('MybigdataApps.html', y_aktual = list(y_train), y_prediksi = list(y_pred2), mape = mape)
  return render_template('MybigdataAppsNonPySpark.html', y_aktual = list(y_train), y_prediksi = list(y_pred2), mape = mape)

@app.route("/contohfp2_spark", methods=["GET", "POST"])
def contohfp2_spark():
  # MLLIB dari Pyspark Simple Linear Regression /Klasifikasi / Clustering
  # Importing the libraries
  import numpy as np
  import matplotlib.pyplot as plt
  import pandas as pd
  from pyspark import SQLContext, SparkConf, SparkContext
  from pyspark.sql import SparkSession
  sc = SparkContext.getOrCreate()
  if (sc is None):
      sc = SparkContext(master="local[*]", appName="Linear Regression")
  spark = SparkSession(sparkContext=sc)
  # sqlcontext = SQLContext(sc)

  # Importing the dataset => ganti sesuai dengan case yg anda usulkan
  # a. Min. 30 Data dari case data simulasi dari yg Anda usulkan
  # b. Min. 30 Data dari real case, sesuai dgn yg Anda usulkan dari tugas minggu ke-3 (dari Kaggle/UCI Repository)
  url = "./Salary_Data.csv"

  sqlcontext = SQLContext(sc)
  data = sqlcontext.read.csv(url, header = True, inferSchema = True)

  from pyspark.ml.feature import VectorAssembler
  # mendifinisikan Salary sebagai variabel label/predictor
  dataset = data.select(data.YearsExperience, data.Salary.alias('label'))
  # split data menjadi 70% training and 30% testing
  training, test = dataset.randomSplit([0.7, 0.3], seed = 100)
  # mengubah fitur menjadi vektor
  assembler = VectorAssembler().setInputCols(['YearsExperience',]).setOutputCol('features')
  trainingSet = assembler.transform(training)
  # memilih kolom yang akan di vektorisasi
  trainingSet = trainingSet.select("features","label")

  from pyspark.ml.regression import LinearRegression
  # fit data training ke model
  lr = LinearRegression()
  lr_Model = lr.fit(trainingSet)
  # assembler : fitur menjadi vektor
  testSet = assembler.transform(test)
  # memilih kolom fitur dan label
  testSet = testSet.select("features", "label")
  # fit testing data ke model linear regression
  testSet = lr_Model.transform(testSet)
  # testSet.show(truncate=False)

  from pyspark.ml.evaluation import RegressionEvaluator
  evaluator = RegressionEvaluator()
  # print(evaluator.evaluate(testSet, {evaluator.metricName: "r2"}))

  y_pred2 = testSet.select("prediction")
  # y_pred2.show()


  return render_template('MybigdataAppsPySpark.html', y_aktual = y_pred2.rdd.flatMap(lambda x: x).collect(), y_prediksi = y_pred2.rdd.flatMap(lambda x: x).collect(), mape = evaluator.evaluate(testSet, {evaluator.metricName: "r2"}))

@app.route("/bigdataApps", methods=["GET", "POST"])
def bigdataApps():
  if request.method == 'POST':
    import pandas as pd
    import numpy as np

    dataset = request.files['inputDataset']
    # url = "./dataset_dump.csv"

    persentase_data_training = 90
    banyak_fitur = int(request.form['banyakFitur'])
    banyak_hidden_neuron = int(request.form['banyakHiddenNeuron'])
    dataset = pd.read_csv(dataset, delimiter=';', names = ['Tanggal', 'Harga'], usecols=['Harga'])
    # dataset = pd.read_csv(url, delimiter=';', names = ['Tanggal', 'Harga'], usecols=['Harga'])
    # dataset = dataset.fillna(method='ffill')
    minimum = int(dataset.min()-10000)
    maksimum = int(dataset.max()+10000)
    new_banyak_fitur = banyak_fitur + 1
    hasil_fitur = []
    for i in range((len(dataset)-new_banyak_fitur)+1):
      kolom = []
      j = i
      while j < (i+new_banyak_fitur):
        kolom.append(dataset.values[j][0])
        j += 1
      hasil_fitur.append(kolom)
    hasil_fitur = np.array(hasil_fitur)
    data_normalisasi = (hasil_fitur - minimum)/(maksimum - minimum)
    data_training = data_normalisasi[:int(persentase_data_training*len(data_normalisasi)/100)]
    data_testing = data_normalisasi[int(persentase_data_training*len(data_normalisasi)/100):]

    #Training
    bobot = np.random.rand(banyak_hidden_neuron, banyak_fitur)
    bias = np.random.rand(banyak_hidden_neuron)
    h = 1/(1 + np.exp(-(np.dot(data_training[:, :banyak_fitur], np.transpose(bobot)) + bias)))
    h_plus = np.dot(np.linalg.inv(np.dot(np.transpose(h),h)),np.transpose(h))
    output_weight = np.dot(h_plus, data_training[:, banyak_fitur])

    #Testing
    h = 1/(1 + np.exp(-(np.dot(data_testing[:, :banyak_fitur], np.transpose(bobot)) + bias)))
    predict = np.dot(h, output_weight)
    predict = predict * (maksimum - minimum) + minimum

    #MAPE
    aktual = np.array(hasil_fitur[int(persentase_data_training*len(data_normalisasi)/100):, banyak_fitur])
    mape = np.sum(np.abs(((aktual - predict)/aktual)*100))/len(predict)

    print("predict = ", predict)
    print("aktual =", aktual)
    print("mape = ", mape)

    # return render_template('bigdataApps.html', data = {'y_aktual' : list(aktual),'y_prediksi' : list(predict),'mape' : mape})
    return render_template('bigdataApps.html', y_aktual = list(aktual), y_prediksi = list(predict), mape = mape)


    # return "Big Data Apps " + str(persentase_data_training) + " banyak_fitur = " + str(banyak_fitur) + " banyak_hidden_neuron = " + str(banyak_hidden_neuron) + " :D"
  else:
    return render_template('bigdataApps.html')

# def connect_db():
#     return sqlite3.connect('fga_big_data.db')



@app.route('/logout')
def logout():
   # remove the name from the session if it is there
   session.pop('mail', None)
   session.pop('name', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
  # db.create_all()
  app.run()  # If address is in use, may need to terminate other sessions:
             # Runtime > Manage Sessions > Terminate Other Sessions
  # app.run(host='0.0.0.0', port=5004)  # If address is in use, may need to terminate other sessions:
             # Runtime > Manage Sessions > Terminate Other Sessions
