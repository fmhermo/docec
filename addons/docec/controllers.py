# -*- coding: utf-8 -*-
from openerp import http

# class Docec(http.Controller):
#     @http.route('/docec/docec/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/docec/docec/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('docec.listing', {
#             'root': '/docec/docec',
#             'objects': http.request.env['docec.docec'].search([]),
#         })

#     @http.route('/docec/docec/objects/<model("docec.docec"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('docec.object', {
#             'object': obj
#         })