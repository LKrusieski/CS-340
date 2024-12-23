 
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
