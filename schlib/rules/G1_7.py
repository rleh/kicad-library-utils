# -*- coding: utf-8 -*-

from rules.rule import *
import platform

class Rule(KLCRule):
    v6 = True
    """
    Create the methods check and fix to use with the kicad lib files.
    """
    def __init__(self, component):
        super(Rule, self).__init__(component, 'Library files must use Unix-style line endings (LF)')
        self.lib_error = False

    def check(self):
        # Only perform this check on linux systems (i.e. Travis)
        # Windows automatically checks out with CR+LF line endings
        if 'linux' in platform.platform().lower():
            if not checkLineEndings(self.component.filename):
                self.lib_error = True
                self.error("Incorrect line endings (.kicad_sym)")
                self.errorExtra("Library files must use Unix-style line endings (LF)")

            if self.lib_error:
                return True

        return False

    def fix(self):
        """
        Proceeds the fixing of the rule, if possible.
        """
        self.success("Line endings will be corrected on save")
