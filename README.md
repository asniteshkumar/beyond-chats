# BeyondChats - Assignment

API endpoint: https://devapi.beyondchats.com/api/get_message_with_sources

Above is a paginated GET API which returns an array of objects where each object contains a response text and a corresponding array of sources. 
source is a JSON array. Each object of the array consists of an id, context, and an optional link.

Your task is to develop a Python program that does the following :

1. Fetch the data from the pages of the API above.
2. Identify whether the response for each response-sources pair came from any of the sources
3. List down the sources from which the response was formed. Returns an empty array if the response did not come from any source. The shortlisted sources will be called citations
4. Return the citations for all objects coming from the API. 
5. Extra points if you can present your solution through a user-friendly UI.


### Output

![image](https://github.com/asniteshkumar/beyond-chats/assets/69412868/53af1b9d-dead-42c5-9c9d-9a4e4f4b065b)



### Tech Stack

* **Python** ([https://www.python.org/](https://www.python.org/))


### Packages

* **[Flask](https://flask.palletsprojects.com/en/3.0.x/)** (Used to create `Web applications in python`)



## How to Run the Project

### Prerequisites

Before running the project, ensure you have the following installed:
* **Python** ([https://www.python.org/](https://www.python.org/))


### Installation
1. Clone the repository to your local machine using the following command :
	``` bash
	git clone git@github.com:asniteshkumar/beyond-chats.git
	```
	
2. Navigate to the project directory :
	``` bash
	cd beyond-chats
	```
	
3. Install the project dependencies using pip:
	``` bash
	pip install requests, flask
	```
	


### Usage
1. Start the server : 
	``` bash
	python app.py
	```
	
2. Open your web browser and visit [http://127.0.0.1:3000](http://127.0.0.1:3000) to access the web application. 

