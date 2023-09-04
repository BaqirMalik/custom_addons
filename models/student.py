# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import re
from odoo import models, fields


class StudentModel(models.Model):
    _name = "res.student"
    _inherit = ['mail.thread']

    name = fields.Char("Student Name", tracking=True)
    father_name = fields.Char("Father Name", tracking=True)
    student_class = fields.Char('Class', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other'),
                               ], string='Gender', default='male',
                             track_visibility='always')
    mobile = fields.Integer("Mobile")
