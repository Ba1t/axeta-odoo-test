# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError, UserError

# class Status(models.Model):
#     _name = 'simpletask.status'
#
#     name = fields.Char('Title', required=True)


STATUSES = ['Open', 'Needs offer', 'Offered', 'Approved', 'In progress',
            'Ready', 'Verified', 'Closed']
STATUSES_SELECT = [(status.lower(), status) for status in STATUSES]


class Task(models.Model):
    _name = 'simpletask.task'

    name = fields.Char('Title', size=64, required=True)
    image = fields.Binary(attachment=True)
    description = fields.Text(required=True)
    finish_date = fields.Date(required=True, default=fields.Date.context_today)
    status = fields.Selection(selection=STATUSES_SELECT, required=True)
    # status_id = fields.Many2one('simpletask.status', ondelete='set null',
    #                             string='Status', required=True)

    @api.one
    @api.constrains('finish_date')
    def _check_finish_date(self):
        if self.finish_date < fields.Date.context_today(self):
            raise ValidationError(
                'Finish date must be greater or equal today')
