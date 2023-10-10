# Quiz-Point-Ranking-System

A quiz score ranking system which turns a series of quizzes into a competitive championship.

## Description

This program takes in the scores of multiple students from a series of quizzes, finds the ranking, and calculates points for the overall championship.
With every quiz, the program will output all the information below:

#### **Quiz Ranking**
The rankings of all the students in order of their results for an individual quiz.

#### **Points Gained**
Depending on the placement of a student on the ranking, they will receive a certain amount of points.

#### **Championship Standings**
The current overall championship points of the students will be added with the points gained of the quiz. 

## Getting Started

### Dependencies

* Python 3.8 or higher
* Reccommended Python 3.11.6

### Installing

* Download the latest release on the github repository
* Extract the files into a new folder

### Executing program

* How to run the program
* Copy the config_template.json file and name it config.json
* Modify config.json by filling in the necesarry data

Example of a completed config.json file:
```json
{
    "points_distribution": [
        25,
        15,
        10,
        8,
        5
    ],

    "subject_mapping": {
        "bio": "Biology",
        "chem": "Chemistry",
        "phy": "Physics"
    },

    "students": [
        "Devin",
        "Kyle",
        "Therius",
        "Kent",
        "Nicholas"
    ],

    "CMA": 75,
    "quiz_folder": "c:/Users/USER/Documents/School/Science Quiz Scores"
}
```
* Create a new folder with any name anywhere
* Copy the list_quizzes_template and name it list_quizzes in the new folder

Example of a completed list_quizzes file:
```json
[
    "bio_1",
    "phy_1",
    "chem_1",
    "phy_2",
    "bio_2",
    "chem_2"
]
```
* To input the score of a quiz, copy the quiz_data_template.json and paste it into the new folder
* Name it according to the established naming convention which is "subjectabbr_quiznum", example: "bio_1"

Example of a completed quiz_data file:
```json
{
    "Devin": 95,
    "Therius": 85,
    "Kyle": 75,
    "Nicholas": 65,
    "Raydon": 55
}
```
* Run main.py either by opening it with the Python interpreter or run the command below
```
python3 main.py
```

## Authors

Contributors names and contact info

#### **Devin Lin** (Main Developer)
* Github: [@devinlin89](https://github.com/devinlin89)
* Twitter: [@devinlin89](https://twitter.com/devinlin89)
* Instagram: [@devin.lin89](https://www.instagram.com/devin.lin89/)
* Discord: @devinlin89

#### **Kyle Temaja** (Contributor)

* Github: [KyleTemajaWashere](https://github.com/KyleTemajaWashere)
* Instagram: [yeet_boiz_2019](https://www.instagram.com/yeet_boiz_2019/)
* Discord: @ye12343

#### **Therius Aaron Chen** (Contributor)

#### **Nicholas Richie Widarta** (Contributor)

* Github: [RiverLogic](https://github.com/RiverLogic)
* Instagram : [@nichc_n](https://www.instagram.com/nichc_n)
* Discord : RiverLogic#2547

## Version History

* Alpha Release
  * First release of this repo

## License

This project is licensed under CC-BY-NC-ND-4.0 - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* Formula 1 Points System
