from evennia.commands.default.muxcommand import MuxCommand


class CmdEnchant(MuxCommand):

    """
       +charm - blesses an object with luck.
    
       Usage: 
         +charm <target>

       Lasts until the luck has all been exhausted.
   
    """   
    help_category = "Fate Magic"
    auto_help = True
   
    key = "+charm"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
            self.caller.msg("You must suply an object for the spell to work.")
            return
        hit =  self.caller.search(self.args)
        if(hit.db.charm == 0):
            self.caller.msg("%s has become a lucky charm." % hit)
            hit.db.charm = hit.db.charm + 1
        else:
            self.caller.msg("%s has become more powerfu." % hit)
            hit.db.charm = hit.db.charm + 1
