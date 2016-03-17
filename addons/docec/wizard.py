# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.osv import osv 

class Asistente(models.TransientModel):
    _name = 'docec.asistente'
    
    def _default_titular(self):
        return self.env['docec.delegado'].browse(self._context.get('active_ids'))

    def _default_organismo(self):
        titular = self.env['docec.delegado'].browse(self._context.get('active_ids'))
        return self.env['docec.organismo'].search([('id','=',titular.id_organismo.id)])
    

    def _get_suplentes_domain(self):
        titular = self.env['docec.delegado'].browse(self._context.get('active_ids'))
        return [('estado','=','S'),('id_organismo','=',titular.id_organismo.id)]

    titular_id = fields.Many2one('docec.delegado', string="Titular", default=_default_titular, readonly=True)
    organismo = fields.Many2one('docec.organismo', string="Organismo", default=_default_organismo, readonly=True)

    suplente_id = fields.Many2one('docec.delegado',
        string="Suplente", domain=_get_suplentes_domain)
    
    @api.multi
    def sustituir(self):
        #suplente = self.env['suplente_id']
        duplicado = self.env['docec.delegado'].search([('dni', '=', self.suplente_id.dni),('estado','=','T')])
        for rec in duplicado:
            print rec.dni
        if duplicado.estado == 'T':
            #raise osv.except_osv(('Error'), ('El suplente ya es titular'))
            return {
                    'type': 'ir.actions.client',
                    'tag': 'action_info',
                    'name': 'Warning',
                    'params': {
                        'title': 'Atención!!!!!!',
                        'text': 'El suplente ya está de alta como titular',
                        'sticky': False
                        }
                    }
        else:
            print "No duplicado"
            self.suplente_id.id_comision = self.titular_id.id_comision
            self.titular_id.id_comision = 5
            self.titular_id.estado = 'R'
            self.suplente_id.estado = 'T'
#        print self.suplente_id.estado
#       titular_id = self.env.context.get('active_id', False)
#       print 'Active_id: ', titular_id
#       delegado = self.env['docec.delegado'].browse(titular_id)
#       print "Delegado: ", delegado.nomDelegado
#       print self.env.context
    

