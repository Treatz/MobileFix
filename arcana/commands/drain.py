from evennia.commands.default.muxcommand import MuxCommand


class CmdDrain(MuxCommand):

    """
       +drain - Drains quintessence from targets willpower.
    
       Usage: 
         +drain <target>

       Target must be unconscious.
    
    """   
    help_category = "Death Magic"
    auto_help = True
   
    key = "+drain"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return
        hit =  self.caller.search(self.args)

        if hit == self.caller:
            hit.msg("This doesn't work by yourself")
        if not self.caller == hit and hit.db.conscious == 0:
            hit.db.willpower = hit.db.willpower - 1
            self.caller.msg("You touch %s, charging your mana with his willpower." % hit)
            hit.msg("%s touches you, draining 1 point of willpower." % self.caller)
            self.caller.db.quintesence = self.caller.db.quintessence + 1
