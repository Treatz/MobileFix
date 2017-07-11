from evennia.commands.default.muxcommand import MuxCommand


class CmdFate(MuxCommand):

    """
       +Fate - View another persons luck / karma.
    
       Usage: 
         +fate <target>

       Read another persons fate.
    
    """   
    help_category = "Fate Magic"
    auto_help = True
   
    key = "+fate"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return

        hit =  self.caller.search(self.args)
        if hit:
            self.caller.msg("The person has charged up |g(%i) |Wpoints of karma." % int(hit.db.blessed - hit.db.cursed))
            self.caller.msg("They have used |g(%s) |Wout of |g(%s) |Wpoints of thier natural Luck." % (hit.db.burned, hit.db.Luck))
        else:
            self.caller.msg("You can't find that person.")
