# -*- coding: utf-8 -*-

from openerp import models, fields, api
#from lxml import etree


class delegado(models.Model):
    _name = 'docec.delegado'
    orden = fields.Integer('Orden')
    id_organismo = fields.Many2one('docec.organismo', 'Organismo')
    id_comision = fields.Many2one('docec.comision', 'Comisión')
    nomDelegado = fields.Char('Nombre')
    dni = fields.Char('DNI')
    estado = fields.Char('Titular/Suplente')
    sexo = fields.Char('Sexo')
    id_org2 = fields.Many2one('docec.organismo', "Org. Secundario")
    antiguedad = fields.Date('Antigüedad')
    acreditado = fields.Boolean('Acreditado')
    material = fields.Char('Material')
    _rec_name = 'nomDelegado'
    
    _order = "id_organismo, estado desc, nomDelegado" 
    
    @api.one
    def acreditar(self):
        self.acreditado=True
        self.material="ENTREGADO"
        #print self.oid
        
    @api.multi
    def sustituir(self):
        print "Yep!!"
        return {
                'type': 'ir.actions.act_window',
                'res_model': 'docec.asistente',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                }
        
class organismo(models.Model):
    _name = 'docec.organismo'
    nomOrganismo = fields.Char('Organismo')
    titulares = fields.Integer('Titulares')
    suplentes = fields.Integer('Suplentes')
    miembrosc1 = fields.Integer('Comisión 1')
    miembrosc2 = fields.Integer('Comisión 2')
    miembrosc3 = fields.Integer('Comisión 3')
    miembrosc4 = fields.Integer('Comisión 4')
    _rec_name = 'nomOrganismo'
    
class comision(models.Model):
    _name = 'docec.comision'
    nomComision = fields.Char('Comisión')
    sala = fields.Many2one('docec.sala','Sala')
    miembros = fields.Integer('Miembros')
    _rec_name = 'nomComision'
    
class sala(models.Model):
    _name = 'docec.sala'
    nomSala = fields.Char("Sala")
    _rec_name = 'nomSala'
    