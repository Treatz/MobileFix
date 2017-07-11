from evennia.commands.default.muxcommand import MuxCommand


class CmdRace(MuxCommand):

    """
       +rush - Increase your speed using forces.
    
       Usage: 
         +rush

       Speeds up your movement with forces.
    
    """   
    help_category = "Forces Magic"
    auto_help = True
   
    key = "+rush"
    locks = "cmd:all()"

    def func(self):
        if(self.caller.db.rush >= 0 and self.caller.db.rush <= 6):
            self.caller.db.rush = self.caller.db.rush + 1
            if self.caller.db.move_speed == "stroll":
                self.caller.db.move_speed = "walk"
            elif self.caller.db.move_speed == "walk":
                self.caller.db.move_speed = "run"
            elif self.caller.db.move_speed == "run":
                self.caller.db.move_speed = "sprint"
            elif self.caller.db.move_speed == "sprint":
                self.caller.db.move_speed = "zoom"     
            self.caller.msg("You are moving faster!")
