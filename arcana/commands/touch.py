from evennia.commands.default.muxcommand import MuxCommand


class CmdReach(MuxCommand):
    """
       +reach - Allow players/ghosts to interact with the other's world.
    
       Usage: 
         +reach
       A temporary spell.
    
    """   
    help_category = "Death Magic"
    auto_help = True   
    key = "+reach"
    locks = "cmd:all()"

    def func(self):
        self.caller.db.touch = 1
        if  self.caller.db.alive:
            self.caller.msg("You can now reach into the spirit world.")
        else:
            self.caller.msg("You can now reach into the physical world.")
