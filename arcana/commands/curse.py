from evennia.commands.default.muxcommand import MuxCommand


class CmdCurse(MuxCommand):

    """
       +Curse - Increases any damamge the target is hit by.
    
       Usage: 
         +curse <target>

       Doesn't expire until the curse is activated.
    
    """   
    help_category = "Fate Magic"
    auto_help = True
   
    key = "+curse"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return
        hit =  self.caller.search(self.args)

        if hit == self.caller:
            hit.msg("You are cursed")
            hit.db.cursed = hit.db.cursed + 1
        if not self.caller == hit:
            hit.db.cursed = hit.db.cursed +1
            self.caller.msg("You curse %s." % hit)
