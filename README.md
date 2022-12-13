<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name"></a>

<h3 align="center">Axon</h3>

  <p align="center">
    Exercise Programming for Fitness Professionals.
    <br />
    <a href="https://axon-beta.herokuapp.com/"><strong>Live Demo</strong></a>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project
Axon provides fitness professionals a client management system. The platform makes a remote api call to:
<br/>
https://rapidapi.com/justin-WFnsXH_t6/api/exercisedb/
<br/>
populating over 1300 exercises in the select drop-down menu making exercise programming seamless. Workouts are saved in the database records
for proper progressive overload and point of reference.

![image](https://user-images.githubusercontent.com/64617718/199347452-75541261-a5b2-4661-9615-16d10424e2a7.png)
![image](https://user-images.githubusercontent.com/64617718/199348088-8a2fade0-14f4-4370-b8dd-35fd41c85587.png)


### Built With
* <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="html"/>
* <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="css"/>
* <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" alt="javascript"/>
* <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="python"/>
* <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="flask"/>
* <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="postgresql"/>

<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Get a free API Key at [https://rapidapi.com/justin-WFnsXH_t6/api/exercisedb/](https://rapidapi.com/justin-WFnsXH_t6/api/exercisedb/)

2. Clone the repo
   ```sh
   git clone https://github.com/Dnhem/axon-beta.git
   ```


* Create virtual environment
   ```sh
   python3 -m venv venv
   ```
* Enter virtual environment
   ```sh
   source venv/bin/activate
   ```
* Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
* Start the app
   ```sh
   FLASK_ENV=development flask run
   ```

### Test files

* Test app routes
   ```sh
   python -m unittest tests_app.py
   ```
* Test app models
   ```sh
   python -m unittest test_models.py
   ```
   
## Contact

Dana Nhem
<br/>

danadevelops@gmail.com
<br/>

https://www.linkedin.com/in/dana-nhem-developer/
<br/>

Project Link - https://github.com/Dnhem/axon-beta

<p align="right">(<a href="#readme-top">back to top</a>)</p>
