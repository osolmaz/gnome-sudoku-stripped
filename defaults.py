import os, os.path
import gettext
DOMAIN = 'gnome-sudoku'
gettext.bindtextdomain(DOMAIN)
gettext.textdomain(DOMAIN)
from gettext import gettext as _
import gtk.glade
gtk.glade.bindtextdomain (DOMAIN)
gtk.glade.textdomain (DOMAIN)

VERSION = "0.7.1"
APPNAME = _("GNOME Sudoku")
COPYRIGHT = _('Copyright (c) 2005, Thomas M. Hinkle. GNU GPL')
DESCRIPTION = _('GNOME Sudoku is a simple sudoku generator and player.  Sudoku is a japanese logic puzzle.')
AUTHORS = ["Thomas M. Hinkle"]
AUTO_SAVE= True
MIN_NEW_PUZZLES = 90

# grab the proper subdirectory, assuming we're in
# lib/python/site-packages/gnome-sudoku/
# special case our standard debian install, which puts
# all the python libraries into /usr/share/gnome-sudoku
if __file__.find('/usr/share/gnome-sudoku')==0:
    usr='/usr'
elif __file__.find('/usr/local/share/gnome-sudoku')==0:
    usr='/usr/local'
else:
    usr=os.path.split(os.path.split(os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0])[0])[0]
    # add share/gnome-sudoku
    # this assumes the user only specified a general build
    # prefix. If they specified data and lib prefixes, we're
    # screwed. See the following email for details:
    # http://mail.python.org/pipermail/python-list/2004-May/220700.html

if usr:
    APP_DATA_DIR = os.path.join(usr,'share')
    ICON_DIR =     os.path.join(APP_DATA_DIR,'pixmaps')
    IMAGE_DIR = os.path.join(ICON_DIR,'gnome-sudoku')
    GLADE_DIR = os.path.join(APP_DATA_DIR,'gnome-sudoku')
    BASE_DIR = os.path.join(APP_DATA_DIR,'gnome-sudoku')
else:
    ICON_DIR = '../../images'
    IMAGE_DIR = '../../images'
    GLADE_DIR = '../../glade'
    BASE_DIR = '../../data'

DATA_DIR = os.path.expanduser('~/.gnome2/gnome-sudoku/')

def initialize_games_dir ():
    if not os.path.exists(DATA_DIR): os.makedirs(DATA_DIR)

