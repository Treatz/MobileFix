from evennia.commands.default.muxcommand import MuxCommand


class CmdStrike(MuxCommand):

    """
       +Strike - Call lightning.
    
       Usage: 
         +strike <target>

       Must be used outside.
    
    """   
    help_category = "Forces Magic"
    auto_help = True
   
    key = "+strike"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return
        hit =  self.caller.search(self.args)

        if hit == self.caller:
            self.caller.msg("You don't want to do that!")
            return                
        if hit:
            hit.msg("You are struck by lightning!")
            self.caller.msg("%s is truck by lightning!" % hit)                  
            hit.db.conscious = 0
            hit.db.lethal = hit.db.lethal + 4
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
