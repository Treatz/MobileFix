from evennia.commands.default.muxcommand import MuxCommand


class CmdInvis(MuxCommand):
    """
       +Invis - Temporarily makes you invisible.
    
       Usage: 
         +invisible
   
       Can only be used on yourself..
    
    """   
    help_category = "Death Magic"
    auto_help = True   
    key = "+invis"
    locks = "cmd:all()"

    def func(self):
        self.caller.db.invis = 1
        self.caller.msg("You are now invisible.")
