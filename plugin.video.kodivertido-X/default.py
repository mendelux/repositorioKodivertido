# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Thanks to the Authors of the base code
# ------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# ------------------------------------------------------------

import os, re
import sys
import plugintools
import xbmc, xbmcaddon, xbmcgui
import xbmcplugin
import requests, urllib2
import base64
import six
myaddon = xbmcaddon.Addon()

if six.PY2:
    translatePath =  xbmc.translatePath
elif six.PY3:
 translatePath = xbmcvfs.translatePath 

def log(message):
    xbmc.log(str(message), xbmc.LOGNOTICE)


def run():
    # Get params
    params = plugintools.get_params()

    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec(action + "(params)")

    plugintools.close_item_list()


# ###########################################   MENU  ###########################################

class Password:
    def __init__(self):
        self.password = plugintools.read("http://perillas.mendelux.es/password.txt").split('"')[1].split('"')[0]
        self.profile = translatePath(xbmcaddon .Addon () .getAddonInfo ('profile')) if six.PY3 else translatePath(xbmcaddon .Addon () .getAddonInfo ('profile').decode("utf-8"))
        self.passfile= self.profile+'clave.txt' 
        
    def check(self):
        global password_file
        if not os.path.isfile(self.passfile):
                password = xbmcgui.Dialog().input('Introduzca la contraseña para entrar al Addon:')
                if password == plugintools.read("http://perillas.mendelux.es/password.txt").split('"')[1].split('"')[0]:
                        if not os.path.exists(self.profile): os.makedirs(self.profile)
                        password_file= self.passfile
                        f = open(password_file,'wb')
                        f.write(password)
                        return True
                else:
                        return False
        else:
                password_file = self.passfile
                with open(self.passfile,'r') as f:
                    password = f.read()
                if password == plugintools.read("http://perillas.mendelux.es/password.txt").split('"')[1].split('"')[0]:
                    return True
                else:
                    return False
 

def main_list(params):
    
    if Password().check()==True:
        
        plugintools.add_item(
            action="",
            title="[COLOR gold][B]***********************************[/B][/COLOR]",
            thumbnail="https://i.imgur.com/rpIKSHm.jpg",
            url="",
            fanart="https://i.imgur.com/jXzIxPF.jpg",
            folder=False)
        plugintools.add_item(
            action="",
            title="[COLOR dodgerblue][B]KODI [COLOR yellow]verti[/COLOR][COLOR magenta] DO[/COLOR] [COLOR lawngreen] X[/B][/COLOR]"
                  "- [COLOR dodgerblue][B]KODI [COLOR yellow]verti[/COLOR][COLOR magenta] DO[/COLOR] [COLOR lawngreen] "
                  "X[/B][/COLOR]",
            thumbnail="https://i.imgur.com/rpIKSHm.jpg",
            url="",
            fanart="https://i.imgur.com/jXzIxPF.jpg",
            folder=False)
        plugintools.add_item(
            action="",
            title="[COLOR gold][B]***********************************[/B][/COLOR]",
            thumbnail="https://i.imgur.com/rpIKSHm.jpg",
            url="",
            fanart="https://i.imgur.com/jXzIxPF.jpg",
            folder=False)

        plugintools.add_item(
            action="kodivertido_tv",
            title="[COLOR lime][B]KODIvertiDO[/COLOR] [COLOR yellow]TV[/B][/COLOR]",
            thumbnail="http://perillas.mendelux.es/1xyz/kodivertido/tv.png",
            url="",
            fanart="https://i.imgur.com/bP8hAy7.jpg",
            folder=True)
        plugintools.add_item(
            action="kodivertido_taquillas",
            title="[COLOR lime][B]TAQUILLAS[/COLOR] [COLOR yellow]MOVISTAR[/B][/COLOR]",
            thumbnail="http://perillas.mendelux.es/1xyz/kodivertido/taquillas.png",
            url="http://perillas.mendelux.es/1xyz/kodivertido/taquillas1",
            fanart="https://i.imgur.com/bP8hAy7.jpg",
            folder=True)
        plugintools.add_item(
            action="cine_kodivertido",
            title="[COLOR lime][B]Cine [/B][/COLOR][COLOR aqua][B]KODI[/B][/COLOR][COLOR yellow][B]verti[/B][/COLOR]["
                  "COLOR white][B]DO[/B][/COLOR]",
            thumbnail="https://cdn0.iconfinder.com/data/icons/film-making/49/10-512.png",
            url="",
            fanart="https://i.imgur.com/bP8hAy7.jpg",
            folder=True)
        plugintools.add_item(
            action="series",
            title="[COLOR lime][B]SERIES [/B][/COLOR][COLOR aqua][B]KODI[/B][/COLOR][COLOR yellow][B]verti[/B]["
                  "/COLOR][COLOR white][B]DO[/B][/COLOR]",
            thumbnail="https://i.imgur.com/GNCzAMt.jpg",
            url="",
            fanart="https://i.imgur.com/bP8hAy7.jpg",
            folder=True)
        plugintools.add_item(
            action="deportes",
            title="[COLOR lime][B]DEPORTES[/COLOR] y [COLOR yellow]DIRECTOS[/B][/COLOR]",
            thumbnail="https://i.imgur.com/E7vzz9Q.jpg",
            url="http://perillas.mendelux.es/1xyz/kodivertido/directos_dailysport",
            fanart="https://i.imgur.com/bP8hAy7.jpg",
            folder=True)
        plugintools.add_item(
            action="betas",
            title="[COLOR lightpink]KODI[/COLOR][COLOR red]vertido[/COLOR][COLOR lightpink]DO[/COLOR][COLOR red][B] "
                  "BETAS[/B][/COLOR]",
            thumbnail="https://images.emojiterra.com/google/android-pie/512px/2622.png",
            url="http://perillas.mendelux.es/1xyz/kodivertido/videoclub",
            fanart="https://i.imgur.com/bP8hAy7.jpg",
            folder=True)
    else:
        xbmcgui .Dialog ().notification ('Info','Contraseña Incorrecta',xbmcgui .NOTIFICATION_ERROR ,4000 )
        os.remove(password_file)
        main_list(params) 
#  ###########################################  SUBMENUS   ###########################################


def kodivertido_tv(params):
    plugintools.add_item(
        action="kodivertido_tdt",
        title="[COLOR darkorange][B]Kodivertido [COLOR blue]TDT[/B][/COLOR]",
        thumbnail="http://perillas.mendelux.es/1xyz/kodivertido/tdt.png",
        url="http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_tdt",
        fanart="https://i.imgur.com/bP8hAy7.jpg",
        folder=True)
    plugintools.add_item(
        action="kodivertido_movistar",
        title="[COLOR darkorange][B]Kodivertido [COLOR blue]MOVISTAR+[/B][/COLOR]",
        thumbnail="http://perillas.mendelux.es/1xyz/kodivertido/vomistar.png",
        url="http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_mvstar",
        fanart="https://i.imgur.com/bP8hAy7.jpg",
        folder=True)
    plugintools.add_item(
        action="kodivertido_documentales",
        title="[COLOR darkorange][B]Kodivertido [COLOR blue]DOCUMENTALES[/B][/COLOR]",
        thumbnail="https://i.imgur.com/Ds14DOT.jpg",
        url="http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_documentales",
        fanart="https://i.imgur.com/bP8hAy7.jpg",
        folder=True)
    plugintools.add_item(
        action="kodivertido_infantiles",
        title="[COLOR darkorange][B]Kodivertido [COLOR blue]INFANTILES[/B][/COLOR]",
        thumbnail="https://www.conmishijos.com/uploads/ocio_familia/television_boing.jpg",
        url="http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_infantiles",
        fanart="https://www.salud.mapfre.es/wp-content/uploads/2018/02/exceso-de-az%C3%BAcar-en-ni%C3%B1os-compressor"
               "-1280x720.jpg",
        folder=True)
    plugintools.add_item(
        action="kodivertido_deportes",
        title="[COLOR darkorange][B]Kodivertido [COLOR blue]DEPORTES[/B][/COLOR]",
        thumbnail="https://i.imgur.com/Apj1Umv.jpg",
        url="http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_deportes",
        fanart="https://i.imgur.com/UofLWEe.jpg"
               "-1280x720.jpg",
        folder=True)
    plugintools.add_item(
        action="kodivertido_musica",
        title="[COLOR darkorange][B]Kodivertido [COLOR blue]MUSICA[/B][/COLOR]",
        thumbnail="https://i.imgur.com/e4TAxwf.jpg",
        url="http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_musicales",
        fanart="https://i.imgur.com/iVR6LkL.jpg"
               "-1280x720.jpg",
        folder=True)
    plugintools.add_item(
        action="kodivertido_cochinos",
        title="[COLOR darkorange][B]Kodivertido [COLOR blue]COCHINOS[/B][/COLOR]",
        thumbnail="https://i.imgur.com/gckjRde.jpg",
        url="http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_cochinos",
        fanart="https://i.imgur.com/b8zWTwf.jpg"
               "-1280x720.jpg",
        folder=True)


def cine_kodivertido(params):
    plugintools.add_item(  # GranTorrent
        action="grantorrent",
        title="[COLOR lime][B]G R A N   [/B][/COLOR][COLOR lime][B]T O [/B][/COLOR][COLOR yellow][B]R[/B][/COLOR]["
              "COLOR white][B] R E N T[/B][/COLOR]",
        thumbnail="https://i.imgur.com/uWqZDRQ.jpg",
        url="",
        fanart="https://i.ytimg.com/vi/7D82gt558g4/maxresdefault.jpg",
        folder=True)
    plugintools.add_item(
        action="cine_pctfenix",
        title="[COLOR lime][B]C I N E    [/B][/COLOR][COLOR lime][B]P C[/B][/COLOR][COLOR yellow][B] T[/B][/COLOR]["
              "COLOR white][B]   F E N I X[/B][/COLOR][COLOR lightpink][B]  --> Necesario   ELEMENTUM <--[/B][/COLOR]",
        thumbnail="https://i.imgur.com/594d676.jpg",
        url="",
        fanart="https://i.imgur.com/594d676.jpg",
        folder=True)
    plugintools.add_item(
        action="cine_videoclub",
        title="[COLOR lightpink]KODI[/COLOR][COLOR aqua]vertido[/COLOR][COLOR lightpink]DO[/COLOR][COLOR yellow][B] VIDEOCLUB[/B][/COLOR]",
        thumbnail="https://i.imgur.com/pmzImSy.jpg",
        url="http://perillas.mendelux.es/1xyz/kodivertido/kodivertido_cine1",
        fanart="https://i.imgur.com/pmzImSy.jpg",
        folder=True)


def grantorrent(params):
    plugintools.add_item(  # hdrip
        action="hdrip",
        title="Grantorrent HDRip",
        thumbnail="https://i.imgur.com/uWqZDRQ.jpg",
        url="https://grantorrent.nl/categoria/HDRip-2/",
        fanart="https://i.ytimg.com/vi/7D82gt558g4/maxresdefault.jpg",
        folder=True)
    plugintools.add_item(  # blueray
        action="blueray",
        title="Grantorrent Bluray-1080p",
        thumbnail="https://i.imgur.com/uWqZDRQ.jpg",
        url="https://grantorrent.nl/categoria/BluRay-1080p/",
        fanart="https://i.ytimg.com/vi/7D82gt558g4/maxresdefault.jpg",
        folder=True)
    plugintools.add_item(  # 4K
        action="cuatrok",
        title="Grantorrent 4K",
        thumbnail="https://i.imgur.com/uWqZDRQ.jpg",
        url="https://grantorrent.nl/categoria/4k-2/",
        fanart="https://i.ytimg.com/vi/7D82gt558g4/maxresdefault.jpg",
        folder=True)
    plugintools.add_item(  # 4K
        action="grantorrent_search",
        title="Buscar",
        thumbnail="https://i.imgur.com/uWqZDRQ.jpg",
        url="https://grantorrent.nl/?s=",
        fanart="https://i.ytimg.com/vi/7D82gt558g4/maxresdefault.jpg",
        folder=True)


def cine_pctfenix(params):
    plugintools.add_item(  # fullbluray_1080p
        action="fullbluray_1080p",
        title="PCTFenix FullBluRay-1080p",
        thumbnail="https://i.imgur.com/594d676.jpg",
        url="https://pctfenix.com/descargar-peliculas/fullbluray-1080p/",
        fanart="https://i.imgur.com/594d676.jpg",
        folder=True)
    plugintools.add_item(  # bluray_1080p
        action="bluray_1080p",
        title="PCTFenix BluRay-1080p",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url="https://pctfenix.com/descargar-peliculas/bluray-1080p/",
        fanart="https://i.imgur.com/maslpiV.jpg",
        folder=True)
    plugintools.add_item(  # dbremux_1080p
        action="dbremux_1080p",
        title="PCTFenix DBremux-1080p",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url="https://pctfenix.com/descargar-peliculas/bdremux-1080p/",
        fanart="https://i.imgur.com/maslpiV.jpg",
        folder=True)
    plugintools.add_item(  # cuatrok_uhdremux
        action="cuatrok_uhdremux",
        title="PCTFenix 4k-UHDremux",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url="https://pctfenix.com/descargar-peliculas/4k-uhdremux/",
        fanart="https://i.imgur.com/maslpiV.jpg",
        folder=True)
    plugintools.add_item(  # 4k uhdmicro
        action="cuatrok_uhdmicro",
        title="PCTFenix 4k-UHDmicro",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url="https://pctfenix.com/descargar-peliculas/4k-uhdmicro/",
        fanart="https://i.imgur.com/maslpiV.jpg",
        folder=True)
    plugintools.add_item(  # 4k uhdrip
        action="cuatrok_uhdrip",
        title="PCTFenix 4k-UHDrip",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url="https://pctfenix.com/descargar-peliculas/4k-uhdrip/",
        fanart="https://i.imgur.com/maslpiV.jpg",
        folder=True)
    plugintools.add_item(  # 4k webrip
        action="cuatrok_webrip",
        title="PCTFenix 4k-WEBrip",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url="https://pctfenix.com/descargar-peliculas/4k-webrip/",
        fanart="https://i.imgur.com/maslpiV.jpg",
        folder=True)
    plugintools.add_item(  # Full UHD4K
        action="full_uhdcuatrok",
        title="PCTFenix Full-UHD4K",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url="https://pctfenix.com/descargar-peliculas/full-uhd4k/",
        fanart="https://i.imgur.com/maslpiV.jpg",
        folder=True)
    plugintools.add_item(  # MicroHD 1080p
        action="microhd_1080p",
        title="PCTFenix MicroHD-1080p",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url="https://pctfenix.com/descargar-peliculas/microhd-1080p/",
        fanart="https://i.imgur.com/maslpiV.jpg",
        folder=True)


def series(params):
    plugintools.add_item(  # GranTorrent_series_nor
        action="grantorrent_series_nor",
        title="[COLOR yellow][B]GRANTORRENT[/B][/COLOR]",
        thumbnail="https://i.imgur.com/GNCzAMt.jpg",
        url="https://grantorrent.nl/series/",
        fanart="https://i.imgur.com/MK6Lqu2.jpg",
        folder=True)
    plugintools.add_item(  # GranTorrent_series_genero
        action="grantorrent_series",
        title="[COLOR yellow][B]Grantorrent Por Genero[/B][/COLOR]",
        thumbnail="https://i.imgur.com/GNCzAMt.jpg",
        url="https://pastebin.com/raw/YxDc4tZZ",
        fanart="https://i.imgur.com/MK6Lqu2.jpg",
        folder=True)
    plugintools.add_item(  # mitorrent_series
        action="mitorrent_series",
        title="[COLOR yellow][B]Mi Torrent[/B][/COLOR]",
        thumbnail="https://i.imgur.com/GNCzAMt.jpg",
        url="https://mitorrent.org/series/",
        fanart="https://i.imgur.com/MK6Lqu2.jpg",
        page="1",
        folder=True)
    plugintools.add_item(  # cinetorrent_series
        action="cinetorrent_series",
        title="[COLOR yellow][B]Cine Torrent[/B][/COLOR]",
        thumbnail="https://i.imgur.com/GNCzAMt.jpg",
        url="http://cinetorrent.co/series/",
        fanart="https://i.imgur.com/MK6Lqu2.jpg",
        page="1",
        folder=True)


def deportes(params):
    plugintools.add_item(
        action="directs",
        title="[COLOR lime][B]Directos[/COLOR] [COLOR bluemarine]KODIvertiDO[/B][/COLOR]",
        thumbnail="https://i.imgur.com/E7vzz9Q.jpg",
        url="http://perillas.mendelux.es/1xyz/kodivertido/directos_dailysport",
        fanart="https://i.imgur.com/E7vzz9Q.jpg",
        folder=True)
    plugintools.add_item(
        action="DailySport",
        title="[COLOR yellow][B]Agenda DailySport[/B][/COLOR]",
        thumbnail="https://i.imgur.com/NCftJ3F.jpg",
        url="https://dailysport.site/",
        fanart="https://i.imgur.com/E7vzz9Q.jpg",
        folder=True)
    plugintools.add_item(
        action="canalesd",
        title="[COLOR lime][B]Canales Deportivos[/B][/COLOR]",
        thumbnail="https://img96.xooimage.com/files/f/1/0/canales-3f3a25c.jpg",
        url="http://perillas.mendelux.es/1xyz/kodivertido/tv_deportes",
        fanart="https://i.imgur.com/E7vzz9Q.jpg",
        folder=True)


def betas(params):
    plugintools.add_item(
        action="videoclub",
        title="[COLOR lime]*[/COLOR][COLOR lightpink] KODI[/COLOR][COLOR aqua]vertido[/COLOR][COLOR lightpink]DO[/COLOR][COLOR yellow][B] "
              "VIDEOCLUB[/B][/COLOR]",
        thumbnail="https://i.imgur.com/SjSFzwc.jpg",
        url="http://perillas.mendelux.es/1xyz/kodivertido/videoclub",
        fanart="https://i.imgur.com/kdhPyKm.jpg",
        folder=True)   
    plugintools.add_item(
        action="tv_betas",
        title="[B][LOWERCASE][CAPITALIZE][COLOR lime]*[COLOR turquoise][COLOR white] canales de la [COLOR gold]lista "
              "kodivertido TV[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",
        thumbnail="https://i.imgur.com/Fi0nmaU.jpg",
        url="http://perillas.mendelux.es/1xyz/kodivertido/tv_betas",
        fanart="https://i.imgur.com/5dGZ06p.jpg",
        folder=True)
    plugintools.add_item(
        action="deportes_betas",
        title="[B][LOWERCASE][CAPITALIZE][COLOR lime]*[COLOR turquoise][COLOR white] canales de la [COLOR gold]lista "
              "kodivertido DEPORTES[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",
        thumbnail="https://lh3.googleusercontent.com/rKIt-MWlBJ0-FBv9FGT2AfiHBlVlhG5iY-QlQiVXVcwivjBecXX87rucMsgrmhEIsDrC",
        url="http://perillas.mendelux.es/1xyz/kodivertido/deportes_betas",
        fanart="https://i.imgur.com/E7vzz9Q.jpg",
        folder=True)
    plugintools.add_item(
        action="taquillas_betas",
        title="[B][LOWERCASE][CAPITALIZE][COLOR lime]*[COLOR turquoise][COLOR white] canales de la [COLOR gold]lista "
              "kodivertido TAQUILLAS[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",
        thumbnail="http://perillas.mendelux.es/1xyz/kodivertido/taquillas.png",
        url="http://perillas.mendelux.es/1xyz/kodivertido/taquillas_beta",
        fanart="https://i.imgur.com/bP8hAy7.jpg",
        folder=True)
    plugintools.add_item(
        action="cochinos_betas",
        title="[B][LOWERCASE][CAPITALIZE][COLOR lime]*[COLOR turquoise][COLOR white] canales de la [COLOR gold]lista "
              "kodivertido COCHINOS[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",
        thumbnail="https://i.imgur.com/29b9UAP.jpg",
        url="http://perillas.mendelux.es/1xyz/kodivertido/cochinos_beta",
        fanart="https://i.imgur.com/mxHSw8B.jpg",
        folder=True)


# ########################################### TV  TV  TV  Tv  ###########################################

def kodivertido_tdt(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()
    matches = re.findall(r'(?s)#EXTINF:-1,(.*?)\n(.*?)\s', url, re.DOTALL)
    for title, url in matches:
        plugintools.add_item(action="resolve_without_resolveurl", title=title, url=url,
                             thumbnail="https://i.imgur.com/RKM3S9q.jpg", fanart="https://i.imgur.com/5UwkEwQ.jpg",
                             folder=False, isPlayable=True)


def kodivertido_movistar(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()
    matches = re.findall(r'(?s)#EXTINF:-1,(.*?)\n(.*?)\s', url, re.DOTALL)
    for title, url in matches:
        plugintools.add_item(action="resolve_without_resolveurl", title=title, url=url,
                             thumbnail="https://i.imgur.com/ybtmUEq.jpg", fanart="https://i.imgur.com/5UwkEwQ.jpg",
                             folder=False, isPlayable=True)


def kodivertido_documentales(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()
    matches = re.findall(r'(?s)#EXTINF:-1,(.*?)\n(.*?)\s', url, re.DOTALL)
    for title, url in matches:
        plugintools.add_item(action="resolve_without_resolveurl", title=title, url=url,
                             thumbnail="https://i.imgur.com/Qfd2aMa.jpg", fanart="https://i.imgur.com/K2qLcF3.jpg",
                             folder=False, isPlayable=True)


def kodivertido_infantiles(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)#EXTINF:-1,(.*?)\n(.*?)\s', url, re.DOTALL)
    for title, url in matches:
        plugintools.add_item(action="resolve_without_resolveurl", title=title, url=url,
                             thumbnail="https://i.imgur.com/6DiJNJw.jpg", fanart="https://i.imgur.com/T2ikxs1.jpg",
                             folder=False, isPlayable=True)


def kodivertido_deportes(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)EXTINF:-1,SP: ES:(.*?)\n(.*?)\s', url, re.DOTALL)
    for title, url in matches:
        plugintools.add_item(action="resolve_without_resolveurl", title=title, url=url,
                             thumbnail="https://i.imgur.com/X4ESsch.jpg", fanart="https://i.imgur.com/vcMwIBD.jpg",
                             folder=False, isPlayable=True)


def kodivertido_musica(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)#EXTINF:-1,(.*?)\n(.*?)\s', url, re.DOTALL)
    for title, url in matches:
        plugintools.add_item(action="resolve_without_resolveurl", title=title, url=url,
                             thumbnail="https://i.imgur.com/dCzcyRl.jpg", fanart="https://i.imgur.com/Tp5r6W1.jpg",
                             folder=False, isPlayable=True)


def kodivertido_cochinos(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)#EXTINF:-1,(.*?)\n(.*?)\s', url, re.DOTALL)
    for title, url in matches:
        plugintools.add_item(action="resolve_without_resolveurl", title=title, url=url,
                             thumbnail="https://i.imgur.com/29b9UAP.jpg", fanart="https://i.imgur.com/mxHSw8B.jpg",
                             folder=False, isPlayable=True)


# ###########################################  TAQUILLAS  ###############################################################

def kodivertido_taquillas(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)#EXTINF:-1,(.+?)\n.*?(.+?)\s', url, re.DOTALL)
    for title, url in matches:
        plugintools.add_item(action="resolve_without_resolveurl", title=title, url=url,
                             thumbnail="https://i.imgur.com/yFFNYjF.jpg", fanart="https://i.imgur.com/GwEkCuA.jpg",
                             folder=False, isPlayable=True)

# ########################################### DEPORTES Y DIRECTOS ###############################################


def directs(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()
    matches = re.findall(r'(?s)"(.*?)".*?"(.*?)"', url, re.DOTALL)
    for title, url in matches:
        plugintools.add_item(action="resolve_without_resolveurl",
                             title="[B][LOWERCASE][CAPITALIZE][COLOR white]" + title + "[/COLOR][/CAPITALIZE][/LOWERCASE][/B]",
                             url=url, fanart='https://i.imgur.com/E7vzz9Q.jpg', folder=False, isPlayable=True)


def DailySport(params):
    url = params.get("url")
    import ssl
    try:
        ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = ssl._create_unverified_context    
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'colspan="5".*?center;">(.*?)<|tr>.*?\n.*?<td>(.*?)<.*?\n.*?<td>(.*?)<[\W\w]*?\<td.*?href="(.*?)">(.*?)<\/', url, re.DOTALL)
    for time, title, title2, url, day in matches:
        plugintools . add_item ( action = "daily_1", title = "[B]" + "[COLOR lime]" + time + " " + "[/COLOR]" + "[COLOR yellow]" + title + " " + title2 + "[/COLOR]" + day + "[/B]", url = url, thumbnail="https://i.imgur.com/xUvhv4k.jpg", folder = True )
        
def daily_1 (params):
    url = "https://dailysport.site/" + params . get ( "url" )
    import ssl
    try:
        ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = ssl._create_unverified_context 
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )        
    matches =  re.findall(r"var player = new Clappr.Player\(\{\s.*?source: window.atob\('([^\']+)", url, re.DOTALL)
    for url in matches:
         try:
            url = base64.b64decode(url)
         except:
             url = url   
         plugintools . add_item ( action = "resolve_without_resolveurl", title = "Ver Evento", url = url, thumbnail="https://i.imgur.com/GsOcanM.jpg", folder = False, isPlayable = True )
         


def canalesd(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()
    matches = re.findall(r'(?s)<title>.*?\[B](.*?)\[/B].*?<.*?url=(.*?)<.*?thumb.*?>(.*?)<.*?fan.*?>(.*?)<', url,
                         re.DOTALL)
    for title, url, thumb, fanart in matches:
        plugintools.add_item(action="resolve_without_resolveurl",
                             title="[B][UPPERCASE][COLOR aquamarine]" + title + "[/COLOR][/UPPERCASE][/B]", url=url,
                             fanart=fanart, thumbnail=thumb, folder=False, isPlayable=True)

# ###########################################  BETAS  ###############################################################


def videoclub(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()
    matches = re.findall(r'(?s).*?tvg-name="(.*?)".*?tvg-logo="(.*?)".*?\n(.*?)\s', url, re.DOTALL)
    for title, thumb, url in matches:
        plugintools.add_item(action="resolve_without_resolveurl", title="[B][UPPERCASE][COLOR chartreuse]" + title + "[/COLOR][/UPPERCASE][/B]", url=url, thumbnail=thumb,
                             fanart="https://i.imgur.com/GwEkCuA.jpg", folder=False, isPlayable=True)
            


def tv_betas(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(
        r'(?s).*?tvg-name="(.*?)".*?tvg-logo="(.*?)".*?group-title=".*?([A-Z]+ [A-Z]......).*?(http://listamy.com:8080/liHM1HdhS3/mWQ3MPr59p/.*?)\s',
        url, re.DOTALL)
    for title, thumb, title2, url in matches:
        plugintools.add_item(action="resolve_without_resolveurl", title="[B][UPPERCASE][COLOR greenyellow]" + title2 + "[/COLOR][/UPPERCASE][/B]" + " " + "[B][UPPERCASE][COLOR magenta]" + title + "[/COLOR][/UPPERCASE][/B]", url=url, thumbnail=thumb,
                             fanart="https://i.imgur.com/GwEkCuA.jpg", folder=False, isPlayable=True)


def deportes_betas(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(
        r'(?s).*?tvg-name="(.*?)".*?tvg-logo="(.*?)".*?group-title=".*?([A-Z]+ [A-Z]......).*?(http://listamy.com:8080/liHM1HdhS3/mWQ3MPr59p/.*?)\s',
        url, re.DOTALL)
    for title, thumb, title2, url in matches:
        plugintools.add_item(action="resolve_without_resolveurl", title="[B][UPPERCASE][COLOR greenyellow]" + title2 + "[/COLOR][/UPPERCASE][/B]" + " " + "[B][UPPERCASE][COLOR magenta]" + title + "[/COLOR][/UPPERCASE][/B]", url=url, thumbnail=thumb,
                             fanart="https://i2.wp.com/sportytell.com/wp-content/uploads/2019/11/Most-popular-sports-in-the-world-right-now.jpg?fit=1280%2C720&ssl=1",
                             folder=False, isPlayable=True)


def taquillas_betas(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s).*?tvg-name="(.*?)".*?tvg-logo="(.*?)".*?(http.*?)\s', url, re.DOTALL)
    for title, thumb, url in matches:
        plugintools.add_item(action="resolve_without_resolveurl", title="[B][UPPERCASE][COLOR greenyellow]" + title + "[/COLOR][/UPPERCASE][/B]", url=url, thumbnail="http://perillas.mendelux.es/1xyz/kodivertido/taquillas.png",
                             fanart="https://i.imgur.com/E7vzz9Q.jpg",
                             folder=False, isPlayable=True)


def cochinos_betas(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s).*?tvg-name="(.*?)".*?(http://listamy.com:8080/liHM1HdhS3/mWQ3MPr59p/.*?)\s', url, re.DOTALL)
    for title, url in matches:
        plugintools.add_item(action="resolve_without_resolveurl", title="[B][UPPERCASE][COLOR greenyellow]" + title + "[/COLOR][/UPPERCASE][/B]", url=url,
                             thumbnail="https://i.imgur.com/29b9UAP.jpg", fanart="https://i.imgur.com/mxHSw8B.jpg",
                             folder=False, isPlayable=True)


# ########################################### GranTorrent  ###########################################


def grantorrent_search(params):
    url = params.get("url") + keyboard_input("", "Buscar:", False).replace(" ", "+")
    url = requests.get(url).text
    matches = re.findall(r'(?s)class="imagen.*?href="(.*?nl/(.*?)/)".*?img src="([^"]+)', url, re.DOTALL)
    next = plugintools.find_single_match(url, '<link rel="next" href="([^"]+)"')
    for url, title, thumb in matches:
        plugintools.add_item(action="hdrip1", title=title, thumbnail=thumb, url=url, fanart=thumb, folder=True)
    plugintools.add_item(action="hdrip", title="PAGINA SIGUIENTE", url=next,
                         thumbnail="https://i.imgur.com/cfwdN1c.jpg", folder=True)


def hdrip(params):
    url = params.get("url")
    url = requests.get(url).text
    matches = re.findall(r'(?s)class="imagen.*?href="(.*?nl/(.*?)/)".*?img src="([^"]+)', url, re.DOTALL)
    next = plugintools.find_single_match(url, '<link rel="next" href="([^"]+)"')
    for url, title, thumb in matches:
        plugintools.add_item(action="hdrip1", title=title, thumbnail=thumb, url=url, fanart=thumb, folder=True)
    plugintools.add_item(action="hdrip", title="PAGINA SIGUIENTE", url=next,
                         thumbnail="https://i.imgur.com/cfwdN1c.jpg", folder=True)


def hdrip1(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)lol.*?title=.*?Castellano.*?.*?td>.*?td>(.*?)<.*?u:\s.([^"]+)', url, re.DOTALL)
    log(matches)
    for title, url in matches:
        plugintools.add_item(action="elementum_gran", title=title, url=url, folder=False, isPlayable=True)


def blueray(params):
    url = params.get("url")
    url = requests.get(url).text

    matches = re.findall(r'(?s)class="imagen.*?href="(.*?nl/(.*?)/)".*?img src="([^"]+)', url, re.DOTALL)
    next = plugintools.find_single_match(url, '<link rel="next" href="([^"]+)"')
    for url, title, thumb in matches:
        plugintools.add_item(action="blueray1", title=title, thumbnail=thumb, url=url, folder=True)
    plugintools.add_item(action="blueray", title="PAGINA SIGUIENTE", url=next,
                         thumbnail="https://i.imgur.com/cfwdN1c.jpg", folder=True)


def blueray1(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)lol.*?title=.*?Castellano.*?.*?td>.*?td>(.*?)<.*?u:\s.([^"]+)', url, re.DOTALL)
    log(matches)
    for title, url in matches:
        plugintools.add_item(action="elementum_gran", title=title, url=url, folder=False, isPlayable=True)


def cuatrok(params):
    url = params.get("url")
    url = requests.get(url).text

    matches = re.findall(r'(?s)class="imagen.*?href="(.*?nl/(.*?)/)".*?img src="([^"]+)', url, re.DOTALL)
    next = plugintools.find_single_match(url, '<link rel="next" href="([^"]+)"')
    for url, title, thumb in matches:
        plugintools.add_item(action="cuatrok1", title=title, thumbnail=thumb, url=url, fanart=thumb, folder=True)
    plugintools.add_item(action="cuatrok", title="PAGINA SIGUIENTE", url=next,
                         thumbnail="https://i.imgur.com/cfwdN1c.jpg", folder=True)


def cuatrok1(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)lol.*?title=.*?Castellano.*?.*?td>.*?td>(.*?)<.*?u:\s.([^"]+)', url, re.DOTALL)
    log(matches)
    for title, url in matches:
        plugintools.add_item(action="elementum_gran", title=title, url=url, folder=False, isPlayable=True)

# ########################################### PCTFenix  ###########################################


def fullbluray_1080p(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
    log(matches)
    for thumb, title, url in matches:
        plugintools.add_item(action="fullbluray_1080p1", title=title, url=url, thumbnail=(("https:") + thumb),
                             folder=True)


def fullbluray_1080p1(params):
    url = (("https://pctfenix.com" + params.get("url")))
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"', url, re.DOTALL)
    log(matches)
    for title, url in matches:
        plugintools.add_item(action="elementum_pctfenix1", title=title, url=url, folder=False, isPlayable=True)


def bluray_1080p(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
    log(matches)
    for thumb, title, url in matches:
        plugintools.add_item(action="bluray_1080p1", title=title, url=url, thumbnail=(("https:") + thumb), folder=True)


def bluray_1080p1(params):
    url = (("https://pctfenix.com" + params.get("url")))
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"', url, re.DOTALL)
    log(matches)
    for title, url in matches:
        plugintools.add_item(action="elementum_pctfenix1", title=title, url=url, folder=False, isPlayable=True)


def dbremux_1080p(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
    log(matches)
    for thumb, title, url in matches:
        plugintools.add_item(action="dbremux_1080p1", title=title, url=url, thumbnail=(("https:") + thumb), folder=True)


def dbremux_1080p1(params):
    url = (("https://pctfenix.com" + params.get("url")))
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"', url, re.DOTALL)
    log(matches)
    for title, url in matches:
        plugintools.add_item(action="elementum_pctfenix1", title=title, url=url, folder=False, isPlayable=True)


def cuatrok_uhdremux(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
    log(matches)
    for thumb, title, url in matches:
        plugintools.add_item(action="cuatrok_uhdremux1", title=title, url=url, thumbnail=(("https:") + thumb),
                             folder=True)


def cuatrok_uhdremux1(params):
    url = (("https://pctfenix.com" + params.get("url")))
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"', url, re.DOTALL)
    log(matches)
    for title, url in matches:
        plugintools.add_item(action="elementum_pctfenix1", title=title, url=url, folder=False, isPlayable=True)


def cuatrok_uhdmicro(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
    log(matches)
    for thumb, title, url in matches:
        plugintools.add_item(action="cuatrok_uhdmicro1", title=title, url=url, thumbnail=(("https:") + thumb),
                             folder=True)


def cuatrok_uhdmicro1(params):
    url = (("https://pctfenix.com" + params.get("url")))
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"', url, re.DOTALL)
    log(matches)
    for title, url in matches:
        plugintools.add_item(action="elementum_pctfenix1", title=title, url=url, folder=False, isPlayable=True)


def cuatrok_uhdrip(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
    log(matches)
    for thumb, title, url in matches:
        plugintools.add_item(action="cuatrok_uhdrip1", title=title, url=url, thumbnail=(("https:") + thumb),
                             folder=True)


def cuatrok_uhdrip1(params):
    url = (("https://pctfenix.com" + params.get("url")))
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"', url, re.DOTALL)
    log(matches)
    for title, url in matches:
        plugintools.add_item(action="elementum_pctfenix1", title=title, url=url, folder=False, isPlayable=True)


def cuatrok_webrip(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
    log(matches)
    for thumb, title, url in matches:
        plugintools.add_item(action="cuatrok_webrip1", title=title, url=url, thumbnail=(("https:") + thumb),
                             folder=True)


def cuatrok_webrip1(params):
    url = (("https://pctfenix.com" + params.get("url")))
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"', url, re.DOTALL)
    log(matches)
    for title, url in matches:
        plugintools.add_item(action="elementum_pctfenix1", title=title, url=url, folder=False, isPlayable=True)


def full_uhdcuatrok(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
    log(matches)
    for thumb, title, url in matches:
        plugintools.add_item(action="full_uhdcuatrok1", title=title, url=url, thumbnail=(("https:") + thumb),
                             folder=True)


def full_uhdcuatrok1(params):
    url = (("https://pctfenix.com" + params.get("url")))
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"', url, re.DOTALL)
    log(matches)
    for title, url in matches:
        plugintools.add_item(action="elementum_pctfenix1", title=title, url=url, folder=False, isPlayable=True)


def microhd_1080p(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
    log(matches)
    for thumb, title, url in matches:
        plugintools.add_item(action="microhd_1080p1", title=title, url=url, thumbnail=(("https:") + thumb), folder=True)


def microhd_1080p1(params):
    url = (("https://pctfenix.com" + params.get("url")))
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"', url, re.DOTALL)
    log(matches)
    for title, url in matches:
        plugintools.add_item(action="elementum_pctfenix1", title=title, url=url, folder=False, isPlayable=True)


# ################################################## MITORRENT #######################################

def mitorrent(params):
    if int(params.get("page")) != 1:
        url = params.get("url") + params.get("page") + "/"
    else:
        url = "https://mitorrent.org/"

    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = plugintools.find_multiple_matches(url, '(?s)(img-responsive".*?browse-movie-tags)')

    next = plugintools.find_single_match(url, '<li><a class="next page-numbers" href="([^"]+)')
    for match in matches:
        title = plugintools.find_single_match(match, 'browse-movie-title">([^<]+)<')
        thumb = plugintools.find_single_match(match, 'sive" src="([^"]+)"')
        url = plugintools.find_single_match(match, 'browse-movie-bottom">.*?href="([^"]+)"')

        plugintools.add_item(action="mitorrent1", title=title, thumbnail=thumb, url=url, folder=True)
    next = str(int(params.get("page")) + 1)
    plugintools.add_item(action="mitorrent", title="Next Page", url="https://mitorrent.org/page/",
                         thumbnail='https://i.imgur.com/cfwdN1c.jpg', page=next, folder=True)


def mitorrent1(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)(torrent)\sbutton-green.*?href="(.+?)"', url, re.DOTALL)
    log(matches)
    for title, url in matches:
        plugintools.add_item(action="elementum", title=title, url=url, folder=False, isPlayable=True)


# ####################################  SERIES #######################################################################

def grantorrent_series_nor(params):
    url = params.get("url")
    url = requests.get(url).text
    matches = re.findall(r'(?s)imagen-post">.*?href="(.+?.nl/series/(.*?)/)".*?src="(.+?)"', url, re.DOTALL)
    next = plugintools.find_single_match(url, '<link rel="next" href="([^"]+)"')
    for url, title, thumb in matches:
        plugintools.add_item(action="grantorrent_series_nor2", title=title, thumbnail=thumb, url=url,
                             fanart="https://i.imgur.com/iHEIey9.jpg", folder=True)
    plugintools.add_item(action="grantorrent_series_nor", title="PAGINA SIGUIENTE", url=next,
                         thumbnail="https://i.imgur.com/cfwdN1c.jpg", fanart="https://i.imgur.com/iHEIey9.jpg",
                         folder=True)


def grantorrent_series_nor2(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)title="(.+?)".*?td>.*?td>(.+?)<.*?td>.*?td>(.+?)<.*?u:\s\'(.+?)\'', url, re.DOTALL)
    log(matches)
    for title, cap, peso, url in matches:
        plugintools.add_item(action="elementum_gran", title=title + "  " + cap + "  " + peso, url=url,
                             thumbnail=params.get("thumbnail"), fanart="https://i.imgur.com/iHEIey9.jpg", folder=False,
                             isPlayable=True)


def grantorrent_series(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)</option><option value="(.+?)"\s>(.+?)<', url, re.DOTALL)
    log(matches)
    for url, title in matches:
        plugintools.add_item(action="grantorrent_series1", title=title, url=url,
                             thumbnail="https://i.imgur.com/uWqZDRQ.jpg", folder=True)


def grantorrent_series1(params):
    url = ((
            "https://grantorrent.nl/series/?unonce=598b7846de&uformid=17&s=uwpsfsearchtrg&taxo[0][name]=category&taxo[0][opt]=1&taxo[0][term]=uwpqsftaxoall&taxo[1][name]=category&taxo[1][opt]=1&taxo[1][term]=" + params.get(
        "url")))
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)imagen-post">.*?href="(.+?.nl/series/(.*?)/)".*?src="(.+?)"', url, re.DOTALL)
    log(matches)
    for url, title, thumb in matches:
        plugintools.add_item(action="grantorrent_series2", title=title, url=url, thumbnail=thumb, folder=True)


def grantorrent_series2(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)title=.*?td.*?td>(.+?)<.*?td>.*?td(.+?)<.+?u: \'(.+?)\'', url, re.DOTALL)
    log(matches)
    for title, cali, url in matches:
        plugintools.add_item(action="elementum_gran", title=title + cali, url=url, folder=False, isPlayable=True)


def mitorrent_series(params):
    if int(params.get("page")) != 1:
        url = params.get("url") + params.get("page") + "/"
    else:
        url = "https://mitorrent.org/series/"

    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = plugintools.find_multiple_matches(url, '(?s)(img-responsive".*?browse-movie-tags)')

    next = plugintools.find_single_match(url, '<li><a class="next page-numbers" href="([^"]+)')
    for match in matches:
        title = plugintools.find_single_match(match, 'browse-movie-title">([^<]+)<')
        thumb = plugintools.find_single_match(match, 'sive" src="([^"]+)"')
        url = plugintools.find_single_match(match, 'browse-movie-bottom">.*?href="([^"]+)"')

        plugintools.add_item(action="mitorrent_series1", title=title, thumbnail=thumb, url=url, folder=True)
    next = str(int(params.get("page")) + 1)
    plugintools.add_item(action="mitorrent_series", title="Next Page", url="https://mitorrent.org/series/page/",
                         thumbnail='https://i.imgur.com/cfwdN1c.jpg', page=next, folder=True)


def mitorrent_series1(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)class="accordion.*?&nbsp;(.+?)<|href="(magnet.+?)".*?Descargar(.+?\d.)', url, re.DOTALL)
    log(matches)
    for temp, url, title in matches:
        plugintools.add_item(action="elementum", title=temp + title, url=url, folder=False, isPlayable=True)


def cinetorrent_series(params):
    if int(params.get("page")) != 1:
        url = params.get("url") + params.get("page") + "/"
    else:
        url = "http://cinetorrent.co/series/"

    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = plugintools.find_multiple_matches(url,
                                                '(?s)(<div class="col-6 col-sm-4 col-lg-3 col-xl-2">.*?</div>\s*</div>)')

    next = plugintools.find_single_match(url, '<li><a class="next page-numbers" href="([^"]+)')
    for match in matches:
        title = plugintools.find_single_match(match, '">([^<]+)</a></h3>')
        thumb = plugintools.find_single_match(match, '<img src="([^"]+)"')
        url = plugintools.find_single_match(match, '<h3 class="card__title"><a href="([^"]+)')
        calidad = plugintools.find_single_match(match, '<li>([^<]+)</li>')

        plugintools.add_item(action="cinetorrent_pelis1", title=title + "\x20" + calidad, thumbnail=thumb, url=url,
                             folder=True)
    next = str(int(params.get("page")) + 1)
    plugintools.add_item(action="cinetorrent_pelis", title="Next Page", url="http://cinetorrent.co/series/page/",
                         thumbnail='https://i.imgur.com/cfwdN1c.jpg', page=next, folder=True)


def cinetorrent_pelis(params):
    if int(params.get("page")) != 1:
        url = params.get("url") + params.get("page") + "/"
    else:
        url = "http://cinetorrent.co/peliculas/"

    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = plugintools.find_multiple_matches(url,
                                                '(?s)(<div class="col-6 col-sm-4 col-lg-3 col-xl-2">.*?</div>\s*</div>)')

    next = plugintools.find_single_match(url, '<li><a class="next page-numbers" href="([^"]+)')
    for match in matches:
        title = plugintools.find_single_match(match, '">([^<]+)</a></h3>')
        thumb = plugintools.find_single_match(match, '<img src="([^"]+)"')
        url = plugintools.find_single_match(match, '<h3 class="card__title"><a href="([^"]+)')
        calidad = plugintools.find_single_match(match, '<li>([^<]+)</li>')

        plugintools.add_item(action="cinetorrent_pelis1", title=title + "\x20" + calidad, thumbnail=thumb, url=url,
                             folder=True)
    next = str(int(params.get("page")) + 1)
    plugintools.add_item(action="cinetorrent_pelis", title="Next Page", url="http://cinetorrent.co/peliculas/page/",
                         thumbnail='https://i.imgur.com/cfwdN1c.jpg', page=next, folder=True)


def cinetorrent_pelis1(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)td>(Español.*?)<.*?href="(.+?)"', url, re.DOTALL)
    log(matches)
    for title, url in matches:
        plugintools.add_item(action="elementum", title=title, url=url, folder=False, isPlayable=True)


def cine_videoclub(params):
    url = params.get("url")
    header = []
    header.append(["User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    read_url, read_header = plugintools.read_body_and_headers(url, headers=header)
    url = read_url.strip()

    matches = re.findall(r'(?s)#EXTINF:-1.*?tvg-name="(.+?)".*?tvg-logo="(.+?)".*?(http.*?)\s', url, re.DOTALL)
    for title, thumb, url in matches:
        plugintools.add_item(action="resolve_without_resolveurl", title=title, url=url, thumbnail=thumb, fanart=thumb,
                             folder=False, isPlayable=True)


# Main menu

def keyboard_input(default_text="", title="", hidden=False):
    keyboard = xbmc.Keyboard(default_text, title, hidden)
    keyboard.doModal()

    if (keyboard.isConfirmed()):
        tecleado = keyboard.getText()
    else:
        tecleado = ""

    return tecleado


def elementum_pctfenix1(params):
    import resolveurl
    finalurl = (("plugin://plugin.video.elementum/play?uri=https:" + params.get("url")))
    plugintools.play_resolved_url(finalurl)


def resolve_resolveurl(params):
    import resolveurl
    finalurl = resolveurl.resolve(params.get("url"))
    plugintools.play_resolved_url(finalurl)


def resolve_without_resolveurl(params):
    import resolveurl
    finalurl = (params.get("url"))
    plugintools.play_resolved_url(finalurl)


def torrent_elementum_grandtorrent(params):
    import resolveurl
    finalurl = (params.get("plugin://plugin.video.elementum/play?uri=url"))
    plugintools.play_resolved_url(finalurl)


def elementum_gran(params):
    import resolveurl
    finalurl = (
        ("plugin://plugin.video.elementum/play?uri=https://grantorrent.nl/download_tt.php?u=" + params.get("url")))
    plugintools.play_resolved_url(finalurl)


def elementum(params):
    import resolveurl
    finalurl = (("plugin://plugin.video.elementum/play?uri=" + params.get("url")))
    plugintools.play_resolved_url(finalurl)


# Main menu


run()
