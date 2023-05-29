import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        # Read the contents of the HTML file
        with open('index.html', 'r') as file:
            html_content = file.read()

        # Set the response content type
        self.response.headers['Content-Type'] = 'text/html'

        # Send the HTML content as the response
        self.response.write(html_content)

app = webapp2.WSGIApplication([('/', MainPage),], debug=True)
