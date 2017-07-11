from evennia import default_cmds


class CmdFind(default_cmds.MuxCommand):
    """
       +Locate - Provides directions to an object or character.
    
       Usage: 
        +locate <args>
    
       Only shows best exit from where you are.
    
    """
    help_category = "Space Magic"    # default
    auto_help = True             # default
    key = "+locate"
    locks = "cmd:all()"

    maxdepth = 4

    def func(self):
        """confirms the target and initiates the search"""

        # save the target object onto the command
        # this will use Evennia's default multimatch handling if more than one object matches
        self.target = self.caller.search(self.args, global_search=True)

        # initialize a list to store rooms we've visited
        self.visited = []
        if not self.args:
            self.caller.msg("You must search for something.")
            return
        # now start the search, passing in depth=0
        if not self._searcher(self.caller.location, 0):
            # give the 'not found' message
            self.caller.msg("You are unable to determine which way to go.")

    def _searcher(self, room, depth):
        """Searches surrounding rooms recursively for an object"""

        # first, record that we've been here
        self.visited.append(room)

        # our end condition is either when the item is found...
        if self.target in room.contents:
            if depth == 0:
                self.caller.msg("It is right here!")
            else:
                self.caller.msg("({})You sense it is {}".format(depth, self.direction))
            return True

        # or we have traveled `maxdepth` rooms away
        if depth > self.maxdepth:
            return False

        # it's not in the current room, so loop through the exits and check them,
        # skipping rooms we've already visited
        exits = [exit for exit in room.exits if exit.destination not in self.visited]
        for next in exits:
            if depth == 0:  # we only want to return the exit out of the current room
                self.direction = next.key
            if self._searcher(next.destination, depth + 1):  # if we found the object, stop searching
                return True

        # we've checked all the exits, so return false
        return False
