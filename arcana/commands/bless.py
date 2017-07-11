from evennia.commands.default.muxcommand import MuxCommand


class CmdBless(MuxCommand):

    """
       +Bless - Ruins your luck at everything.
    
       Usage: 
         +bless <target>

       Can be increased if used again.
    
    """   
    help_category = "Fate Magic"
    auto_help = True
   
    key = "+bless"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return
        hit =  self.caller.search(self.args)

        if hit == self.caller:
                if hit.db.blssed >= 0:
                   hit.db.blessed = hit.db.blessed +1
                   hit.msg("You are blessed")
                elif hit.db.blessed < 0:
                    hit.db.blessed = 0
                    hit.msg("You are no loner hexed")
        if not self.caller == hit:
               if hit.db.blessed >= 0:
                  hit.db.blessed = hit.db.blessed + 1
                  self.caller.msg("You bless %s." % hit)
                  hit.msg("You are blessed")
               elif hit.db.blessed < 0:
                   hit.db.blessed = 0
                   hit.msg("You are no longer hexed")
                   self.caller.msg("%s is no longer blessed." % hit)
