from evennia.commands.default.muxcommand import MuxCommand


class CmdHex(MuxCommand):

    """
       +Hex - Ruins your luck at everything.
    
       Usage: 
         +hex <target>

       Can be increased if used again.
    
    """   
    help_category = "Fate Magic"
    auto_help = True
   
    key = "+hex"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return
        hit =  self.caller.search(self.args)

        if hit == self.caller:
                if hit.db.blssed <= 0:
                   hit.db.blessed = hit.db.blessed -1
                   hit.msg("You are hexed")
                elif hit.db.blessed > 0:
                    hit.db.blessed = 0
                    hit.msg("You are no loner blessed")
        if not self.caller == hit:
               if hit.db.blessed <= 0:
                  hit.db.blessed = hit.db.blessed - 1
                  self.caller.msg("You hex %s." % hit)
                  hit.msg("You are hexed")
               elif hit.db.blessed > 0:
                   hit.db.blessed = 0
                   hit.msg("You are no longer blessed")
                   self.caller.msg("%s is no longer blessed." % hit)
