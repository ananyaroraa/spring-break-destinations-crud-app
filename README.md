# Spring Break Destinations CRUD Application

An application that allows you to view, add, edit, and search through popular spring break destinations. Inspired by U.S. News Travel website. 

The application has the following functionality:

#### 1. Home Page:
Using Bootstrap rows and columns, I created the homepage to display three popular destinations. Instead of showing all the information about the destination, I have shown just enough to entice the user and make them want to find out more about them. The visual design resembles a polaroid picture and are clickable so the user can find out more.
<br>
<br>
<kbd>
<img width="1440" alt="home_page" src="https://user-images.githubusercontent.com/89229370/164251894-4a44c979-9231-4d90-97bb-2c8032ec9366.png">
</kbd>

#### 2. View Data:
Each destination renders a view with details of the destination. Each destination page is dynmaically rendered and not hard-coded.
<br>
<br>
<kbd>
<img width="877" alt="bahamas_page" src="https://user-images.githubusercontent.com/89229370/164257953-6701fa3a-9a3c-4616-b275-c0ca6d61fae6.png">
</kbd>



#### 3. Search Functionality:
There are three fields of data about each destination that can be searched - city, country and type of destination (either beach or mountains). 
<br>
<br>
The user can enter their search query in the navbar and on pressing 'Enter' or clicking the 'Search' button, they will be shown the search results. The results are filtered by the fileds it matched. The searching functionality is not case-sensitive and not exact. Following the design prinicple of feedback, the matched term in each category is highlighted.
<br>
<br>
<kbd>
<img width="905" alt="search_page" src="https://user-images.githubusercontent.com/89229370/164254647-64d2f4f5-82af-494e-84fd-fe750da561bc.png">
</kbd>
<br>
<br>
The mini sidebar on a view page is clickable and leads to a search directly.
<br>
<br>
<img width="277" alt="image" src="https://user-images.githubusercontent.com/89229370/164258388-782cf4e1-6a5c-465d-8d03-6cf9f9336972.png">



#### 3. Add Data Page:
The user can add new destinations they want by clicking the 'Add' button on the navbar and filling a form. Notice how the form has placeholder texts to guide a user and make the application user-friendly. 
<br>
<br>
<kbd>
<img width="1085" alt="image" src="https://user-images.githubusercontent.com/89229370/164258967-d34296c7-2b83-49db-a802-4eb5c935ca0e.png">
</kbd>

#### 4. Edit Data Page:
The user can also edit details of the destination which automatically reflect in the backend. Notice how the existing details of the destination are pre-populated.
<br>
<br>
<kbd>
<img width="1085" alt="image" src="https://user-images.githubusercontent.com/89229370/164259796-96497c0a-fa06-4050-b125-916481357abc.png">
</kbd>

#### 5. Accessibility:
Each media file has an alternate text.

#### 6. Design Principles Followed:
1. Visibility of system status
2. Error Prevention
3. Help users recognize, diagnose, and recover from errors


#### Tech Stack:
Frontend: HTML5, CSS3, JavaScript, JQuery, Bootstrap
<br>
Backend: Python (Flask framework)

#### How to run this application:
1. Clone the repository
2. Using the terminal, get into the specific directory that the repository is stored
3. Run this command to activate the Flask server ``` python3 server.py ```
