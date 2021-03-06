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
    self.redirect('mailto:admin@larcolabs.com')


class Portfolio(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'templates/portfolio.html')
    self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([
  ('/playground/?', Playground),
  ('/contact/?', Contact),
  ('/portfolio/?', Portfolio),
  ('/.*', Landing)
], debug=True)