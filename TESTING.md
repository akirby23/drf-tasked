# DRF Tasked API | Testing

[Return to README.md](README.md)

## Table of Contents

- [Automated Testing](#automated-testing)
- [Manual Testing](#manual-testing)
    - [User Stories](#user-stories)
    - [Validator Testing](#validator-testing)
- [Bugs](#bugs)

## Automated Testing

Automated tests were written to test the API's endpoints using Django Rest Framework's APITestCase. 

All tests that have been written have passed.

| App | Screenshot | Test Cases |
|---|---|---|
|  categories | ![Categories Tests](documentation/testing/automated-testing/categories-tests.PNG)  | - Superuser can create a category <br> - Non superuser cannot create a category <br> - Can retrieve category list <br> - Can retrieve category with valid ID <br> - Cannot retrieve category with invalid ID <br> - Superuser can update category <br> - Non superuser cannot update category  |
| comments | ![Comments Tests](documentation/testing/automated-testing/comments-tests.PNG)  | - Logged in user can create a comment <br> - Can retrieve comment list <br> - Can retrieve comment with valid ID <br> - Cannot retrieve comment with invalid ID <br> - Can update own comment while logged in <br> - Cannot update other user's comment while logged in <br> - Logged out user cannot update own comment|
| prioritylevels | ![Priority Levels Tests](documentation/testing/automated-testing/prioritylevels-tests.PNG)   | - Superuser can create priority level <br> - Non superuser cannot create priority level <br> - Can retrieve priority level list <br> - Can retrieve priority level with valid ID <br> - Cannot retrieve priority level with invalid ID <br> - Superuser can update priority level <br> - Non superuser cannot update priority level |
| profiles | ![Profiles Tests](documentation/testing/automated-testing/profiles-tests.PNG)  | - Profile created upon signup <br> - Can retrieve profile list <br> - Can retrieve profile with valid ID <br> - Cannot retrieve profile with invalid ID <br> - Can update own profile while logged in <br> - Can cannot update other user's profile while logged in <br> - Logged out user cannot update  profile |
| tasks | ![Tasks Tests](documentation/testing/automated-testing/tasks-tests.PNG)  | - Logged in user can create a task <br> - Can retrieve task list <br> - Can retrieve task with valid ID <br> - Cannot retrieve task with invalid ID <br> - Can update own task while logged in <br> - Assignee can update task <br> - Non assignee/non owner cannot update task <br> - Cannot update other user's task while logged in <br> - Logged out user cannot update task |
| all apps | ![All automated test](documentation/testing/automated-testing/all-automated-tests.PNG)  | All of the test cases above |

## Manual Testing

### User Stories

| User Story  |  Status |
|---|---|
| **Task Endpoints** <br> As a site owner/developer, I can access task endpoints so that I can create, read, update & delete tasks. | Pass  |
| **Comment Endpoints** <br> As a site owner/developer, I can access comment endpoints so that I can create, read, update & delete comments. | Pass  |
| **Categorisation Endpoints** <br> As a site owner/developer, I can access categorisation endpoints so that tasks can be categorised by their types. | Pass |
| **Prioritisation Endpoints** <br> As a site owner/developer, I can access prioritisation endpoints so that tasks can be prioritised depending on their importance/urgency. | Pass  |
| **Account Registration Endpoint** <br> As a site owner/developer, I can access an account registration endpoint that allows users to create an account to access the app's features. | Pass |
| **Account Sign In Endpoint** <br> As a site owner/developer, I can access an account sign in endpoint that allows users to sign in to access the app's features. | Pass  |
| **Profile Endpoints** <br> As a site owner/developer, I can access profile endpoints so that I can create, read, update & delete profiles. | Pass  |
| **Search for API Data** <br> As a site owner/developer, I can search for specific data within the API so that I can easily find the results that I need. | Pass |
| **Filter API Data** <br> As a site owner/developer, I can filter the API's data so that I can retrieve the specific data that I need. | Pass  |

### API Features

| Feature | Expected Behaviour | Status |
|---|---|---|
| Task Search | Users can search for tasks by title or by category | Pass  |
| Task Filter  | Tasks can be filtered by owner, category, priority level, assignee & status  | Pass  |
| Profile Filter  | Profiles can be filtered by profile owner | Pass  |
| Comments Filter  | Comments can be filtered by their associated tasks  | Pass |
| Admin Panel  | Superusers can access the admin panel to perform CRUD actions on tasks, categories, priority levels, comments, profiles & users  | Pass  |

### Validator Testing

All Python files have been validated via the [CI PEP8 Python Linter](https://pep8ci.herokuapp.com/).

<details>
<summary>categories</summary>

| File | Screenshot | Status |
|---|---|---|
| categories admin.py  | ![PEP8 categories admin.py file validated](documentation/testing/manual-testing/pep8-categories-admin.PNG)  | Passed with no errors  |
| categories apps.py  |  ![PEP8 categories apps.py file validated](documentation/testing/manual-testing/pep8-categories-app.PNG) |  Passed with no errors  |
| categories models.py | ![PEP8 categories models.py file validated](documentation/testing/manual-testing/pep8-categories-models.PNG)  | Passed with no errors   |
| categories serializers.py | ![PEP8 categories serializers.py file validated](documentation/testing/manual-testing/pep8-categories-serializers.PNG)  | Passed with no errors   |
| categories tests.py | ![PEP8 categories tests.py file validated](documentation/testing/manual-testing/pep8-categories-tests.PNG)  | Passed with no errors   |
| categories urls.py | ![PEP8 categories urls.py file validated](documentation/testing/manual-testing/pep8-categories-urls.PNG) | Passed with no errors   |
| categories views.py | ![PEP8 categories views.py file validated](documentation/testing/manual-testing/pep8-categories-views.PNG)  | Passed with no errors  |
</details>

<details>
<summary>comments</summary>

| File | Screenshot | Status |
|---|---|---|
| comments apps.py  |  ![PEP8 comments app.py file validated](documentation/testing/manual-testing/pep8-comments-app.PNG) |  Passed with no errors  |
| comments models.py | ![PEP8 comments models.py file validated](documentation/testing/manual-testing/pep8-comments-models.PNG)  | Passed with no errors   |
| comments serializers.py  | ![PEP8 comments serializers.py file validated](documentation/testing/manual-testing/pep8-comments-serializers.PNG)  | Passed with no errors   |
| comments tests.py | ![PEP8 comments tests.py file validated](documentation/testing/manual-testing/pep8-comments-tests.PNG)  | Passed with no errors   |
| comments urls.py | ![PEP8 comments urls.py file validated](documentation/testing/manual-testing/pep8-comments-urls.PNG) | Passed with no errors   |
| comments views.py | ![PEP8 comments views.py file validated](documentation/testing/manual-testing/pep8-comments-views.PNG)  | Passed with no errors  |
</details>

<details>
<summary>drf_tasked</summary>

| File | Screenshot | Status |
|---|---|---|
| drf_tasked permissions.py  | ![PEP8 drf_tasked permissions.py file validated](documentation/testing/manual-testing/pep8-drf_tasked-permissions.PNG)  | Passed with no errors  |
| drf_tasked serializers.py  | ![PEP8 drf_tasked serializers.py file validated](documentation/testing/manual-testing/pep8-drf_tasked-serializers.PNG)  | Passed with no errors   |
| drf_tasked settings.py | ![PEP8 drf_tasked settings.py file validated](documentation/testing/manual-testing/pep8-drf_tasked-settings.PNG)  | AUTH_PASSWORD_VALIDATORS have produced a 'Line too long' error, which has been left as is. Otherwise, the code has passed with no errors   |
| drf_tasked urls.py | ![PEP8 drf_tasked urls.py file validated](documentation/testing/manual-testing/pep8-drf_tasked-urls.PNG) | Passed with no errors   |
| drf_tasked views.py | ![PEP8 drf_tasked views.py file validated](documentation/testing/manual-testing/pep8-drf_tasked-views.PNG) | Passed with no errors  |
</details>

<details>
<summary>prioritylevels</summary>

| File | Screenshot | Status |
|---|---|---|
| prioritylevels admin.py  | ![PEP8 prioritylevels admin.py file validated](documentation/testing/manual-testing/pep8-prioritylevels-admin.PNG)  | Passed with no errors  |
| prioritylevels apps.py  |  ![PEP8 prioritylevels apps.py file validated](documentation/testing/manual-testing/pep8-prioritylevels-apps.PNG) |  Passed with no errors  |
| prioritylevels models.py | ![PEP8 prioritylevels models.py file validated](documentation/testing/manual-testing/pep8-prioritylevels-models.PNG)  | Passed with no errors   |
| prioritylevels serializers.py  | ![PEP8 prioritylevels serializers.py.py file validated](documentation/testing/manual-testing/pep8-prioritylevels-serializers.PNG)  | Passed with no errors   |
| prioritylevels tests.py | ![PEP8 prioritylevels tests.py file validated](documentation/testing/manual-testing/pep8-prioritylevels-tests.PNG)  | Passed with no errors   |
| prioritylevels urls.py | ![PEP8 prioritylevels urls.py file validated](documentation/testing/manual-testing/pep8-prioritylevels-urls.PNG) | Passed with no errors   |
| prioritylevels urls.py | ![PEP8 prioritylevels views.py file validated](documentation/testing/manual-testing/pep8-prioritylevels-views.PNG)  | Passed with no errors  |
</details>

<details>
<summary>profiles</summary>

| File | Screenshot | Status |
|---|---|---|
| profiles admin.py  | ![PEP8 profiles admin.py file validated](documentation/testing/manual-testing/pep8-profiles-admin.PNG)  | Passed with no errors  |
| profiles apps.py  |  ![PEP8 profiles apps.py file validated](documentation/testing/manual-testing/pep8-profiles-apps.PNG) |  Passed with no errors  |
| profiles models.py | ![PEP8 profiles models.py file validated](documentation/testing/manual-testing/pep8-profiles-models.PNG)  | Passed with no errors   |
| profiles serializers.py  | ![PEP8 profiles serializers.py file validated](documentation/testing/manual-testing/pep8-profiles-serializers.PNG)  | Passed with no errors  |
| profiles tests.py | ![PEP8 profiles test.py file validated](documentation/testing/manual-testing/pep8-profiles-tests.PNG)  | Passed with no errors   |
| profiles urls.py | ![PEP8 profiles urls.py file validated](documentation/testing/manual-testing/pep8-profiles-urls.PNG) | Passed with no errors   |
| profiles views.py | ![PEP8 profiles views.py file validated](documentation/testing/manual-testing/pep8-profiles-views.PNG)  | Passed with no errors  |
</details>

<details>
<summary>tasks</summary>

| File | Screenshot | Status |
|---|---|---|
| tasks admin.py  | ![PEP8 tasks admin.py file validated](documentation/testing/manual-testing/pep8-tasks-admin.PNG)  | Passed with no errors  |
| tasks apps.py  | ![PEP8 tasks apps.py file validated](documentation/testing/manual-testing/pep8-tasks-apps.PNG) |  Passed with no errors  |
| tasks models.py | ![PEP8 tasks models.py file validated](documentation/testing/manual-testing/pep8-tasks-models.PNG)  | Passed with no errors   |
| tasks serializers.py | ![PEP8 tasks serializers.py file validated](documentation/testing/manual-testing/pep8-tasks-serializers.PNG)  | Passed with no errors   |
| tasks tests.py | ![PEP8 tasks tests.py file validated](documentation/testing/manual-testing/pep8-tasks-tests.PNG)  | Passed with no errors   |
| tasks urls.py | ![PEP8 tasks urls.py file validated](documentation/testing/manual-testing/pep8-tasks-urls.PNG) | Passed with no errors   |
| tasks views.py | ![PEP8 tasks views.py file validated](documentation/testing/manual-testing/pep8-tasks-views.PNG)  | Passed with no errors  |
</details>



## Bugs

| Feature  |  Issue | Status  | Notes  |
|---|---|---|---|
| Image Validation  | Logic has been added to the Profile serializer to throw ValidationErrors if a user attempts to upload a profile picture that is over 2MB in size or over 1080px in height or width. Validation errors are not being thrown  | Unresolved  | This issue has not yet been resolved due to time constraints. User experience is not negatively affected as default profile pictures are set upon profile creation, and this bug does not prevent users from uploading new profile pictures.  |


[Back to the top](#drf-tasked-api--testing)
<br>
[Return to README.md](README.md)

