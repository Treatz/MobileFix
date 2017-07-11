from evennia.commands.default.muxcommand import MuxCommand


class CmdDeathTouch(MuxCommand):

    """
       +Deathtouch - Knock a subject unconscious.
    
       Usage: 
         +deathtouch <target>

       Causes a temporary unconsciousness.
    
    """   
    help_category = "Death Magic"
    auto_help = True
   
    key = "+deathtouch"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return
        hit =  self.caller.search(self.args)

        if hit == self.caller:
            hit.msg("This doesn't work by yourself")
        if not self.caller == hit:
            hit.db.lethal = hit.db.lethal + 1
            self.caller.msg("You touch %s, causing 1 point of lethal damage." % hit)
            hit.msg("%s touches you, causing 1 point of lethal damage." % self.caller)
            healthbar = "|X|[wHealth:"
            total = hit.db.lethal + hit.db.bashing
            for i in range(0,8):
                if i < hit.db.lethal:
                    healthbar += " X"
                elif i < total:
                    healthbar += " /"
                else:
                    healthbar += " 0"
        
                hit.msg(prompt=healthbar)
