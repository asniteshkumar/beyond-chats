from flask import Flask, render_template_string
import requests

app = Flask(__name__)


url = 'https://devapi.beyondchats.com/api/get_message_with_sources'
response = requests.get(url)

# Empty citations list is created
citations = []

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Convert the response to JSON
    pages = data['data']['links'] # Get all the pages from data
    for link in pages: # Loop over the pages
        if link['url'] != None: # Check whether link is not None
            url = link['url'] # Get the url 
            response = requests.get(url) # Send request to the page
            if response.status_code == 200: 
                data = response.json()  # Convert the response to JSON
                response_source = data['data']['data'] # get data
                for rs in response_source: # Loop over response
                    if rs['response']: # if response
                        source = rs['source'] # Store the source
                        for s in source: # Loop over Source
                            if s['link'] != "": # Check whether Source Link is not empty
                                # Push the object in citations list 
                                citations.append({ 
                                    'id': s['id'],
                                    'link': s['link']
                                })
    # Console Output
    for citation in citations:
        print(citation)
    
else:
    # If response is not present
    print(f"Failed to retrieve data: {response.status_code}")


# Route to display the list
@app.route('/')
def display_list():
    # Render the list using an HTML template
    html = """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>BeyondChats</title>
    </head>
    <body>
        <h1>Citations</h1>
        <ul>
            {% for citation in citations %}
                <li>{{ citation }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """
    return render_template_string(html, citations=citations)

if __name__ == '__main__':
    app.run(debug=True, port=3000)