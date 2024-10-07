Monthly Challenges is a Django web application that provides users with different learning challenges for each month. The project demonstrates the use of Django’s URL routing, views, and template inheritance to display dynamic content based on the month selected.

_Features_ 

Dynamic Monthly Content: Each month presents a unique learning challenge, especially focused on Django.
Template Inheritance: Utilizes Django’s template system to extend a base template and override specific content blocks.
URL Parameters: Routes are dynamically handled with URL parameters to fetch the relevant month's challenge.
File Structure
Views: Logic for handling the monthly challenges is written in views.py.
Templates: HTML templates (index.html and month.html) demonstrate how to structure pages using template inheritance.
Routing: The urls.py files handle routing for both the project and the app, ensuring that each month's challenge can be accessed via /challenges/<month>/.
