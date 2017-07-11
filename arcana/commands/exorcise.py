from evennia.commands.default.muxcommand import MuxCommand


class CmdExorcise(MuxCommand):

    """
       +Exorcise - Send ghosts back to where they belong.
    
       Usage: +exorcise target

       Only used on dead players and ghosts.
    
    """   

    help_category = "Death Magic"
    auto_help = True
   
    key = "+exorcise"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return
        hit =  self.caller.search(self.args)
        if hit:
            hit.db.conscious  = 0
            self.caller.msg("You reach across the spirit world and drain strength from %s." % hit)
            hit.msg("%s reaches across the spirit world and drains your strength." % self.caller)
        else:
            self.caller.msg("You can't sense them here.")
