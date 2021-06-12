Deployin a flask app on elastic bean stack

(1)Create a virtual environment in local machine and deploy the flask app in it.

(2)Flask app sholuld contain application.py file which calls the flask app

(3)The name of the app is preferably application

(4)Create a folder .ebextensiobns folder.

(5)Create a file named python.config in .ebextensions folder with below code:

option_settings:
  "aws:elasticbeanstalk:container:python":
    WSGIPath: application:application

(6) pip freeze > requirements.txt

(7) Create a zip file with the following files:  
    (a) application.py  
    (b) requirements.txt  
    (c) .ebextensions folder  
    (d) Other related files like static,modules which app requires 
 
 Note:  
 Directly download the zip file and deploy to ebs or download the required files create a zip and deploy to elasticbeanstack  
