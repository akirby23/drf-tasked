# DRF Tasked API

## Table of Contents

- [Features](#features)
- [Database Design](#database)
- [Agile Methodology](#agile-methodology)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries & Programs](#frameworks-libraries--programs)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## Features

- User Authentication
- Task Creation
- Task Categorisation
- Task Prioritisation
- Commenting
- Task Assignment
- Timestamps

## Database Design  

## Agile Methodology

## Technologies Used

### Languages

- Python

### Frameworks, Libraries & Programs

- [Django](https://www.djangoproject.com/) to build the API.
- [Django REST Framework](https://www.django-rest-framework.org/) to build the API.
- [Django AllAuth](https://docs.allauth.org/en/latest/) for user authentication.
- [Django-cors-headers](https://pypi.org/project/django-cors-headers/) for handling the server headers required for Cross-Origin Resource Sharing (CORS).
- [Cloudinary](https://console.cloudinary.com/) to host the images.
- [Pillow](https://pypi.org/project/pillow/) for image processing.
- [PostgreSQL](https://www.postgresql.org/) as the object-relational database.
- [Heroku](https://www.heroku.com/) to deploy the API.
- [Git](https://git-scm.com/) for version control.
- [GitHub](https://github.com/) for storing the code in its repository.
- [GitPod](https://gitpod.io/) for writing the code.

## Testing

All testing details are documented within the [TESTING.md](TESTING.md) file.

## Deployment

### Heroku Deployment

This application has been deployed to Heroku using the following steps:

#### Create the app
1. Create a Heroku account on [heroku.com](https://heroku.com/)
2. From the top right hand corner of the dashboard, click "New", then click "Create new app".
3. Give the app a unique name and select the relevant region.
4. Click "Create app".

#### Create the database 

**Placeholder**

#### Cloudinary

This app uses Cloudinary to store images online. 

To obtain your Cloudinary key:

1. Navigate to [cloudinary.com](https://cloudinary.com/) and create an account. 
2. Navigate to the dashboard to obtain your API Environment Variable.
3. When copying the API Environment Variable, be sure to remove the "CLOUDINARY_URL=" from the start of the URL.

#### Set the Config Vars

From the settings tab on the app dashboard, navigate to "Config Vars and click "Reveal Config Vars".

Set them as follows:

| Key | Value | 
| --- | --- |
| CLOUDINARY_URL| Your Cloudinary URL |
| DATABASE_URL| Your own database URL |
| DISABLE_COLLECTSTATIC | 1 (temporary step, to be removed before deployment)
| SECRET_KEY | Your own secret key |


#### Prepare required files
- In your preferred IDE, install the project's requirements by running the following command:
  `pip3 install -r requirements.txt`
- Create a Procfile within the root directory.
- In the procfile, add the following code: web: `gunicorn PROJ_NAME.wsgi`
   - Replace the PROJ_NAME with your own main Django app name.
- Push the changes to GitHub. 


#### Deploy to Heroku

- Navigate to the "Deploy" tab. 
- Link the GitHub repository in the Deployment Method section. 
- Deploy manually or enable automatic deploys if you would prefer. 
- If any errors occur during deployment, the build logs can be used to troubleshoot them.

The app will now be live.

### Local Deployment

- Create an env.py file in the root directory if there isn't one already. 
- Ensure to add the env.py file to your .gitignore file <u>before</u> commiting or pushing to GitHub to prevent credentials from being exposed. 
- Add `import.os` to the top of the env.py file. 
- Add your secret key, Cloudinary URL & database URL in this format: 
<br>
`os.environ.["SECRET_KEY] = "YOUR_SECRET_KEY"`
<br>
`os.environ.["CLOUDINARY_URL"] = "YOUR_URL"`
<br>
`os.environ.["DATABASE_URL] = "YOUR_URL"`
- Add your environment variables to the settings.py file. 

Note: Ensure to set "DEBUG" to "False" in production or during deployment.


#### Forking the repository

1. Navigate to the [drf-tasked GitHub repository](https://github.com/akirby23/drf-tasked).
2. At the top right-hand corner of the page, click on "Fork".
3. Rename or change the description if you wish.
4. Click "Create Fork".
5. A copy of the original repository should now appear on your GitHub account.

#### Cloning the repository

1. Navigate to the [drf-tasked GitHub repository](https://github.com/akirby23/drf-tasked).
2. Navigate to the "<> Code" button and click on it.
3. Choose your preferred cloning option (HTTPS, SSH or GitHub CLI).
4. Open Git Bash or Terminal.
5. Change the current working directory to the location where you want the cloned directory.
6. In your terminal, enter the following command to clone the drf-tasked repository:
     ``git clone https://github.com/akirby23/drf-tasked``
7. Press enter to create a local clone in your preferred IDE.

## Credits 

- [Django](https://docs.djangoproject.com/en/5.0/) & [Django REST Framework](https://www.django-rest-framework.org/) documentation were consulted regularly throughout the development of the API. 
- Credit to [andreagrandi](https://gist.github.com/andreagrandi/14e07afd293fafaea770f69cf66cac14) for the IsAdminOrReadOnly permission class.
- Default profile picture was obtained from [mostkingto on Vecteezy](https://www.vecteezy.com/vector-art/20765399-default-profile-account-unknown-icon-black-silhouette).

[Back to the top](#drf-tasked-api)

