from evennia.commands.default.muxcommand import MuxCommand


class CmdSight(MuxCommand):
    """
       +sight - Temporarily see into the spirit world.
    
       Usage: 
         +sight

       Also allows ghosts to see into the physical world.
    
    """   
    help_category = "Death Magic"
    auto_help = True   
    key = "+sight"
    locks = "cmd:all()"

    def func(self):
        self.caller.db.sight = 1
        if self.caller.db.alive:
            self.caller.msg("You can now see into the spirit world.")
        else:
            self.caller.msg("You can now see into the physical world.")
