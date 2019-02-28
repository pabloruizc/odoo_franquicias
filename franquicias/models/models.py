# -*- coding: utf-8 -*-

from odoo import models, fields, api

class franquicias(models.Model):

    _name = 'franquicias.franquicias'
    id = fields.Char(string = "IDENTIFICADOR", required = True)
    name = fields.Char(string = "Nombre", required = True)
    propietario = fields.Char(string = "Propietario", required = True)
    num_tiendas = fields.Integer(compute = "_totaltiendas")

    tienda = fields.One2many("franquicias.tienda", "franquicias", string="tienda")
    _sql_constraints = [('PK_NM', 'unique (id)','Ese id ya existe')]


    @api.one
    @api.depends('tienda')
    def _totaltiendas(self):
        self.num_tiendas = len(self.tienda)

class tienda(models.Model):

    _name = 'franquicias.tienda'
    id = fields.Char(string = "IDENTIFICADOR", required = True)
    propietario = fields.Char(string = "Propietario", required = True)
    ubicacion = fields.Char(string = "Ubicacion", required = True)
    ganancias_totales = fields.Float(compute = "_ganancias")
    franquicia = fields.Char(compute = "_nombrefranq", store = True)

    empleado = fields.One2many("franquicias.empleado", "tienda", string="Empleado")
    franquicias = fields.Many2one("franquicias.franquicias", string="Franquicia")
    ventas = fields.One2many("franquicias.ventas", "tienda", string="Ventas")

    @api.one
    @api.depends('franquicias')
    def _nombrefranq(self):
        self.franquicia = str(self.franquicias.name)

    @api.one
    @api.depends('ventas')
    def _ganancias(self):
        n = 0
        for record in self.ventas:
            self.ganancias_totales = self.ganancias_totales + record.precio




class empleado(models.Model):

    _name = 'franquicias.empleado'
    id = fields.Char(string = "DNI", required = True)
    name = fields.Char(string = "Nombre", required = True)
    domicilio = fields.Char(string = "Domicilio")
    ventas_empleado = fields.Float(compute = "_numventas")

    ventas = fields.One2many("franquicias.ventas", "empleado", string="Ventas")
    tienda = fields.Many2one("franquicias.tienda", string="Tienda")

    @api.one
    @api.depends('ventas')
    def _numventas(self):
        self.ventas_empleado = len(self.ventas)

class ventas(models.Model):

    _name = 'franquicias.ventas'
    id = fields.Char(string = "Numero de venta", required = True)
    fecha_venta = fields.Date(string = "Fecha de venta", required = True)
    producto = fields.Char(string = "Producto", required = True)
    precio = fields.Integer(string = "Precio", required = True)
    nombre_tienda = fields.Char(compute = "_nombretienda", store = True)

    tienda = fields.Many2one("franquicias.tienda", string="Tienda")
    empleado = fields.Many2one("franquicias.empleado", string= "Empleado")

    @api.one
    @api.depends('tienda')
    def _nombretienda(self):
        self.nombre_tienda = "Tienda de " + str(self.tienda.propietario)
