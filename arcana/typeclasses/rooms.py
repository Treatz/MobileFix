"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
from evennia.utils.utils import inherits_from
from typeclasses import exits

class Room(DefaultRoom):
    def at_object_creation(self):
        self.db.image = "http://mud.streetwitch.com/static/website/images/1.jpg"

    def return_appearance(self, looker):
        if not looker:
            return
        looker.msg(image=[self.db.image, ""])
        # get and identify all objects
      #  visible = (con for con in self.contents if con != looker and con.access(looker, "view") 
#and (looker.db.alive == con.db.alive or looker.db.sight ==1 or con.destination) and con.db.invis == 0)
        visible = (con for con in self.contents if con != looker and con.access(looker, "view") and ((looker.db.alive == con.db.alive) or (looker.db.sight or con.destination)))

        exits, users, things = [], [], []
        for con in visible:
            key = con.get_display_name(looker)
            if con.destination:
                exits.append("|c|lc%s|lt%s|le" % (con, key))
            elif con.has_player:
                if(con.db.alive == 0 and con.db.invis == 0):
                    users.append("{c|b|lclook %s|lt%s|le{n" % (con, key))
                if(con.db.alive == 1 and con.db.invis == 0):
                    users.append("{c|lclook %s|lt%s|le{n" % (con, key))
            else:
                things.append("{c|lclook %s|lt%s|le" % (con, key))
        # get description, build string
        string = "{c%s{n\n" % self.get_display_name(looker)
        if(looker.db.alive == 1):
            desc = self.db.desc
        if(looker.db.alive == 0):
            desc = self.db.spiritdesc
        if desc:
            string += "%s" % desc
        if exits:
            string += "\n{wExits:{n " + ", ".join(exits)
        if users or things:
            string += "\n{wYou see:{n " + ", ".join(users + things)
        return string
