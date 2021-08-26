# Easy Deploy Machine Learning WEB with Flask
This repo provide machine learning web app with some ready feature using flask and deploy it in [pythonanywhere](https://www.pythonanywhere.com)

## About The Project
This poject is provided by my [Instructur](https://github.com/imamcs19/FGA-Big-Data-Using-Python-Filkom-x-Mipa-UB-2021) with some little edit from me. This project supposed to just provide ready enviromental web development and editted later by programmer, not supposed to be final product.

![feature](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/provide1.jpg)

Feature (by default / before you edit it) :
* Login and Register
* Machine Learning with Linear Regression using SKLearn and PySpark and visualize the result in graph.
* Upload File, Download File, and File Management
* API


## Getting Started
### Prerequisites

What you need to prepare:
* Have verified account at https://www.pythonanywhere.com
* Install Spark (opsional, its required if you use ML that need Spark). You can follow my other repo  [install-pyspark-split1](https://github.com/f3rry12/install-pyspark-split1) (you can install it later after deploy this web project)

### How to Deploy

1. Open [pythonanywhere](https://www.pythonanywhere.com) (make sure to login), go to web section , then click add a new web app
![ss1](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss1.jpg)

Just click next
![ss2](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss2.jpg)

Choose Flask
![ss3](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss3.jpg)

 You can choose whatever version, but I recommend to use 3.7 if you don’t have plan in mind
![ss3k5](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss3_5.jpg)

 Just click Next
![ss4](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss4.jpg)

Now your site server in [pythonanywhere](https://www.pythonanywhere.com) ready.

2. Go to files section, then create new directory called tar
![ss5](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss5.jpg)

3. After you make tar directory, back to main directory then choose mysite directory
   Then delete flask_app.py (we don’t need it because we already have this file ready in this git repository)
![ss6](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss6.jpg)


Special thanks o my Instructur Imam Cholissodin, S.Si., M.Kom.

