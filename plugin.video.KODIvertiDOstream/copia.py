# -*- coding: utf-8 -*-
#------------------------------------------------------------
# KODIvertiDOstream - XBMC Add-on by Mendelux
# Version 1.0.0 (01.05.2022)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a la librería plugintools de Jesús (www.mimediacenter.info)
import os 
import sys                                      # Importamos librerías necesarias para el funcionamiento de nuestro Addon pero saber tambien
import re                                       # que no son todas necesarias,al igual que las funciones que se encuentran al final del código.                                                
import xbmc                                     # Las iremos utilizando en siguientes cursos de la Academia KODIvertiDO TEAM,en los que iremos
import xbmcgui                                  # introduciendo otro tipo de contenido.
import xbmcaddon
import xbmcplugin
import plugintools                              # Esta librería es la que nos va ha facilitar tanto la compatibilidad de nuestro Addon con 
import base64                                   # Kodi 18 y 19 como la propia programación.
import requests
import base64
import six
import xbmcvfs
from resolveurl.plugins.lib import jsunpack
myaddon =xbmcaddon .Addon ()

if six.PY2:
   translatePath = xbmc.translatePath
   LOG = xbmc.LOGNOTICE
elif six.PY3:
   translatePath = xbmcvfs.translatePath
   LOG = xbmc.LOGINFO

def run():                                               # Esta función def run() es la encargada de reaccionar cuando hacemos click en una opción del MENU prinicipal de nuestro Addon.
   plugintools.log("---> kodivertido-X.run <---")        # El funcionamiento,o la lógica del programa es muy sencilla y se ve rapido a golpe de ojo. Así funciona:
   plugintools.set_view(plugintools.LIST)              # Al hacer click en una opción,la funcion def run() hace posible enlazar esa opción con su función correspondiente a traves 
                                                         # del parametro action.Al igual que el menu que se muestra en pantalla tiene su función con su código,las opciones de este    
    # Get params                                         # menu también tine cada una su función(def).   
   params = plugintools.get_params()                     
    
   if params.get("action") is None:                      # Aqui es donde se establece que mientras no se pulse ninguna opción se muestre el menu en pantalla(funcion def main_list)
      main_list(params)                                  # Y si se pulsa una de sus opciones,se encarga primero de reconocer cual es(parametro action) y desvía el flujo del 
   else:                                                 # programa hacia esa función.
      action = params.get("action")
      exec (action+"(params)")
    
   plugintools.close_item_list()

#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------


#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------

def main_list(params):

   # cada plugintools.add_item(que es una instruccion) es un texto que corresponde con cada una de las opciones del MENU.
   # A parte del texto(title),por que las funciones cuando saltan de un sitio a otro del programa(action),transportan otros datos necesarios(parametros) 
   # como el icono(thumbnail) y el fondo(fanart) que se muestra cuando pasas por encima de la opcion.Tambien se puede indicar mas parametros 
   # como son folder=False(o True) que le comunica a la funcion que el destino de la accion(action) no mostrara(False) una lista de contenidos,
   # o el parametro isPlayable=False(o True) que le dice que no(false) es un contenido a reproducir. 
   # Como se ve,tanto el thumbnail como el fanart,en este ejercicio los he definido con su url que he obtenido con imgur.
   # Todos estos parametros title,thumbnail,fanart los podeis cambiar a vuestro gusto al igual de los colores([COLOR blue]).
   # El codigo para cada color siempre en minusculas y podeis encontrar todas las definiciones de colores en la red(colores python),red,white,lightpink...
   # Y para conseguir que un texto se muestre en negrita utilizamos [B],en mayusculas [UPPERCASE]...

   # En estas 4 primeras linea vemos que action = "",esto quiere decir que es un simple texto decorativo pues carece de accion(action).No tiene accion.
   plugintools.add_item(action = "" , title = "[COLOR lime][B]#######[COLOR aqua] KODIvertiDOstream [COLOR lime]#######[/B][/COLOR]", thumbnail ="https://i.imgur.com/NQkZlus.jpg", fanart = "https://i.imgur.com/D09v4Sm.jpg",  folder = False )


   plugintools.add_item(action = "" , title = "[COLOR lime][B]##                      [COLOR white]M  [COLOR yellow]E  [COLOR lime]N  [COLOR aqua]U                       [COLOR lime]##[/B][/COLOR]",  thumbnail ="https://i.imgur.com/NQkZlus.jpg", fanart = "https://i.imgur.com/D09v4Sm.jpg", folder = False )


   plugintools.add_item(action = "" , title = "[COLOR lime][B]#######[COLOR aqua] KODIvertiDOstream[COLOR lime]#######[/B][/COLOR]", thumbnail ="https://i.imgur.com/NQkZlus.jpg", fanart = "https://i.imgur.com/D09v4Sm.jpg",  folder = False )


   plugintools.add_item(action = "" , title = "", thumbnail ="https://i.imgur.com/NQkZlus.jpg", fanart = "https://i.imgur.com/D09v4Sm.jpg", folder = False )


   # Aqui estan las opciones que el usuario visualizara en su pantalla
   # En este curso solo daremos utilidad a una de las tres opciones, pero las dejo por si alguien quisiera implementar es aqui donde puede hacerlo
   # para lo que se tiene que definir el parametro action,y la funcion que la desarrolle.
   plugintools.add_item(action = "Item_1" , title = "[COLOR aqua][B]CONTENIDO [/COLOR] [COLOR yellow]1[/B][/COLOR]" , thumbnail = "https://i.imgur.com/NQkZlus.jpg" , url = "" , fanart = "https://i.imgur.com/n8F1hk2.jpg" , folder = True )


   plugintools.add_item(action = "Item_2" , title = "[COLOR aqua][B]CONTENIDO [/COLOR] [COLOR yellow] 2[/B][/COLOR]" , thumbnail = "https://i.imgur.com/NQkZlus.jpg" , url = "" , fanart = "https://i.imgur.com/n8F1hk2.jpg" , folder = True )

   
   plugintools.add_item(action = "acestream_link" , title = "[COLOR lime][B]Acestream[/B][/COLOR]" , thumbnail = "https://i.imgur.com/pDh2Gmp.jpg"  , fanart = "https://i.imgur.com/pDh2Gmp.jpg" , plot = "",  folder = True,isPlayable = False  )

   
#########################################  SUBMENUS   ###########################################   SUBMENUS   ###########################################   SUBMENUS   ###########################################       
#########################################  SUBMENUS   ###########################################   SUBMENUS   ###########################################   SUBMENUS   ###########################################
#########################################  SUBMENUS   ###########################################   SUBMENUS   ###########################################   SUBMENUS   ###########################################

# En estos submenus es donde damos vida a las distintas opciones del MENU principal y para esto,definimos la Funcion que corresponde a cada una de las opciones del
# MENU y las cuales ya hemos dado un nombre(action). En las funciones Item_1/Item_2 podeis incluir por ejemplo la entrada a una lista iptv, o una pelicula, o
# cualquier otro tipo de contenido que os gustaria mostrar y que como ya he dicho,iremos desarrollando en otros cursos.


##-----------------KODIvertiDOstream_Item_1##-------------------KODIvertiDOstream_Item_1#-------------------#KODIvertiDOstream_Item_1#-----------------------------------------------------------##
##-----------------KODIvertiDOstream_Item_1##-------------------KODIvertiDOstream_Item_1#-------------------#KODIvertiDOstream_Item_1#-----------------------------------------------------------##


def Item_1(params):
   return


##-----------------KODIvertiDOstream_Item_2##-------------------KODIvertiDOstream_Item_2#-------------------#KODIvertiDOstream_Item_2#-----------------------------------------------------------##
##-----------------KODIvertiDOstream_Item_2##-------------------KODIvertiDOstream_Item_2#-------------------#KODIvertiDOstream_Item_2#-----------------------------------------------------------##



def Item_2(params):
   return




def acestream_link(params):
  
   canales={}
   canales = {"canal01" : {"nombre" : "Liga Tv Bar 1080" ,
                           "id" : "608ffde844a8e6f4f7c7fb9783aa3459c818b9f8"} ,     # Aqui, a esta funcion def acestream_link, es donde se dirige la ejecucion de nuestro programa
                "canal02" : {"nombre" : "M. La Liga 1080 MultiAudio" ,              # cuando pulsamos sobre ella.
                           "id" : "167e3b44a520cd76d4372f6d30fe6d7ccd524175"} ,     # Como veis,he creado un diccionario al que le he llamado canales con la instruccion
                "canal03" : {"nombre" : "M.La Liga 720" ,                           # canales = {}
                           "id" : "df139bbcd7ae6825b46d5955c52d639f1215346a"} ,     # Despues lo lleno con esta logica:
                "canal04" : {"nombre" : "M. La Liga 1 1080" ,                       # A Cada uno de los canales le asigno su nombre,id(tambien se podrian incluir icono,fondo mediante sus url's,..) 
                           "id" : "4229d640fecf3c0897674241bcf851b67f4310e3"} ,     # Podeis poner los enlace Acestream que querais pero respetar escrupulosamente los espacios(identacion) del
                "canal05" : {"nombre" : "M.La Liga 2 1080 (Update)" ,               # codigo de lo contrario a nada que os comais unas comillas,una coma causara un error fatal y el Addon
                           "id" : "ed147166c7df93f7aecba44d4e2fc9383d028218"} ,     # os mostrara ese conocido mensaje de error al instalar.
                "canal06" : {"nombre" : "M.La Liga 3 1080" ,                        # Cortar y pegar los nombres,enlaces a vuestro gusto,ya que estos que yo he colocado
                           "id" : "e693d6b35ee9dc2c6a0d0593edec281268e79440"} ,     # dejaran de funcionar algun dia.
                "canal07" : {"nombre" : "Vamos 1080 update" ,
                           "id" : "069431a1199eb2545a14c0a724095e57bdc58e9c"} ,
                "canal08" : {"nombre" : "M. Deportes 1080" ,
                           "id" : "49acacbbbcf33be6e843958ceedc7da8dd4f1486"} ,
                "canal09" : {"nombre" : "M. Deportes 1 1080" ,
                           "id" : "c47f756750190e4b2a9eefe8afdac48a2203b8d6"} ,
                "canal10" : {"nombre" : "M. Deportes 2 1080" ,
                           "id" : "85bd65161dfd8c4033194da3c978c0450c9111db"} ,
                "canal11" : {"nombre" : "M. Deportes 3 720" ,
                           "id" : "0c8935087510ee1c5117243a6cc46f9d6d795faf"} ,
                "canal12" : {"nombre" : "M. Deportes 4 720" ,
                           "id" : "a88195215f9b6e38bf6363d28bfe84000a12d46a"} ,
                "canal13" : {"nombre" : "M. Deportes 5 720 update" ,
                           "id" : "5da3c25c14d111cb9c33cf6e0b45b7cab88fe741"} ,
                "canal14" : {"nombre" : "M. Liga de Campeones 1080 (Update)" ,
                           "id" : "aedf221240a0f8513d90b555bf1b6e5306ac1e76"} ,
                "canal15" : {"nombre" : "M. Liga de Campeones 720 (Update)" ,
                           "id" : "f8d89bf80b813631e6eb85fc8c185b00fe9ab88d"} ,
                "canal16" : {"nombre" : "M. Liga de Campeones 1 1080 (Update)" ,
                           "id" : "9b76d0739f87555ccd3f42fc8e548762a0b94c28"} ,
                "canal17" : {"nombre" : "M. Liga de Campeones 1  720" ,
                           "id" : "f8d89bf80b813631e6eb85fc8c185b00fe9ab88d"} ,
                "canal18" : {"nombre" : "M. Liga de Campeones 2 1080" ,
                           "id" : "612eed86f1ec250ebff3649e74e6729687c456f7"} ,
                "canal19" : {"nombre" : "M. Liga de Campeones 3 1080" ,
                           "id" : "a5d22610cb7bd5608c14249e3984bacb54dfe487"} ,
                "canal20" : {"nombre" : "M. Golf 1080 update" ,
                           "id" : "4f945b0ba4206fa2676b61e9eaa465ac3dcc8122"} ,
                "canal21" : {"nombre" : "DAZN 1 1080  (Update)" ,
                           "id" : "ad7973215880d12940a75699aa7044839a13a6f1"} ,
                "canal22" : {"nombre" : "DAZN 2 1080 update" ,
                           "id" : "b402c07f2e8bfe253815e08df0b7e0a6b0fad8e3"} ,
                "canal23" : {"nombre" : "DAZN 2 720 update" ,
                           "id" : "201b498f3c8d5366394ba4c0f0c4756131a4899a"} ,
                "canal24" : {"nombre" : "DAZN 3  1080 (Update)" ,
                           "id" : "bfbcda5a0999256360ce560caf2a6473aafc3f11"} ,
                "canal25" : {"nombre" : "DAZN 4 1080 update" ,
                           "id" : "3634ae8e7443f637222e0255f0fc70bf3f050e64"} ,
                "canal26" : {"nombre" : "F1 1080" ,
                           "id" : "c372020ed2744033f56548b6beb11a9f3e740f37"} ,
                "canal27" : {"nombre" : "F1 720" ,
                           "id" : "3f1c74da240b0933efaa572c0bdc24a7406ca7bf"} ,
                "canal28" : {"nombre" : "dazn F1 SD" ,
                           "id" : "4a03e14ec4e40afce24781e7c54ba9e3575dfe0a"} ,
                "canal29" : {"nombre" : "EuroSport 1 1080" ,
                           "id" : "36930ae99889bb571389e5eb5557e3d8ab2b1fda"} ,
                "canal30" : {"nombre" : "EUROSPORT  2 1080 (Update)" ,
                           "id" : "f2c46015fab59944d1f75487fe1ec725f9d74720"} ,
                "canal31" : {"nombre" : "SPORTV 1 update" ,
                           "id" : "3092996191aa30c04085bc5b0dec198dcfc11d6f"} ,
                "canal32" : {"nombre" : "SPORTV 2 update" ,
                           "id" : "b402a5fc3d93860c7f4a9c46463ff5469b6436f6"} ,
                "canal33" : {"nombre" : "SPORTV 3 update" ,
                           "id" : "4d78fadc6701008fb528202d9671e1d0f2acd486"} ,
                "canal35" : {"nombre" : "ESPN 2 1080" ,
                           "id" : "5ae9afd963961cd07e8f690e44a6596a2bb4e51e"} ,
                "canal36" : {"nombre" : "BEIN SPAÑOL" ,
                           "id" : "5da88bd42cd50b54570cd61fbae8749d9d886722"} ,
                "canal37" : {"nombre" : "Barsatv" ,
                           "id" : "6f292be252c8a3288de090a1243a8ab03f1e5288"} ,
                "canal38" : {"nombre" : "CUATRO 1080" ,
                           "id" : "0746c5511701c3db76c433f684c44549debad44f"} ,
                "canal39" : {"nombre" : "TELEDEPORTE 1080 update" ,
                           "id" : "a537d162cb8c5cfa72c09be09ecac69e2f2cc535"} ,                        
               "canal40" : {"nombre" : "GOL TV 1080" , 
                           "id" : "49c35606668ebf7a895434ec4c9243a163d87718"} ,
               "canal41" : {"nombre" : "BEIN SPAÑOL" ,
                          "id" : "5da88bd42cd50b54570cd61fbae8749d9d886722"}}
 # Recorrer un diccionario, imprimiendo su claves(nombre del canal)
   for key in canales:
       title = canales[key]['nombre']
       plot = canales[key]['id']
 # Y con esta instruccion coloco en pantalla esos nombres de cada canal como una lista items
 # que al pulsar sobre cualquiera de ellos nos dirigira a la funcion encargada de reproducir,ahora ya si,ese canal.
 # para lo que necesito enviar tanto la id como el nombre del canal.Esto lo hacemos recogiendo el nombre en   title = canales[key]['nombre']
 # y la id con plot = canales[key]['id']      
       plugintools.add_item ( action = "resolve_acestream" , title = "[COLOR yellow][B]" + title + "[/B][/COLOR]" , plot = plot, url="", thumbnail = "https://i.imgur.com/pDh2Gmp.jpg"  , fanart = "https://i.imgur.com/pDh2Gmp.jpg" , folder = False , isPlayable = True )
                       

 # Estas funciones las utilizaremos en otra ocasion.

def keyboard_input(default_text="" , title="" , hidden=False):
   keyboard = xbmc.Keyboard ( default_text , title , hidden )
   keyboard.doModal ()

   if (keyboard.isConfirmed ()):
       tecleado = keyboard.getText ()
   else:
       tecleado = ""

   return tecleado

def resolve_resolveurl(params):
   import resolveurl
   finalurl = resolveurl.resolve ( params.get ( "url" ) )
   plugintools.play_resolved_url ( finalurl )

def resolve_without_resolveurl(params):
   import resolveurl
   finalurl = (params.get ( "url" ))
   plugintools.play_resolved_url ( finalurl )

def play(params):
   import resolveurl
   url = (params.get ( "url" ))
   finalurl = url.encode("utf-8", "strict")
   plugintools.play_resolved_url ( finalurl )  
 
 # Aqui se reproduce el enlace Acestream que le hemos pasado utilizando el parametro id(params.get("plot") es quie recoge la id de cada canal)
def resolve_acestream ( params ) :
   import resolveurl
   finalurl = "plugin://script.module.horus?action=play&id={}&title={}&iconimage={}".format(params.get("plot"),params.get("title"),params.get("thumbnail"))
   plugintools.log("###############"+finalurl)
   plugintools . play_resolved_url ( finalurl )     
    
run()