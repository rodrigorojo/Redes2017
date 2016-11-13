#! /usr/bin/env python
# -*- coding: utf-8 -*-


#####################################################
# PURPOSE: Clase que manejara los clientes que se   #
#          conectan y desconectan al sistema        #
#                                                   #
# Vilchis Dominguez Miguel Alonso                   #
#       <mvilchis@ciencias.unam.mx>                 #
#                                                   #
# Notes:                                            #
#                                                   #
# Copyright   17-08-2015                            #
#                                                   #
# Distributed under terms of the MIT license.       #
#####################################################
#python DirectoryServer.py port_number -l
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

#           Mis bibliotecas
import sys,getopt
sys.path.insert(0, '../')
sys.path.insert(0, 'Constants')
from Constants.AuxiliarFunctions import get_ip_address
import Constants.Constants
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class GeneralDirectory:
    """ Constructor de la clase, si recibe un puerto, entonces
        Trabajara de manera local, de otra manera, utilizará  la ip
        con la que cuenta.
        @param port <int> Si trabaja de manera local, representa el
                        número del puerto por el cual recibirá las peticiones
    """
    def __init__(self, port = None):
        self.client_dictionary = {}
        if(port == None):
            self.server = SimpleXMLRPCServer((get_ip_address(), 5555), allow_none = True)
            print "Directorio de ubicacion activo, mi direccion es:"
            print "(%s, %s)" %(get_ip_address(), 5555)
        else:
            self.server = SimpleXMLRPCServer(("localhost", int(port)), allow_none = True)
            print "Directorio de ubicacion activo, mi direccion es:"
            print "(%s, %s)" %("localhost", str(int(port)))
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        functionWrapper = FunctionWrapperDirectory(self.client_dictionary)
        self.server.register_instance(functionWrapper)




class FunctionWrapperDirectory:
    """ **************************************************
    Constructor de la clase
    @clients_dictionary (Diccionario) Contiene la información de
                todos los clientes (Usa username como llave, y contiene el nombre del usuario)
    ************************************************** """
    def __init__(self,client_dictionary):
        self.client_dictionary = client_dictionary

    """ **************************************************
    Metodo que regresa los contactos activos en el directorio excluyendo el contacto actual.
    ************************************************** """
    def get_contacts_wrapper(self, username):
        temp0 = {}
        for key in self.client_dictionary.keys():
            if(username != key):
                temp0[key] = self.client_dictionary[key]
        print "get:"
        print temp0
        return temp0

    """ **************************************************
    Metodo que agrega al cliente al diccionario de usuarios activos.
    ************************************************** """
    def connect_wrapper(self, ip_string, port_string, username):
        self.client_dictionary[str(username)] = {'NAME_CONTACT': username, 'IP_CONTACT':ip_string, 'PORT_CONTACT':port_string}
    """ **************************************************
    Metodo que elimina al cliente de los usuarios activos.
    ************************************************** """
    def disconnect_wrapper(self, ip_string, port_string):
        for key in self.client_dictionary.keys():
            temp1 = self.client_dictionary[key]
            if(temp1['IP_CONTACT'] == ip_string) and (temp1['PORT_CONTACT'] == port_string):
                del self.client_dictionary[key]
    """ **************************************************
    Metodo que elimina al cliente de los usuarios activos, por nombre de usuario.
    ************************************************** """
    def disconnect_wrapper_username(self, username):
        del self.client_dictionary[str(username)]
# **************************************************
#  Definicion de la funcion principal
#**************************************************
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "l", ["local="])
    except getopt.GetoptError:
        print 'Uso con puertos locales:'
        print '$ python Directory/DirectoryServer.py -l <puerto>'
        print 'Uso entre computadoras dentro de la red'
        print '$ python Directory/DirectoryServer.py '
        sys.exit(2)
    #if opts: #Si el usuario mandó alguna bandera
    if opts and ('-l' in opts[0]):
        local = True
    else:
        local = False
    if local:
        print args[0]
        general_server = GeneralDirectory(port = args[0]).server
    else:
        print "entro"
        general_server = GeneralDirectory().server
    general_server.serve_forever()


if __name__ == '__main__':
    main(sys.argv[1:])
