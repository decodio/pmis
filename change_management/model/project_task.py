# -*- coding: utf-8 -*-
# Copyright (C) 2015 Matmoz d.o.o. (<http://www.matmoz.si>).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class ProjectTask (models.Model):
    _name = 'project.task'
    _inherit = 'project.task'

    change_id = fields.Many2one(
        'change.management.change', 'Action on Change', readonly=True,
        help="Task is an action on a change identified by this label."
    )


class ProjectProject (models.Model):
    _name = 'project.project'
    _inherit = 'project.project'

    change_ids = fields.One2many(
        'change.management.change',
        'project_id',
        'Project changes'
    )
