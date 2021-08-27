# Easy Deploy Machine Learning WEB with Flask
This repository provide machine learning web app with some ready feature using flask and deploy it in [pythonanywhere](https://www.pythonanywhere.com)

## About The Project
This project is provided by my [Instructur](https://github.com/imamcs19/FGA-Big-Data-Using-Python-Filkom-x-Mipa-UB-2021) with some little edit from me. This project supposed to just provide ready enviromental web development and editted later by programmer, not supposed to be final product.

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
* Install Spark (opsional, its required if you use ML that need Spark). You can follow my guide in my other repository  [install-pyspark-split1](https://github.com/f3rry12/install-pyspark-split1) (you can install it later after deploy this web project)

### How to Deploy

1. Open [pythonanywhere](https://www.pythonanywhere.com) (make sure to login), go to web section , then click add a new web app
![ss1](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss1.jpg)

  Just click next <br>
![ss2](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss2.jpg)

  Choose Flask <br>
![ss3](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss3.jpg)

  You can choose whatever version, but I recommend to use 3.7 if you don’t have plan in mind
![ss3k5](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss3_5.jpg)

  Just click Next <br>
![ss4](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss4.jpg)

Now your site server in [pythonanywhere](https://www.pythonanywhere.com) ready.

2. Go to Files section, then create new directory called tar
![ss5](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss5.jpg)

3. After you make tar directory, back to main directory then choose mysite directory
   Then delete flask_app.py (we don’t need it because we already have this file ready in this git repository)
![ss6](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss6.jpg)

4. Go to Consoles section, then click Bash
![ss7](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss7.jpg)

Then follow this command to clone this repository
   ```sh
   cd tar
   ```
   ```sh
   git clone https://github.com/f3rry12/EasyDeployFlask.git
   ```
![ss8](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss8.jpg)

Move the project from tar directory to mysite directory
   ```sh
   cd
   mv /home/yourusername/tar/EasyDeployFlask/* /home/yourusername/mysite/
   ```
![ss9](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss9.jpg)


5. Install module flask cors 
   ```sh
   pip3.7 install --user flask_cors
   ```
![ss10](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss10.jpg)

6. Go to Web section, then click reload button
![ss11](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss11.jpg)

You can visit your web to check if it success
![ss12](https://github.com/f3rry12/EasyDeployFlask/blob/main/readMeAsset/ss12.jpg)

7. Last, because free user [pythonanywhere](https://www.pythonanywhere.com) have limited space. Try clear some space by deleting tar directory and read me asset

## Acknowledgements
Special thanks to my Instructur [Imam Cholissodin](https://github.com/imamcs19), S.Si., M.Kom.

