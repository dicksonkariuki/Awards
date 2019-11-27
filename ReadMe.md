# Awwwards
This python project is a clone of the 'awwwards' website.


By: Dickson Kariuki

## Description
This web-app allows a user to create a Profile and upload a Project after which other users can vote after visting the projects site.

## Setup/Installation Requirements
### Cloning the repository
1. Open the terminal and enter:'git clone https://github.com/dicksonkariuki/Awards.git'
### Installation requirements
1. Open the cloned project folder on your IDE.
2. Install the latest version of pip using :curl https://bootstrap.pypa.io/get-pip.py | python
3. Activate the virtual environment using :source virtual/bin/activate
4. Check the requirements file and install all the dependencies.
5. Create a database and run migrations.
### Running the application
1. Run the command 'python3.6 manage.py runserver' to start the application

### Known Bugs
* The user has to click the submit button and go to view site to see the uploaded project.
* The project submit button dissaranges when a user has a long name.
### Behaviour Driven Development
1. The application displays the names of all projects and their photos.
2. Upon clicking an individual project link the user is redirected to the site page to vote.

| Behavior      | Input         | Output|
| ------------- |:-------------:| -----:|
| Create user profile    | user inputs a name and profile photo | User profile image and name displayed at the right-top of navbar |
| User can upload a project     | Title,landingpageimage,description,link,technologies,categories,and color   |   User's project on the homepage |
|Allows a user to view uploaded projects |Page onload  |     |
|  Allows a user to vote on other user's projects           |Numerical scores based on design,usability,creativity,and content               | A numerical score indicating a user's average in each area    |

### Technologies Used
* Python was used as the backend languange.
* Django framework for application administration
* Bootstrap for styling.
* Html to diaplay webpages
* Django-countries library to display countries list on the admin side.
### Support and contact details
* You can contact me via email at :dicksonkariuki4@gmail.com


### License
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
