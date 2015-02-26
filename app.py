from google.appengine.ext.webapp import template
import webapp2
import os


class Landing(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'templates/landing.html')
    self.response.out.write(template.render(path, template_values))


class Playground(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'templates/playground.html')
    self.response.out.write(template.render(path, template_values))


class Contact(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'templates/contact.html')
    self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([
  ('/playground/?', Playground),
  ('/contact/?', Contact),
  ('/.*', Landing)
], debug=True)