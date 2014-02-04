__author__ = 'ubaldino'
from Dispositivo import Dispositivo
import wx

class Main ( wx.Frame ):
  def __init__(self):
    wx.Frame.__init__( self, None, -1, 'Slider tricopter', size=( 500 , 700) )
    self.panel = wx.Panel( self , -1 )
    self.count_conect = 0
    self.dispositivos = Dispositivo()
    #  A E T R
    # botones  a , d

    btn_armar = wx.Button( self.panel , label='Armar', pos=( 20 , 1 ) )
    btn_desarmar = wx.Button( self.panel , label='Desarmar', pos=( 150 , 1 ))
    btn_buscar = wx.Button( self.panel , label='Buscar', pos=( 20 , 600 ))
    btn_conectar = wx.Button( self.panel , label='Conectar', pos=( 260 , 600 ))
    btn_desconectar = wx.Button( self.panel , label='Desconectar', pos=( 350 , 600 ))

    btn_armar.Bind( wx.EVT_BUTTON , self.armar )
    btn_desarmar.Bind( wx.EVT_BUTTON , self.desarmar )
    btn_buscar.Bind( wx.EVT_BUTTON , self.buscar_bluetooth )
    btn_conectar.Bind( wx.EVT_BUTTON , self.conectar_bluetooth )
    btn_desconectar.Bind( wx.EVT_BUTTON , self.desconectar_bluetooth )

    h_aleron = wx.Slider( self.panel , -1, 5, 0, 180,
            size=( 350, -1) , pos=( 20 , 50 ) , name="aleron",
            style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS )
    wx.StaticText( self.panel, -1, "Aleron", pos=( 123 , 90 ) , style=wx.ALIGN_CENTRE )
    h_aleron.SetTickFreq( 1 , 1)

    h_elevador = wx.Slider( self.panel , -1, 5, 0, 180,
            size=( 350, -1) , pos=( 20 , 130 ) ,
            style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS )
    wx.StaticText( self.panel, -1, "Elevador", pos=( 125 , 170 ) , style=wx.ALIGN_CENTRE )
    h_elevador.SetTickFreq( 1 , 1)

    h_timon = wx.Slider( self.panel , -1, 5, 0, 180,
            size=( 350, -1) , pos=( 20 , 210 ) ,
            style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS )
    wx.StaticText( self.panel, -1, "Timon", pos=( 130 , 250 ) , style=wx.ALIGN_CENTRE )
    h_timon.SetTickFreq( 1 , 1)

    h_acelerador = wx.Slider( self.panel , -1, 5, 0, 180,
            size=( 350, -1) , pos=( 20 , 290 ) ,
            style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS )
    wx.StaticText( self.panel, -1, "Acelerador", pos=( 120 , 330 ) , style=wx.ALIGN_CENTRE )
    h_acelerador.SetTickFreq( 1 , 1)
    self.txt_result = wx.StaticText( self.panel , label="Logs", pos=( 50 ,440 ) )
    self.txt_result.SetForegroundColour( wx.RED )

    h_aleron.Bind( wx.EVT_SCROLL, self.scroll_a )
    h_elevador.Bind( wx.EVT_SCROLL, self.scroll_e )
    h_timon.Bind( wx.EVT_SCROLL, self.scroll_t )
    h_acelerador.Bind( wx.EVT_SCROLL, self.scroll_r )

  def scroll_a( self, evt):
    self.dispositivos.enviar_mensage( str( evt.GetSelection() )+"a" )
    evt.Skip()

  def scroll_e( self, evt):
    self.dispositivos.enviar_mensage( str( evt.GetSelection() )+"e" )
    evt.Skip()

  def scroll_t( self, evt):
    self.dispositivos.enviar_mensage( str( evt.GetSelection() )+"t" )
    evt.Skip()

  def scroll_r( self, evt):
    self.dispositivos.enviar_mensage( str( evt.GetSelection() )+"r" )
    evt.Skip()



  def armar( self , evt):
    self.dispositivos.enviar_mensage( "q" )
    self.txt_result.SetLabel( "armado" )

  def desarmar( self , evt):
    self.dispositivos.enviar_mensage( "w" )
    self.txt_result.SetLabel( "desarmado" )

  def buscar_bluetooth(self , evt):
    self.devs_list = [] ; self.lista_devs = []
    self.txt_result.SetLabel( "| " )
    for address, name in self.dispositivos.buscar_dispositivos():
      self.devs_list.append( address )
      self.lista_devs.append( name )
      self.txt_result.SetLabel( self.txt_result.GetLabel()+name+" | " )
    self.cb_devices = wx.ComboBox( self.panel , pos=( 105, 600 ), size=( 150, -1), choices=self.lista_devs, style=wx.CB_READONLY )
    self.Bind( wx.EVT_COMBOBOX, self.OnSelect)

  def OnSelect(self, event):
    self.item = event.GetSelection()

  def conectar_bluetooth( self , evt ):
    print self.devs_list[self.item]
    print self.item
    self.dispositivos.conectar_dispositivo( str( self.devs_list[self.item] ) , int( self.item) )

    self.txt_result.SetLabel( "Conectado a : "+str(self.lista_devs[self.item]) )

  def desconectar_bluetooth( self, evt ):
    self.dispositivos.cerrar_conexion()
    self.txt_result.SetLabel( "Desconectado de : "+str(self.lista_devs[self.item]) )


app = wx.App(None)
frame = Main()
frame.Show()
app.MainLoop()
