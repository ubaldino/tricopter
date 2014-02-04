__author__ = 'ubaldino'

from bluetooth import *

class Dispositivo:
  def buscar_dispositivos( self ):
    dispositivos = discover_devices( lookup_names = True )
    return dispositivos

  def conectar_dispositivo( self , mac , portf ):
    self.client_socket = BluetoothSocket( RFCOMM )
    self.client_socket.connect( ( mac , portf  ) )
    self.client_socket.send( "0" )
    #[('20:13:05:14:20:05', 'HC-06'), ('CC:52:AF:23:47:11', 'PAVILIONG4-PC'), ('00:AA:70:1F:97:7F', 'Ozzirisc'), ('E0:2A:82:7A:C9:30', 'DERIVE-PC')]
    return "Dispositivo conectado"

  def cerrar_conexion( self ):
    self.client_socket.close()
    return "Bluetoth Desconectado"

  def enviar_mensage( self , msg ):
    self.client_socket.send( msg )
