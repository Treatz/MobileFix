from evennia.commands.default.muxcommand import MuxCommand


class CmdKinetic(MuxCommand):

    """
       +kinetic - Changes unarmed attacks to lethal.
    
       Usage: 
         +kinetic

       Increases the kinetic forces of your fists.
    
    """   
    help_category = "Forces Magic"
    auto_help = True
   
    key = "+kinetic"
    locks = "cmd:all()"

    def func(self):     
        self.caller.db.kinetic = 1
        self.caller.msg("You are full of kinetic force.")
