# Copyright 2019 Thore Baden
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class Project(models.Model):
    _inherit = 'project.project'

    is_template = fields.Boolean(string='save as template')
    template_id = fields.Many2one(
        comodel_name='project.project',
        string='Template'
    )

    @api.model
    def create(self, vals):
        if 'template_id' in vals and vals['template_id']:
            # load the template
            template = self.env['project.project'].browse(vals['template_id'])
            new_template = template.copy()
            # set correct name after copy action
            new_template.name = vals['name']
            return new_template
        return super(Project, self).create(vals)

    @api.multi
    def copy(self):
        # unset template state after copy action
        new_project = super(Project, self).copy()
        new_project.is_template = False
        return new_project
