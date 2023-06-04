# import the main window object (mw) from aqt
from aqt import mw
from aqt import gui_hooks
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *
from anki import notes

from typing import List
from _collections_abc import Mapping
import re


def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)    

class Token:
    def __init__(self, word: str, pos: int) -> None:
        self.word = remove_html_tags(word)
        self.pos = pos
        
    def print(self):
        print(self.word, self.pos)
        
class TokenSet: 
    def __init__(self, text: str = "") -> None:
        self._text = text
        self._tokens: List[Token] = []
    
    def update_tokens(self, text: str):
        pos = 0
        self._tokens = []
        new_line_tokens = []
        
        
        
        while pos < len(text):
            if text[pos] in set([' ', '\n', '\r', '\t', '\f']):                    
                new_line_tokens.append((pos, 1))
            pos += 1
            
        nb_list = [(m.start(), len("&nbsp;")) for m in re.finditer('&nbsp;', text)]
        br_list = [(m.start(), len("<br>")) for m in re.finditer('<br>', text)]
        
        token_index = nb_list + new_line_tokens + br_list
        
        token_index.sort(key=lambda x: x[0])
        token_index.append((len(text), 0))
        
        print(text)
        print(token_index)
        start_pos = 0
        
        for token in token_index:
            rtext = text[start_pos: token[0]]
            if len(rtext) > 0:
                self._tokens.append(Token(rtext, start_pos))
                start_pos = start_pos + len(rtext) + token[1]
                        
               
        for i in range(0, len(self._tokens)):
            self._tokens[i].print()
                
        
class SpellCheckerStatus: 
    def __init__(self) -> None:
        self._active_field_index= -1
        self._active_field_key = ""
        self._fields: Mapping[str, TokenSet] = {}
    
    
    def update_field(self, note: notes.Note):
        self._fields[self._active_field_key].update_tokens(note.fields[self._active_field_index])
        
    def set_active_field(self, field_id: int):
        self._active_field_index = field_id
        
        if str(field_id) not in self._fields:
            self._fields[str(field_id)] = TokenSet()
            
        self._active_field_key = str(field_id)
             
    def get_active_field(self) -> TokenSet:
        return self._fields[self._active_field_key]
    
    
    
scs = SpellCheckerStatus()   


def handler_focus_field(note: notes.Note, field_id: int):
    scs.set_active_field(field_id)

def handling_timing_typer(note: notes.Note):
    scs.update_field(note)

def tokenizer(note: notes.Note):
    pass

