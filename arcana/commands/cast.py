from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils.search import search_channel
from evennia.utils.evmenu import EvMenu
 
def node_get_1(caller):
    text = "Please enter each sphere you are using:\n"
    options = ({'key': '_default',
        'goto': 'node_get_2'},)  
    return text, options 
                         
def node_get_2(caller, raw_string):
    caller.ndb._menutree.desc1 = raw_string
    text = "Please enter who or what is your target:\n"
    options = ({'key': '_default',
        'goto': 'node_get_3'},)
    return text, options
 
def node_get_3(caller, raw_string):
    caller.ndb._menutree.desc2 = raw_string
    text = "Please describe the spell you are casting:\n"
    options = ({'key': '_default',
        'goto': 'node_final'},)
    return text, options
 
def node_final(caller, raw_string):
    desc0 = "Name: " + caller.key
    desc1 = "Spheres: " + caller.ndb._menutree.desc1
    desc2 = "Target: " + caller.ndb._menutree.desc2
    desc3 = "Effect: " + raw_string
 
    channel = search_channel('spells')
    channel[0].msg(desc0)
    channel[0].msg(desc1)
    channel[0].msg(desc2)
    channel[0].msg(desc3)
    text = "Successfully completed spell!"
    return text, None
 
class CmdCast(MuxCommand):
    """
   Cast a Spell
 
   Usage:
        +cast 
   """
    key = "+cast"
    locks = "cmd:all()"
 
    def func(self):
            EvMenu(self.caller, 'commands.cast',
                   startnode='node_get_1')
