import os
import plone.api
from Products.Five.browser import BrowserView
from plone.app.layout.viewlets import common as base


class PagedJS(base.ViewletBase):

    def portal_url(self):
        return plone.api.portal.get().absolute_url()

class PagedJSView(BrowserView):

    def styles(self):
        dirname = os.path.dirname(__file__)
        fn = os.path.join(dirname, 'static', 'styles.css')
        with open(fn, 'rb') as fp:
            css = fp.read()
        self.request.response.setStatus(200)
        self.request.response.setHeader("content-type", "text/css")
        self.request.response.setHeader("content-length", str(len(css)))
        self.request.response.write(css)
