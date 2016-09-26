# Waves Website 2016

[![codecov](https://codecov.io/gh/SebastinSanty/WavesWebsite2016/branch/master/graph/badge.svg)](https://codecov.io/gh/SebastinSanty/WavesWebsite2016)![travis](https://travis-ci.org/OSDLabs/WavesWebsite2016.svg?branch=master)

##About
The official repository of the site of Waves, the annual cultural fest of BITS Pilani, Goa. 
Made using Django Framework of Python for server side. 
Includes Django REST Framework to output JSON.

##Link
Hosted live on [bits-waves.org](http://bits-waves.org). The changes will be pushed thrice a week (or as and when necessary).

## Contribution

### Installation

If you are new to github, follow [git-task](https://github.com/OSDLabs/git-task) repository for basic knowledge on how to contribute.

* Make a fork of this repository on your account.

* Assuming you have python 3.4 already installed, go to the desired folder on your machine and follow these commands to clone the repository and install dependencies in a virtual environment:

```
$ virtualenv waves
$ source bin/activate
$ git clone https://github.com//WavesWebsite2016 src
$ cd src
$ pip install -r requirements.txt
```

* db.sqlite3 is the database for this repository, you can delete that if you want to start with a fresh database and follow: (But not required and can skip this step)

```
$ python manage.py migrate
```

* Create a superuser for admin controls (accessible at localhost:8000/admin)

```
$ python manage.py createsuperuser
```

* Run the server and access at localhost:8000

```
$ python manage.py runserver
```


### Contributing Guidelines

If you have any issues with the code or anything, put in one at the issues section of the repository before giving in a pull request. 

##Authors

* Sebastin Santy
* Chaitanya Mukka
* Rhett D'Souza

##Planned Features

* Full Automation, with registration from gates/portals
* Implementing Webhooks to send JSON over to the Firebase used by MAC as its primary database for Android app
