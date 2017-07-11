from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils.evmenu import EvMenu
 
# Following this are the menu nodes. EvMenu
# imports all these as nodes, so be careful
# what functions you put here
def node_get_1(caller):
    # This is the first node called by EvMenu.
    # It just sets a prompt, and since the only
    # command is _default, it just passes that
    # to the next node.
    text = "Please enter first description:\n"
    options = ({'key': '_default',
        'goto': 'node_get_2'},) # goto tells EvMenu where to go next
 
    return text, options # call signature - every function for an
                         # evmenu has to return text, options
 
def node_get_2(caller, raw_string):
    # each node is passed the text entered
    # via raw_string. technically we should use
    # raw_string.strip()
    # _menutree is set by EvMenu on the caller.
    # use it to store info you need through the menu
    # it deletes itself after
    caller.ndb._menutree.desc1 = raw_string
    text = "Please enter second description:\n"
    options = ({'key': '_default',
        'goto': 'node_get_3'},)
    return text, options
 
def node_get_3(caller, raw_string):
    # each node is passed the text entered
    # via raw_string. technically we should use
    # raw_string.strip()
    # _menutree is set by EvMenu on the caller.
    # use it to store info you need through the menu
    # it deletes itself after
    caller.ndb._menutree.desc2 = raw_string
    text = "Please enter third description:\n"
    options = ({'key': '_default',
        'goto': 'node_get_4'},)
    return text, options

def node_get_4(caller, raw_string):
    # each node is passed the text entered
    # via raw_string. technically we should use
    # raw_string.strip()
    # _menutree is set by EvMenu on the caller.
    # use it to store info you need through the menu
    # it deletes itself after
    caller.ndb._menutree.desc3 = raw_string
    text = "Please enter attribute to change:\n"
    options = ({'key': '_default',
        'goto': 'node_get_5'},)
    return text, options

def node_get_5(caller, raw_string):
    caller.ndb._menutree.desc4 = raw_string
    text = "Please enter new value:\n"
    options = ({'key': '_default',
        'goto': 'node_get_6'},)
    return text, options

def node_get_6(caller, raw_string):
    caller.ndb._menutree.desc5 = raw_string
    text = "Add another attribute:\n"
    options = ({'key': '|yfinish',
                'goto': 'node_final'},
               {'key': '|ymore',
                'goto': 'node_get_7'},)
    return text, options

def node_get_7(caller, raw_string):
    # each node is passed the text entered
    # via raw_string. technically we should use
    # raw_string.strip()
    # _menutree is set by EvMenu on the caller.
    # use it to store info you need through the menu
    # it deletes itself after
    caller.ndb._menutree.desc6 = raw_string
    text = "Please enter attribute to change:\n"
    options = ({'key': '_default',
        'goto': 'node_get_8'},)
    return text, options

def node_get_8(caller, raw_string):
    caller.ndb._menutree.desc7 = raw_string
    text = "Please enter new value:\n"
    options = ({'key': '_default',
        'goto': 'node_final'},)
    return text, options

def node_final(caller, raw_string):
    # final node, lots going on here
 
    # first we pull our descriptions out of the _menutree
    desc1 = caller.ndb._menutree.desc1
    desc2 = caller.ndb._menutree.desc2
    desc3 = caller.ndb._menutree.desc3
    attr1 = caller.ndb._menutree.desc4
    val1 = caller.ndb._menutree.desc5
    # we're passed a final string from the last node
    attr2 = caller.ndb._menutree.desc6
    val2 = raw_string
 
    # in our initialization of EvMenu, we added these arguments.
    # EvMenu stores this info in _menutree automagically.
    player_a = caller.ndb._menutree.player_a
    player_b = caller.ndb._menutree.player_b

    player_b.attributes.add(attr1, int(val1))
    player_b.attributes.add(attr2, int(val2))
    # past here, do as you will with the data. this is an example
    healthbar = "|X|[wHealth:"
    total = player_b.db.lethal + player_b.db.bashing
    for i in range(0,8):
        if i < player_b.db.lethal - 1:
            healthbar += " X"
        elif i < total:
            healthbar += " /"
        else:
            healthbar += " 0"
        
        player_b.msg(prompt=healthbar)

    # so here, we could just use caller.location.msg, or you could uncomment the confusing generator.
    # up to you
    """
   players = [con for con in caller.location.contents if con.has_player]
   for player in players:
       player.msg(desc3)
   """
    caller.location.msg_contents(desc3, exclude=[player_a, player_b])
 
    text = "Successfully completed spell!"
    return text, None
 
class CmdSpell(MuxCommand):
    """
   Cast a Spell
 
   Usage:
        +spell [target-1] [target-2]
   """
    key = "+spell"
    locks = "cmd:all()"
 
    def func(self):
        if not self.args:
            self.msg("You must provide a target for your spell.")
            return
        if ' ' in self.args:
            arg1, arg2 = self.args.split(' ', 1)
            playerA = self.caller.search(arg1)
            playerB = self.caller.search(arg2)
 
            # just in case we don't get a player target, we return if so
            if not playerA or not playerB:
                self.caller.msg("Couldn't find those players")
                return
            # this calls EvMenu with our menu. It imports from the
            # module we give it, in this case, our own module.
            # in practice you should store your menus somewhere else.
            EvMenu(self.caller, 'commands.spells',
                   startnode='node_get_1', # this is the initial node
                   player_a=playerA, # any data we give as kwargs is passed
                   player_b=playerB) # to the menu in caller.ndb._menutree
