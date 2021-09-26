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
import unicodedata
import base64
import requests
import shutil
import base64
import time
import six
import xbmcvfs
addon = xbmcaddon.Addon()
addonname = '[B][LOWERCASE][CAPITALIZE][COLOR white]KODIvertiDO_fuentes[COLOR gold]Kodi[/CAPITALIZE][/LOWERCASE][/B][/COLOR]'
icon = addon.getAddonInfo('icon')
myaddon = xbmcaddon.Addon("plugin.KODIvertiDO_fuentesKodi")
Set_Color = myaddon.getSetting('SetColor')
Set_View = myaddon.getSetting('SetView')

def run():
 
    plugintools.set_view(plugintools.LIST)
 
    # Get params
    params = plugintools.get_params()
 
    if params.get("action") is None:
        main_list(params)
    else:
       action = params.get("action")
       url = params.get("url")
       exec(action+"(params)")
    plugintools.close_item_list()
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

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow] kodivertidoteam[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://imgur.com/a/TDCvMxI", fanart = "https://imgur.com/a/kmDBgGd",  folder = False )   

    
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]A C T U A L I Z A D O R [COLOR yelllow]   D E [COLOR white]  F U E N T E S[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail ="https://imgur.com/a/TDCvMxI", fanart = "https://imgur.com/a/kmDBgGd",  folder = False ) 

 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow] kodivertidoteam[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://imgur.com/a/TDCvMxI", fanart = "https://imgur.com/a/kmDBgGd",  folder = False )   


    if six.PY2:
        translatePath = xbmc.translatePath
    elif six.PY3:
        translatePath = xbmcvfs.translatePath


    r = requests.get("https://pastebin.com/raw/QzC8ujfd")
    t = r.text
    sources = xbmc.translatePath('special://profile/sources.xml')    
    respuesta = xbmcgui.Dialog().yesno("[COLOR blue]"+"KODIvertiDO TEAM"+"[/COLOR]", "[COLOR yellow]"+"Script desarollado por"+"[COLOR blue]"+" Mendelux"+"[COLOR yellow]"+" para el grupo"+"[COLOR blue]"+" KODIvertidoTEAM."+"[COLOR yellow]"+"Pulsa el Ok par borrar tus fuentes y añadir las pricipales"+" fuentes actulizadas."+"[COLOR lightpink]"+" Reiniciar Kodi para que coja los cambios."+"[/COLOR]", "No","Si")
   

    if respuesta:       
        if not os.path.isfile(sources):
            file = open(sources, 'w+')
            source_data = file.read()
            #file.truncate(0)
            file.seek(0)
            for linea in t:
                file.write(linea)
            file.seek(0)    
            file.close()
            xbmcgui.Dialog().notification('[COLOR blue]'+'KODIvertiDO'+'[/COLOR]', '[COLOR lightgreen]'+'COPIA DE FUENTES REALIZADA EXITOSAMENTE.'+'[/COLOR]', xbmcgui.NOTIFICATION_INFO, 5000)
            
        else:
            file = open(sources,'w+')
            file.seek(0)
            file.truncate(0)
            for linea in t:
                file.write(linea)
            file.seek(0)    
            file.close()
            xbmcgui.Dialog().notification('KODIvertiDO', 'COPIA DE FUENTES REALIZADA EXITOSAMENTE.', xbmcgui.NOTIFICATION_INFO, 5000)
            
    else:
        xbmcgui.Dialog().notification('Info', 'CANCELADA LA COPIA DE FUENTES.', xbmcgui.NOTIFICATION_ERROR, 4000) 
    exit(0)            
run()