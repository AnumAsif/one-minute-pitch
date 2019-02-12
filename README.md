# One Minute  Pitch
#### A web application that allows various users to submit a short pitch. , 01/02/2019.
#### By **ANUM ASIF**
## Description
This application is developed to give user an oppoutunity to practice to say something meaningful if the user was ever given only one minute in life to say something. To se this site effectively user has to register first. If not registered, user can only see the pitches from other users but if registered, user can add a category for the pitch or he can add a pitch in the existing category. User can also like/dislike or comment on the pitches
## Specifications
### Application:
1. display a list of categories
   - INPUT:"Show category button pressed"
   - OUTPUT:"An area displaying all the existing categories" 
2. displays a link to see pitches of a particular category
   - INPUT:"source link clicked"
   - OUTPUT:"A page displaying all the pitches in a category"
3. adds a new pitch
   - INPUT:"Add new pitch button pressed"
   - OUTPUT:"New pitch in a particular category added"
4. registers user to the website
   - INPUT:"A form containing required info of user is submitted"
   - OUTPUT:"User is registered with a specific email and password"
5. login user to the website
   - INPUT:"User enter password and email address"
   - OUTPUT:"User loggedin to the system" 
## Setup/Installation Requirements
- Python 3.6
- Flask Framework
- HTML, CSS, JavaScript and Bootstrap
- PostgreSQL
## Running the Application
   * To run the application, in your terminal:

    1. Clone or download the Repository
    2. Create a virtual environment
    3. Read the requirements file and Install all the requirements. Or run pip3 install -r requirements.txt to automatically install all the requirements
    4. Prepare environment variables
    -export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitchit'
    -export SECRET_KEY='Your secret key'
    4. Run chmod a+x start.sh
    5. Run ./start.sh
    6. Access the application through `localhost:5000`
	
### Development
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 
## Known Bugs
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/AnumAsif/one-minute-pitch/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/AnumAsif/one-minute-pitch/issues/new). Please include sample queries and their corresponding results.
## Technologies Used
- This project was generated with [Python3.6](https://devdocs.io/python~3.6/) and using [Flask](http://flask.pocoo.org/) framework
## Support and contact details
Please feel free to contact me if you have any suggestion for me to improve this website.
- Email: anum@cockar.com
## Link to live website
- [One Minute Pitch](https://pitch-one-minute.herokuapp.com/)
### License
*MIT*
Copyright (c) 2018 **ANUM ASIF**

