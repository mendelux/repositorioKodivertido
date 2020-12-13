# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
#------------------------------------------------------------

import os, re
import sys
import plugintools
import xbmc,xbmcaddon,xbmcgui
import requests,urllib2
import base64
myaddon =xbmcaddon .Addon ()
  
def log(message):
    xbmc.log(str(message),xbmc.LOGNOTICE)  

def run():
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec (action+"(params)")
    
    plugintools.close_item_list()

def main_list(params): 
    
          
    plugintools.add_item( 
        action="kodivertido_tv", 
        title="KODIvertiDO TV",
        thumbnail="https://i.imgur.com/VLuTfNH.jpg",
        url= "http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_tv",
        url2 = "http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_tv1",
		fanart="https://i.imgur.com/bP8hAy7.jpg",
        folder=True )   
    plugintools.add_item( 
        action="taquillas_tv", 
        title="TAQUILLAS",
        thumbnail="https://i0.pngocean.com/files/322/879/682/centre-stage-ticket-box-office-cinema-bar-ticket-thumb.jpg",
        url= "http://perillas.mendelux.es/1xyz/kodivertido/taquillas_test11",
		fanart="https://i.imgur.com/bP8hAy7.jpg",
        folder=True )
    
def kodivertido_tv (params):  
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 plugintools . add_item ( action = "kodivertido_tv1" , title = "[B][I][COLOR lightyellow]LISTA DE CANALES 1[/B][/I][/COLOR]" , url = url , thumbnail = "https://images-na.ssl-images-amazon.com/images/I/81slb674nLL.png" , folder = True , isPlayable = False) 
 plugintools . add_item ( action = "kodivertido_tv2" , title = "[B][I][COLOR lightpink]LISTA DE CANALES 2[/B][/I][/COLOR]" , url = url2 , thumbnail = "https://images-na.ssl-images-amazon.com/images/I/81slb674nLL.png" , folder = True , isPlayable = False)
 
def kodivertido_tv1 (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s).*?tvg-name="(.+?)".*?(http:\/\/.*?\/.*?\/.*?\/\d+)', url, re.DOTALL)
 for title, thumb, url in matches:
  plugintools . add_item ( action = "resolve_without_resolveurl" , title = title , url = url , thumbnail = thumb , folder = False , isPlayable = True)

def resolve_without_resolveurl ( params ) :
 import resolveurl
 finalurl =  ( params . get ( "url" ) ) 
 plugintools . play_resolved_url ( finalurl )

def kodivertido_tv2 (params):
 
 url2 = params . get ( "url2" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url2 , read_header = plugintools . read_body_and_headers ( url2 , headers = header )
 url2 = read_url2 . strip ( )
 matches =  re.findall(r'(?s)tvg-name=\"([^"]+).*?(http.+?)\s', url2, re.DOTALL)
 for title, thumb, url2 in matches:
  plugintools . add_item ( action = "resolve_without_resolveurl1" , title = title , url = url2 , thumbnail = thumb , folder = False , isPlayable = True)

def resolve_without_resolveurl1 ( params ) :
 import resolveurl
 finalurl =  ( params . get ( "url2" ) ) 
 plugintools . play_resolved_url ( finalurl )
  
def taquillas_tv (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)<title>(.*?)<.+?<link>(.*?)<.+?<thumbnail>(.*?)<.+?<fanart>(.*?)<', url, re.DOTALL)
 for title, url, thumb, fanart in matches:
  plugintools . add_item ( action = "resolve_without_resolveurl" , title = title , url = url , thumbnail = thumb , fanart = fanart , folder = False , isPlayable = True)

def resolve_without_resolveurl ( params ) :
  import resolveurl
  finalurl =  ( params . get ( "url" ) ) 
  plugintools . play_resolved_url ( finalurl )      

# Main menu
 


run()
