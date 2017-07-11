from evennia.commands.default.muxcommand import MuxCommand


class CmdUse(MuxCommand):

    """
       +Use - Use luck on yourself or a charmed object.
    
       Usage: 
         +use <target>

       Can be increased if used again.
    
    """   
    help_category = "Fate Magic"
    auto_help = True
   
    key = "+use"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return

        if(self.args == 'luck' or self.args == 'Luck'):
            if(self.caller.db.burned <= self.caller.db.luck):
                self.caller.msg("You sacrifice some of your natural luck.")
                self.caller.db.burned = self.caller.db.burned + 1
                self.caller.db.blessed = self.caller.db.blessed + 1
            else:
                self.caller.msg("You have burned up all of your natural luck.")
            return
        hit =  self.caller.contents
        for item in hit:
            if item.key == self.args:
                if item.db.charm:
                    item.db.charm = item.db.charm - 1
                    self.caller.msg("You use some of the luck in %s." % item)
                    self.caller.db.blessed = self.caller.db.blessed + 1
                else:
                    self.caller.msg("There is no luck left in %s." % item)
            else:
                self.caller.msg("You don't have that.")
