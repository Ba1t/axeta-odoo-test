# -*- coding: utf-8 -*-
from openerp import http

# class Simpletask(http.Controller):
#     @http.route('/simpletask/simpletask/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/simpletask/simpletask/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('simpletask.listing', {
#             'root': '/simpletask/simpletask',
#             'objects': http.request.env['simpletask.simpletask'].search([]),
#         })

#     @http.route('/simpletask/simpletask/objects/<model("simpletask.simpletask"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('simpletask.object', {
#             'object': obj
#         })