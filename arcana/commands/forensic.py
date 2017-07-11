from evennia.commands.default.muxcommand import MuxCommand


class CmdLastBreath(MuxCommand):

    """
       +lastbreath - Determine identity and cause of corpses.
    
       Usage: 
         +lastbreath target

       Not usable on ghosts themselves.
    
    """   
    help_category = "Death Magic"
    auto_help = True
   
    key = "+lastbreath"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return
        hit =  self.caller.search(self.args)
        if hit.db.lastname:
            self.caller.msg("They used to be named %s." % hit.db.lastname)
            self.caller.msg("The last person to attack %s was %s." % (hit.db.lastname, hit.db.target))
        else:
              self.caller.msg("The last person to attack %s was %s." % (hit, hit.db.target))
