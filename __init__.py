# import the main window object (mw) from aqt
from aqt import mw
from aqt import gui_hooks
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *
from anki import notes

from .spellcheck import handler_focus_field, handling_timing_typer, SpellCheckerStatus
# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

    


gui_hooks.editor_did_fire_typing_timer.append(handling_timing_typer)

gui_hooks.editor_did_focus_field.append(handler_focus_field)
