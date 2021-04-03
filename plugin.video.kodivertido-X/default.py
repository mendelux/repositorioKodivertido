# -*- coding: utf-8 -*-
#------------------------------------------------------------
# mitelechopo - XBMC Add-on by Torete
# Version 0.2.5 (15.05.2014)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a la librería plugintools de Jesús (www.mimediacenter.info)
import os 
import sys
import re
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import plugintools
import base64
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

def run():
    
    plugintools.log("---> kodivertido-X.run <---")
    #plugintools.set_view(plugintools.LIST)

    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec (action+"(params)")
    
    plugintools.close_item_list()

class Password:
    def __init__(self):
        self.password = plugintools.read("http://perillas.mendelux.es/password.txt").split('"')[1].split('"')[0]
        self.profile = translatePath(xbmcaddon.Addon().getAddonInfo('profile')) if six.PY3 else translatePath(
            xbmcaddon.Addon().getAddonInfo('profile'))
        self.passfile = self.profile + 'clave.txt'

    def check(self):
        global password_file
        if not os.path.isfile(self.passfile):
            password = xbmcgui.Dialog().input('Introduzca la contraseña para entrar al Addon:')
            if password == plugintools.read("http://perillas.mendelux.es/password.txt").split('"')[1].split('"')[0]:
                if not os.path.exists(self.profile): os.makedirs(self.profile)
                password_file = self.passfile
                f = open(password_file, 'w+')
                f.write(password)
                return True
            else:
                return False
        else:
            password_file = self.passfile
            with open(self.passfile, 'r') as f:
                password = f.read()
            if password == plugintools.read("http://perillas.mendelux.es/password.txt").split('"')[1].split('"')[0]:
                return True
            else:
                return False


###########################################   MENU   ###########################################   MENU   ###########################################   MENU   ###########################################
###########################################   MENU   ###########################################   MENU   ###########################################   MENU   ###########################################   
###########################################   MENU   ###########################################   MENU   ###########################################   MENU   ###########################################


#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------


#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------



#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------



###########################################   MENU   ###########################################   MENU   ###########################################   MENU   ###########################################
###########################################   MENU   ###########################################   MENU   ###########################################   MENU   ###########################################   
###########################################   MENU   ###########################################   MENU   ###########################################   MENU   ###########################################


#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------


#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------



#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------



def main_list(params):
    
    
    
        if Password().check() == True:
               

##--------- CABECERA -------------##--------- CABECERA -------------##--------- CABECERA -------------##--------- CABECERA -------------##

            plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/rpIKSHm.jpg", fanart = "https://i.imgur.com/n8F1hk2.jpg",  folder = False )


            plugintools.add_item(action = "" , title = "[B][COLOR white]            M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U[/B][/COLOR]",  thumbnail ="https://i.imgur.com/rpIKSHm.jpg", fanart = "https://i.imgur.com/n8F1hk2.jpg", folder = False )


            plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/rpIKSHm.jpg", fanart = "https://i.imgur.com/n8F1hk2.jpg",  folder = False )


            plugintools.add_item(action = "" , title = "", thumbnail ="https://i.imgur.com/rpIKSHm.jpg", fanart = "https://i.imgur.com/n8F1hk2.jpg",  folder = False )




            plugintools.add_item(action = "kodivertido_tv" , title = "[COLOR lime][B]KODIvertiDO[/COLOR] [COLOR yellow]TV[/B][/COLOR]" , thumbnail = "http://perillas.mendelux.es/1xyz/kodivertido/tv.png" , url = "" , fanart = "https://i.imgur.com/n8F1hk2.jpg" , folder = True )


            plugintools.add_item(action = "kodivertido_iptv" , title = "[COLOR lime][B]LISTAS[/COLOR] [COLOR yellow] IPTV[/B][/COLOR]" , thumbnail = "https://i.imgur.com/wn3vGhZ.jpg" , url = "http://perillas.mendelux.es/1xyz/kodivertido/lista_addon" , fanart = "https://i.imgur.com/n8F1hk2.jpg" , folder = True )


            plugintools.add_item(action = "cine_kodivertido" , title = "[COLOR lime][B]Cine [/B][/COLOR][COLOR aqua][B]KODI[/B][/COLOR][COLOR yellow][B]verti[/B][/COLOR][COLOR white][B]DO[/B][/COLOR]" , thumbnail = "https://cdn0.iconfinder.com/data/icons/film-making/49/10-512.png" , url = "" , fanart = "https://i.imgur.com/n8F1hk2.jpg" , folder = True )


            plugintools.add_item(action = "series" , title = "[COLOR lime][B]SERIES [/B][/COLOR][COLOR aqua][B]KODI[/B][/COLOR][COLOR yellow][B]verti[/B][/COLOR][COLOR white][B]DO[/B][/COLOR]" , thumbnail = "https://i.imgur.com/GNCzAMt.jpg" , url = "" , fanart = "https://i.imgur.com/n8F1hk2.jpg" , folder = True )


            plugintools.add_item(action = "kodivertido_tvinternete" , title = "[COLOR lime][B]DEPORTES[/COLOR] y [COLOR yellow]TV [COLOR yellow]DE INTERNET[/B][/COLOR]" , thumbnail = "https://i.imgur.com/O3Eb6MR.jpg" , fanart = "https://i.imgur.com/n8F1hk2.jpg" , folder = True )



            plugintools.add_item(action = "betas" , title = "[COLOR lightpink]KODI[/COLOR][COLOR red]vertido[/COLOR][COLOR lightpink]DO[/COLOR][COLOR red][B] BETAS[/B][/COLOR]" , thumbnail = "https://images.emojiterra.com/google/android-pie/512px/2622.png" , url = "http://perillas.mendelux.es/1xyz/kodivertido/videoclub" , fanart = "https://i.imgur.com/n8F1hk2.jpg" , folder = True )

        else:
            xbmcgui.Dialog().notification('Info', 'Contraseña Incorrecta', xbmcgui.NOTIFICATION_ERROR, 4000)
            os.remove(password_file)
            main_list(params)
#########################################  SUBMENUS   ###########################################   SUBMENUS   ###########################################   SUBMENUS   ###########################################       
#########################################  SUBMENUS   ###########################################   SUBMENUS   ###########################################   SUBMENUS   ###########################################
#########################################  SUBMENUS   ###########################################   SUBMENUS   ###########################################   SUBMENUS   ###########################################



##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------
##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------


def kodivertido_tv(params):

##--------- CABECERA -------------##--------- CABECERA -------------##--------- CABECERA -------------##--------- CABECERA -------------##
    
    
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://perillas.mendelux.es/1xyz/kodivertido/tv.png", fanart = "https://i.imgur.com/bP8hAy7.jpg",  folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR mediumspringgreen]TV[/B][/COLOR]",  thumbnail ="http://perillas.mendelux.es/1xyz/kodivertido/tv.png", fanart = "https://i.imgur.com/bP8hAy7.jpg", folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://perillas.mendelux.es/1xyz/kodivertido/tv.png", fanart = "https://i.imgur.com/bP8hAy7.jpg",  folder = False )


    plugintools.add_item(action = "" , title = "", thumbnail ="http://perillas.mendelux.es/1xyz/kodivertido/tv.png", fanart = "https://i.imgur.com/bP8hAy7.jpg",  folder = False )




    plugintools.add_item(action = "kodivertido_tdt" , title = "[COLOR darkorange][B]Kodivertido [COLOR blue]TDT[/B][/COLOR]" , thumbnail = "http://perillas.mendelux.es/1xyz/kodivertido/tdt.png" , url = "http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_tdt" , fanart = "https://i.imgur.com/urYNkVc.jpg" , folder = True )

    plugintools.add_item(action = "kodivertido_movistar" , title = "[COLOR darkorange][B]Kodivertido [COLOR blue]MOVISTAR+[/B][/COLOR]" , thumbnail = "http://perillas.mendelux.es/1xyz/kodivertido/vomistar.png" , url = "http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_mvstar" , fanart = "https://i.imgur.com/wcf3nYG.jpg" , folder = True )

    plugintools.add_item(action = "kodivertido_documentales" , title = "[COLOR darkorange][B]Kodivertido [COLOR blue]DOCUMENTALES[/B][/COLOR]" , thumbnail = "https://i.imgur.com/Ds14DOT.jpg" , url = "http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_documentales" , fanart = "https://i.imgur.com/UB9BlgK.jpg" , folder = True )

    plugintools.add_item(action = "kodivertido_infantiles" , title = "[COLOR darkorange][B]Kodivertido [COLOR blue]INFANTILES[/B][/COLOR]" , thumbnail = "https://www.conmishijos.com/uploads/ocio_familia/television_boing.jpg" , url = "http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_infantiles" , fanart = "https://i.imgur.com/ZXFHwWI.jpg" , folder = True )

    plugintools.add_item(action = "kodivertido_deportes" , title = "[COLOR darkorange][B]Kodivertido [COLOR blue]DEPORTES[/B][/COLOR]" , thumbnail = "https://i.imgur.com/Apj1Umv.jpg" , url = "http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_deportes" , fanart = "https://i.imgur.com/UofLWEe.jpg" , folder = True )

    plugintools.add_item(action = "kodivertido_musica" , title = "[COLOR darkorange][B]Kodivertido [COLOR blue]MUSICA[/B][/COLOR]" , thumbnail = "https://i.imgur.com/e4TAxwf.jpg" , url = "http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_musicales" , fanart = "https://i.imgur.com/iVR6LkL.jpg" , folder = True )

    plugintools.add_item(action = "kodivertido_cochinos" , title = "[COLOR darkorange][B]Kodivertido [COLOR blue]COCHINOS[/B][/COLOR]" , thumbnail = "https://i.imgur.com/gckjRde.jpg" , url = "http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_cochinos" , fanart = "https://i.imgur.com/b8zWTwf.jpg" , folder = True )

    plugintools.add_item(action = "kodivertido_tvinternete" , title = "[COLOR darkorange][B]Kodivertido [COLOR blue]ESPECIAL [COLOR lime]TV [COLOR lightpink]INTERNET[/B][/COLOR]" , thumbnail = "https://i.imgur.com/30Tq1VI.jpg"  , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = True )



##-----------------kodivertido_taquillas##-------------------kodivertido_taquillas#-------------------#kodivertido_taquillas#-----------------------------------------------------------
##-----------------kodivertido_taquillas##-------------------kodivertido_taquillas#-------------------#kodivertido_taquillas#-----------------------------------------------------------##-----------------kodivertido_taquillas##-------------------kodivertido_taquillas#-------------------#kodivertido_taquillas#-----------------------------------------------------------##-----------------kodivertido_taquillas##-------------------kodivertido_taquillas#-------------------#kodivertido_taquillas#-----------------------------------------------------------##-----------------kodivertido_taquillas##-------------------kodivertido_taquillas#-------------------#kodivertido_taquillas#-----------------------------------------------------------##-----------------kodivertido_taquillas##-------------------kodivertido_taquillas#-------------------#kodivertido_taquillas#-----------------------------------------------------------##-----------------kodivertido_taquillas##-------------------kodivertido_taquillas#-------------------#kodivertido_taquillas#-----------------------------------------------------------##-----------------kodivertido_taquillas##-------------------kodivertido_taquillas#-------------------#kodivertido_taquillas#-----------------------------------------------------------##-----------------kodivertido_taquillas##-------------------kodivertido_taquillas#-------------------#kodivertido_taquillas#-----------------------------------------------------------##-----------------kodivertido_taquillas##-------------------kodivertido_taquillas#-------------------#kodivertido_taquillas#-----------------------------------------------------------##-----------------kodivertido_taquillas##-------------------kodivertido_taquillas#-------------------#kodivertido_taquillas#-----------------------------------------------------------##-----------------kodivertido_taquillas##-------------------kodivertido_taquillas#-------------------#kodivertido_taquillas#-----------------------------------------------------------


def kodivertido_taquillas(params):

##--------- CABECERA -------------##--------- CABECERA -------------##--------- CABECERA -------------##--------- CABECERA -------------##


    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://perillas.mendelux.es/1xyz/kodivertido/taquillas.png", fanart = "https://i.imgur.com/bP8hAy7.jpg",  folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR gold]TAQUILLAS[/B][/COLOR]",  thumbnail ="http://perillas.mendelux.es/1xyz/kodivertido/taquillas.png", fanart = "https://i.imgur.com/bP8hAy7.jpg", folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://perillas.mendelux.es/1xyz/kodivertido/taquillas.png", fanart = "https://i.imgur.com/bP8hAy7.jpg",  folder = False )


    plugintools.add_item(action = "" , title = "", thumbnail ="http://perillas.mendelux.es/1xyz/kodivertido/taquillas.png", fanart = "https://i.imgur.com/bP8hAy7.jpg",  folder = False )





    plugintools.add_item(action = "kodivertido_taquillas1" , title = "[COLOR lime][B]TAQUILLAS[/COLOR] [COLOR yellow]MOVISTAR[/B][/COLOR]" , thumbnail = "http://perillas.mendelux.es/1xyz/kodivertido/taquillas.png" , url = "http://perillas.mendelux.es/1xyz/kodivertido/taquillas1" , fanart = "https://i.imgur.com/bP8hAy7.jpg" , folder = True )




##-----------------cine_kodivertido##-------------------cine_kodivertido#-------------------#cine_kodivertido#-----------------------------------------------------------
##-----------------cine_kodivertido##-------------------cine_kodivertido#-------------------#cine_kodivertido#-----------------------------------------------------------##-----------------cine_kodivertido##-------------------cine_kodivertido#-------------------#cine_kodivertido#-----------------------------------------------------------##-----------------cine_kodivertido##-------------------cine_kodivertido#-------------------#cine_kodivertido#-----------------------------------------------------------##-----------------cine_kodivertido##-------------------cine_kodivertido#-------------------#cine_kodivertido#-----------------------------------------------------------##-----------------cine_kodivertido##-------------------cine_kodivertido#-------------------#cine_kodivertido#-----------------------------------------------------------##-----------------cine_kodivertido##-------------------cine_kodivertido#-------------------#cine_kodivertido#-----------------------------------------------------------##-----------------cine_kodivertido##-------------------cine_kodivertido#-------------------#cine_kodivertido#-----------------------------------------------------------##-----------------cine_kodivertido##-------------------cine_kodivertido#-------------------#cine_kodivertido#-----------------------------------------------------------##-----------------cine_kodivertido##-------------------cine_kodivertido#-------------------#cine_kodivertido#-----------------------------------------------------------##-----------------cine_kodivertido##-------------------cine_kodivertido#-------------------#cine_kodivertido#-----------------------------------------------------------##-----------------cine_kodivertido##-------------------cine_kodivertido#-------------------#cine_kodivertido#-----------------------------------------------------------


def cine_kodivertido(params):

##--------- CABECERA -------------##--------- CABECERA -------------##--------- CABECERA -------------##--------- CABECERA -------------##

    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/fQHuZgC.jpg", fanart = "https://i.imgur.com/bP8hAy7.jpg",  folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR darkorange]CINE[/B][/COLOR]",  thumbnail ="https://i.imgur.com/fQHuZgC.jpg", fanart = "https://i.imgur.com/bP8hAy7.jpg", folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/fQHuZgC.jpg", fanart = "https://i.imgur.com/bP8hAy7.jpg",  folder = False )


    plugintools.add_item(action = "" , title = "", thumbnail ="https://i.imgur.com/fQHuZgC.jpg", fanart = "https://i.imgur.com/bP8hAy7.jpg",  folder = False )




    # GranTorrent
    plugintools.add_item(action = "grantorrent" , title = "[COLOR lime][B]G R A N   [/B][/COLOR][COLOR lime][B]T O [/B][/COLOR][COLOR yellow][B]R[/B][/COLOR][COLOR white][B] R E N T[/B][/COLOR]" , thumbnail = "https://i.imgur.com/uWqZDRQ.jpg" , url = "" , fanart = "https://i.ytimg.com/vi/7D82gt558g4/maxresdefault.jpg" , folder = True )

    # Pctfenix
    plugintools.add_item(action = "cine_pctfenix" , title = "[COLOR lime][B]C I N E    [/B][/COLOR][COLOR lime][B]P C[/B][/COLOR][COLOR yellow][B] T[/B][/COLOR][COLOR white][B]   F E N I X[/B][/COLOR][COLOR lightpink][B]  --> Necesario   ELEMENTUM <--[/B][/COLOR]" , thumbnail = "https://i.imgur.com/594d676.jpg" , url = "" , fanart = "https://i.imgur.com/594d676.jpg" , folder = True )
    
    
    # Videoclub
    plugintools.add_item(action = "cine_videoclub" , title = "[COLOR lightpink]KODI[/COLOR][COLOR aqua]vertido[/COLOR][COLOR lightpink]DO[/COLOR][COLOR yellow][B] VIDEOCLUB[/B][/COLOR]" , thumbnail = "https://i.imgur.com/pmzImSy.jpg" , url = "http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_cine1" , fanart = "https://i.imgur.com/pmzImSy.jpg" , folder = True )

    
    
##-----------------series##-------------------series#-------------------#series#-----------------------------------------------------------
##-----------------series##-------------------series#-------------------#series#-----------------------------------------------------------##-----------------series##-------------------series#-------------------#series#-----------------------------------------------------------##-----------------series##-------------------series#-------------------#series#-----------------------------------------------------------##-----------------series##-------------------series#-------------------#series#-----------------------------------------------------------##-----------------series##-------------------series#-------------------#series#-----------------------------------------------------------##-----------------series##-------------------series#-------------------#series#-----------------------------------------------------------##-----------------series##-------------------series#-------------------#series#-----------------------------------------------------------##-----------------series##-------------------series#-------------------#series#-----------------------------------------------------------##-----------------series##-------------------series#-------------------#series#-----------------------------------------------------------##-----------------series##-------------------series#-------------------#series#-----------------------------------------------------------##-----------------series##-------------------series#-------------------#series#-----------------------------------------------------------


def series(params):

    ##--------- CABECERA series-------------##--------- CABECERA series-------------##--------- CABECERA series-------------##--------- CABECERA series-------------##--------- CABECERA series-------------##--------- CABECERA series-------------##--------- CABECERA series-------------##--------- CABECERA series-------------##


    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/GNCzAMt.jpg" , fanart = "https://i.imgur.com/bP8hAy7.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR yellow]SERIES[/B][/COLOR]" , thumbnail = "https://i.imgur.com/GNCzAMt.jpg" , fanart = "https://i.imgur.com/bP8hAy7.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/GNCzAMt.jpg" , fanart = "https://i.imgur.com/bP8hAy7.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/GNCzAMt.jpg", fanart = "https://i.imgur.com/bP8hAy7.jpg", folder = False)




    plugintools.add_item(action = "grantorrent_series_nor" , title = "[COLOR yellow][B]GRANTORRENT[/B][/COLOR]" , thumbnail = "https://i.imgur.com/GNCzAMt.jpg" , url = "https://grantorrent.nl/series/" , fanart = "https://i.imgur.com/MK6Lqu2.jpg" , folder = True )


    plugintools.add_item(action = "mitorrent_series" , title = "[COLOR yellow][B]Mi Torrent[/B][/COLOR]" , thumbnail = "https://i.imgur.com/GNCzAMt.jpg" , url = "https://mitorrent.org/series/" , fanart = "https://i.imgur.com/MK6Lqu2.jpg" , page = "1" , folder = True )
   

    plugintools.add_item(action = "cinetorrent_series" , title = "[COLOR yellow][B]Cine Torrent[/B][/COLOR]" , thumbnail = "https://i.imgur.com/GNCzAMt.jpg" , url = "http://cinetorrent.co/series/" , fanart = "https://i.imgur.com/MK6Lqu2.jpg" , page = "1" , folder = True )


'''

##-----------------deportes##-------------------deportes#-------------------#deportes#-----------------------------------------------------------
##-----------------deportes##-------------------deportes#-------------------#deportes#-----------------------------------------------------------##-----------------deportes##-------------------deportes#-------------------#deportes#-----------------------------------------------------------##-----------------deportes##-------------------deportes#-------------------#deportes#-----------------------------------------------------------##-----------------deportes##-------------------deportes#-------------------#deportes#-----------------------------------------------------------##-----------------deportes##-------------------deportes#-------------------#deportes#-----------------------------------------------------------##-----------------deportes##-------------------deportes#-------------------#deportes#-----------------------------------------------------------##-----------------deportes##-------------------deportes#-------------------#deportes#-----------------------------------------------------------##-----------------deportes##-------------------deportes#-------------------#deportes#-----------------------------------------------------------##-----------------deportes##-------------------deportes#-------------------#deportes#-----------------------------------------------------------##-----------------deportes##-------------------deportes#-------------------#deportes#-----------------------------------------------------------##-----------------deportes##-------------------deportes#-------------------#deportes#-----------------------------------------------------------


def deportes(params):

    ##--------- CABECERA deportes-------------##--------- CABECERA deportes-------------##--------- CABECERA deportes-------------##--------- CABECERA deportes-------------##--------- CABECERA deportes-------------##--------- CABECERA deportes-------------##--------- CABECERA deportes-------------##--------- CABECERA deportes-------------##

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E7vzz9Q.jpg" , fanart = "https://i.imgur.com/E7vzz9Q.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR lightpink]DEPORTES Y DIRECTOS[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E7vzz9Q.jpg" , fanart = "https://i.imgur.com/E7vzz9Q.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E7vzz9Q.jpg" , fanart = "https://i.imgur.com/E7vzz9Q.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/E7vzz9Q.jpg", fanart = "https://i.imgur.com/E7vzz9Q.jpg", folder = False)




    plugintools.add_item (action = "directs" , title = "[COLOR lime][B]Directos[/COLOR] [COLOR bluemarine]KODIvertiDO[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E7vzz9Q.jpg" , url = "http://perillas.mendelux.es/1xyz/kodivertido/directos_dailysport" , fanart = "https://i.imgur.com/E7vzz9Q.jpg" , folder = True )


    plugintools.add_item (action = "DailySport" , title = "[COLOR yellow][B]Agenda DailySport[/B][/COLOR]" , thumbnail = "https://i.imgur.com/NCftJ3F.jpg" , url = "https://dailysport.bar/" , fanart = "https://i.imgur.com/E7vzz9Q.jpg" , folder = True )


    plugintools.add_item (action = "canalesd" , title = "[COLOR lime][B]Canales Deportivos[/B][/COLOR]" , thumbnail = "https://img96.xooimage.com/files/f/1/0/canales-3f3a25c.jpg" , url = "http://perillas.mendelux.es/1xyz/kodivertido/canalesdeportivos" , fanart = "https://i.imgur.com/E7vzz9Q.jpg" , folder = True )


'''


##-----------------betas##-------------------betas#-------------------#betas#-----------------------------------------------------------
##-----------------betas##-------------------betas#-------------------#betas#-----------------------------------------------------------##-----------------betas##-------------------betas#-------------------#betas#-----------------------------------------------------------##-----------------betas##-------------------betas#-------------------#betas#-----------------------------------------------------------##-----------------betas##-------------------betas#-------------------#betas#-----------------------------------------------------------##-----------------betas##-------------------betas#-------------------#betas#-----------------------------------------------------------##-----------------betas##-------------------betas#-------------------#betas#-----------------------------------------------------------##-----------------betas##-------------------betas#-------------------#betas#-----------------------------------------------------------##-----------------betas##-------------------betas#-------------------#betas#-----------------------------------------------------------##-----------------betas##-------------------betas#-------------------#betas#-----------------------------------------------------------##-----------------betas##-------------------betas#-------------------#betas#-----------------------------------------------------------##-----------------betas##-------------------betas#-------------------#betas#-----------------------------------------------------------


def betas(params):

    ##--------- CABECERA betas-------------##--------- CABECERA betas-------------##--------- CABECERA betas-------------##--------- CABECERA betas-------------##--------- CABECERA betas-------------##--------- CABECERA betas-------------##--------- CABECERA betas-------------##--------- CABECERA betas-------------##

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/amzK6w7.jpg" , fanart = "https://i.imgur.com/bP8hAy7.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR lime]BETAS[/B][/COLOR]" , thumbnail = "https://i.imgur.com/amzK6w7.jpg" , fanart = "https://i.imgur.com/bP8hAy7.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/amzK6w7.jpg" , fanart = "https://i.imgur.com/bP8hAy7.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/amzK6w7.jpg", fanart = "https://i.imgur.com/bP8hAy7.jpg", folder = False)




    plugintools.add_item (action = "videoclub" , title = "[COLOR lime]*[/COLOR][COLOR lightpink] KODI[/COLOR][COLOR aqua]vertido[/COLOR][COLOR lightpink]DO[/COLOR][COLOR yellow][B] VIDEOCLUB[/B][/COLOR]" , thumbnail = "https://i.imgur.com/SjSFzwc.jpg" , url = "http://perillas.mendelux.es/1xyz/kodivertido/videoclub" , fanart = "https://i.imgur.com/kdhPyKm.jpg" , folder = True )


    plugintools.add_item (action = "tv_betas" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]*[COLOR turquoise][COLOR white] canales de la [COLOR gold]lista kodivertido TV[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/Fi0nmaU.jpg" , url = "http://perillas.mendelux.es/1xyz/kodivertido/tv_betas" , fanart = "https://i.imgur.com/5dGZ06p.jpg" , folder = True )


    plugintools.add_item (action = "deportes_betas" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]*[COLOR turquoise][COLOR white] canales de la [COLOR gold]lista kodivertido DEPORTES[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://lh3.googleusercontent.com/rKIt-MWlBJ0-FBv9FGT2AfiHBlVlhG5iY-QlQiVXVcwivjBecXX87rucMsgrmhEIsDrC" , url = "http://perillas.mendelux.es/1xyz/kodivertido/deportes_betas" , fanart = "https://i.imgur.com/E7vzz9Q.jpg" , folder = True )


    plugintools.add_item (action = "taquillas_betas" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]*[COLOR turquoise][COLOR white] canales de la [COLOR gold]lista kodivertido TAQUILLAS[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "http://perillas.mendelux.es/1xyz/kodivertido/taquillas.png" , url = "http://perillas.mendelux.es/1xyz/kodivertido/taquillas_beta" , fanart = "https://i.imgur.com/bP8hAy7.jpg" , folder = True )


    plugintools.add_item (action = "cochinos_betas" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]*[COLOR turquoise][COLOR white] canales de la [COLOR gold]lista kodivertido COCHINOS[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/29b9UAP.jpg" , url = "http://perillas.mendelux.es/1xyz/kodivertido/cochinos_beta" , fanart = "https://i.imgur.com/mxHSw8B.jpg" , folder = True )


    #plugintools.add_item (action = "test_betas" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]*[COLOR turquoise][COLOR yellow] T [COLOR gold]E S T[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/29b9UAP.jpg" , url = "http://perillas.mendelux.es/1xyz/kodivertido/test_betas" , fanart = "https://i.imgur.com/mxHSw8B.jpg" , folder = True )





#########################################  TV   ###########################################   TV   ###########################################   TV   ####################################################################################  TV   ###########################################   TV   ###########################################   TV   ###########################################
##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------
##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------##-----------------kodivertido_tv##-------------------kodivertido_tv#-------------------#kodivertido_tv#-----------------------------------------------------------
#########################################  TV   ###########################################   TV   ###########################################   TV   ####################################################################################  TV   ###########################################   TV   ###########################################   TV   ###########################################






def kodivertido_tdt(params):
    
    ##--------- CABECERA kodivertido_tdt-------------##--------- CABECERA kodivertido_tdt-------------##--------- CABECERA kodivertido_tdt-------------##--------- CABECERA kodivertido_tdt-------------##--------- CABECERA kodivertido_tdt-------------##--------- CABECERA kodivertido_tdt-------------##--------- CABECERA kodivertido_tdt-------------##--------- CABECERA kodivertido_tdt-------------##
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/RKM3S9q.jpg" , fanart = "https://i.imgur.com/5UwkEwQ.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR red]T[COLOR lime]D[COLOR aqua]T[/B][/COLOR]" , thumbnail = "https://i.imgur.com/RKM3S9q.jpg" , fanart = "https://i.imgur.com/5UwkEwQ.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/RKM3S9q.jpg" , fanart = "https://i.imgur.com/5UwkEwQ.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/RKM3S9q.jpg", fanart = "https://i.imgur.com/5UwkEwQ.jpg", folder = False)

  

    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    #url = body.strip ().decode ("utf-8" , "ignore")
    
    matches = plugintools.find_multiple_matches(url,r'(?s)EXTINF.*?name=".*?".*?logo=".*?".*?http.*?\s')
    
    for match in matches:
        patron = plugintools.find_single_match ( match , r'(?s)EXTINF.*?name="(.*?)".*?logo="(.*?)".*?(http.*?)\s' )
        title = patron[0]
        thumb = patron[1]
        url = patron[2]
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = "https://i.imgur.com/5UwkEwQ.jpg" , folder = False , isPlayable = True )
 

##-----------------kodivertido_movistar##-------------------kodivertido_movistar#-------------------#kodivertido_movistar#-----------------------------------------------------------
##-----------------kodivertido_movistar##-------------------kodivertido_movistar#-------------------#kodivertido_movistar#-----------------------------------------------------------##-----------------kodivertido_movistar##-------------------kodivertido_movistar#-------------------#kodivertido_movistar#-----------------------------------------------------------##-----------------kodivertido_movistar##-------------------kodivertido_movistar#-------------------#kodivertido_movistar#-----------------------------------------------------------##-----------------kodivertido_movistar##-------------------kodivertido_movistar#-------------------#kodivertido_movistar#-----------------------------------------------------------##-----------------kodivertido_movistar##-------------------kodivertido_movistar#-------------------#kodivertido_movistar#-----------------------------------------------------------##-----------------kodivertido_movistar##-------------------kodivertido_movistar#-------------------#kodivertido_movistar#-----------------------------------------------------------##-----------------kodivertido_movistar##-------------------kodivertido_movistar#-------------------#kodivertido_movistar#-----------------------------------------------------------##-----------------kodivertido_movistar##-------------------kodivertido_movistar#-------------------#kodivertido_movistar#-----------------------------------------------------------##-----------------kodivertido_movistar##-------------------kodivertido_movistar#-------------------#kodivertido_movistar#-----------------------------------------------------------##-----------------kodivertido_movistar##-------------------kodivertido_movistar#-------------------#kodivertido_movistar#-----------------------------------------------------------##-----------------kodivertido_movistar##-------------------kodivertido_movistar#-------------------#kodivertido_movistar#-----------------------------------------------------------

def kodivertido_movistar(params):
    
##--------- CABECERA kodivertido_movistar-------------##--------- CABECERA kodivertido_tdt-------------##--------- CABECERA kodivertido_tdt-------------##--------- CABECERA kodivertido_tdt-------------##--------- CABECERA kodivertido_tdt-------------##--------- CABECERA kodivertido_tdt-------------##--------- CABECERA kodivertido_tdt-------------##--------- CABECERA kodivertido_tdt-------------##  
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/ybtmUEq.jpg" , fanart = "https://i.imgur.com/5UwkEwQ.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR white]CANALES[COLOR bluemarine]MOVISTAR[/B][/COLOR]" , thumbnail = "https://i.imgur.com/ybtmUEq.jpg" , fanart = "https://i.imgur.com/5UwkEwQ.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/ybtmUEq.jpg" , fanart = "https://i.imgur.com/5UwkEwQ.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/ybtmUEq.jpg", fanart = "https://i.imgur.com/5UwkEwQ.jpg", folder = False)

 
    
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches(url,r'(?s)EXTINF.*?name=".*?".*?logo=".*?".*?http.*?\s')
    
    for match in matches:
        patron = plugintools.find_single_match ( match , r'(?s)EXTINF.*?name="(.*?)".*?logo="(.*?)".*?(http.*?)\s' )
        title = patron[0]
        thumb = patron[1]
        url = patron[2]
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = "https://i.imgur.com/5UwkEwQ.jpg" , folder = False , isPlayable = True )
 
    

##-----------------kodivertido_documentales##-------------------kodivertido_documentales#-------------------#kodivertido_documentales#-----------------------------------------------------------
##-----------------kodivertido_documentales##-------------------kodivertido_documentales#-------------------#kodivertido_documentales#-----------------------------------------------------------##-----------------kodivertido_documentales##-------------------kodivertido_documentales#-------------------#kodivertido_documentales#-----------------------------------------------------------##-----------------kodivertido_documentales##-------------------kodivertido_documentales#-------------------#kodivertido_documentales#-----------------------------------------------------------##-----------------kodivertido_documentales##-------------------kodivertido_documentales#-------------------#kodivertido_documentales#-----------------------------------------------------------##-----------------kodivertido_documentales##-------------------kodivertido_documentales#-------------------#kodivertido_documentales#-----------------------------------------------------------##-----------------kodivertido_documentales##-------------------kodivertido_documentales#-------------------#kodivertido_documentales#-----------------------------------------------------------##-----------------kodivertido_documentales##-------------------kodivertido_documentales#-------------------#kodivertido_documentales#-----------------------------------------------------------##-----------------kodivertido_documentales##-------------------kodivertido_documentales#-------------------#kodivertido_documentales#-----------------------------------------------------------##-----------------kodivertido_documentales##-------------------kodivertido_documentales#-------------------#kodivertido_documentales#-----------------------------------------------------------##-----------------kodivertido_documentales##-------------------kodivertido_documentales#-------------------#kodivertido_documentales#-----------------------------------------------------------##-----------------kodivertido_documentales##-------------------kodivertido_documentales#-------------------#kodivertido_documentales#-----------------------------------------------------------

def kodivertido_documentales(params):
    
##--------- CABECERA kodivertido_documentales-------------##--------- CABECERA kodivertido_documentales-------------##--------- CABECERA kodivertido_documentales-------------##--------- CABECERA kodivertido_documentales-------------##--------- CABECERA kodivertido_documentales-------------##--------- CABECERA kodivertido_documentales-------------##--------- CABECERA kodivertido_documentales-------------##--------- CABECERA kodivertido_documentales-------------##    
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/Qfd2aMa.jpg" , fanart = "https://i.imgur.com/K2qLcF3.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR lime]DOCU[COLOR green]MENTALES[/B][/COLOR]" , thumbnail = "https://i.imgur.com/Qfd2aMa.jpg" , fanart = "https://i.imgur.com/K2qLcF3.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/Qfd2aMa.jpg" , fanart = "https://i.imgur.com/K2qLcF3.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/Qfd2aMa.jpg", fanart = "https://i.imgur.com/K2qLcF3.jpg", folder = False)


  
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches(url,r'(?s)EXTINF.*?name=".*?".*?logo=".*?".*?http.*?\s')
    
    for match in matches:
        patron = plugintools.find_single_match ( match , r'(?s)EXTINF.*?name="(.*?)".*?logo="(.*?)".*?(http.*?)\s' )
        title = patron[0]
        thumb = patron[1]
        url = patron[2]
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = "https://i.imgur.com/5UwkEwQ.jpg" , folder = False , isPlayable = True )
 
 
 

##-----------------kodivertido_infantiles##-------------------kodivertido_infantiles#-------------------#kodivertido_infantiles#-----------------------------------------------------------
##-----------------kodivertido_infantiles##-------------------kodivertido_infantiles#-------------------#kodivertido_infantiles#-----------------------------------------------------------##-----------------kodivertido_infantiles##-------------------kodivertido_infantiles#-------------------#kodivertido_infantiles#-----------------------------------------------------------##-----------------kodivertido_infantiles##-------------------kodivertido_infantiles#-------------------#kodivertido_infantiles#-----------------------------------------------------------##-----------------kodivertido_infantiles##-------------------kodivertido_infantiles#-------------------#kodivertido_infantiles#-----------------------------------------------------------##-----------------kodivertido_infantiles##-------------------kodivertido_infantiles#-------------------#kodivertido_infantiles#-----------------------------------------------------------##-----------------kodivertido_infantiles##-------------------kodivertido_infantiles#-------------------#kodivertido_infantiles#-----------------------------------------------------------##-----------------kodivertido_infantiles##-------------------kodivertido_infantiles#-------------------#kodivertido_infantiles#-----------------------------------------------------------##-----------------kodivertido_infantiles##-------------------kodivertido_infantiles#-------------------#kodivertido_infantiles#-----------------------------------------------------------##-----------------kodivertido_infantiles##-------------------kodivertido_infantiles#-------------------#kodivertido_infantiles#-----------------------------------------------------------##-----------------kodivertido_infantiles##-------------------kodivertido_infantiles#-------------------#kodivertido_infantiles#-----------------------------------------------------------##-----------------kodivertido_infantiles##-------------------kodivertido_infantiles#-------------------#kodivertido_infantiles#-----------------------------------------------------------

def kodivertido_infantiles(params):
    
##--------- CABECERA kodivertido_infantiles-------------##--------- CABECERA kodivertido_infantiles-------------##--------- CABECERA kodivertido_infantiles-------------##--------- CABECERA kodivertido_infantiles-------------##--------- CABECERA kodivertido_infantiles-------------##--------- CABECERA kodivertido_infantiles-------------##--------- CABECERA kodivertido_infantiles-------------##--------- CABECERA kodivertido_infantiles-------------##    
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/6DiJNJw.jpg" , fanart = "https://i.imgur.com/T2ikxs1.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR lime]IN[COLOR fuchsia]FAN[COLOR white]TI[COLOR lightpink]LES[/B][/COLOR]" , thumbnail = "https://i.imgur.com/6DiJNJw.jpg" , fanart = "https://i.imgur.com/T2ikxs1.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/6DiJNJw.jpg" , fanart = "https://i.imgur.com/T2ikxs1.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/6DiJNJw.jpg", fanart = "https://i.imgur.com/T2ikxs1.jpg", folder = False)

 
 
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches(url,r'(?s)EXTINF.*?name=".*?".*?logo=".*?".*?http.*?\s')
    
    for match in matches:
        patron = plugintools.find_single_match ( match , r'(?s)EXTINF.*?name="(.*?)".*?logo="(.*?)".*?(http.*?)\s' )
        title = patron[0]
        thumb = patron[1]
        url = patron[2]
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = "https://i.imgur.com/5UwkEwQ.jpg" , folder = False , isPlayable = True )
        
    
    

##-----------------kodivertido_deportes##-------------------kodivertido_deportes#-------------------#kodivertido_deportes#-----------------------------------------------------------
##-----------------kodivertido_deportes##-------------------kodivertido_deportes#-------------------#kodivertido_deportes#-----------------------------------------------------------##-----------------kodivertido_deportes##-------------------kodivertido_deportes#-------------------#kodivertido_deportes#-----------------------------------------------------------##-----------------kodivertido_deportes##-------------------kodivertido_deportes#-------------------#kodivertido_deportes#-----------------------------------------------------------##-----------------kodivertido_deportes##-------------------kodivertido_deportes#-------------------#kodivertido_deportes#-----------------------------------------------------------##-----------------kodivertido_deportes##-------------------kodivertido_deportes#-------------------#kodivertido_deportes#-----------------------------------------------------------##-----------------kodivertido_deportes##-------------------kodivertido_deportes#-------------------#kodivertido_deportes#-----------------------------------------------------------##-----------------kodivertido_deportes##-------------------kodivertido_deportes#-------------------#kodivertido_deportes#-----------------------------------------------------------##-----------------kodivertido_deportes##-------------------kodivertido_deportes#-------------------#kodivertido_deportes#-----------------------------------------------------------##-----------------kodivertido_deportes##-------------------kodivertido_deportes#-------------------#kodivertido_deportes#-----------------------------------------------------------##-----------------kodivertido_deportes##-------------------kodivertido_deportes#-------------------#kodivertido_deportes#-----------------------------------------------------------##-----------------kodivertido_deportes##-------------------kodivertido_deportes#-------------------#kodivertido_deportes#-----------------------------------------------------------

def kodivertido_deportes(params):
    
##--------- CABECERA kodivertido_deportes-------------##--------- CABECERA kodivertido_deportes-------------##--------- CABECERA kodivertido_deportes-------------##--------- CABECERA kodivertido_deportes-------------##--------- CABECERA kodivertido_deportes-------------##--------- CABECERA kodivertido_deportes-------------##--------- CABECERA kodivertido_deportes-------------##--------- CABECERA kodivertido_deportes-------------##

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/Apj1Umv.jpg" , fanart = "https://i.imgur.com/UofLWEe.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR yellow]DE[COLOR lime]POR[COLOR aqua]TES[/B][/COLOR]" , thumbnail = "https://i.imgur.com/Apj1Umv.jpg" , fanart = "https://i.imgur.com/UofLWEe.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/Apj1Umv.jpg" , fanart = "https://i.imgur.com/UofLWEe.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/Apj1Umv.jpg", fanart = "https://i.imgur.com/UofLWEe.jpg", folder = False)


    
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches(url,r'(?s)EXTINF.*?name=".*?".*?logo=".*?".*?http.*?\s')
    
    for match in matches:
        patron = plugintools.find_single_match ( match , r'(?s)EXTINF.*?name="(.*?)".*?logo="(.*?)".*?(http.*?)\s' )
        title = patron[0]
        thumb = patron[1]
        url = patron[2]
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = "https://i.imgur.com/5UwkEwQ.jpg" , folder = False , isPlayable = True )
        
        


##-----------------kodivertido_musica##-------------------kodivertido_musica#-------------------#kodivertido_musica#-----------------------------------------------------------
##-----------------kodivertido_musica##-------------------kodivertido_musica#-------------------#kodivertido_musica#-----------------------------------------------------------##-----------------kodivertido_musica##-------------------kodivertido_musica#-------------------#kodivertido_musica#-----------------------------------------------------------##-----------------kodivertido_musica##-------------------kodivertido_musica#-------------------#kodivertido_musica#-----------------------------------------------------------##-----------------kodivertido_musica##-------------------kodivertido_musica#-------------------#kodivertido_musica#-----------------------------------------------------------##-----------------kodivertido_musica##-------------------kodivertido_musica#-------------------#kodivertido_musica#-----------------------------------------------------------##-----------------kodivertido_musica##-------------------kodivertido_musica#-------------------#kodivertido_musica#-----------------------------------------------------------##-----------------kodivertido_musica##-------------------kodivertido_musica#-------------------#kodivertido_musica#-----------------------------------------------------------##-----------------kodivertido_musica##-------------------kodivertido_musica#-------------------#kodivertido_musica#-----------------------------------------------------------##-----------------kodivertido_musica##-------------------kodivertido_musica#-------------------#kodivertido_musica#-----------------------------------------------------------##-----------------kodivertido_musica##-------------------kodivertido_musica#-------------------#kodivertido_musica#-----------------------------------------------------------##-----------------kodivertido_musica##-------------------kodivertido_musica#-------------------#kodivertido_musica#-----------------------------------------------------------

def kodivertido_musica(params):
    
##--------- CABECERA kodivertido_musica-------------##--------- CABECERA kodivertido_musica-------------##--------- CABECERA kodivertido_musica-------------##--------- CABECERA kodivertido_musica-------------##--------- CABECERA kodivertido_musica-------------##--------- CABECERA kodivertido_musica-------------##--------- CABECERA kodivertido_musica-------------##--------- CABECERA kodivertido_musica-------------##    

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/dCzcyRl.jpg" , fanart = "https://i.imgur.com/Tp5r6W1.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR lime]MU[COLOR dodgerblue]SI[COLOR turquoise]CA[/B][/COLOR]" , thumbnail = "https://i.imgur.com/dCzcyRl.jpg" , fanart = "https://i.imgur.com/Tp5r6W1.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/dCzcyRl.jpg" , fanart = "https://i.imgur.com/Tp5r6W1.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/dCzcyRl.jpg", fanart = "https://i.imgur.com/Tp5r6W1.jpg", folder = False)


    
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches(url,r'(?s)EXTINF.*?name=".*?".*?logo=".*?".*?http.*?\s')
    
    for match in matches:
        patron = plugintools.find_single_match ( match , r'(?s)EXTINF.*?name="(.*?)".*?logo="(.*?)".*?(http.*?)\s' )
        title = patron[0]
        thumb = patron[1]
        url = patron[2]
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = "https://i.imgur.com/5UwkEwQ.jpg" , folder = False , isPlayable = True )

        
     

##-----------------kodivertido_cochinos##-------------------kodivertido_cochinos#-------------------#kodivertido_cochinos#-----------------------------------------------------------
##-----------------kodivertido_cochinos##-------------------kodivertido_cochinos#-------------------#kodivertido_cochinos#-----------------------------------------------------------##-----------------kodivertido_cochinos##-------------------kodivertido_cochinos#-------------------#kodivertido_cochinos#-----------------------------------------------------------##-----------------kodivertido_cochinos##-------------------kodivertido_cochinos#-------------------#kodivertido_cochinos#-----------------------------------------------------------##-----------------kodivertido_cochinos##-------------------kodivertido_cochinos#-------------------#kodivertido_cochinos#-----------------------------------------------------------##-----------------kodivertido_cochinos##-------------------kodivertido_cochinos#-------------------#kodivertido_cochinos#-----------------------------------------------------------##-----------------kodivertido_cochinos##-------------------kodivertido_cochinos#-------------------#kodivertido_cochinos#-----------------------------------------------------------##-----------------kodivertido_cochinos##-------------------kodivertido_cochinos#-------------------#kodivertido_cochinos#-----------------------------------------------------------##-----------------kodivertido_cochinos##-------------------kodivertido_cochinos#-------------------#kodivertido_cochinos#-----------------------------------------------------------##-----------------kodivertido_cochinos##-------------------kodivertido_cochinos#-------------------#kodivertido_cochinos#-----------------------------------------------------------##-----------------kodivertido_cochinos##-------------------kodivertido_cochinos#-------------------#kodivertido_cochinos#-----------------------------------------------------------##-----------------kodivertido_cochinos##-------------------kodivertido_cochinos#-------------------#kodivertido_cochinos#-----------------------------------------------------------

def kodivertido_cochinos(params):
    
##--------- CABECERA kodivertido_cochinos-------------##--------- CABECERA kodivertido_cochinos-------------##--------- CABECERA kodivertido_cochinos-------------##--------- CABECERA kodivertido_cochinos-------------##--------- CABECERA kodivertido_cochinos-------------##--------- CABECERA kodivertido_cochinos-------------##--------- CABECERA kodivertido_cochinos-------------##--------- CABECERA kodivertido_cochinos-------------##    

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/29b9UAP.jpg" , fanart = "https://i.imgur.com/mxHSw8B.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR orangered]CO[COLOR magenta]CHI[COLOR orchid]NOS[/B][/COLOR]" , thumbnail = "https://i.imgur.com/29b9UAP.jpg" , fanart = "https://i.imgur.com/mxHSw8B.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/29b9UAP.jpg" , fanart = "https://i.imgur.com/mxHSw8B.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/29b9UAP.jpg", fanart = "https://i.imgur.com/mxHSw8B.jpg", folder = False)


    
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    thumb_vacio = "https://i.imgur.com/29b9UAP.jpg"
    
    matches = plugintools.find_multiple_matches(url,r'(?s)#EXTINF:.*?,.*?\n.*?\s')
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s)#EXTINF.*?tvg-name="([^"]+).*?logo="(.*?)".*?(http.*?)\s')
        title = patron[0]
        thumb = patron[1]
        if thumb == '':
            thumb = thumb_vacio
        else: 
            thumb = thumb      
        url = patron[2]
        plugintools.add_item (action = "resolve_without_resolveurl" , title ="[B][COLOR yellow]" + title + "[/B][/COLOR]", url = url , thumbnail = thumb , fanart = "https://i.imgur.com/mxHSw8B.jpg" , folder = False , isPlayable = True )
      


 
#########################################  IPTV   ###########################################   IPTV   ###########################################   IPTV   ####################################################################################  IPTV   ###########################################   IPTV   ###########################################   IPTV   ###########################################
##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------
##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------
#########################################  IPTV   ###########################################   IPTV   ###########################################   IPTV   ####################################################################################  IPTV   ###########################################   IPTV   ###########################################   IPTV   ###########################################





##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------
##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------##-----------------kodivertido_IPTV##-------------------kodivertido_IPTV#-------------------#kodivertido_IPTV#-----------------------------------------------------------


def kodivertido_iptv(params):
    
##--------- CABECERA kodivertido_iptv-------------##--------- CABECERA kodivertido_ipv-------------##--------- CABECERA kodivertido_iptv-------------##--------- CABECERA kodivertido_iptv-------------##--------- CABECERA kodivertido_iptv-------------##--------- CABECERA kodivertido_iptv-------------##--------- CABECERA kodivertido_iptv-------------##--------- CABECERA kodivertido_iptv-------------##
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV [/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/E1eqVTq.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/E1eqVTq.jpg", fanart = "https://i.imgur.com/mdBw4t6.jpg", folder = False)

    
    plugintools.add_item(action = "iptv1" , title = "[B][COLOR white]KODI[COLOR cyan]verti[COLOR yellow]DO [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV[COLOR lime] GranQuilito [COLOR aqua]1[/B][/COLOR]" , url = "http://perillas.mendelux.es/1xyz/kodivertido/listasIPTV/quilito.txt", thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = True )
    
    
    plugintools.add_item(action = "iptv2" , title = "[B][COLOR white]KODI[COLOR cyan]verti[COLOR yellow]DO [COLOR orangered]LISTA[COLOR greenyellow]--[COLOR yellow] IPTV[COLOR lime] GranQuilito [COLOR aqua]2[/B][/COLOR]" , url = "http://perillas.mendelux.es/1xyz/kodivertido/listasIPTV/quilito2.txt", thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = True )


    plugintools.add_item(action = "iptv3" , title = "[B][COLOR white]KODI[COLOR cyan]verti[COLOR yellow]DO [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV[COLOR lime] GranQuilito [COLOR aqua]3[/B][/COLOR]" , url = "http://perillas.mendelux.es/1xyz/kodivertido/listasIPTV/quilito3.txt", thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = True )
    
    
    plugintools.add_item(action = "sansat" , title = "[B][COLOR white]KODI[COLOR cyan]verti[COLOR yellow]DO [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV[COLOR lime] 4 [COLOR cyan] Servidor [COLOR yellow]SAMSAT[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = True )
    
    
    plugintools.add_item(action = "sansat2" , title = "[B][COLOR white]KODI[COLOR cyan]verti[COLOR yellow]DO [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV[COLOR lime] 5 [COLOR cyan] Servidor [COLOR yellow]SAMSAT[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = True )
    
    
    plugintools.add_item(action = "iptv6" , title = "[B][COLOR white]KODI[COLOR cyan]verti[COLOR yellow]DO [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV[COLOR lime] 6[COLOR dodgerblue] Grupo [COLOR lime]KODIvedertiDO[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = True )
    
    
    plugintools.add_item(action = "iptv7" , title = "[B][COLOR white]KODI[COLOR cyan]verti[COLOR yellow]DO [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV[COLOR lime] 7[COLOR dodgerblue] Grupo [COLOR lime]KODIvedertiDO[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = True )
    

    plugintools.add_item(action = "iptv8" , title = "[B][COLOR white]KODI[COLOR cyan]verti[COLOR yellow]DO [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV[COLOR lime] 8[COLOR dodgerblue] Grupo [COLOR lime]KODIvedertiDO[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = True )
    
    
    plugintools.add_item(action = "iptv9" , title = "[B][COLOR white]KODI[COLOR cyan]verti[COLOR yellow]DO [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV[COLOR lime] 9[COLOR dodgerblue] Grupo [COLOR lime]KODIvedertiDO[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = True )
        
    
    plugintools.add_item(action = "iptv10" , title = "[B][COLOR white]KODI[COLOR cyan]verti[COLOR yellow]DO [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV[COLOR lime] 10[COLOR dodgerblue] Grupo [COLOR lime]KODIvedertiDO[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = True )    



##--------- CABECERA kodivertido_iptv1-------------##--------- CABECERA kodivertido_ipv1-------------##--------- CABECERA kodivertido_iptv1-------------##--------- CABECERA kodivertido_iptv1-------------##--------- CABECERA kodivertido_iptv1-------------##--------- CABECERA kodivertido_iptv1-------------##--------- CABECERA kodivertido_iptv1-------------##--------- CABECERA kodivertido_iptv1-------------##



def iptv1(params):
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV GranQuilito [COLOR aqua]1[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/E1eqVTq.jpg", fanart = "https://i.imgur.com/d3Lq6JS.jpg", folder = False)
        
    
    
    url3 = "http://perillas.mendelux.es/1xyz/kodivertido/listasIPTV/quilito.txt"
    request_headers = [ ]
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url3 , headers = request_headers )
    url = read_url.strip ( )
    
    #matches = re.findall(r'(?s)#EXTINF.*?name="([^"]+).*?logo="([^"]+).*?group-title="([^"]+).*?(http.*?)\s', url, re.DOTALL)
    matches = plugintools.find_multiple_matches(url,r'(?s)#EXTINF.*?\nhttp.*?\s')
      
         
    for match in matches:
        
        patron = plugintools.find_single_match(match, r'(?s)#EXTINF.*?tvg-id.*?group-title="([^"]+).*?,(.*?)\n(http.*?)\s')
        name = patron[0]
        grupo_canales = patron[1]
        url = patron[2]             
                
        plugintools.add_item (action = "resolve_without_resolveurl", title = "[B][COLOR yellow]" + name + "[/COLOR][/B]", url = url, thumbnail = "https://i.imgur.com/E1eqVTq.jpg", fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False , isPlayable = True )
  
  
        
##--------- CABECERA kodivertido_iptv2-------------##--------- CABECERA kodivertido_ipv2-------------##--------- CABECERA kodivertido_iptv2-------------##--------- CABECERA kodivertido_iptv2-------------##--------- CABECERA kodivertido_iptv2-------------##--------- CABECERA kodivertido_iptv2-------------##--------- CABECERA kodivertido_iptv2-------------##--------- CABECERA kodivertido_iptv2-------------##



def iptv2(params):
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV GranQuilito [COLOR aqua]2[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/E1eqVTq.jpg", fanart = "https://i.imgur.com/d3Lq6JS.jpg", folder = False)
  
              
    
    url3 = "http://perillas.mendelux.es/1xyz/kodivertido/listasIPTV/quilito2.txt"
    request_headers = [ ]
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url3 , headers = request_headers )
    url = read_url.strip ( )
    
    #matches = re.findall(r'(?s)#EXTINF.*?name="([^"]+).*?logo="([^"]+).*?group-title="([^"]+).*?(http.*?)\s', url, re.DOTALL)
    matches = plugintools.find_multiple_matches(url,r'(?s)#EXTINF.*?\nhttp.*?\s')
    grupo_canales = plugintools.find_single_match(matches,r'(?s)#EXTINF.*?group-title="([^"]+).*?\nhttp.*?\s')      
    plugintools.add_item (action = "", title = "[B][COLOR yellow]------ " + grupo_canales + " ------[/COLOR][/B]", thumbnail = "https://i.imgur.com/E1eqVTq.jpg", fanart = "https://i.imgur.com/d3Lq6JS.jpg")
         
    for match in matches:
        
        patron = plugintools.find_single_match(match, r'(?s)#EXTINF.*?tvg-logo="([^"]+).*?,(.*?)\n(http.*?)\s')
        thumb = patron[0]
        name = patron[1]
        url = patron[2]             
        plugintools.add_item (action = "resolve_without_resolveurl", title = "[B][COLOR yellow]" + name + "[/COLOR][/B]", url = url, thumbnail = thumb, fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False , isPlayable = True )



##--------- CABECERA kodivertido_iptv3-------------##--------- CABECERA kodivertido_ipv2-------------##--------- CABECERA kodivertido_iptv3-------------##--------- CABECERA kodivertido_iptv3-------------##--------- CABECERA kodivertido_iptv3-------------##--------- CABECERA kodivertido_iptv3-------------##--------- CABECERA kodivertido_iptv3-------------##--------- CABECERA kodivertido_iptv3-------------##
    

def iptv3(params):
    
    
        
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV GranQuilito [COLOR aqua]3[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/E1eqVTq.jpg", fanart = "https://i.imgur.com/d3Lq6JS.jpg", folder = False)


    
    url3 = "http://perillas.mendelux.es/1xyz/kodivertido/listasIPTV/quilito3.txt"
    request_headers = [ ]
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url3 , headers = request_headers )
    url = read_url.strip ( )
    
    #matches = re.findall(r'(?s)#EXTINF.*?name="([^"]+).*?logo="([^"]+).*?group-title="([^"]+).*?(http.*?)\s', url, re.DOTALL)
    matches = plugintools.find_multiple_matches(url,r'(?s)#EXTINF.*?\nhttp.*?\s')
    grupo_canales = plugintools.find_single_match(matches,r'(?s)#EXTINF.*?group-title="([^"]+).*?\nhttp.*?\s')      
    plugintools.add_item (action = "", title = "[B][COLOR yellow]------ " + grupo_canales + " ------[/COLOR][/B]", thumbnail = "https://i.imgur.com/E1eqVTq.jpg", fanart = "https://i.imgur.com/d3Lq6JS.jpg")
         
    for match in matches:
        
        patron = plugintools.find_single_match(match, r'(?s)#EXTINF.*?tvg-logo="([^"]+).*?,(.*?)\n(http.*?)\s')
        thumb = patron[0]
        name = patron[1]
        url = patron[2]             
        plugintools.add_item (action = "resolve_without_resolveurl", title = "[B][COLOR yellow]" + name + "[/COLOR][/B]", url = url, thumbnail = thumb, fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False , isPlayable = True )
   
    

##--------- CABECERA kodivertido_iptv4-------------##--------- CABECERA kodivertido_ipv4-------------##--------- CABECERA kodivertido_iptv4-------------##--------- CABECERA kodivertido_iptv4-------------##--------- CABECERA kodivertido_iptv4-------------##--------- CABECERA kodivertido_iptv4-------------##--------- CABECERA kodivertido_iptv4-------------##--------- CABECERA kodivertido_iptv4-------------##


def sansat(params):  
    
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV 4 [COLOR cyan] Servidor [COLOR lime]SAMSAT[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )
    


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/E1eqVTq.jpg", fanart = "https://i.imgur.com/d3Lq6JS.jpg", folder = False)

    
    categorias = []
    url = "http://sansat.net:25461/get.php?username=02023095082495&password=QUfJsvIiu1TDyDC&type=m3u_plus&output=mpegts"  
    header = []
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url.strip ()  
    matches = plugintools.find_multiple_matches(url, 'group-title="([^"]+)') 
    for categoria in sorted(matches): 
        if categoria not in categorias: 
            categorias.append(categoria)
    
    
    categorias.append("Todos")
    for x in sorted(categorias):
        plugintools . add_item ( action = "lasopciones" , title =  x , url = x, thumbnail =  params.get("thumbnail") , fanart="https://i.imgur.com/d3Lq6JS.jpg", folder = True)


def lasopciones(params):    
    categoria = params.get("title")
    url3 = "http://sansat.net:25461/get.php?username=02023095082495&password=QUfJsvIiu1TDyDC&type=m3u_plus&output=mpegts"
    request_headers = [ ]
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url3 , headers = request_headers )
    url = read_url.strip ( )
    
    #matches = re.findall(r'(?s)#EXTINF.*?name="([^"]+).*?logo="([^"]+).*?group-title="([^"]+).*?(http.*?)\s', url, re.DOTALL)
    matches = plugintools.find_multiple_matches(url,r'(?s)#EXTINF.*?name.*?logo.*?group.*?http.*?\s')
      
         
    for match in matches:
        
        patron = plugintools.find_single_match(match, r'(?s)#EXTINF.*?name="([^"]+).*?logo="(.*?)".*?group-title="([^"]+).*?(http.*?)\s')
        name = patron[0]
        thumb = patron[1]
        grupo_canales = patron[2]
        url = patron[3]             
        url2 = url.replace('sansat.net','152.89.63.250')
        
        if categoria in grupo_canales:
            plugintools.add_item (action = "resolve_without_resolveurl", title = "[B][COLOR yellow]" + name + "[/COLOR][/B]", url = url2, thumbnail = thumb, fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False , isPlayable = True )
        elif categoria == "Todos":
            plugintools.add_item (action = "resolve_without_resolveurl", title = "[B][COLOR yellow]" + name + "[/COLOR][/B]", url = url2, thumbnail = thumb, fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False , isPlayable = True )
        else:
            pass
    
    
##--------- CABECERA kodivertido_iptv5-------------##--------- CABECERA kodivertido_ipv5-------------##--------- CABECERA kodivertido_iptv5-------------##--------- CABECERA kodivertido_iptv5-------------##--------- CABECERA kodivertido_iptv5-------------##--------- CABECERA kodivertido_iptv5-------------##--------- CABECERA kodivertido_iptv5-------------##--------- CABECERA kodivertido_iptv5-------------##


def sansat2(params):  
    
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV 5 [COLOR cyan] Servidor [COLOR lime]SAMSAT[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/E1eqVTq.jpg", fanart = "https://i.imgur.com/d3Lq6JS.jpg", folder = False)

    
    categorias = []
    url = "http://sansat.net:25461/get.php?username=02027852236127&password=KSL1SnedRtLQnsZ&type=m3u_plus&output=mpegts"  
    header = []
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url.strip ()  
    matches = plugintools.find_multiple_matches(url, 'group-title="([^"]+)') 
    for categoria in sorted(matches): 
        if categoria not in categorias: 
            categorias.append(categoria)
    
    
    categorias.append("Todos")
    for x in sorted(categorias):
        plugintools . add_item ( action = "lasopciones2" , title =  x , url = x, thumbnail =  params.get("thumbnail") , fanart="https://i.imgur.com/d3Lq6JS.jpg", folder = True)


def lasopciones2(params):    
    categoria = params.get("title")
    url3 = "http://sansat.net:25461/get.php?username=02027852236127&password=KSL1SnedRtLQnsZ&type=m3u_plus&output=mpegts"
    request_headers = [ ]
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url3 , headers = request_headers )
    url = read_url.strip ( )
    
    matches = re.findall(r'(?s)#EXTINF.*?name="([^"]+).*?logo="(.*?)".*?group-title="([^"]+).*?(http.*?)\s', url, re.DOTALL)
    #matches = plugintools.find_multiple_matches(url,r'(?s)#EXTINF.*?name.*?logo.*?group.*?http.*?\s')
      
    for name, thumb, grupo_canales, url in matches:     
    #for match in matches:
        
        #patron = plugintools.find_single_match(match, r'(?s)#EXTINF.*?name="([^"]+).*?logo="(.*?)".*?group-title="([^"]+).*?(http.*?)\s')
        #name = patron[0]
        #thumb = patron[1]
        #grupo_canales = patron[2]
        #url = patron[3]             
        url2 = url.replace('sansat.net','152.89.63.250')
        
        if categoria in grupo_canales:
            plugintools.add_item (action = "resolve_without_resolveurl", title = "[B][COLOR yellow]" + name + "[/COLOR][/B]", url = url2, thumbnail = thumb, fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False , isPlayable = True )
        elif categoria == "Todos":
            plugintools.add_item (action = "resolve_without_resolveurl", title = "[B][COLOR yellow]" + name + "[/COLOR][/B]", url = url2, thumbnail = thumb, fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False , isPlayable = True )
        else:
            pass
 
   
##--------- CABECERA kodivertido_iptv6-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_ipv6-------------##--------- CABECERA kodivertido_iptv6-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv6-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv6-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv6-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv6-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv6-GrupoKODIvertiDO-------------##


def iptv6(params):  
    
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV 6 [COLOR blue] Grupo [COLOR lime]KODIvedertiDO[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/E1eqVTq.jpg", fanart = "https://i.imgur.com/d3Lq6JS.jpg", folder = False)

    
    categorias = []
    url = "http://perillas.mendelux.es/1xyz/kodivertido/listasIPTV/joseangel_adril_1.m3u"  
    header = []
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url.strip ()  
    matches = plugintools.find_multiple_matches(url, 'group-title="([^"]+)') 
    for categoria in sorted(matches): 
        if categoria not in categorias: 
            categorias.append(categoria)
    
    
    categorias.append("Todos")
    for x in sorted(categorias):
        plugintools . add_item ( action = "lasopciones3" , title =  x , url = x, thumbnail =  params.get("thumbnail") , fanart="https://i.imgur.com/d3Lq6JS.jpg", folder = True)


def lasopciones3(params):    
    categoria = params.get("title")
    url3 = "http://perillas.mendelux.es/1xyz/kodivertido/listasIPTV/joseangel_adril_1.m3u"
    request_headers = [ ]
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url3 , headers = request_headers )
    url = read_url.strip ( )
    
    matches = re.findall(r'(?s)#EXTINF.*?name="([^"]+).*?logo="(.*?)".*?group-title="([^"]+).*?(http.*?)\s', url, re.DOTALL)
    #matches = plugintools.find_multiple_matches(url,r'(?s)#EXTINF.*?name.*?logo.*?group.*?http.*?\s')
      
    for name, thumb, grupo_canales, url in matches:     
    #for match in matches:
        
        #patron = plugintools.find_single_match(match, r'(?s)#EXTINF.*?name="([^"]+).*?logo="(.*?)".*?group-title="([^"]+).*?(http.*?)\s')
        #name = patron[0]
        #thumb = patron[1]
        #grupo_canales = patron[2]
        #url = patron[3]             
        url2 = url.replace('sansat.net','152.89.63.250')
        
        if categoria in grupo_canales:
            plugintools.add_item (action = "resolve_without_resolveurl", title = "[B][COLOR yellow]" + name + "[/COLOR][/B]", url = url2, thumbnail = thumb, fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False , isPlayable = True )
        elif categoria == "Todos":
            plugintools.add_item (action = "resolve_without_resolveurl", title = "[B][COLOR yellow]" + name + "[/COLOR][/B]", url = url2, thumbnail = thumb, fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False , isPlayable = True )
        else:
            pass



##--------- CABECERA kodivertido_iptv7-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_ipv7-------------##--------- CABECERA kodivertido_iptv7-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv7-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv7-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv7-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv7-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv7-GrupoKODIvertiDO-------------##


def iptv7(params):  
    
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV 7 [COLOR blue] Grupo [COLOR lime]KODIvedertiDO[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/E1eqVTq.jpg", fanart = "https://i.imgur.com/d3Lq6JS.jpg", folder = False)

    
    categorias = []
    url = "http://perillas.mendelux.es/1xyz/kodivertido/listasIPTV/joseandrl_abril2.m3u"  
    header = []
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url.strip ()  
    matches = plugintools.find_multiple_matches(url, 'group-title="([^"]+)') 
    for categoria in sorted(matches): 
        if categoria not in categorias: 
            categorias.append(categoria)
    
    
    categorias.append("Todos")
    for x in sorted(categorias):
        plugintools . add_item ( action = "lasopciones4" , title =  x , url = x, thumbnail =  params.get("thumbnail") , fanart="https://i.imgur.com/d3Lq6JS.jpg", folder = True)


def lasopciones4(params):    
    categoria = params.get("title")
    url3 = "http://perillas.mendelux.es/1xyz/kodivertido/listasIPTV/joseandrl_abril2.m3u"
    request_headers = [ ]
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url3 , headers = request_headers )
    url = read_url.strip ( )
    
    matches = re.findall(r'(?s)#EXTINF.*?name="([^"]+).*?logo="(.*?)".*?group-title="([^"]+).*?(http.*?)\s', url, re.DOTALL)
    #matches = plugintools.find_multiple_matches(url,r'(?s)#EXTINF.*?name.*?logo.*?group.*?http.*?\s')
      
    for name, thumb, grupo_canales, url in matches:     
    #for match in matches:
        
        #patron = plugintools.find_single_match(match, r'(?s)#EXTINF.*?name="([^"]+).*?logo="(.*?)".*?group-title="([^"]+).*?(http.*?)\s')
        #name = patron[0]
        #thumb = patron[1]
        #grupo_canales = patron[2]
        #url = patron[3]             
        url2 = url.replace('sansat.net','152.89.63.250')
        
        if categoria in grupo_canales:
            plugintools.add_item (action = "resolve_without_resolveurl", title = "[B][COLOR yellow]" + name + "[/COLOR][/B]", url = url2, thumbnail = thumb, fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False , isPlayable = True )
        elif categoria == "Todos":
            plugintools.add_item (action = "resolve_without_resolveurl", title = "[B][COLOR yellow]" + name + "[/COLOR][/B]", url = url2, thumbnail = thumb, fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False , isPlayable = True )
        else:
            pass


##--------- CABECERA kodivertido_iptv8-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv8-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv8-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv8-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv8-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv8-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv8-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv8-GrupoKODIvertiDO-------------##


def iptv8(params):  
    
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV 8 [COLOR blue] Grupo [COLOR lime]KODIvedertiDO[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/E1eqVTq.jpg", fanart = "https://i.imgur.com/d3Lq6JS.jpg", folder = False)

    
    categorias = []
    url = "http://perillas.mendelux.es/1xyz/kodivertido/listasIPTV/joseangel_abril3.m3u"  
    header = []
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url.strip ()  
    matches = plugintools.find_multiple_matches(url, 'group-title="([^"]+)') 
    for categoria in sorted(matches): 
        if categoria not in categorias: 
            categorias.append(categoria)
    
    
    categorias.append("Todos")
    for x in sorted(categorias):
        plugintools . add_item ( action = "lasopciones5" , title =  x , url = x, thumbnail =  params.get("thumbnail") , fanart="https://i.imgur.com/d3Lq6JS.jpg", folder = True)


def lasopciones5(params):    
    categoria = params.get("title")
    url3 = "http://perillas.mendelux.es/1xyz/kodivertido/listasIPTV/joseangel_abril3.m3u"
    request_headers = [ ]
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url3 , headers = request_headers )
    url = read_url.strip ( )
    
    matches = re.findall(r'(?s)#EXTINF.*?name="([^"]+).*?logo="(.*?)".*?group-title="([^"]+).*?(http.*?)\s', url, re.DOTALL)
    #matches = plugintools.find_multiple_matches(url,r'(?s)#EXTINF.*?name.*?logo.*?group.*?http.*?\s')
      
    for name, thumb, grupo_canales, url in matches:     
    #for match in matches:
        
        #patron = plugintools.find_single_match(match, r'(?s)#EXTINF.*?name="([^"]+).*?logo="(.*?)".*?group-title="([^"]+).*?(http.*?)\s')
        #name = patron[0]
        #thumb = patron[1]
        #grupo_canales = patron[2]
        #url = patron[3]             
        url2 = url.replace('sansat.net','152.89.63.250')
        
        if categoria in grupo_canales:
            plugintools.add_item (action = "resolve_without_resolveurl", title = "[B][COLOR yellow]" + name + "[/COLOR][/B]", url = url2, thumbnail = thumb, fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False , isPlayable = True )
        elif categoria == "Todos":
            plugintools.add_item (action = "resolve_without_resolveurl", title = "[B][COLOR yellow]" + name + "[/COLOR][/B]", url = url2, thumbnail = thumb, fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False , isPlayable = True )
        else:
            pass


##--------- CABECERA kodivertido_iptv9-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv9-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv9-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv9-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv9-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv9-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv9-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv9-GrupoKODIvertiDO-------------##


def iptv9(params):
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV 9 [COLOR blue] Grupo [COLOR lime]KODIvedertiDO[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/E1eqVTq.jpg", fanart = "https://i.imgur.com/d3Lq6JS.jpg", folder = False)
    
    
    url = "http://perillas.mendelux.es/1xyz/kodivertido/listasIPTV/tv_channels_xuan.m3u"
    request_headers = [ ]
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ( )
    
    matches = re.findall(r'(?s)#EXTINF.*?,(.*?)\n.*?(.*?)\s', url, re.DOTALL)
    
    for name, url in matches:  
        plugintools.add_item (action = "resolve_without_resolveurl", title = "[B][COLOR yellow]" + name + "[/COLOR][/B]", url = url, thumbnail = "https://i.imgur.com/wn3vGhZ.jpg", fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False , isPlayable = True )
        
    
##--------- CABECERA kodivertido_iptv10-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv10-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv10-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv10-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv10-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv10-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv10-GrupoKODIvertiDO-------------##--------- CABECERA kodivertido_iptv10-GrupoKODIvertiDO-------------##


def iptv10(params):  
    
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR orangered]LISTA[COLOR yellow]--[COLOR greenyellow] IPTV 10 [COLOR blue] Grupo [COLOR lime]KODIvedertiDO[/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/E1eqVTq.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/E1eqVTq.jpg", fanart = "https://i.imgur.com/d3Lq6JS.jpg", folder = False)

    
    categorias = []
    url = "http://client-urostream.club/get.php?username=yass&password=yass&type=m3u_plus"  
    header = []
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url.strip ()  
    matches = plugintools.find_multiple_matches(url, 'group-title="([^"]+)') 
    for categoria in sorted(matches): 
        if categoria not in categorias: 
            categorias.append(categoria)
    
    
    categorias.append("Todos")
    for x in sorted(categorias):
        plugintools . add_item ( action = "iptv10_canales" , title =  x , url = x, thumbnail =  params.get("thumbnail") , fanart="https://i.imgur.com/d3Lq6JS.jpg", folder = True)


def iptv10_canales(params):    
    categoria = params.get("title")
    url3 = "http://client-urostream.club/get.php?username=yass&password=yass&type=m3u_plus"
    request_headers = [ ]
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url3 , headers = request_headers )
    url = read_url.strip ( )
    
    matches = re.findall(r'(?s)#EXTINF.*?name="([^"]+).*?logo="(.*?)".*?group-title="([^"]+).*?(http.*?)\s', url, re.DOTALL)
    #matches = plugintools.find_multiple_matches(url,r'(?s)#EXTINF.*?name.*?logo.*?group.*?http.*?\s')
      
    for name, thumb, grupo_canales, url in matches:     
    #for match in matches:
        
        #patron = plugintools.find_single_match(match, r'(?s)#EXTINF.*?name="([^"]+).*?logo="(.*?)".*?group-title="([^"]+).*?(http.*?)\s')
        #name = patron[0]
        #thumb = patron[1]
        #grupo_canales = patron[2]
        #url = patron[3]             
        url2 = url.replace('sansat.net','152.89.63.250')
        
        if categoria in grupo_canales:
            plugintools.add_item (action = "resolve_without_resolveurl", title = "[B][COLOR yellow]" + name + "[/COLOR][/B]", url = url2, thumbnail = thumb, fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False , isPlayable = True )
        elif categoria == "Todos":
            plugintools.add_item (action = "resolve_without_resolveurl", title = "[B][COLOR yellow]" + name + "[/COLOR][/B]", url = url2, thumbnail = thumb, fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False , isPlayable = True )
        else:
            pass



#plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=NAME&amp;url=urllib.quote_plus(URL)

#########################################  CINE   ###########################################   CINE   ###########################################   CINE   ####################################################################################  CINE   ###########################################   CINE   ###########################################   CINE   ###########################################
##-----------------kodivertido_CINE##-------------------kodivertido_CINE#-------------------#kodivertido_CINE#-----------------------------------------------------------
##-----------------kodivertido_CINE##-------------------kodivertido_CINE#-------------------#kodivertido_CINE#-----------------------------------------------------------##-----------------kodivertido_CINE##-------------------kodivertido_CINE#-------------------#kodivertido_CINE#-----------------------------------------------------------##-----------------kodivertido_CINE##-------------------kodivertido_CINE#-------------------#kodivertido_CINE#-----------------------------------------------------------##-----------------kodivertido_CINE##-------------------kodivertido_CINE#-------------------#kodivertido_CINE#-----------------------------------------------------------##-----------------kodivertido_CINE##-------------------kodivertido_CINE#-------------------#kodivertido_CINE#-----------------------------------------------------------##-----------------kodivertido_CINE##-------------------kodivertido_CINE#-------------------#kodivertido_CINE#-----------------------------------------------------------##-----------------kodivertido_CINE##-------------------kodivertido_CINE#-------------------#kodivertido_CINE#-----------------------------------------------------------##-----------------kodivertido_CINE##-------------------kodivertido_CINE#-------------------#kodivertido_CINE#-----------------------------------------------------------##-----------------kodivertido_CINE##-------------------kodivertido_CINE#-------------------#kodivertido_CINE#-----------------------------------------------------------##-----------------kodivertido_CINE##-------------------kodivertido_CINE#-------------------#kodivertido_CINE#-----------------------------------------------------------##-----------------kodivertido_CINE##-------------------kodivertido_CINE#-------------------#kodivertido_CINE#-----------------------------------------------------------
#########################################  CINE   ###########################################   CINE   ###########################################   CINE   ####################################################################################  CINE   ###########################################   CINE   ###########################################   CINE   ###########################################







##-----------------grantorrent##-------------------grantorrent#-------------------#grantorrent#-----------------------------------------------------------
##-----------------grantorrent##-------------------grantorrent#-------------------#grantorrent#-----------------------------------------------------------##-----------------grantorrent##-------------------grantorrent#-------------------#grantorrent#-----------------------------------------------------------##-----------------grantorrent##-------------------grantorrent#-------------------#grantorrent#-----------------------------------------------------------##-----------------grantorrent##-------------------grantorrent#-------------------#grantorrent#-----------------------------------------------------------##-----------------grantorrent##-------------------grantorrent#-------------------#grantorrent#-----------------------------------------------------------##-----------------grantorrent##-------------------grantorrent#-------------------#grantorrent#-----------------------------------------------------------##-----------------grantorrent##-------------------grantorrent#-------------------#grantorrent#-----------------------------------------------------------##-----------------grantorrent##-------------------grantorrent#-------------------#grantorrent#-----------------------------------------------------------##-----------------grantorrent##-------------------grantorrent#-------------------#grantorrent#-----------------------------------------------------------##-----------------grantorrent##-------------------grantorrent#-------------------#grantorrent#-----------------------------------------------------------##-----------------grantorrent##-------------------grantorrent#-------------------#grantorrent#-----------------------------------------------------------


def grantorrent(params):

    ##--------- CABECERA grantorrent-------------##--------- CABECERA grantorrent-------------##--------- CABECERA grantorrent-------------##--------- CABECERA grantorrent-------------##--------- CABECERA grantorrent-------------##--------- CABECERA grantorrent-------------##--------- CABECERA grantorrent-------------##--------- CABECERA grantorrent-------------##

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/uWqZDRQ.jpg" , fanart = "https://i.imgur.com/YTrtjLD.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR gold]GRANTORRENT[/B][/COLOR]" , thumbnail = "https://i.imgur.com/uWqZDRQ.jpg" , fanart = "https://i.imgur.com/YTrtjLD.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/uWqZDRQ.jpg" , fanart = "https://i.imgur.com/YTrtjLD.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "", thumbnail ="https://i.imgur.com/uWqZDRQ.jpg", fanart = "https://i.imgur.com/YTrtjLD.jpg",  folder = False )




    

    plugintools.add_item(action = "hdrip" , title = "[B][COLOR yellow]" + "Grantorrent HDRip" + "[/B][/COLOR]" , thumbnail = "https://i.imgur.com/uWqZDRQ.jpg" , url = "https://grantorrent.nl/categoria/HDRip-2/" , fanart = "https://i.ytimg.com/vi/7D82gt558g4/maxresdefault.jpg" , folder = True )


    plugintools.add_item(action = "blueray" , title = "[B][COLOR yellow]" + "Grantorrent Bluray-1080p" + "[/B][/COLOR]" , thumbnail = "https://i.imgur.com/uWqZDRQ.jpg" , url = "https://grantorrent.nl/categoria/BluRay-1080p/" , fanart = "https://i.ytimg.com/vi/7D82gt558g4/maxresdefault.jpg" , folder = True )


    plugintools.add_item(action = "cuatrok" , title = "[B][COLOR yellow]" + "Grantorrent 4K" + "[/B][/COLOR]" , thumbnail = "https://i.imgur.com/uWqZDRQ.jpg" , url = "https://grantorrent.nl/categoria/4k-2/" , fanart = "https://i.ytimg.com/vi/7D82gt558g4/maxresdefault.jpg" , folder = True )


    plugintools.add_item(action = "grantorrent_search" , title = "[B][COLOR yellow]" + "Buscar" + "[/B][/COLOR]" , thumbnail = "https://i.imgur.com/uWqZDRQ.jpg" , url = "https://grantorrent.nl/?s=" , fanart = "https://i.ytimg.com/vi/7D82gt558g4/maxresdefault.jpg" , folder = True )


######################  hdrip  ######################  hdrip  ######################  hdrip  ######################  hdrip  ######################  hdrip  ############################################  hdrip  ######################  hdrip  ######################  hdrip  ######################  hdrip  ######################  hdrip  ######################


def hdrip(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    
    matches = plugintools.find_multiple_matches(url,'(?s)class="imagen-post".*?href=".*?".*?lazy-src=".*?".*?inferior">..*?<')              
    next = plugintools.find_single_match ( url , '<link rel="next" href="([^"]+)"' )
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s)class="imagen-post".*?href="(.*?)".*?lazy-src="(.*?)".*?inferior">.(.*?)<')
        url = patron[0]  
        title = patron[2]
        thumb = patron[1]
        plugintools.add_item ( action = "hdrip1" , title = title , thumbnail = thumb , url = url , fanart = thumb , folder = True )
    plugintools.add_item ( action = "hdrip" , title = "[B][COLOR lime]" + "PAGINA SIGUIENTE" + "[/B][/COLOR]" , url = next , thumbnail = "https://i.imgur.com/cfwdN1c.jpg" , folder = True )
    
    
def hdrip1(params):
    url = params.get ( "url" )
    thumb = params.get ( "thumbnail" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    
    matches = plugintools.find_multiple_matches(url,'(?s)<tr class="lol">.*?\}')
    plot =  plugintools.find_single_match(url,'(?s)active"><p>(.*?)<' )
    for match in matches:
        idioma = plugintools.find_single_match(match, r'(?s)<tr class="lol">.*?title="([^"]+)')
        calidad = plugintools.find_single_match(match, r'(?s)<tr class="lol">.*?lazy-src=.*?<td>(.*?)<')
        peso = plugintools.find_single_match(match, r'(?s)<tr class="lol">.*?lazy-src=.*?<td>.*?<.*?<td>(.*?)<')
        url = plugintools.find_single_match(match, r"(?s)<tr class=.*?>.*?u:.*?'(.*?)'")
        plugintools.add_item ( action = "link" , title = idioma + " " + calidad + " " + peso , thumbnail = thumb , url = url , fanart = thumb , plot = plot )
        
    
#    matches = re.findall ( r'(?s).*?<noscript><img src="([^"]+)".*?class="page">(.*?)<.*?class="tabcontent.*?<p>(.*?)<|.*?</td><td>(.*?)</td><td>(.*?)<.*?u=(.*?)"' , url , re.DOTALL )  #(?s).*?<title>(.*?)<|.*?<\/td><td>(.*?)<\/td><td>(.*?)<.*?href.*?u=(.*?)"
#    for thumb , title , info , calidad , tam , url in matches:
#        plugintools.add_item ( action = "link" , title = title + calidad + tam , thumbnail = thumb , url = url , plot = info , fanart = thumb , folder = True , isPlayable = True ) 
        #xbmc.log(url, xbmc.LOGINFO)          
        

######################  blueray  ######################  blueray  ######################  blueray  ######################  blueray  ######################  blueray  ######################


def blueray(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    
    matches = plugintools.find_multiple_matches(url,'(?s)class="imagen-post".*?href=".*?".*?lazy-src=".*?".*?inferior">..*?<')              
    next = plugintools.find_single_match ( url , '<link rel="next" href="([^"]+)"' )
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s)class="imagen-post".*?href="(.*?)".*?lazy-src="(.*?)".*?inferior">.(.*?)<')
        url = patron[0]  
        title = patron[2]
        thumb = patron[1]
        plugintools.add_item ( action = "blueray1" , title = title , thumbnail = thumb , url = url , fanart = thumb , folder = True )
    plugintools.add_item ( action = "blueray" , title = "[B][COLOR lime]" + "PAGINA SIGUIENTE" + "[/B][/COLOR]" , url = next , thumbnail = "https://i.imgur.com/cfwdN1c.jpg" , folder = True )


def blueray1(params):
    url = params.get ( "url" )
    thumb = params.get ( "thumbnail" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
     
    matches = plugintools.find_multiple_matches(url,'(?s)<tr class="lol">.*?\}')
    plot =  plugintools.find_single_match(url,'(?s)active"><p>(.*?)<' )
    for match in matches:
        idioma = plugintools.find_single_match(match, r'(?s)<tr class="lol">.*?title="([^"]+)')
        calidad = plugintools.find_single_match(match, r'(?s)<tr class="lol">.*?lazy-src=.*?<td>(.*?)<')
        peso = plugintools.find_single_match(match, r'(?s)<tr class="lol">.*?lazy-src=.*?<td>.*?<.*?<td>(.*?)<')
        url = plugintools.find_single_match(match, r"(?s)<tr class=.*?>.*?u:.*?'(.*?)'")
        plugintools.add_item ( action = "link" , title = idioma + " " + calidad + " " + peso , thumbnail = thumb , url = url , fanart = thumb , plot = plot )

######################  cuatrok  ######################  cuatrok  ######################  cuatrok  ######################  cuatrok  ######################  cuatrok  ######################


def cuatrok(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    
    matches = plugintools.find_multiple_matches(url,'(?s)class="imagen-post".*?href=".*?".*?lazy-src=".*?".*?inferior">..*?<')              
    next = plugintools.find_single_match ( url , '<link rel="next" href="([^"]+)"' )
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s)class="imagen-post".*?href="(.*?)".*?lazy-src="(.*?)".*?inferior">.(.*?)<')
        url = patron[0]  
        title = patron[2]
        thumb = patron[1]
        plugintools.add_item ( action = "cuatrok1" , title = title , thumbnail = thumb , url = url , fanart = thumb , folder = True )
    plugintools.add_item ( action = "cuatrok" , title = "[B][COLOR lime]" + "PAGINA SIGUIENTE" + "[/B][/COLOR]" , url = next , thumbnail = "https://i.imgur.com/cfwdN1c.jpg" , folder = True )


def cuatrok1(params):
    url = params.get ( "url" )
    thumb = params.get ( "thumbnail" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
     
    matches = plugintools.find_multiple_matches(url,'(?s)<tr class="lol">.*?\}')
    plot =  plugintools.find_single_match(url,'(?s)active"><p>(.*?)<' )
    for match in matches:
        idioma = plugintools.find_single_match(match, r'(?s)<tr class="lol">.*?title="([^"]+)')
        calidad = plugintools.find_single_match(match, r'(?s)<tr class="lol">.*?lazy-src=.*?<td>(.*?)<')
        peso = plugintools.find_single_match(match, r'(?s)<tr class="lol">.*?lazy-src=.*?<td>.*?<.*?<td>(.*?)<')
        url = plugintools.find_single_match(match, r"(?s)<tr class=.*?>.*?u:.*?'(.*?)'")
        plugintools.add_item ( action = "link" , title = idioma + " " + calidad + " " + peso , thumbnail = thumb , url = url , fanart = thumb , plot = plot )
        
        
######################  grantorrent_search  ######################  grantorrent_search  ######################  grantorrent_search  ######################  grantorrent_search  ######################  grantorrent_search  ######################        


def grantorrent_search(params):
    url = params.get ( "url" ) + keyboard_input ( "" , "Buscar:" , False ).replace ( " " , "+" )
    url = requests.get ( url ).text
    matches = re.findall ( r'(?s)class="imagen.*?href="(.*?nl/(.*?)/)".*?data-lazy-src="([^"]+)' , url , re.DOTALL )
    next = plugintools.find_single_match ( url , '(?s)<div class="nav-links">.*?next page-numbers" href="([^"]+)"' )
    for url , title , thumb in matches:
        plugintools.add_item ( action = "hdrip1" , title ="[B][COLOR yellow]" + title + "[/B][/COLOR]", thumbnail = thumb , url = url , fanart = thumb ,
            folder = True )
    plugintools.add_item ( action = "hdrip" , title = "[B][COLOR lime]" + "PAGINA SIGUIENTE" + "[/B][/COLOR]" , url = next ,
        thumbnail = "https://i.imgur.com/cfwdN1c.jpg" , folder = True )        

#####################  REPRODUCTOR DE GRANTORRENT ##############


def link(params):
    import re, six, base64
    url = params.get ( "url" )   
    #url = (base64.b64decode(url).decode("utf-8"))
    url = (base64.b64decode(url.encode("utf-8", "strict"))).decode("utf-8", "strict")
    plugintools.add_item ( action = "elementum" , title = "[B][COLOR lime]REPRODUCIR" + "[/COLOR][/B]" , url = url , thumbnail = "https://i.imgur.com/1VJQ5Qp.jpg" ,folder = False , isPlayable = True )



##-----------------cine_pctfenix##-------------------cine_pctfenix#-------------------#cine_pctfenix#-----------------------------------------------------------
##-----------------cine_pctfenix##-------------------cine_pctfenix#-------------------#cine_pctfenix#-----------------------------------------------------------##-----------------cine_pctfenix##-------------------cine_pctfenix#-------------------#cine_pctfenix#-----------------------------------------------------------##-----------------cine_pctfenix##-------------------cine_pctfenix#-------------------#cine_pctfenix#-----------------------------------------------------------##-----------------cine_pctfenix##-------------------cine_pctfenix#-------------------#cine_pctfenix#-----------------------------------------------------------##-----------------cine_pctfenix##-------------------cine_pctfenix#-------------------#cine_pctfenix#-----------------------------------------------------------##-----------------cine_pctfenix##-------------------cine_pctfenix#-------------------#cine_pctfenix#-----------------------------------------------------------##-----------------cine_pctfenix##-------------------cine_pctfenix#-------------------#cine_pctfenix#-----------------------------------------------------------##-----------------cine_pctfenix##-------------------cine_pctfenix#-------------------#cine_pctfenix#-----------------------------------------------------------##-----------------cine_pctfenix##-------------------cine_pctfenix#-------------------#cine_pctfenix#-----------------------------------------------------------##-----------------cine_pctfenix##-------------------cine_pctfenix#-------------------#cine_pctfenix#-----------------------------------------------------------##-----------------cine_pctfenix##-------------------cine_pctfenix#-------------------#cine_pctfenix#-----------------------------------------------------------


def cine_pctfenix(params):

    ##--------- CABECERA cine_pctfenix-------------##--------- CABECERA cine_pctfenix-------------##--------- CABECERA cine_pctfenix-------------##--------- CABECERA cine_pctfenix-------------##--------- CABECERA cine_pctfenix-------------##--------- CABECERA cine_pctfenix-------------##--------- CABECERA cine_pctfenix-------------##--------- CABECERA cine_pctfenix-------------##

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/594d676.jpg" , fanart = "https://i.imgur.com/594d676.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR springgreen]PCTFENIX[/B][/COLOR]" , thumbnail = "https://i.imgur.com/594d676.jpg" , fanart = "https://i.imgur.com/594d676.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/594d676.jpg" , fanart = "https://i.imgur.com/594d676.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "", thumbnail ="https://i.imgur.com/594d676.jpg", fanart = "https://i.imgur.com/594d676.jpg",  folder = False )




    plugintools.add_item(action = "fullbluray_1080p" , title="PCTFenix FullBluRay-1080p", thumbnail = "https://i.imgur.com/594d676.jpg" , url = "https://pctfenix.com/descargar-peliculas/fullbluray-1080p/" , fanart = "https://i.imgur.com/594d676.jpg" , folder = True )


    plugintools.add_item(action = "bluray_1080p" , title = "PCTFenix BluRay-1080p" , thumbnail = "https://i.imgur.com/maslpiV.jpg" , url = "https://pctfenix.com/descargar-peliculas/bluray-1080p/" , fanart = "https://i.imgur.com/maslpiV.jpg" , folder = True )


    plugintools.add_item(action = "dbremux_1080p" ,  title= "PCTFenix DBremux-1080p" , thumbnail = "https://i.imgur.com/maslpiV.jpg" , url = "https://pctfenix.com/descargar-peliculas/bdremux-1080p/" , fanart = "https://i.imgur.com/maslpiV.jpg" , folder = True )


    plugintools.add_item(action = "cuatrok_uhdremux" , title = "PCTFenix 4k-UHDremux" , thumbnail = "https://i.imgur.com/maslpiV.jpg" , url = "https://pctfenix.com/descargar-peliculas/4k-uhdremux/" , fanart = "https://i.imgur.com/maslpiV.jpg" , folder = True )


    plugintools.add_item(action = "cuatrok_uhdmicro" , title = "PCTFenix 4k-UHDmicro" , thumbnail = "https://i.imgur.com/maslpiV.jpg" , url = "https://pctfenix.com/descargar-peliculas/4k-uhdmicro/" , fanart = "https://i.imgur.com/maslpiV.jpg" , folder = True )


    plugintools.add_item(action = "cuatrok_uhdrip" , title = "PCTFenix 4k-UHDrip" , thumbnail = "https://i.imgur.com/maslpiV.jpg" , url = "https://pctfenix.com/descargar-peliculas/4k-uhdrip/" , fanart = "https://i.imgur.com/maslpiV.jpg" , folder = True )


    plugintools.add_item(action = "cuatrok_webrip" , title = "PCTFenix 4k-WEBrip" , thumbnail = "https://i.imgur.com/maslpiV.jpg" , url = "https://pctfenix.com/descargar-peliculas/4k-webrip/" , fanart = "https://i.imgur.com/maslpiV.jpg" , folder = True )


    plugintools.add_item(action = "full_uhdcuatrok" , title = "PCTFenix Full-UHD4K" , thumbnail = "https://i.imgur.com/maslpiV.jpg" , url = "https://pctfenix.com/descargar-peliculas/full-uhd4k/" , fanart = "https://i.imgur.com/maslpiV.jpg" , folder = True )


    plugintools.add_item(action = "microhd_1080p" , title = "PCTFenix MicroHD-1080p" , thumbnail = "https://i.imgur.com/maslpiV.jpg" , url = "https://pctfenix.com/descargar-peliculas/microhd-1080p/" , fanart = "https://i.imgur.com/maslpiV.jpg" , folder = True )




######################  fullbluray_1080p  ######################  fullbluray_1080p  ######################  fullbluray_1080p  ######################  fullbluray_1080p  ######################  fullbluray_1080p  ######################

def fullbluray_1080p(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches(url,r'(?s).*?<div class="mv-img">.*?<img src="[^"]+.*?="[^"]+.*?href="[^"]+')
     
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s).*?<div class="mv-img">.*?<img src="([^"]+).*?="([^"]+).*?href="([^"]+)')
        thumb = patron[0]  
        title = patron[1]
        url = patron[2]
        plugintools.add_item (action = "fullbluray_1080p1" , title ="[B][COLOR gold]" + title + "[/B][/COLOR]" , url = url , thumbnail = (("https:") + thumb) , folder = True )


def fullbluray_1080p1(params):
    url = (("https://pctfenix.com" + params.get ( "url" )))
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    matches = plugintools.find_multiple_matches(url,'ctn-download-.*?data-ut=.*?title')
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"')
        title = patron[0]  
        url = patron[1]
        plugintools.add_item (action = "elementum_pctfenix1" , title = "[B][COLOR darkorange]" + title + "[/B][/COLOR]" , url = url , folder = False , isPlayable = True )


######################  bluray_1080p  ######################  bluray_1080p  ######################  bluray_1080p  ######################  bluray_1080p  ######################  bluray_1080p  ######################


def bluray_1080p(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches(url,r'(?s)<div class="mv-img">.*?</a>\n</div>')
     
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s).*?<div class="mv-img">\n<img src="([^"]+)".*?="([^"]+)".*?a href="([^"]+)"')
        thumb = patron[0]  
        title = patron[1]
        url = patron[2]
        plugintools.add_item (action = "bluray_1080p1" , title = "[B][COLOR gold]" + title + "[/B][/COLOR]" , url = url , thumbnail = (("https:") + thumb) , folder = True )


def bluray_1080p1(params):
    url = (("https://pctfenix.com" + params.get ( "url" )))
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    matches = plugintools.find_multiple_matches(url,'ctn-download-.*?data-ut=.*?title')
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"')
        title = patron[0]  
        url = patron[1]
        plugintools.add_item (action = "elementum_pctfenix1" , title = "[B][COLOR darkorange]" + title + "[/B][/COLOR]" , url = url , folder = False , isPlayable = True )


######################  bluray_1080p  ######################  bluray_1080p  ######################  bluray_1080p  ######################  bluray_1080p  ######################  bluray_1080p  ######################


def dbremux_1080p(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches(url,r'(?s)<div class="mv-img">.*?</a>\n</div>')
     
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s).*?<div class="mv-img">\n<img src="([^"]+)".*?="([^"]+)".*?a href="([^"]+)"')
        thumb = patron[0]  
        title = patron[1]
        url = patron[2]
        plugintools.add_item (action = "dbremux_1080p1" , title = "[B][COLOR gold]" + title + "[/B][/COLOR]" , url = url , thumbnail = (("https:") + thumb) , folder = True )


def dbremux_1080p1(params):
    url = (("https://pctfenix.com" + params.get ( "url" )))
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    matches = plugintools.find_multiple_matches(url,'ctn-download-.*?data-ut=.*?title')
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"')
        title = patron[0]  
        url = patron[1]
        plugintools.add_item (action = "elementum_pctfenix1" , title = "[B][COLOR darkorange]" + title + "[/B][/COLOR]" , url = url , folder = False , isPlayable = True )
        
        
######################  cuatrok_uhdremux  ######################  cuatrok_uhdremux  ######################  cuatrok_uhdremux  ######################  cuatrok_uhdremux  ######################  cuatrok_uhdremux  ######################


def cuatrok_uhdremux(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches(url,r'(?s)<div class="mv-img">.*?</a>\n</div>')
     
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s).*?<div class="mv-img">\n<img src="([^"]+)".*?="([^"]+)".*?a href="([^"]+)"')
        thumb = patron[0]  
        title = patron[1]
        url = patron[2]
        plugintools.add_item (action = "cuatrok_uhdremux1" , title = "[B][COLOR gold]" + title + "[/B][/COLOR]" , url = url , thumbnail = (("https:") + thumb) , folder = True )


def cuatrok_uhdremux1(params):
    url = (("https://pctfenix.com" + params.get ( "url" )))
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    matches = plugintools.find_multiple_matches(url,'ctn-download-.*?data-ut=.*?title')
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"')
        title = patron[0]  
        url = patron[1]
        plugintools.add_item (action = "elementum_pctfenix1" , title = "[B][COLOR darkorange]" + title + "[/B][/COLOR]" , url = url , folder = False , isPlayable = True )


######################  cuatrok_uhdmicro  ######################  cuatrok_uhdmicro  ######################  cuatrok_uhdmicro  ######################  cuatrok_uhdmicro  ######################  cuatrok_uhdmicro  ######################


def cuatrok_uhdmicro(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches(url,r'(?s)<div class="mv-img">.*?</a>\n</div>')
     
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s).*?<div class="mv-img">\n<img src="([^"]+)".*?="([^"]+)".*?a href="([^"]+)"')
        thumb = patron[0]  
        title = patron[1]
        url = patron[2]
        plugintools.add_item (action = "cuatrok_uhdmicro1" , title = "[B][COLOR gold]" + title + "[/B][/COLOR]" , url = url , thumbnail = (("https:") + thumb) , folder = True )


def cuatrok_uhdmicro1(params):
    url = (("https://pctfenix.com" + params.get ( "url" )))
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    matches = plugintools.find_multiple_matches(url,'ctn-download-.*?data-ut=.*?title')
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"')
        title = patron[0]  
        url = patron[1]
        plugintools.add_item (action = "elementum_pctfenix1" , title = "[B][COLOR darkorange]" + title + "[/B][/COLOR]" , url = url , folder = False , isPlayable = True )


######################  cuatrok_uhdrip  ######################  cuatrok_uhdrip  ######################  cuatrok_uhdrip  ######################  cuatrok_uhdrip  ######################  cuatrok_uhdrip  ######################


def cuatrok_uhdrip(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches(url,r'(?s)<div class="mv-img">.*?</a>\n</div>')
     
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s).*?<div class="mv-img">\n<img src="([^"]+)".*?="([^"]+)".*?a href="([^"]+)"')
        thumb = patron[0]  
        title = patron[1]
        url = patron[2]
        plugintools.add_item (action = "cuatrok_uhdrip1" , title = "[B][COLOR gold]" + title + "[/B][/COLOR]" , url = url , thumbnail = (("https:") + thumb) , folder = True )


def cuatrok_uhdrip1(params):
    url = (("https://pctfenix.com" + params.get ( "url" )))
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    matches = plugintools.find_multiple_matches(url,'ctn-download-.*?data-ut=.*?title')
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"')
        title = patron[0]  
        url = patron[1]
        plugintools.add_item (action = "elementum_pctfenix1" , title = "[B][COLOR darkorange]" + title + "[/B][/COLOR]" , url = url , folder = False , isPlayable = True )
 

######################  cuatrok_webrip  ######################  cuatrok_webrip  ######################  cuatrok_webrip  ######################  cuatrok_webrip  ######################  cuatrok_webrip  ######################


def cuatrok_webrip(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches(url,r'(?s)<div class="mv-img">.*?</a>\n</div>')
     
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s).*?<div class="mv-img">\n<img src="([^"]+)".*?="([^"]+)".*?a href="([^"]+)"')
        thumb = patron[0]  
        title = patron[1]
        url = patron[2]
        plugintools.add_item (action = "cuatrok_webrip1" , title = "[B][COLOR gold]" + title + "[/B][/COLOR]" , url = url , thumbnail = (("https:") + thumb) , folder = True )


def cuatrok_webrip1(params):
    url = (("https://pctfenix.com" + params.get ( "url" )))
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    matches = plugintools.find_multiple_matches(url,'ctn-download-.*?data-ut=.*?title')
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"')
        title = patron[0]  
        url = patron[1]
        plugintools.add_item (action = "elementum_pctfenix1" , title = "[B][COLOR darkorange]" + title + "[/B][/COLOR]" , url = url , folder = False , isPlayable = True )


######################  full_uhdcuatrok  ######################  full_uhdcuatrok  ######################  full_uhdcuatrok  ######################  full_uhdcuatrok  ######################  full_uhdcuatrok  ######################


def full_uhdcuatrok(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches(url,r'(?s)<div class="mv-img">.*?</a>\n</div>')
     
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s).*?<div class="mv-img">\n<img src="([^"]+)".*?="([^"]+)".*?a href="([^"]+)"')
        thumb = patron[0]  
        title = patron[1]
        url = patron[2]
        plugintools.add_item (action = "full_uhdcuatrok1" , title = "[B][COLOR gold]" + title + "[/B][/COLOR]" , url = url , thumbnail = (("https:") + thumb) , folder = True )


def full_uhdcuatrok1(params):
    url = (("https://pctfenix.com" + params.get ( "url" )))
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    matches = plugintools.find_multiple_matches(url,'ctn-download-.*?data-ut=.*?title')
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"')
        title = patron[0]  
        url = patron[1]
        plugintools.add_item (action = "elementum_pctfenix1" , title = "[B][COLOR darkorange]" + title + "[/B][/COLOR]" , url = url , folder = False , isPlayable = True )

 
######################  microhd_1080p  ######################  microhd_1080p  ######################  microhd_1080p  ######################  microhd_1080p  ######################  microhd_1080p  ######################


def microhd_1080p(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches(url,r'(?s)<div class="mv-img">.*?</a>\n</div>')
     
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s).*?<div class="mv-img">\n<img src="([^"]+)".*?="([^"]+)".*?a href="([^"]+)"')
        thumb = patron[0]  
        title = patron[1]
        url = patron[2]
        plugintools.add_item (action = "microhd_1080p1" , title = "[B][COLOR gold]" + title + "[/B][/COLOR]" , url = url , thumbnail = (("https:") + thumb) , folder = True )


def microhd_1080p1(params):
    url = (("https://pctfenix.com" + params.get ( "url" )))
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    matches = plugintools.find_multiple_matches(url,'ctn-download-.*?data-ut=.*?title')
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"')
        title = patron[0]  
        url = patron[1]
        plugintools.add_item (action = "elementum_pctfenix1" , title = "[B][COLOR darkorange]" + title + "[/B][/COLOR]" , url = url , folder = False , isPlayable = True )    


##-----------------cine_videoclub##-------------------cine_videoclub#-------------------#cine_videoclub#-----------------------------------------------------------
##-----------------cine_videoclub##-------------------cine_videoclub#-------------------#cine_videoclub#-----------------------------------------------------------##-----------------cine_videoclub##-------------------cine_videoclub#-------------------#cine_videoclub#-----------------------------------------------------------##-----------------cine_videoclub##-------------------cine_videoclub#-------------------#cine_videoclub#-----------------------------------------------------------##-----------------cine_videoclub##-------------------cine_videoclub#-------------------#cine_videoclub#-----------------------------------------------------------##-----------------cine_videoclub##-------------------cine_videoclub#-------------------#cine_videoclub#-----------------------------------------------------------##-----------------cine_videoclub##-------------------cine_videoclub#-------------------#cine_videoclub#-----------------------------------------------------------##-----------------cine_videoclub##-------------------cine_videoclub#-------------------#cine_videoclub#-----------------------------------------------------------##-----------------cine_videoclub##-------------------cine_videoclub#-------------------#cine_videoclub#-----------------------------------------------------------##-----------------cine_videoclub##-------------------cine_videoclub#-------------------#cine_videoclub#-----------------------------------------------------------##-----------------cine_videoclub##-------------------cine_videoclub#-------------------#cine_videoclub#-----------------------------------------------------------##-----------------cine_videoclub##-------------------cine_videoclub#-------------------#cine_videoclub#-----------------------------------------------------------


def cine_videoclub(params):

    ##--------- CABECERA cine_videoclub-------------##--------- CABECERA cine_videoclub-------------##--------- CABECERA cine_videoclub-------------##--------- CABECERA cine_videoclub-------------##--------- CABECERA cine_videoclub-------------##--------- CABECERA cine_videoclub-------------##--------- CABECERA cine_videoclub-------------##--------- CABECERA cine_videoclub-------------##

    plugintools.add_item(action = "", title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail = "https://i.imgur.com/pmzImSy.jpg", fanart = "https://i.imgur.com/pmzImSy.jpg", folder = False )


    plugintools.add_item(action = "", title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR magenta]VIDEO CLUB[/B][/COLOR]", thumbnail = "https://i.imgur.com/pmzImSy.jpg", fanart = "https://i.imgur.com/pmzImSy.jpg", folder = False )


    plugintools.add_item(action = "", title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail = "https://i.imgur.com/pmzImSy.jpg", fanart = "https://i.imgur.com/pmzImSy.jpg", folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/pmzImSy.jpg", fanart = "https://i.imgur.com/pmzImSy.jpg", folder = False )



    
    categorias = []
    header = []
    url = params.get ( "url")
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url.strip ()  
    matches = plugintools.find_multiple_matches(url, 'group-title="([^"]+)') 
    for categoria in sorted(matches): 
        if categoria not in categorias: 
            categorias.append(categoria)
    for x in sorted(categorias):
        if x == "VOD | Castellano" or x == "VOD | Castellano 4K":  
            plugintools . add_item ( action = "resolve_lista" , title = x , url = x, thumbnail =  params.get("thumbnail") , fanart="https://i.imgur.com/sNJCKGL.jpg", folder = True)
        else:  
            pass
        
def resolve_lista(params):

    url2 = "http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_cine1" 
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url2 , headers = request_headers )
    url = read_url.strip ()     
    migrupo = params.get( "title" )
    
    matches = plugintools.find_multiple_matches(url,r'(?s)#EXTINF.*?\nhttp.*?\s')
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s)#EXTINF.*?tvg-name="([^"]+).*?logo="([^"]+).*?group-title="([^"]+).*?(http.*?)\s')
        title = patron[0]
        thumb = patron[1]
        grupo = patron[2]
        url = patron[3]
        if migrupo ==  grupo:  
            plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][COLOR lime]" + title + "[/B][/COLOR]", url = url , thumbnail = thumb , fanart= "https://i.imgur.com/sNJCKGL.jpg" , folder = False , isPlayable = True )
        else:  
            pass
                       




#########################################  SERIES   ###########################################   SERIES   ###########################################   SERIES   ####################################################################################  SERIES   ###########################################   SERIES   ###########################################   SERIES   ###########################################
##-----------------kodivertido_SERIES##-------------------kodivertido_SERIES#-------------------#kodivertido_SERIES#-----------------------------------------------------------
##-----------------kodivertido_SERIES##-------------------kodivertido_SERIES#-------------------#kodivertido_SERIES#-----------------------------------------------------------##-----------------kodivertido_SERIES##-------------------kodivertido_SERIES#-------------------#kodivertido_SERIES#-----------------------------------------------------------##-----------------kodivertido_SERIES##-------------------kodivertido_SERIES#-------------------#kodivertido_SERIES#-----------------------------------------------------------##-----------------kodivertido_SERIES##-------------------kodivertido_SERIES#-------------------#kodivertido_SERIES#-----------------------------------------------------------##-----------------kodivertido_SERIES##-------------------kodivertido_SERIES#-------------------#kodivertido_SERIES#-----------------------------------------------------------##-----------------kodivertido_SERIES##-------------------kodivertido_SERIES#-------------------#kodivertido_SERIES#-----------------------------------------------------------##-----------------kodivertido_SERIES##-------------------kodivertido_SERIES#-------------------#kodivertido_SERIES#-----------------------------------------------------------##-----------------kodivertido_SERIES##-------------------kodivertido_SERIES#-------------------#kodivertido_SERIES#-----------------------------------------------------------##-----------------kodivertido_SERIES##-------------------kodivertido_SERIES#-------------------#kodivertido_SERIES#-----------------------------------------------------------##-----------------kodivertido_SERIES##-------------------kodivertido_SERIES#-------------------#kodivertido_SERIES#-----------------------------------------------------------##-----------------kodivertido_SERIES##-------------------kodivertido_SERIES#-------------------#kodivertido_SERIES#-----------------------------------------------------------
#########################################  SERIES   ###########################################   SERIES   ###########################################   SERIES   ####################################################################################  SERIES   ###########################################   SERIES   ###########################################   SERIES   ###########################################






##-----------------grantorrent_series_nor##-------------------grantorrent_series_nor#-------------------#grantorrent_series_nor#-----------------------------------------------------------
##-----------------grantorrent_series_nor##-------------------grantorrent_series_nor#-------------------#grantorrent_series_nor#-----------------------------------------------------------##-----------------grantorrent_series_nor##-------------------grantorrent_series_nor#-------------------#grantorrent_series_nor#-----------------------------------------------------------##-----------------grantorrent_series_nor##-------------------grantorrent_series_nor#-------------------#grantorrent_series_nor#-----------------------------------------------------------##-----------------grantorrent_series_nor##-------------------grantorrent_series_nor#-------------------#grantorrent_series_nor#-----------------------------------------------------------##-----------------grantorrent_series_nor##-------------------grantorrent_series_nor#-------------------#grantorrent_series_nor#-----------------------------------------------------------##-----------------grantorrent_series_nor##-------------------grantorrent_series_nor#-------------------#grantorrent_series_nor#-----------------------------------------------------------##-----------------grantorrent_series_nor##-------------------grantorrent_series_nor#-------------------#grantorrent_series_nor#-----------------------------------------------------------##-----------------grantorrent_series_nor##-------------------grantorrent_series_nor#-------------------#grantorrent_series_nor#-----------------------------------------------------------##-----------------grantorrent_series_nor##-------------------grantorrent_series_nor#-------------------#grantorrent_series_nor#-----------------------------------------------------------##-----------------grantorrent_series_nor##-------------------grantorrent_series_nor#-------------------#grantorrent_series_nor#-----------------------------------------------------------##-----------------grantorrent_series_nor##-------------------grantorrent_series_nor#-------------------#grantorrent_series_nor#-----------------------------------------------------------


def grantorrent_series_nor(params):
    
    url = params.get ( "url" )
    url = requests.get ( url ).text
    #matches = re.findall ( r'(?s)imagen-post">.*?href="(.+?.nl/series/(.*?)/)".*?src="(.+?)"' , url , re.DOTALL )
    matches = plugintools.find_multiple_matches(url,r'(?s)imagen-post">.*?href=".+?.nl/series/.*?/".*?src=".+?"')
    next = plugintools.find_single_match ( url , '<link rel="next" href="([^"]+)"' )
    
    for match in matches:
        patron = plugintools.find_single_match(match, r'(?s)imagen-post">.*?href="(.+?.nl/series/(.*?)/)".*?src="(.+?)"')
        url = patron[0]  
        title = patron[1]
        thumb = patron[2]
        plugintools.add_item (action = "grantorrent_series_nor2" , title = "[B][COLOR darkorange]" + title + "[/B][/COLOR]" , thumbnail = thumb , url = url , fanart = "https://i.imgur.com/3C0ZrFs.jpg" , folder = True )    

        #plugintools.add_item ( action = "grantorrent_series_nor2" , title = title , thumbnail = thumb , url = url , fanart = "https://i.imgur.com/3C0ZrFs.jpg" , folder = True )
    plugintools.add_item ( action = "grantorrent_series_nor" , title = "[B][COLOR yellow]" +"PAGINA SIGUIENTE" + "[/B][/COLOR]" , url = next , thumbnail = "https://i.imgur.com/cfwdN1c.jpg" , fanart = "https://i.imgur.com/3C0ZrFs.jpg" , folder = True )


def grantorrent_series_nor2(params):
    
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    #matches = re.findall ( r'(?s)<div class="ima.*?<img src="([^"]+)".*?class="bold">Título original:\s(.*?)<.*?p>(.*?)<|<td><img src=".*?<td>(.*?)<.*?<td>(.*?)<.*?u=(.*?)"' , url , re.DOTALL )
    #(?s)<div class="ima.*?<img src="([^"]+)".*?class="bold">Título original:\s(.*?)<.*?p>(.*?)<|<td><img src=".*?<td>(.*?)<.*?<td>(.*?)<.*?u.*?'(.*?)'
    #for thumb , title , info , cap , tam , url in matches:
       #plugintools.add_item ( action = "link1" , title = "[B][COLOR magenta]Titulo: [/COLOR][/B]" + title + " " + cap + " " + tam , plot = info , url = url , thumbnail = thumb , fanart = thumb , folder = True , isPlayable = False )
    matches = plugintools.find_multiple_matches(url,r'(?s)<div class="ima.*?<img src="[^"]+".*?class="bold">Título original:\s.*?<.*?p>.*?<|<td><img src=".*?<td>.*?<.*?<td>.*?<.*?u.*?}')
    for match in matches:
        thumb = plugintools.find_single_match(match, r'(?s)<div class="ima.*?<img src="([^"]+)')
        title = plugintools.find_single_match(match, r'(?s)>Título original:\s(.*?)<')
        info = plugintools.find_single_match(match, r'(?s)>Título original:\s.*?<.*?p>(.*?)<')
        capitulo = plugintools.find_single_match(match, r'(?s)<td><img src=".*?<td>(.*?)<')
        peso = plugintools.find_single_match(match, r'(?s)<td><img src=".*?/td>.*?/td>.*?<td>(.*?)<')
        url = plugintools.find_single_match(match, r"(?s)lol.*?u:.*?'([^']+)")
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = title , url = url , thumbnail = thumb , fanart = thumb , folder = False , isPlayable = True )

 

def link1(params): 
    
    url = params.get ( "url" ).text
    thumb = params.get ( "thumbnail" )
    import re, six, base64, requests
    url = (base64.b64decode(url.encode("utf-8", "strict"))).decode("utf-8", "strict")
    plugintools.add_item ( action = "elementum" , title = "[B][COLOR lime]DESCARGAR[/COLOR][/B]" , url = url , thumbnail = thumb , folder = False , isPlayable = True )  
    #xbmc.log("[COLOR lime][B]url: [/B][/COLOR]" + url, xbmc.LOGINFO)


##-----------------mitorrent_series##-------------------mitorrent_series#-------------------#mitorrent_series#-----------------------------------------------------------
##-----------------mitorrent_series##-------------------mitorrent_series#-------------------#mitorrent_series#-----------------------------------------------------------##-----------------mitorrent_series##-------------------mitorrent_series#-------------------#mitorrent_series#-----------------------------------------------------------##-----------------mitorrent_series##-------------------mitorrent_series#-------------------#mitorrent_series#-----------------------------------------------------------##-----------------mitorrent_series##-------------------mitorrent_series#-------------------#mitorrent_series#-----------------------------------------------------------##-----------------mitorrent_series##-------------------mitorrent_series#-------------------#mitorrent_series#-----------------------------------------------------------##-----------------mitorrent_series##-------------------mitorrent_series#-------------------#mitorrent_series#-----------------------------------------------------------##-----------------mitorrent_series##-------------------mitorrent_series#-------------------#mitorrent_series#-----------------------------------------------------------##-----------------mitorrent_series##-------------------mitorrent_series#-------------------#mitorrent_series#-----------------------------------------------------------##-----------------mitorrent_series##-------------------mitorrent_series#-------------------#mitorrent_series#-----------------------------------------------------------##-----------------mitorrent_series##-------------------mitorrent_series#-------------------#mitorrent_series#-----------------------------------------------------------##-----------------mitorrent_series##-------------------mitorrent_series#-------------------#mitorrent_series#-----------------------------------------------------------


def mitorrent_series(params):
    
    if int ( params.get ( "page" ) ) != 1:
        url = params.get ( "url" ) + params.get ( "page" ) + "/"
    else:
        url = "https://mitorrent.org/series/"

    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    matches = plugintools.find_multiple_matches ( url , '(?s)(img-responsive".*?browse-movie-tags)' )

    next = plugintools.find_single_match ( url , '<li><a class="next page-numbers" href="([^"]+)' )
    for match in matches:
        title = plugintools.find_single_match ( match , 'browse-movie-title">([^<]+)<' )
        thumb = plugintools.find_single_match ( match , 'sive" src="([^"]+)"' )
        url = plugintools.find_single_match ( match , '(?s)browse-movie-bottom">.*?href="([^"]+)"' )

        plugintools.add_item ( action = "mitorrent_series1" , title = title , thumbnail = thumb , url = url , folder = True )
    next = str ( int ( params.get ( "page" ) ) + 1 )
    plugintools.add_item ( action = "mitorrent_series" , title = "SIGUIENTE" , url = "https://mitorrent.org/series/page/" , thumbnail = 'https://i.imgur.com/cfwdN1c.jpg' , page = next ,
        folder = True )


def mitorrent_series1(params):
    
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    matches = re.findall ( r'(?s)class="accordion.*?&nbsp;(.+?)<|href="(magnet.+?)".*?Descargar(.+?\d.)' , url , re.DOTALL )
    
    for temp , url , title in matches:
        plugintools.add_item ( action = "elementum" , title = temp + title , url = url , folder = False , isPlayable = True )
    xbmc.log("[COLOR lime][B]url: [/B][/COLOR]" + url, xbmc.LOGINFO)


##-----------------cinetorrent_pelis##-------------------cinetorrent_pelis#-------------------#cinetorrent_pelis#-----------------------------------------------------------
##-----------------cinetorrent_pelis##-------------------cinetorrent_pelis#-------------------#cinetorrent_pelis#-----------------------------------------------------------##-----------------cinetorrent_pelis##-------------------cinetorrent_pelis#-------------------#cinetorrent_pelis#-----------------------------------------------------------##-----------------cinetorrent_pelis##-------------------cinetorrent_pelis#-------------------#cinetorrent_pelis#-----------------------------------------------------------##-----------------cinetorrent_pelis##-------------------cinetorrent_pelis#-------------------#cinetorrent_pelis#-----------------------------------------------------------##-----------------cinetorrent_pelis##-------------------cinetorrent_pelis#-------------------#cinetorrent_pelis#-----------------------------------------------------------##-----------------cinetorrent_pelis##-------------------cinetorrent_pelis#-------------------#cinetorrent_pelis#-----------------------------------------------------------##-----------------cinetorrent_pelis##-------------------cinetorrent_pelis#-------------------#cinetorrent_pelis#-----------------------------------------------------------##-----------------cinetorrent_pelis##-------------------cinetorrent_pelis#-------------------#cinetorrent_pelis#-----------------------------------------------------------##-----------------cinetorrent_pelis##-------------------cinetorrent_pelis#-------------------#cinetorrent_pelis#-----------------------------------------------------------##-----------------cinetorrent_pelis##-------------------cinetorrent_pelis#-------------------#cinetorrent_pelis#-----------------------------------------------------------##-----------------cinetorrent_pelis##-------------------cinetorrent_pelis#-------------------#cinetorrent_pelis#-----------------------------------------------------------


def cinetorrent_series(params):
    if int ( params.get ( "page" ) ) != 1:
        url = params.get ( "url" ) + params.get ( "page" ) + "/"
    else:
        url = "http://cinetorrent.co/peliculas/"

    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    matches = plugintools.find_multiple_matches ( url ,r'(?s)(<div class="col-6 col-sm-4 col-lg-3 col-xl-2">.*?</div>\s*</div>)' )

    next = plugintools.find_single_match ( url , '<li><a class="next page-numbers" href="([^"]+)' )
    for match in matches:
        title = plugintools.find_single_match ( match , '">([^<]+)</a></h3>' )
        thumb = plugintools.find_single_match ( match , '<img src="([^"]+)"' )
        url = plugintools.find_single_match ( match , '<h3 class="card__title"><a href="([^"]+)' )
        calidad = plugintools.find_single_match ( match , '<li>([^<]+)</li>' )

        plugintools.add_item ( action = "cinetorrent_series1" , title = title + "\x20" + calidad , thumbnail = thumb ,
            url = url , folder = True )
    next = str ( int ( params.get ( "page" ) ) + 1 )
    plugintools.add_item ( action = "cinetorrent_series" , title = "Next Page" ,
        url = "http://cinetorrent.co/peliculas/page/" , thumbnail = 'https://i.imgur.com/cfwdN1c.jpg' , page = next ,
        folder = True )


def cinetorrent_series1(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    matches = re.findall ( r'(?s)td>(Español.*?)<.*?href="(.+?)"' , url , re.DOTALL )
    log ( matches )
    for title , url in matches:
        plugintools.add_item ( action = "elementum" , title = title , url = url , folder = False , isPlayable = True )




#########################################  ESPECIAL TV INTERNET   ###########################################   ESPECIAL TV INTERNET   ###########################################   ESPECIAL TV INTERNET   ####################################################################################  ESPECIAL TV INTERNET   ###########################################   ESPECIAL TV INTERNET   ###########################################   ESPECIAL TV INTERNET   ###########################################
##-----------------kodivertido_ESPECIAL TV INTERNET##-------------------kodivertido_ESPECIAL TV INTERNET#-------------------#kodivertido_ESPECIAL TV INTERNET#-----------------------------------------------------------
##-----------------kodivertido_ESPECIAL TV INTERNET##-------------------kodivertido_ESPECIAL TV INTERNET#-------------------#kodivertido_ESPECIAL TV INTERNET#-----------------------------------------------------------##-----------------kodivertido_ESPECIAL TV INTERNET##-------------------kodivertido_ESPECIAL TV INTERNET#-------------------#kodivertido_ESPECIAL TV INTERNET#-----------------------------------------------------------##-----------------kodivertido_ESPECIAL TV INTERNET##-------------------kodivertido_ESPECIAL TV INTERNET#-------------------#kodivertido_ESPECIAL TV INTERNET#-----------------------------------------------------------##-----------------kodivertido_ESPECIAL TV INTERNET##-------------------kodivertido_ESPECIAL TV INTERNET#-------------------#kodivertido_ESPECIAL TV INTERNET#-----------------------------------------------------------##-----------------kodivertido_ESPECIAL TV INTERNET##-------------------kodivertido_ESPECIAL TV INTERNET#-------------------#kodivertido_ESPECIAL TV INTERNET#-----------------------------------------------------------##-----------------kodivertido_ESPECIAL TV INTERNET##-------------------kodivertido_ESPECIAL TV INTERNET#-------------------#kodivertido_ESPECIAL TV INTERNET#-----------------------------------------------------------##-----------------kodivertido_ESPECIAL TV INTERNET##-------------------kodivertido_ESPECIAL TV INTERNET#-------------------#kodivertido_ESPECIAL TV INTERNET#-----------------------------------------------------------##-----------------kodivertido_ESPECIAL TV INTERNET##-------------------kodivertido_ESPECIAL TV INTERNET#-------------------#kodivertido_ESPECIAL TV INTERNET#-----------------------------------------------------------##-----------------kodivertido_ESPECIAL TV INTERNET##-------------------kodivertido_ESPECIAL TV INTERNET#-------------------#kodivertido_ESPECIAL TV INTERNET#-----------------------------------------------------------##-----------------kodivertido_ESPECIAL TV INTERNET##-------------------kodivertido_ESPECIAL TV INTERNET#-------------------#kodivertido_ESPECIAL TV INTERNET#-----------------------------------------------------------##-----------------kodivertido_ESPECIAL TV INTERNET##-------------------kodivertido_ESPECIAL TV INTERNET#-------------------#kodivertido_ESPECIAL TV INTERNET#-----------------------------------------------------------
#########################################  ESPECIAL TV INTERNET   ###########################################   ESPECIAL TV INTERNET   ###########################################   ESPECIAL TV INTERNET   ####################################################################################  ESPECIAL TV INTERNET   ###########################################   ESPECIAL TV INTERNET   ###########################################   ESPECIAL TV INTERNET   ###########################################




##-----------------kodivertido_especial tv internet##-------------------kodivertido_especial tv internet#-------------------#kodivertido_especial tv internet#-----------------------------------------------------------
##-----------------kodivertido_especial tv internet##-------------------kodivertido_especial tv internet#-------------------#kodivertido_especial tv internet#-----------------------------------------------------------##-----------------kodivertido_especial tv internet##-------------------kodivertido_especial tv internet#-------------------#kodivertido_especial tv internet#-----------------------------------------------------------##-----------------kodivertido_especial tv internet##-------------------kodivertido_especial tv internet#-------------------#kodivertido_especial tv internet#-----------------------------------------------------------##-----------------kodivertido_especial tv internet##-------------------kodivertido_especial tv internet#-------------------#kodivertido_especial tv internet#-----------------------------------------------------------##-----------------kodivertido_especial tv internet##-------------------kodivertido_especial tv internet#-------------------#kodivertido_especial tv internet#-----------------------------------------------------------##-----------------kodivertido_especial tv internet##-------------------kodivertido_especial tv internet#-------------------#kodivertido_especial tv internet#-----------------------------------------------------------##-----------------kodivertido_especial tv internet##-------------------kodivertido_especial tv internet#-------------------#kodivertido_especial tv internet#-----------------------------------------------------------##-----------------kodivertido_especial tv internet##-------------------kodivertido_especial tv internet#-------------------#kodivertido_especial tv internet#-----------------------------------------------------------##-----------------kodivertido_especial tv internet##-------------------kodivertido_especial tv internet#-------------------#kodivertido_especial tv internet#-----------------------------------------------------------##-----------------kodivertido_especial tv internet##-------------------kodivertido_especial tv internet#-------------------#kodivertido_especial tv internet#-----------------------------------------------------------##-----------------kodivertido_especial tv internet##-------------------kodivertido_especial tv internet#-------------------#kodivertido_especial tv internet#-----------------------------------------------------------


def kodivertido_tvinternete(params):
    
##--------- CABECERA especial tv internet-------------##--------- CABECERA especial tv internet-------------##--------- CABECERA especial tv internet-------------##--------- CABECERA especial tv internet-------------##--------- CABECERA especial tv internet-------------##--------- CABECERA especial tv internet-------------##--------- CABECERA especial tv internet-------------##--------- CABECERA especial tv internet-------------##    
    
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/30Tq1VI.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][COLOR white]M  [COLOR cyan]E  [COLOR yellow]N  [COLOR aqua]U    [COLOR orangered]ESPECIAL [COLOR magenta]TV[COLOR lime] INTERNET[/B][/COLOR]" , thumbnail = "https://i.imgur.com/30Tq1VI.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------[COLOR aqua] kodivertidoXZ[COLOR lime]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail = "https://i.imgur.com/30Tq1VI.jpg" , fanart = "https://i.imgur.com/d3Lq6JS.jpg" , folder = False )


    plugintools.add_item(action = "", title = "", thumbnail = "https://i.imgur.com/29b9UAP.jpg", fanart = "https://i.imgur.com/d3Lq6JS.jpg", folder = False)
    


    plugintools.add_item(  #Guia TV   
        action="guiatv", 
        title="[COLOR gold]Guia TV[/COLOR]",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/71ik1wFIPOL.png",
        url= "https://www.formulatv.com/programacion/movistarplus/",
        fanart="https://images-na.ssl-images-amazon.com/images/I/71ik1wFIPOL.png",
        folder=True )  
    plugintools.add_item(  #adictos  
        action="adictos", 
        title="[COLOR gold]Tdt+Premium[/COLOR] [COLOR red]NECESARIO VPN[/COLOR]",
        thumbnail="https://i.imgur.com/msnvpNz.jpg",
        url= "https://adictosalatele.com/canales-de-espana/",
        fanart="https://i.imgur.com/msnvpNz.jpg",
        folder=True )
    plugintools.add_item(  #latinos  
        action="adictos", 
        title="[COLOR gold]Latinos[/COLOR] [COLOR red]NECESARIO VPN[/COLOR]",
        thumbnail="https://i.imgur.com/tTT0lFz.jpg",
        url= "https://adictosalatele.com/canales-latinos/",
        fanart="https://i.imgur.com/tTT0lFz.jpg",
        folder=True )        
    plugintools.add_item(  #Tv infantil  
        action="adictos", 
        title="[COLOR gold]Tv infantil[/COLOR] [COLOR red]NECESARIO VPN[/COLOR]",
        thumbnail="https://i.imgur.com/w5alGoX.jpg",
        url= "https://adictosalatele.com/infantiles/",
        fanart="https://i.imgur.com/w5alGoX.jpg",
        folder=True ) 
    plugintools.add_item(  #Daqueen TV  
        action="daqueen_tv", 
        title="[COLOR gold]Tv Premium[/COLOR]",
        thumbnail="https://i.imgur.com/gyrXGxr.jpg",
        url= "https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/canales%20vergol",
        fanart="https://i.imgur.com/gyrXGxr.jpg",
        folder= True )      
    plugintools.add_item(  #Seccion Daqueen  
        action="daqueen",                    
        title="[COLOR gold]Deportes[/COLOR]",
        thumbnail="https://i.imgur.com/sR5eZMj.jpg",
        url= "",
        fanart="https://i.imgur.com/sR5eZMj.jpg",
        folder= True )     
    plugintools.add_item(  #Tdtchannels.com   
        action="tdtchannels", 
        title="[COLOR gold]TDTChannels[/COLOR]",
        thumbnail="https://i.imgur.com/mN2YQ8p.jpg",
        url= "https://www.tdtchannels.com/lists/tv.m3u",
        fanart="https://i.imgur.com/mN2YQ8p.jpg",
        folder=True )  
    plugintools.add_item(  #TeleOnline.org    
        action="canales", 
        title="[COLOR gold]TeleOnline.org[/COLOR]",
        thumbnail="https://i.imgur.com/mN2YQ8p.jpg",
        url= "https://teleonline.org/",
        fanart="https://i.imgur.com/mN2YQ8p.jpg",
        folder=True )            
    plugintools.add_item(  #Television Mundial   
        action="tdtmun", 
        title="[COLOR gold]Television Mundial[/COLOR]",
        thumbnail="https://i.imgur.com/CCcdjsY.jpg",
        url= "https://raw.githubusercontent.com/telegrambotdev/iptv/ba58c7c0b2c9c7653f6b2cd3b4b64012d854d81e/index.m3u",
        fanart="https://i.imgur.com/CCcdjsY.jpg",
        folder=True )    
    plugintools.add_item(  #Fluxus   
        action="fluxus", 
        title="[COLOR gold]Fluxus[/COLOR]",
        thumbnail="https://i.imgur.com/N2r6pj6.jpg",
        url= "https://fluxustvespanol.blogspot.com/p/fluxus-iptv.html",
        fanart="https://i.imgur.com/N2r6pj6.jpg",
        folder=True )   
    plugintools.add_item(  #canales deportivos sd  
        action="canalesd", 
        title="[COLOR gold]Mas[COLOR lime] Canales de Deportes[/COLOR] [COLOR red]KODIvertido[/COLOR]",
        thumbnail="https://i.imgur.com/hZYamJT.jpg",
        url= "http://perillas.mendelux.es/1xyz/kodivertido/canalesdeportivos",
        fanart="https://i.imgur.com/MVgNv8l.jpg",
        folder=True )     


##--------- CABECERA guiatv-------------##--------- CABECERA guiatv-------------##--------- CABECERA guiatv-------------##--------- CABECERA guiatv-------------##--------- CABECERA guiatv-------------##--------- CABECERA guiatv-------------##--------- CABECERA guiatv-------------##--------- CABECERA guiatv-------------##    
 
    
def guiatv ( params ):
    url = params.get("url")  
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )    
    matches = re.findall(r'(?s)class="cadena">.*?<a href="([^"]+)" title="Programación ([^"]+)".*?|<div class="(ahora)">\s*(.*?)<.*?|<div class="luego">\s*<span class="date">(\d+:\d+)<\/span>\s*([^<]+)|<div class="mastarde">\s*<span class="date">(\d+:\d+)<\/span>\s*([^<]+)\s*|<span class="remain"><\/span>\s*<a class="mas" href="([^"]+)"><span>(Parrilla completa)<\/span',url)
    for url, channel, nowhour, now, laterhour, later, morelaterhour, morelater, url2, completed in matches:
        nowhour = "\x20" + nowhour
        if url:
            url = url
        else:
            if url2:
                url = url2    
        title = "[B][COLOR snow]" + channel + "[/COLOR][/B]\x20" + nowhour + "\x20" + now + laterhour + "\x20" + later +  morelaterhour + morelater + "[COLOR orange]" + completed + "[/COLOR]"


        plugintools . add_item ( action = "parse_guiatv" , title = title, url = url, thumbnail =  params.get("thumbnail") , fanart="https://i.imgur.com/iUuLEBI.jpg", folder = True)
def parse_guiatv ( params ):
    url = params.get("url")  
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )    
    matches = re.findall(r'{"@context":"[^"]+","@type":"Event","name":"(\d+:\d+ - [^"]+)","description":"([^"]+)"',url)
    for title, desc in matches: 
        plugintools . add_item ( action = "" , title = title, url = url, plot=desc,thumbnail =  params.get("thumbnail") , fanart="http://perillas.mendelux.es/1xyz/kodivertido/KODIVERTIDOX.gif", folder = True)
 
 
##--------- CABECERA adictos-------------##--------- CABECERA adictos-------------##--------- CABECERA adictos-------------##--------- CABECERA adictos-------------##--------- CABECERA adictos-------------##--------- CABECERA adictos-------------##--------- CABECERA adictos-------------##--------- CABECERA adictos-------------##    
  
 
def adictos ( params ):
    url = params.get("url")  
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    header . append ( [ "Referer" , "https://adictosaldeporte.com/" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )    
    bloque = plugintools.find_single_match(url,'<div class="imagenes">(.*?)</h4>')
    matches = re.findall(r'(?s)<td>.*?<a href="(.*?)" title="(.*?) en.*?><img src="(.*?)"',bloque)
    for url,title,thumb in matches: 
        plugintools . add_item ( action = 'adictos1' , title = title, url ='https:'+ url,thumbnail ='https://adictosalatele.com'+ thumb , fanart="http://perillas.mendelux.es/1xyz/kodivertido/KODIVERTIDOX.gif", folder =False,isPlayable= True)
def adictos1 ( params ):
    url = params.get('url')
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()    
    if 'adictosalatele' in url:
        url ='https:'+ plugintools.find_single_match(url,'(?s)<div class="video">.*?src="(.*?)"')
    else:
        url ='https:'+ plugintools.find_single_match(url,'(?s)<center><textarea.*?src="(.*?)"')
    #plugintools . add_item ( action = "" , title =url,url = url,thumbnail =  "" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True)
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    request_headers.append(["Referer","https://adictosalatele.com/tve-1-en-directo-online-gratis/"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()   
    url = plugintools.find_single_match(url,'(?s)<iframe src="(https.*?wigistream.*?)"')
    #plugintools . add_item ( action = "" , title =url,url = url,thumbnail =  "" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True)
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    request_headers.append(["Referer","https://adictosalatele.com/tve-1-en-directo-online-gratis/"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()    
    pack = plugintools.find_single_match(url,'(?s)(eval\(function\(p,a,c,k,e,d.*?)</script>')
    unpacked = jsunpack.unpack(pack).replace('\\', '')
    finalurl = plugintools.find_single_match(unpacked,'(?s)player=new Clappr.Player.*?source."(.*?)"')
    plugintools . play_resolved_url ( finalurl )                                
    #plugintools . add_item ( action = "" , title =finalurl,url = finalurl,thumbnail =  "" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder =True)   
    
    
##--------- CABECERA daqueen_tv-------------##--------- CABECERA daqueen_tv-------------##--------- CABECERA daqueen_tv-------------##--------- CABECERA daqueen_tv-------------##--------- CABECERA daqueen_tv-------------##--------- CABECERA daqueen_tv-------------##--------- CABECERA daqueen_tv-------------##--------- CABECERA daqueen_tv-------------##    
 

def daqueen_tv (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)title.*?=.*?"(.+?)".*?thumb.*?=.*?"(.*?)".*?url.*?=.*?"(.+?)"', url, re.DOTALL)
 for title, thumb, url in matches:  
  plugintools . add_item ( action = "resolvers" , title = title, url = vergol(url) , thumbnail=thumb , fanart="http://perillas.mendelux.es/1xyz/kodivertido/KODIVERTIDOX.gif", folder = False , isPlayable = True )  
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)(\d+\d+:.*?) <.*?color: #5185c9;">.*?>(.*?)<.*?|strong></span>(.*?)(Channel )(.*?)<', url, re.DOTALL)
 for hora, title, even, channel, url in matches:  
  plugintools . add_item ( action = "wstream1" , title = "[COLOR lime]"+hora+"[/COLOR]" + "  " + "[COLOR darkorange]"+title+"[/COLOR]" + "  " + "[COLOR yellow]"+even+"[/COLOR]" + "  " + channel + url, url = url , thumbnail= "https://i.imgur.com/lnVf69v.jpg" , fanart="http://perillas.mendelux.es/1xyz/kodivertido/KODIVERTIDOX.gif", folder = False , isPlayable = True ) 


def resolvers ( params ):
    url = params.get("url")
    if "mixdrop" in url: 
        from resolveurl .plugins .lib import jsunpack  
        header = [ ]
        header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
        header.append ( [ "Cookie" , "sucuri_cloudproxy_uuid_ddce1ba0a=2c39acd488e40ab0a783c0d7e3db62ee" ] )
        read_url , read_header = plugintools . read_body_and_headers ( url )
        url = read_url . strip ( )
        pack = plugintools.find_single_match(url,r'(?s)Spanish.*?(eval\(function\(p,a,c,k,e,d.*?)</script>')
        unpacked = jsunpack.unpack(pack).replace('\\', '')
        finalurl = plugintools.find_single_match(unpacked,'MDCore.wurl="([^"]+)')
        plugintools . play_resolved_url ( "https:" + finalurl )      
    elif "upstream" in url:
        from resolveurl .plugins .lib import jsunpack 
        header = [ ] 
        header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] ) 
        read_url , read_header = plugintools . read_body_and_headers ( url ) 
        url = read_url . strip ( ) 
        pack = plugintools.find_single_match(url,r'(?s)(eval\(function\(p,a,c,k,e,d.*?)</script>')
        unpacked = jsunpack.unpack(pack).replace('\\', '')
        finalurl = plugintools.find_single_match(unpacked,'(?s)else.*?sources.*?file:"([^"]+)"')
        finalurl+='|Referer={}'.format(params.get("url"))
        plugintools . play_resolved_url ( finalurl ) 
    elif "gamovideo" in url:        
        from resolveurl .plugins .lib import jsunpack 
        header = [ ] 
        header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] ) 
        read_url , read_header = plugintools . read_body_and_headers ( url ) 
        url = read_url . strip ( ) 
        pack = plugintools.find_single_match(url,r'(?s)jwplayer.key=.*?(eval\(function\(p,a,c,k,e,d.*?)</script>')
        unpacked = jsunpack.unpack(pack).replace('\\', '')
        finalurl = plugintools.find_single_match(unpacked,'(?s)sources:.*?,.*?file:"([^"]+)"')
        finalurl+='|Referer={}'.format(params.get("url"))
        plugintools . play_resolved_url ( finalurl ) 
    elif "clipwatching" in url:        
        from resolveurl .plugins .lib import jsunpack 
        header = [ ] 
        header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] ) 
        read_url , read_header = plugintools . read_body_and_headers ( url ) 
        url = read_url . strip ( ) 
        url = plugintools.find_single_match(url,'(?s)sources: \[\{src: "(.+?)"')
        url+='|Referer={}'.format(params.get("url"))
        plugintools . play_resolved_url ( url )         
    elif "aparat.cam" in url:        
        from resolveurl .plugins .lib import jsunpack 
        header = [ ] 
        header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] ) 
        read_url , read_header = plugintools . read_body_and_headers ( url ) 
        url = read_url . strip ( ) 
        url = plugintools.find_single_match(url,'(?s)sources: \[\{src: "(.+?)"')
        url+='|Referer={}'.format(params.get("url"))
        plugintools . play_resolved_url ( url )      
    elif "vidtobo" in url: 
        from resolveurl .plugins .lib import jsunpack  
        header = [ ]
        header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
        read_url , read_header = plugintools . read_body_and_headers ( url )
        url = read_url . strip ( )
        pack = plugintools.find_single_match(url,r'(?s)javascript\'>(eval\(function\(p,a,c,k,e,d\).*?)</script>')
        unpacked = jsunpack.unpack(pack).replace('\\', '')
        finalurl = plugintools.find_single_match(unpacked,'(?s)file:"(.+?.mp4)"')
        plugintools . play_resolved_url ( finalurl )  
    elif "embed_cload_video" in url:        
        from resolveurl .plugins .lib import jsunpack 
        header = [ ] 
        header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] ) 
        read_url , read_header = plugintools . read_body_and_headers ( url ) 
        url = read_url . strip ( ) 
        url = plugintools.find_single_match(url,'(?s)jwplayer.*?file:\s"([^"]+)"')
        url+='|Referer={}'.format(params.get("url"))
        plugintools . play_resolved_url ( url )
    elif "uqload" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'sources: \["([^"]+)"\]')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl) 
    elif "yourupload" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)jwplayerOptions.*?file: \'(.+?)\'')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)                     
    elif "jawcloud" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)height="510"><source src="(.+?)"')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)                     
    elif "v2.zplayer" in url: 
        from resolveurl .plugins .lib import jsunpack  
        header = [ ]
        header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
        read_url , read_header = plugintools . read_body_and_headers ( url )
        url = read_url . strip ( )
        pack = plugintools.find_single_match(url,r'(?s)(eval\(function\(p,a,c,k,e,d.*?)</script>')
        unpacked = jsunpack.unpack(pack).replace('\\', '')
        finalurl = plugintools.find_single_match(unpacked,'(?s)sources.*?file:"(.+?)"')
        plugintools . play_resolved_url ( finalurl )          
    elif "zplayer" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)else.*?"file": "(.+?)"')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)         
    elif "4shared" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)source src="(.+?)"')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)
    elif "assia1" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)Clappr.Player.*?source:\s\'(.+?)\'')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)          
    elif "m3u8" in url:
        plugintools . play_resolved_url ( url )
    elif "emb.apl19.me" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)pl.init(\'(.+?)\'')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)   
    elif "livestream" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'mp4","m3u8_url":"(.+?)"')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)    
    elif "pcast" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)Clappr.Player\(.*?source: "(.+?)"')
        finalurl = regex
        finalurl += "|Referer={}".format("https:" + url)
        plugintools.play_resolved_url(finalurl)         
    elif "sports24.club" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)var xurl = atob\(\'(.+?)\'')
        finalurl = regex
        finalurl = base64.b64decode(finalurlurl)
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url("https:" + finalurl)   
    elif "espn-live" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)Clappr.Player.*?source: \'(.+?)\'')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)
    elif "yandex" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)Clappr.Player.*?source: \'(.+?)\'')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)
    elif "sportstvstreams" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)player.src\({.*?src:\s"(.+?)"')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl) 
        
def vergol (url): 
    url =url 
    finalurl = ''
    if "vergol"in url :
        origname =plugintools.find_single_match (url ,r'live\/([^\.]+)').capitalize ()
        if not origname :origname =os .path .basename (url ).split (".")[0 ].capitalize ()
        headers_dict ={}
        headers_dict ['User-Agent']='Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0'
        headers_dict ['Referer']=url 
        headers_dict ['Accept']='*/*'
        post ={'manzana66':'12345'}
        response =requests .Session ()
        read_response =response .post (url ,headers =headers_dict ,data =post )  
        matches =re .findall (r"""(?s)<script src="/player/player.js">.*?source: '(.*?)'""",read_response .content.decode("utf-8") )
        for finalurl in matches :
            finalurl =("https:{}|User-Agent={}&referer={}&origin={}".format (finalurl ,"Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0",url ,"https://vergol.com/"))
    else :
        finalurl =url 
    return finalurl       
                                   
def wstream1(params):    
    url = "https://sportscart.xyz/ch/scplayer-" + params.get("url")+ ".php"
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])

    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url = body.strip().decode('utf-8')
    url = plugintools.find_single_match(url,'iframe.+?src="(.+?)"') 
    def wstram (url):
        import re, requests, resolveurl
        from resolveurl.plugins.lib import jsunpack 
        url=url
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1", "Referer":"https://sportscart.xyz/ch/scplayer-82.php"
    }
 
        marcador = requests.get(url, headers=headers, verify=False)
        r = marcador.text
        pack=re.findall("(eval\(function\(p,a,c,k,e,d.*m3u8.*)", r)[0]
        unpack=jsunpack.unpack(pack).replace('\\', '')
        return re.findall('source:"(.*?)"', unpack)[0].replace('ul.cdn946.net', '185.39.10.72')

    url=wstram(url)
    
    plugintools.play_resolved_url( url)
def wstream2(params):    
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])

    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url = body.strip()
    url = plugintools.find_single_match(url,'iframe.+?src="(.+?)" width="100.*?allowfullscreen="true') 
    def wstram (url):
        import re, requests, resolveurl
        from resolveurl.plugins.lib import jsunpack 
        url=url
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1", "Referer":"https://daddylive.club/stream/stream-1.php"
    }
          
        marcador = requests.get(url, headers=headers, verify=False)
        r = marcador.text
        pack=re.findall("(eval\(function\(p,a,c,k,e,d.*m3u8.*)", r)[0]
        unpack=jsunpack.unpack(pack).replace('\\', '')
        return re.findall('source:"(.*?)"', unpack)[0].replace('ul.cdn946.net', '185.39.10.72')

    url=wstram(url)
    
    plugintools.play_resolved_url( url)    

##--------- CABECERA daqueen-------------##--------- CABECERA daqueen-------------##--------- CABECERA daqueen-------------##--------- CABECERA daqueen-------------##--------- CABECERA daqueen-------------##--------- CABECERA daqueen-------------##--------- CABECERA daqueen-------------##--------- CABECERA daqueen-------------##    
 

def daqueen(params): 
   
    plugintools.add_item(  #Agenda Zona deportes Iberiko   
        action="daddylive", 
        title="[COLOR gold]Agenda DaddyLive[/COLOR]",
        thumbnail="https://i.imgur.com/2bsfGN5.jpg",
        url= "https://daddylive.club/",
        fanart="https://i.imgur.com/2bsfGN5.jpg",
        folder=True )  
    plugintools.add_item(  #Agenda SportZonline  
        action="SportZonline", 
        title="[COLOR gold]Agenda SportZonline[/COLOR]",
        thumbnail="https://i.imgur.com/N0YcFQR.jpg",
        url= "https://v3.sportzonline.to/prog.txt",
        fanart="https://i.imgur.com/N0YcFQR.jpg",
        folder=True )       
    plugintools.add_item(  #acestream  
        action="acestream", 
        title="[COLOR gold]Acestream 1080[/COLOR]",
        thumbnail="https://i.imgur.com/FjbBFzQ.jpg",
        url= "https://textbin.net/raw/F5zvW0F0IP",
        fanart="https://i.imgur.com/FjbBFzQ.jpg",
        folder=True )      
    plugintools.add_item(  #adictosaldeporte  
        action="adictosdeporte", 
        title="[COLOR gold]Canales de Deportes[/COLOR] [COLOR red]NECESARIO VPN[/COLOR]",
        thumbnail="https://i.imgur.com/RjQPYIB.jpg",
        url= "https://adictosaldeporte.com/",
        fanart="https://i.imgur.com/RjQPYIB.jpg",
        folder=True )

######################### daddylive #########################
#############################################################
    
def daddylive (params): 
    url = params . get ( "url" )
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )
 
    matches =  re.findall(r'(?s)(\d\d:\d\d)\s(.+?):\s(.+?)<|href="(.+?)".*?#ff0000;">(.*?)<', url, re.DOTALL)
    for hora, liga, partido, url, canal in matches:  
        plugintools . add_item ( action = "wstream2" , title = "[COLOR lime]"+hora+"[/COLOR]" + "  " + "[COLOR darkorange]"+liga+"[/COLOR]" + "  " + "[COLOR blue]"+partido+"[/COLOR]" + "  " + "[COLOR yellow]"+canal+"[/COLOR]", url = url , thumbnail= "https://i.imgur.com/2bsfGN5.jpg" , fanart="https://i.imgur.com/2bsfGN5.jpg", folder = False , isPlayable = True ) 

######################### SportZonline #########################
################################################################

def SportZonline (params): 
    url = params . get ( "url" )
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )
 
    matches =  re.findall(r'(\d.*?:\d\d).*?(\w.*?)\|.*?(http.*?.php)', url, re.DOTALL)
    for hora, title, url in matches:  
         plugintools . add_item ( action = "zonlinefin" , title = "[COLOR lime]"+hora+"[/COLOR]" + "  " + "[COLOR darkorange]"+title+"[/COLOR]", url = url , thumbnail= "https://i.imgur.com/N0YcFQR.jpg" , fanart="https://i.imgur.com/N0YcFQR.jpg", folder = False , isPlayable = True ) 

def zonlinefin(params): 
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    def dailyy(url):
        import re, requests 
 
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'Referer': 'https://sportzonline.co/channels/hd/hd1.php', 'Accept' : 'application/json, text/plain, */*', 'Accept-Language' : 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3'}   
        r = requests.get(url,headers=headers, verify=False)
        contenido = r.text
        return contenido
    url=dailyy(url)
    url = 'https:'+plugintools.find_single_match(url,'iframe.+?src="(.+?)"')
    def wstram(url):
        import re, requests, resolveurl
        from resolveurl.plugins.lib import jsunpack 
        url=url
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1", "Referer":"https://sportzonline.to/channels/pt/sporttv1.php"
    }
 
        marcador = requests.get(url, headers=headers, verify=False)
        r = marcador.text
        pack=re.findall("(eval\(function\(p,a,c,k,e,d.*m3u8.*)", r)[0]
        unpack=jsunpack.unpack(pack).replace('\\', '')
        return re.findall('source:"(.*?)"', unpack)[0].replace('ul.cdn946.net', '185.39.10.72')

    url=wstram(url)
    
    plugintools.play_resolved_url( url) 
    
######################### acestream #########################
#############################################################

def acestream (params):
    url = params . get ( "url" )
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )
 
    matches =  plugintools.find_multiple_matches(url, r'(?s)title\s=\s"([^"]+).*?link.*?url=(.+?)".*?thumb\s=\s"(.+?)".*?fanart\s=\s"(.+?)"')
    for title, url, thumb, fana in matches:
        plugintools . add_item ( action = "resolve_acestream" , title = title, url = url , thumbnail = thumb, fanart = fana, folder = False , isPlayable = True )
 

######################### adictosaldeporte #########################
####################################################################


def adictosdeporte ( params ):
    url = params.get("url")  
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    header . append ( [ "Referer" , "https://adictosaldeporte.com/" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )    
    bloque = plugintools.find_single_match(url,'<center><div class="imagenes">(.*?)</div></center></div>')
    matches = re.findall(r'(?s)<a href="(.*?)" title="(.*?) en.*?><img src="(.*?)"',bloque)
    for url,title,thumb in matches: 
        plugintools . add_item ( action = 'adictos1' , title = title, url ='https:'+ url,thumbnail ='https://adictosalatele.com'+ thumb , fanart="http://perillas.mendelux.es/1xyz/kodivertido/KODIVERTIDOX.gif", folder =False,isPlayable= True)
def adictos ( params ):
    url = params.get("url")  
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    header . append ( [ "Referer" , "https://adictosaldeporte.com/" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )    
    bloque = plugintools.find_single_match(url,'<div class="imagenes">(.*?)</h4>')
    matches = re.findall(r'(?s)<td>.*?<a href="(.*?)" title="(.*?) en.*?><img src="(.*?)"',bloque)
    for url,title,thumb in matches: 
        plugintools . add_item ( action = 'adictos1' , title = title, url ='https:'+ url,thumbnail ='https://adictosalatele.com'+ thumb , fanart="http://perillas.mendelux.es/1xyz/kodivertido/KODIVERTIDOX.gif", folder =False,isPlayable= True)
def adictos1 ( params ):
    url = params.get('url')
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()    
    if 'adictosalatele' in url:
        url ='https:'+ plugintools.find_single_match(url,'(?s)<div class="video">.*?src="(.*?)"')
    else:
        url ='https:'+ plugintools.find_single_match(url,'(?s)<center><textarea.*?src="(.*?)"')
    #plugintools . add_item ( action = "" , title =url,url = url,thumbnail =  "" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True)
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    request_headers.append(["Referer","https://adictosalatele.com/tve-1-en-directo-online-gratis/"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()   
    url = plugintools.find_single_match(url,'(?s)<iframe src="(https.*?wigistream.*?)"')
    #plugintools . add_item ( action = "" , title =url,url = url,thumbnail =  "" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True)
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    request_headers.append(["Referer","https://adictosalatele.com/tve-1-en-directo-online-gratis/"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()    
    pack = plugintools.find_single_match(url,'(?s)(eval\(function\(p,a,c,k,e,d.*?)</script>')
    unpacked = jsunpack.unpack(pack).replace('\\', '')
    finalurl = plugintools.find_single_match(unpacked,'(?s)player=new Clappr.Player.*?source."(.*?)"')
    plugintools . play_resolved_url ( finalurl )                                
    #plugintools . add_item ( action = "" , title =finalurl,url = finalurl,thumbnail =  "" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder =True) 


##--------- CABECERA tdtchannels-------------##--------- CABECERA tdtchannels-------------##--------- CABECERA tdtchannels-------------##--------- CABECERA tdtchannels-------------##--------- CABECERA tdtchannels-------------##--------- CABECERA tdtchannels-------------##--------- CABECERA tdtchannels-------------##--------- CABECERA tdtchannels-------------##    
 
def tdtchannels (params):
    categorias = []
    url = params . get ( "url" )  
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )  
    matches = plugintools.find_multiple_matches(url, 'group-title="([^"]+)') 
    for categoria in sorted(matches): 
        if categoria not in categorias: 
            categorias.append(categoria)
    categorias.append("Todos")
    for x in sorted(categorias):
        plugintools . add_item ( action = "parse_tdtchannels" , title = x, url = x, thumbnail =  params.get("thumbnail") , fanart="http://perillas.mendelux.es/1xyz/kodivertido/KODIVERTIDOX.gif", folder = True)
def parse_tdtchannels ( params ):  
    categoria = params.get("url")
    if categoria == "Todos":
        categoria = '[^"]+'
    url = "https://www.tdtchannels.com/lists/tv.m3u" 
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )    
    matches = re.findall(r'tvg-logo="([^"]+)" group-title="{0}" tvg-name="[^"]+",(.*)\s*(.*)'.format(categoria),url)
    for thumb, name, url in matches:
        plugintools . add_item ( action = "resolve_without_resolveurl" , title = name, url = url, thumbnail =  thumb , fanart="http://perillas.mendelux.es/1xyz/kodivertido/KODIVERTIDOX.gif", folder = False, isPlayable = True)   
 

##--------- CABECERA canales-------------##--------- CABECERA canales-------------##--------- CABECERA canales-------------##--------- CABECERA canales-------------##--------- CABECERA canales-------------##--------- CABECERA canales-------------##--------- CABECERA canales-------------##--------- CABECERA canales-------------##    
 
 
def canales ( params ):
    url = params . get ( "url" )
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header  = plugintools .read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )
    matches =  re.findall(r'(?s)<header class="entry-.*?href="(.*?)".*?title="(.*?)".*?src="(.*?)"', url, re.DOTALL)
    for url, title,thumb, in matches:
        plugintools . add_item ( action = "canale1" , title = title, thumbnail = thumb , url = url , fanart="http://perillas.mendelux.es/1xyz/kodivertido/KODIVERTIDOX.gif", folder = True )
def canale1 ( params ):
    url = params . get ( "url" )
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header  = plugintools .read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )
    matches =  re.findall(r'(?s) - (.+?.m3u8)', url, re.DOTALL)
    for url in matches:
        plugintools . add_item ( action = "resolvers" , title = "Ver Opción", thumbnail = params . get ( "thumbnail" ), url = url , fanart="http://perillas.mendelux.es/1xyz/kodivertido/KODIVERTIDOX.gif", folder = False , isPlayable = True )
 

##--------- CABECERA tdtmun-------------##--------- CABECERA tdtmun-------------##--------- CABECERA tdtmun-------------##--------- CABECERA tdtmun-------------##--------- CABECERA tdtmun-------------##--------- CABECERA tdtmun-------------##--------- CABECERA tdtmun-------------##--------- CABECERA tdtmun-------------##    
 
 
def tdtmun (params):
    url = params . get ( "url" )
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )
 
    matches =  re.findall(r'(?s)#EXTINF:-1,(.+?)\n.*?(.+?)\s', url, re.DOTALL)
    for title, url in matches:
        plugintools . add_item ( action = "tdtmun1" , title = title, url = url , thumbnail="https://cdn.pixabay.com/photo/2017/09/12/20/23/globe-png-2743543_960_720.png" , fanart="http://perillas.mendelux.es/1xyz/kodivertido/KODIVERTIDOX.gif", folder = True )
def tdtmun1 (params): 
    url = (  ( "https://raw.githubusercontent.com/telegrambotdev/iptv/ba58c7c0b2c9c7653f6b2cd3b4b64012d854d81e/" + params . get("url") ) )
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )
 
    matches =  re.findall(r'(?s)#EXTINF:-1.*?logo="(.+?)".*?title=.*?,(.+?)\n.*?(.+?)\s', url, re.DOTALL)
    for thumb, title, url in matches:
        plugintools . add_item ( action = "resolve_without_resolveurl" , title = title , url = url , thumbnail = thumb, fanart="http://perillas.mendelux.es/1xyz/kodivertido/KODIVERTIDOX.gif", folder = False , isPlayable = True )  


##--------- CABECERA fluxus-------------##--------- CABECERA fluxus-------------##--------- CABECERA fluxus-------------##--------- CABECERA fluxus-------------##--------- CABECERA fluxus-------------##--------- CABECERA fluxus-------------##--------- CABECERA fluxus-------------##--------- CABECERA fluxus-------------##    


def fluxus (params):
    url = params . get ( "url" )
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )
 
    matches =  re.findall(r'(?s)large;"><b>(.+?)<.*?URL.*?value="(.+?)"', url, re.DOTALL)
    for title, url in matches:
        plugintools . add_item ( action = "fluxus1" , title = title, url = url , thumbnail = "https://koditips.com/wp-content/uploads/fluxus-tv-kodi.png", fanart="http://perillas.mendelux.es/1xyz/kodivertido/KODIVERTIDOX.gif", folder = True )  
def fluxus1 (params):
    url = params . get ( "url" )
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )
 
    matches =  re.findall(r'(?s)#EXTINF:-1.*?logo="(.+?)".*?,(.+?)\n.*?(.+?)\s', url, re.DOTALL)
    for thumb, title, url in matches:
        plugintools . add_item ( action = "resolve_without_resolveurl" , title = title , url = url , thumbnail = thumb, fanart="http://perillas.mendelux.es/1xyz/kodivertido/KODIVERTIDOX.gif", folder = False , isPlayable = True )  


##--------- CABECERA canalesd-------------##--------- CABECERA canalesd-------------##--------- CABECERA canalesd-------------##--------- CABECERA canalesd-------------##--------- CABECERA canalesd-------------##--------- CABECERA canalesd-------------##--------- CABECERA canalesd-------------##--------- CABECERA canalesd-------------##    


def canalesd(params):
    
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches(url,r'(?s)EXTINF.*?name=".*?".*?logo=".*?".*?http.*?\s')
    
    for match in matches:
        patron = plugintools.find_single_match ( match , r'(?s)EXTINF.*?name="(.*?)".*?logo="(.*?)".*?(http.*?)\s' )
        title = patron[0]
        thumb = patron[1]
        url = patron[2]
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = "https://i.imgur.com/E7vzz9Q.jpg" , folder = False , isPlayable = True )
 



'''

#########################################  DEPORTES Y DIRECTOS   ###########################################   DEPORTES Y DIRECTOS   ###########################################   DEPORTES Y DIRECTOS   ####################################################################################  DEPORTES Y DIRECTOS   ###########################################   DEPORTES Y DIRECTOS   ###########################################   DEPORTES Y DIRECTOS   ###########################################
##-----------------kodivertido_DEPORTES Y DIRECTOS##-------------------kodivertido_DEPORTES Y DIRECTOS#-------------------#kodivertido_DEPORTES Y DIRECTOS#-----------------------------------------------------------
##-----------------kodivertido_DEPORTES Y DIRECTOS##-------------------kodivertido_DEPORTES Y DIRECTOS#-------------------#kodivertido_DEPORTES Y DIRECTOS#-----------------------------------------------------------##-----------------kodivertido_DEPORTES Y DIRECTOS##-------------------kodivertido_DEPORTES Y DIRECTOS#-------------------#kodivertido_DEPORTES Y DIRECTOS#-----------------------------------------------------------##-----------------kodivertido_DEPORTES Y DIRECTOS##-------------------kodivertido_DEPORTES Y DIRECTOS#-------------------#kodivertido_DEPORTES Y DIRECTOS#-----------------------------------------------------------##-----------------kodivertido_DEPORTES Y DIRECTOS##-------------------kodivertido_DEPORTES Y DIRECTOS#-------------------#kodivertido_DEPORTES Y DIRECTOS#-----------------------------------------------------------##-----------------kodivertido_DEPORTES Y DIRECTOS##-------------------kodivertido_DEPORTES Y DIRECTOS#-------------------#kodivertido_DEPORTES Y DIRECTOS#-----------------------------------------------------------##-----------------kodivertido_DEPORTES Y DIRECTOS##-------------------kodivertido_DEPORTES Y DIRECTOS#-------------------#kodivertido_DEPORTES Y DIRECTOS#-----------------------------------------------------------##-----------------kodivertido_DEPORTES Y DIRECTOS##-------------------kodivertido_DEPORTES Y DIRECTOS#-------------------#kodivertido_DEPORTES Y DIRECTOS#-----------------------------------------------------------##-----------------kodivertido_DEPORTES Y DIRECTOS##-------------------kodivertido_DEPORTES Y DIRECTOS#-------------------#kodivertido_DEPORTES Y DIRECTOS#-----------------------------------------------------------##-----------------kodivertido_DEPORTES Y DIRECTOS##-------------------kodivertido_DEPORTES Y DIRECTOS#-------------------#kodivertido_DEPORTES Y DIRECTOS#-----------------------------------------------------------##-----------------kodivertido_DEPORTES Y DIRECTOS##-------------------kodivertido_DEPORTES Y DIRECTOS#-------------------#kodivertido_DEPORTES Y DIRECTOS#-----------------------------------------------------------##-----------------kodivertido_DEPORTES Y DIRECTOS##-------------------kodivertido_DEPORTES Y DIRECTOS#-------------------#kodivertido_DEPORTES Y DIRECTOS#-----------------------------------------------------------
#########################################  DEPORTES Y DIRECTOS   ###########################################   DEPORTES Y DIRECTOS   ###########################################   DEPORTES Y DIRECTOS   ####################################################################################  DEPORTES Y DIRECTOS   ###########################################   DEPORTES Y DIRECTOS   ###########################################   DEPORTES Y DIRECTOS   ###########################################





##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------
##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------


def directs(params):
    
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    matches = re.findall(r'(?s)"(.*?)".*?"(.*?)"', url, re.DOTALL)
    for title, url in matches:
        plugintools.add_item(action="resolve_without_resolveurl", title="[B][LOWERCASE][CAPITALIZE][COLOR white]" + title + "[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", url=url, fanart='https://i.imgur.com/E7vzz9Q.jpg', folder=False, isPlayable=True )


##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------
##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------##-----------------directs##-------------------directs#-------------------#directs#-----------------------------------------------------------


def DailySport(params):
    
    plugintools.set_view(plugintools.LIST)
    url = params.get("url")
    import ssl
    try:
        ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = ssl._create_unverified_context
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    matches = re.findall(r'(?s)<td><b>(.+?)</b>|<td>(\d{1,2}.*?)<|<td>(\b.+?)</td>|<td><a href="(.+?)">(.+?)</a></td>', url, re.DOTALL)
 
    for time, title, title2, url, day in matches: 
        plugintools . add_item ( action = "daily_1" , title = "[B]" + "[COLOR lime]" + time + " " + "[/COLOR]" + "[COLOR fuchsia]" + title + "[/COLOR]" + " " + "[COLOR cyan]" + title2 + "[/COLOR]" + day + "[/B]", url=url, thumbnail =  'https://i.imgur.com/GsOcanM.jpg' , fanart='https://i.imgur.com/UofLWEe.jpg',  folder = False , isPlayable = True )        


def daily_1(params):
    
    url = "https://dailysport.bar/" + params.get("url")
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    import ssl
    try:
        ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = ssl._create_unverified_context

    matches = re.findall( '(?s)p2pml.hlsjs.initClapprPlayer.*?var player = new Clappr.Player.*?window.atob."(.*?)"', url, re.DOTALL)
    
    import base64
    for url in matches:
        try:
            #url = base64.b64decode(url)
            url = (base64.b64decode(url.encode("utf-8", "strict"))).decode("utf-8", "strict")
        except:
            url = url
        xbmc.log("[COLOR lime][B]#################################### url: [/B][/COLOR]" + url, xbmc.LOGINFO)     
        plugintools.play_resolved_url(url)
        #plugintools.add_item(action="resolve_without_resolveurl", title="Ver Evento " + url, url=url, thumbnail="https://i.imgur.com/GsOcanM.jpg", folder=False, isPlayable=True)


##-----------------canalesd##-------------------canalesd#-------------------#canalesd#-----------------------------------------------------------
##-----------------canalesd##-------------------canalesd#-------------------#canalesd#-----------------------------------------------------------##-----------------canalesd##-------------------canalesd#-------------------#canalesd#-----------------------------------------------------------##-----------------canalesd##-------------------canalesd#-------------------#canalesd#-----------------------------------------------------------##-----------------canalesd##-------------------canalesd#-------------------#canalesd#-----------------------------------------------------------##-----------------canalesd##-------------------canalesd#-------------------#canalesd#-----------------------------------------------------------##-----------------canalesd##-------------------canalesd#-------------------#canalesd#-----------------------------------------------------------##-----------------canalesd##-------------------canalesd#-------------------#canalesd#-----------------------------------------------------------##-----------------canalesd##-------------------canalesd#-------------------#canalesd#-----------------------------------------------------------##-----------------canalesd##-------------------canalesd#-------------------#canalesd#-----------------------------------------------------------##-----------------canalesd##-------------------canalesd#-------------------#canalesd#-----------------------------------------------------------##-----------------canalesd##-------------------canalesd#-------------------#canalesd#-----------------------------------------------------------


def canalesd(params):
    
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches(url,r'(?s)EXTINF.*?name=".*?".*?logo=".*?".*?http.*?\s')
    
    for match in matches:
        patron = plugintools.find_single_match ( match , r'(?s)EXTINF.*?name="(.*?)".*?logo="(.*?)".*?(http.*?)\s' )
        title = patron[0]
        thumb = patron[1]
        url = patron[2]
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR yellow]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = "https://i.imgur.com/E7vzz9Q.jpg" , folder = False , isPlayable = True )
 
'''        
 



#########################################  BETAS   ###########################################   BETAS   ###########################################   BETAS   ####################################################################################  BETAS   ###########################################   BETAS   ###########################################   BETAS   ###########################################
##-----------------BETAS##-------------------BETAS#-------------------#BETAS#-----------------------------------------------------------
##-----------------BETAS##-------------------BETAS#-------------------#BETAS#-----------------------------------------------------------##-----------------BETAS##-------------------BETAS#-------------------#BETAS#-----------------------------------------------------------##-----------------BETAS##-------------------BETAS#-------------------#BETAS#-----------------------------------------------------------##-----------------BETAS##-------------------BETAS#-------------------#BETAS#-----------------------------------------------------------##-----------------BETAS##-------------------BETAS#-------------------#BETAS#-----------------------------------------------------------##-----------------BETAS##-------------------BETAS#-------------------#BETAS#-----------------------------------------------------------##-----------------BETAS##-------------------BETAS#-------------------#BETAS#-----------------------------------------------------------##-----------------BETAS##-------------------BETAS#-------------------#BETAS#-----------------------------------------------------------##-----------------BETAS##-------------------BETAS#-------------------#BETAS#-----------------------------------------------------------##-----------------BETAS##-------------------BETAS#-------------------#BETAS#-----------------------------------------------------------##-----------------BETAS##-------------------BETAS#-------------------#BETAS#-----------------------------------------------------------
#########################################  BETAS   ###########################################   BETAS   ###########################################   BETAS   ####################################################################################  BETAS   ###########################################   BETAS   ###########################################   BETAS   ###########################################





##-----------------videoclub##-------------------videoclub#-------------------#videoclub#-----------------------------------------------------------
##-----------------videoclub##-------------------videoclub#-------------------#videoclub#-----------------------------------------------------------##-----------------videoclub##-------------------videoclub#-------------------#videoclub#-----------------------------------------------------------##-----------------videoclub##-------------------videoclub#-------------------#videoclub#-----------------------------------------------------------##-----------------videoclub##-------------------videoclub#-------------------#videoclub#-----------------------------------------------------------##-----------------videoclub##-------------------videoclub#-------------------#videoclub#-----------------------------------------------------------##-----------------videoclub##-------------------videoclub#-------------------#videoclub#-----------------------------------------------------------##-----------------videoclub##-------------------videoclub#-------------------#videoclub#-----------------------------------------------------------##-----------------videoclub##-------------------videoclub#-------------------#videoclub#-----------------------------------------------------------##-----------------videoclub##-------------------videoclub#-------------------#videoclub#-----------------------------------------------------------##-----------------videoclub##-------------------videoclub#-------------------#videoclub#-----------------------------------------------------------##-----------------videoclub##-------------------videoclub#-------------------#videoclub#-----------------------------------------------------------


def videoclub(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches ( url ,r'(?s)#EXTINF:.*?\n.*?\s' )
    for match in matches:
        patron = plugintools.find_single_match ( match , r'(?s)#EXTINF:.*?,(.*?)\n(.*?)\s' )
        title = patron[0]
        url = patron[1]
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR greenyellow]" + "* " + "[B][UPPERCASE][COLOR magenta]" + title + "[B][UPPERCASE][COLOR greenyellow]" + " *" + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = "https://i.imgur.com/1VJQ5Qp.jpg" , fanart = "https://i.imgur.com/GwEkCuA.jpg" , folder = False , isPlayable = True )
 

##-----------------tv_betas##-------------------tv_betas#-------------------#tv_betas#-----------------------------------------------------------
##-----------------tv_betas##-------------------tv_betas#-------------------#tv_betas#-----------------------------------------------------------##-----------------tv_betas##-------------------tv_betas#-------------------#tv_betas#-----------------------------------------------------------##-----------------tv_betas##-------------------tv_betas#-------------------#tv_betas#-----------------------------------------------------------##-----------------tv_betas##-------------------tv_betas#-------------------#tv_betas#-----------------------------------------------------------##-----------------tv_betas##-------------------tv_betas#-------------------#tv_betas#-----------------------------------------------------------##-----------------tv_betas##-------------------tv_betas#-------------------#tv_betas#-----------------------------------------------------------##-----------------tv_betas##-------------------tv_betas#-------------------#tv_betas#-----------------------------------------------------------##-----------------tv_betas##-------------------tv_betas#-------------------#tv_betas#-----------------------------------------------------------##-----------------tv_betas##-------------------tv_betas#-------------------#tv_betas#-----------------------------------------------------------##-----------------tv_betas##-------------------tv_betas#-------------------#tv_betas#-----------------------------------------------------------##-----------------tv_betas##-------------------tv_betas#-------------------#tv_betas#-----------------------------------------------------------


def tv_betas(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    matches = plugintools.find_multiple_matches ( url , r'(?s).*?tvg-name=".*?".*?tvg-logo=".*?".*?group-title=".*?[A-Z]+ [A-Z].......*?http://listamy.com:8080/liHM1HdhS3/mWQ3MPr59p/.*?\s' )
    for match in matches:
        patron = plugintools.find_single_match ( match , r'(?s).*?tvg-name="(.*?)".*?tvg-logo="(.*?)".*?group-title=".*?([A-Z]+ [A-Z]......).*?(http://listamy.com:8080/liHM1HdhS3/mWQ3MPr59p/.*?)\s' )
        title = patron[0]
        thumb = patron[1]
        title2 = patron[2]
        url = patron[3]
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR greenyellow]" + title2 + " " + "[B][UPPERCASE][COLOR magenta]" + title + "[B][UPPERCASE][COLOR greenyellow]" + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = "https://i.imgur.com/GwEkCuA.jpg" , folder = False , isPlayable = True )
    

##-----------------deportes_betas##-------------------deportes_betas#-------------------#deportes_betas#-----------------------------------------------------------
##-----------------deportes_betas##-------------------deportes_betas#-------------------#deportes_betas#-----------------------------------------------------------##-----------------deportes_betas##-------------------deportes_betas#-------------------#deportes_betas#-----------------------------------------------------------##-----------------deportes_betas##-------------------deportes_betas#-------------------#deportes_betas#-----------------------------------------------------------##-----------------deportes_betas##-------------------deportes_betas#-------------------#deportes_betas#-----------------------------------------------------------##-----------------deportes_betas##-------------------deportes_betas#-------------------#deportes_betas#-----------------------------------------------------------##-----------------deportes_betas##-------------------deportes_betas#-------------------#deportes_betas#-----------------------------------------------------------##-----------------deportes_betas##-------------------deportes_betas#-------------------#deportes_betas#-----------------------------------------------------------##-----------------deportes_betas##-------------------deportes_betas#-------------------#deportes_betas#-----------------------------------------------------------##-----------------deportes_betas##-------------------deportes_betas#-------------------#deportes_betas#-----------------------------------------------------------##-----------------deportes_betas##-------------------deportes_betas#-------------------#deportes_betas#-----------------------------------------------------------##-----------------deportes_betas##-------------------deportes_betas#-------------------#deportes_betas#-----------------------------------------------------------


def deportes_betas(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()

    matches = plugintools.find_multiple_matches ( url , r'(?s).*?tvg-name=".*?".*?tvg-logo=".*?".*?group-title=".*?[A-Z]+ [A-Z].......*?http://listamy.com:8080/liHM1HdhS3/mWQ3MPr59p/.*?\s' )
    for match in matches:
        patron = plugintools.find_single_match ( match , r'(?s).*?tvg-name="(.*?)".*?tvg-logo="(.*?)".*?group-title=".*?([A-Z]+ [A-Z]......).*?(http://listamy.com:8080/liHM1HdhS3/mWQ3MPr59p/.*?)\s' )
        title = patron[0]
        thumb = patron[1]
        title2 = patron[2]
        url = patron[3]
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR greenyellow]" + title2 + "[/COLOR][/UPPERCASE][/B]" + " " + "[B][UPPERCASE][COLOR magenta]" + title + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = "https://i2.wp.com/sportytell.com/wp-content/uploads/2019/11/Most-popular-sports-in-the-world-right-now.jpg?fit=1280%2C720&ssl=1" , folder = False , isPlayable = True )


##-----------------taquillas_betas##-------------------taquillas_betas#-------------------#taquillas_betas#-----------------------------------------------------------
##-----------------taquillas_betas##-------------------taquillas_betas#-------------------#taquillas_betas#-----------------------------------------------------------##-----------------taquillas_betas##-------------------taquillas_betas#-------------------#taquillas_betas#-----------------------------------------------------------##-----------------taquillas_betas##-------------------taquillas_betas#-------------------#taquillas_betas#-----------------------------------------------------------##-----------------taquillas_betas##-------------------taquillas_betas#-------------------#taquillas_betas#-----------------------------------------------------------##-----------------taquillas_betas##-------------------taquillas_betas#-------------------#taquillas_betas#-----------------------------------------------------------##-----------------taquillas_betas##-------------------taquillas_betas#-------------------#taquillas_betas#-----------------------------------------------------------##-----------------taquillas_betas##-------------------taquillas_betas#-------------------#taquillas_betas#-----------------------------------------------------------##-----------------taquillas_betas##-------------------taquillas_betas#-------------------#taquillas_betas#-----------------------------------------------------------##-----------------taquillas_betas##-------------------taquillas_betas#-------------------#taquillas_betas#-----------------------------------------------------------##-----------------taquillas_betas##-------------------taquillas_betas#-------------------#taquillas_betas#-----------------------------------------------------------##-----------------taquillas_betas##-------------------taquillas_betas#-------------------#taquillas_betas#-----------------------------------------------------------


def taquillas_betas(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches ( url ,r'(?s)#EXTINF:.*?\n.*?\s' )
    for match in matches:
        patron = plugintools.find_single_match ( match , r'(?s)#EXTINF:.*?,(.*?)\n(.*?)\s' )
        title = patron[0]
        url = patron[1]
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR greenyellow]" + "* " + "[B][UPPERCASE][COLOR magenta]" + title + "[B][UPPERCASE][COLOR greenyellow]" + " *" + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = "http://perillas.mendelux.es/1xyz/kodivertido/taquillas.png" , fanart = "https://i.imgur.com/E7vzz9Q.jpg" , folder = False , isPlayable = True )
 

##-----------------cochinos_betas##-------------------cochinos_betas#-------------------#cochinos_betas#-----------------------------------------------------------
##-----------------cochinos_betas##-------------------cochinos_betas#-------------------#cochinos_betas#-----------------------------------------------------------##-----------------cochinos_betas##-------------------cochinos_betas#-------------------#cochinos_betas#-----------------------------------------------------------##-----------------cochinos_betas##-------------------cochinos_betas#-------------------#cochinos_betas#-----------------------------------------------------------##-----------------cochinos_betas##-------------------cochinos_betas#-------------------#cochinos_betas#-----------------------------------------------------------##-----------------cochinos_betas##-------------------cochinos_betas#-------------------#cochinos_betas#-----------------------------------------------------------##-----------------cochinos_betas##-------------------cochinos_betas#-------------------#cochinos_betas#-----------------------------------------------------------##-----------------cochinos_betas##-------------------cochinos_betas#-------------------#cochinos_betas#-----------------------------------------------------------##-----------------cochinos_betas##-------------------cochinos_betas#-------------------#cochinos_betas#-----------------------------------------------------------##-----------------cochinos_betas##-------------------cochinos_betas#-------------------#cochinos_betas#-----------------------------------------------------------##-----------------cochinos_betas##-------------------cochinos_betas#-------------------#cochinos_betas#-----------------------------------------------------------##-----------------cochinos_betas##-------------------cochinos_betas#-------------------#cochinos_betas#-----------------------------------------------------------


def cochinos_betas(params):
    url = params.get ( "url" )
    request_headers = []
    request_headers.append ( ["User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"] )
    read_url, response_headers = plugintools.read_body_and_headers ( url , headers = request_headers )
    url = read_url.strip ()
    
    matches = plugintools.find_multiple_matches ( url ,r'(?s)#EXTINF.+?name=".*?".*?logo=".*?"+.*?\n.*?\s' )
    for match in matches:
        patron = plugintools.find_single_match ( match , r'(?s)#EXTINF.+?name="(.*?)".*?logo="(.*?)"+.*?\n(.*?)\s' )
        title = patron[0]
        url = patron[2]
        thumb = patron[1]
        if thumb.startswith("http://"):
            thumb= thumb 
        else:
            thumb = "https://i.imgur.com/29b9UAP.jpg"  
                 
        plugintools.add_item ( action = "resolve_without_resolveurl" , title = "[B][UPPERCASE][COLOR greenyellow]" + "* " + "[B][UPPERCASE][COLOR magenta]" + title + "[B][UPPERCASE][COLOR greenyellow]" + " *" + "[/COLOR][/UPPERCASE][/B]" , url = url , thumbnail = thumb , fanart = "https://i.imgur.com/mxHSw8B.jpg" , folder = False , isPlayable = True )
   
   
   
   
##-----------------TEST_betas##-------------------TEST_betas#-------------------#TEST_betas#-----------------------------------------------------------
##-----------------TEST_betas##-------------------TEST_betas#-------------------#TEST_betas#-----------------------------------------------------------##-----------------TEST_betas##-------------------TEST_betas#-------------------#TEST_betas#-----------------------------------------------------------##-----------------TEST_betas##-------------------TEST_betas#-------------------#TEST_betas#-----------------------------------------------------------##-----------------TEST_betas##-------------------TEST_betas#-------------------#TEST_betas#-----------------------------------------------------------##-----------------TEST_betas##-------------------TEST_betas#-------------------#TEST_betas#-----------------------------------------------------------##-----------------TEST_betas##-------------------TEST_betas#-------------------#TEST_betas#-----------------------------------------------------------##-----------------TEST_betas##-------------------TEST_betas#-------------------#TEST_betas#-----------------------------------------------------------##-----------------TEST_betas##-------------------TEST_betas#-------------------#TEST_betas#-----------------------------------------------------------##-----------------TEST_betas##-------------------TEST_betas#-------------------#TEST_betas#-----------------------------------------------------------##-----------------TEST_betas##-------------------TEST_betas#-------------------#TEST_betas#-----------------------------------------------------------##-----------------TEST_betas##-------------------TEST_betas#-------------------#TEST_betas#-----------------------------------------------------------


##--------- CABECERA TEST_betas-------------##--------- CABECERA TEST_betas-------------##--------- CABECERA TEST_betas-------------##--------- CABECERA TEST_betas-------------##--------- CABECERA TEST_betas-------------##--------- CABECERA TEST_betas-------------##--------- CABECERA TEST_betas-------------##--------- CABECERA TEST_betas-------------##
 
  
  
  
def test_betas(params):
    
    plugintools.add_item(action = "menu_cliver_mas_vistas" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white] PORTADA [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/4DBQ44t.jpg",fanart = "https://lh3.googleusercontent.com/KvDD0bxSYCxpa4dppzxnNK9GC7gXmoNKlGchQGpo4wcP-KHWWkL1Uls051tAU_mKEg",page='1',url= 'https://cliver.site/peliculas/estrenos?tipo=index&page=', folder=True )
  
def menu_cliver_mas_vistas(params): 
    #plugintools.log("chopolatino.menu_cliver_mas_vistas")


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua] PELICULAS [COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://cliver.site/static/img/logo.png",fanart = "https://lh3.googleusercontent.com/KvDD0bxSYCxpa4dppzxnNK9GC7gXmoNKlGchQGpo4wcP-KHWWkL1Uls051tAU_mKEg",  folder = False )
    thumbnail = params.get("thumbnail")
    url8 = params.get("url")
    page = params.get("page")
    url = url8 + page
    page =str(int(page)+1)
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()     
    data = plugintools.find_multiple_matches(url,'((?s)<div class="portada-p">.*?href="/pelicula/.*?".*?<img src=".*?" alt=".*?".*?<div class="titulo-p">.*?<span>.*?<)')

    
    for generos in data:
        
        patron = plugintools.find_single_match(generos,'(?s)<div class="portada-p">.*?href="(/pelicula/.*?)".*?<img src="(.*?)" alt="(.*?)".*?<div class="titulo-p">.*?<span>(.*?)<')
        url ="https://cliver.site"+ patron [0]
        titulo = patron [2]
        foto ='https:'+ patron [1] 


        plugintools.add_item(action = "menu_cliver_pelis" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[COLOR red]""[/B][/COLOR][/CAPITALIZE][/LOWERCASE]",thumbnail =foto, fanart =foto,url =url,  folder=True )
    
    
    plugintools.add_item( action="menu_cliver_mas_vistas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow] ir a la pagina siguiente[COLOR lime] "+page+" [/B][/COLOR][/CAPITALIZE][/LOWERCASE]",page=page ,url=url8 , thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True )

    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua] PELIS [COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail ="https://cliver.site/static/img/logo.png",fanart = "https://lh3.googleusercontent.com/KvDD0bxSYCxpa4dppzxnNK9GC7gXmoNKlGchQGpo4wcP-KHWWkL1Uls051tAU_mKEg",  folder = False )    

#https://stream01.peliscloud.net/public/dist/index.html?id=ad6152375fbe33a9c8b823d555a8377e
#(?s)video="(https://stream01.*?)".*?src=.*?>(.*?)<
def menu_cliver_pelis(params):
    
    url = params.get ( "url" )
    thumbnail = params.get("thumbnail")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua] OPCIONES [COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail = thumbnail,fanart = "https://lh3.googleusercontent.com/KvDD0bxSYCxpa4dppzxnNK9GC7gXmoNKlGchQGpo4wcP-KHWWkL1Uls051tAU_mKEg" )
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()     
    data = plugintools.find_multiple_matches(url,'((?s)video="https://stream01.*?".*?src=.*?contenido)')
    
    for generos in data:
        
        patron = plugintools.find_single_match(generos,'(?s)video="(https://stream01.*?)".*?src=.*?>(.*?)<')
        url = patron [0]
        titulo = patron [1]
        
        plugintools.add_item(action = "resolve_without_resolveurl" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[COLOR red]""[/B][/COLOR][/CAPITALIZE][/LOWERCASE]",thumbnail =thumbnail, fanart = thumbnail, url =url)
  



   
    
def keyboard_input(default_text="" , title="" , hidden=False):
    keyboard = xbmc.Keyboard ( default_text , title , hidden )
    keyboard.doModal ()

    if (keyboard.isConfirmed ()):
        tecleado = keyboard.getText ()
    else:
        tecleado = ""

    return tecleado


def elementum_pctfenix1(params):
    import resolveurl
    finalurl = (("plugin://plugin.video.elementum/play?uri=https:" + params.get ( "url" )))
    plugintools.play_resolved_url ( finalurl )


def resolve_resolveurl(params):
    import resolveurl
    finalurl = resolveurl.resolve ( params.get ( "url" ) )
    plugintools.play_resolved_url ( finalurl )


def resolve_without_resolveurl(params):
    import resolveurl
    finalurl = (params.get ( "url" ))
    plugintools.play_resolved_url ( finalurl )


def torrent_elementum_grandtorrent(params):
    import resolveurl
    finalurl = (params.get ( "plugin://plugin.video.elementum/play?uri=url" ))
    plugintools.play_resolved_url ( finalurl )


def elementum_gran(params):
    import resolveurl
    finalurl = (
        ("plugin://plugin.video.elementum/play?uri=https://grantorrent.nl/download_tt.php?u=" + params.get ( "url" )))
    plugintools.play_resolved_url ( finalurl )


def elementum(params):
    import resolveurl
    finalurl = (("plugin://plugin.video.elementum/play?uri=" + params.get ( "url" )))
    plugintools.play_resolved_url ( finalurl )

def play(params):
    import resolveurl
    url = (params.get ( "url" ))
    finalurl = url.encode("utf-8", "strict")
    plugintools.play_resolved_url ( finalurl )  

def resolve_acestream ( params ) :
    import resolveurl
    finalurl = "plugin://program.plexus/?url={}&mode=1&name={}".format(params.get("url"),params.get("title"))
    plugintools . play_resolved_url ( finalurl )     
     
run()