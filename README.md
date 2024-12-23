# Questions:
### *How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?*

Personally I try to focus on maintaining uniform spacing in languages that are not white space dependent, and use seperations between blocks of code to make the code easier to read. I also include comments to ensure the functionality and intent is clearly communicated. In order to have code be adaptable, I make sure that it remains modular via object oriented programming practices. 

### *How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?*

My approach as a computer scientist is to understand the general form of the problem, not just the request as presented. Understanding the basis of the request or the underlying data structure informs my approach. In the case of the Grazioso Salvare needs, creating the CRUD functinality to interact with the database as a middle layer allows for the access to the database to be generalized, so that other use cases could leverage the same AnimalShelter CRUD functionality.

### *What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?*

Computer Scientists have the task of applying knowledge of mathematics and computer systems to develop software and systems to manipulate information into usable data. Systems such as was created here allow for the most precious resource of all, time, to be saved. The opportunity cost of development eliminates the future need of Grazioso Salvare employees to sort through information to find suitable candidates manually.
 
Grazioso Salvare Rescue Candidate Tool
README
Larry E Krusieski
CS-340-12615-M01


Purpose: 
The purpose of the Grazioso Salvare Rescue Candidate Tool (GSRCT) is to identify canines that match candidate profiles for rescue work from the Austin Animal Center’s network of shelters. 
Functionality:
The functionality of the GSRCT is to create a dashboard that allows for interactive data presentation based on the profiles for rescue dog candidates. In service of this there are radio buttons on the dashboard that allow the user to select one of the three profiles: Water Rescue, Mountain Rescue, and Disaster Rescue. There is a fourth radio button labeled Reset which allows the user to return the results to the starting point. The results are initially filtered from the Austin Animal Center’s list to only show dogs.

Additional Functionality
Additional functionality present in the GSRCT is a selectable data table, which will show the selected animal’s geolocation on a map as well as the percentages of each breed type (where applicable) from the active filter’s results. These are shown in the additional images above.

Installation:
The GSRCT can be installed using the following files:
AnimalShelter python (CRUD Module)
ProjectTwoDashboard.ipynb (Client Side)
MongoDB (Server Side)
These files represent a Model-View-Controller design pattern that allows the user to interact with the underlying MongoDB database. 
The AnimalShelter CRUD module represents the controller portion of the design pattern and forms the intermediary between the MongoDB that constitutes the model portion while  the client side Dashboard which represents the view portion of the design pattern.

Authors:
Larry E Krusieski
larry.krusieski@snhu.edu

Acknowledgement:
The author would like to acknowledge the generosity of the Austin Animal Center for providing access to their shelter records to support the work of Grazioso Salvare.
