"""
Command sets

All commands in the game must be grouped in a cmdset.  A given command
can be part of any number of cmdsets and cmdsets can be added/removed
and merged onto entities at runtime.

To create new commands to populate the cmdset, see
`commands/command.py`.

This module wraps the default command sets of Evennia; overloads them
to add/remove commands from the default lineup. You can create your
own cmdsets by inheriting from them or directly from `evennia.CmdSet`.

"""

from evennia import default_cmds
from commands.teleport import CmdTeleportExample
from commands.scry import CmdScryExample
from commands.command import Kill
from commands.command import Heal
from commands.spiritdesc import SpiritDesc
from commands.find import CmdFind
from typeclasses.exits import CmdFaster
from typeclasses.exits import CmdSlower
from evennia.contrib.slow_exit import CmdSetSpeed
from commands.combat import CmdAttack
from commands.command import FooBar
from commands.command import Sheet
from commands.command import Image
from commands.command import Wield
from commands.command import OverLook
from commands.command import OverInventory
from commands.command import OverSay
from commands.command import OverGet
from commands.command import OverGive
from commands.command import OverDrop
from commands.command import OverPose
from commands.command import OverWhisper
from commands.spells import CmdSpell
from commands.cast import CmdCast
from commands.forensic import CmdLastBreath
from commands.sight import CmdSight
from commands.touch import CmdReach
from commands.general import CmdGet
from commands.exorcise import CmdExorcise
from commands.summon import CmdSummon
from commands.inflict import CmdInflict
from commands.invis import CmdInvis
from commands.bless import CmdBless
from commands.hex import CmdHex
from commands.curse import CmdCurse
from commands.enchant import CmdEnchant
from commands.use import CmdUse
from commands.fate import CmdFate
from commands.astro import CmdAstro
from commands.death import CmdDeathTouch
from commands.drain import CmdDrain
from commands.intimidate import CmdIntimidate
from commands.kinetic import CmdKinetic
from commands.ban import CmdBan
from commands.push import CmdPush
from commands.race import CmdRace
from commands.strike import CmdStrike

class CharacterCmdSet(default_cmds.CharacterCmdSet):
    """
    The `CharacterCmdSet` contains general in-game commands like `look`,
    `get`, etc available on in-game Character objects. It is merged with
    the `PlayerCmdSet` when a Player puppets a Character.
    """
    key = "DefaultCharacter"

    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        super(CharacterCmdSet, self).at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #
        self.add(CmdSetSpeed())
        self.add(OverLook())
        self.add(OverInventory())
        self.add(OverSay())
        self.add(OverDrop())
        self.add(OverGet())
        self.add(OverGive())
        self.add(OverPose())
        self.add(OverWhisper())
        self.add(CmdGet())
class PlayerCmdSet(default_cmds.PlayerCmdSet):
    """
    This is the cmdset available to the Player at all times. It is
    combined with the `CharacterCmdSet` when the Player puppets a
    Character. It holds game-account-specific commands, channel
    commands, etc.
    """
    key = "DefaultPlayer"

    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        super(PlayerCmdSet, self).at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #


class UnloggedinCmdSet(default_cmds.UnloggedinCmdSet):
    """
    Command set available to the Session before being logged in.  This
    holds commands like creating a new account, logging in, etc.
    """
    key = "DefaultUnloggedin"

    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        super(UnloggedinCmdSet, self).at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #


class SessionCmdSet(default_cmds.SessionCmdSet):
    """
    This cmdset is made available on Session level once logged in. It
    is empty by default.
    """
    key = "DefaultSession"

    def at_cmdset_creation(self):
        """
        This is the only method defined in a cmdset, called during
        its creation. It should populate the set with command instances.

        As and example we just add the empty base `Command` object.
        It prints some info.
        """
        super(SessionCmdSet, self).at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #
        self.add(CmdTeleportExample())
        self.add(CmdScryExample())
        self.add(Kill())
        self.add(Heal())
        self.add(SpiritDesc())
        self.add(CmdFind())
        self.add(CmdFaster())
        self.add(CmdSlower())
        self.add(CmdSetSpeed())
        self.add(CmdAttack())
        self.add(FooBar())
        self.add(Sheet())
        self.add(Image())
	self.add(Wield())
	self.add(OverLook())
        self.add(OverInventory())
	self.add(OverSay())
	self.add(OverGet())
	self.add(OverDrop())
	self.add(OverGive())
	self.add(OverPose())
	self.add(OverWhisper())
	self.add(CmdSpell())
        self.add(CmdCast())
        self.add(CmdLastBreath())
        self.add(CmdSight())
        self.add(CmdReach())
        self.add(CmdExorcise())
        self.add(CmdSummon())
        self.add(CmdInflict())
        self.add(CmdInvis())
        self.add(CmdBless())
        self.add(CmdHex())
        self.add(CmdCurse())
        self.add(CmdEnchant())
        self.add(CmdUse())
        self.add(CmdFate())
        self.add(CmdAstro())
        self.add(CmdDeathTouch())
        self.add(CmdDrain())
        self.add(CmdIntimidate())
        self.add(CmdBan())
        self.add(CmdKinetic())
        self.add(CmdPush())
        self.add(CmdRace())
        self.add(CmdStrike())
