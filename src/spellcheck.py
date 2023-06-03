# import the main window object (mw) from aqt
from aqt import mw
from aqt import gui_hooks
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *
from anki import notes

_status = {
    'activeFieldId': -1
}

def focus_field_changed(note)