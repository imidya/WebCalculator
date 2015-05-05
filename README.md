#Simle Web Calculator

It is a simple web caculator for Behavior Driven Development (BDD) example.

The app is written in Python with Flask framework and use Ruby's Cucumber to run the step files.

Feature files are put in the "features" folder and step files are in the "features/step_definitions".

### DEMO
[Live Demo on Heroku](http://webcalculator.herokuapp.com/)

### Screenshot
![Screenshot](https://raw.githubusercontent.com/imidya/WebCalculator/master/static/img/screenshot.png)
### Installation
- You need install Python and Ruby first.
- Change driectory.
```sh
$ cd WebCalculator
```
- Install Python required packages.
```sh
$ pip install -r requirements.txt
```
- Install Cucumber.
```sh
$ gem install cucumber
```
- Install Watir web driver.
```sh
$ gem install watir
```
- Install Rspec.
```sh
$ gem install rspec
```
- Try to run the unit tests. It should all pass.
```sh
$ py.test CalculatorTest.py
```
- Run web app. The app will run on 127.0.0.1:5000
```sh
$ python run.py
```
- Run Cucumber.
```sh
$ cucumber features/calculator.feature
```
- You done!