from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import gametime 
from evennia.utils import utils
import time

class CmdAstro(MuxCommand):

    """
       +Astro - View another persons luck / karma.
    
       Usage: 
         +astro <target>

       Read another persons fate.
    
    """   
    help_category = "Fate Magic"
    auto_help = True
   
    key = "+astro"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return
        if(self.args == "Use" or self.args == "use"):
            if(self.caller.db.astro == 0):
                self.caller.db.astro = 1
                self.caller.db.blessed = int(self.caller.db.blessed) + 1
                self.caller.msg("You are aligned with the universe.")
            else:
                self.caller.msg("Try again soon.")
            return

        hit =  self.caller.search(self.args)
        if hit:
            t = gametime.gametime(absolute=True)
            tst = time.strftime("%m", time.gmtime(t))           
            
            self.caller.msg("Month: %s" % int(tst))
            self.caller.msg("Star Sign: %s'" % int(hit.db.starsign))
            if(int(tst) == int(hit.db.starsign)):
                self.caller.msg("The stars are aligned for %s." % hit)
        else:
            self.caller.msg("You can't find that person.")

