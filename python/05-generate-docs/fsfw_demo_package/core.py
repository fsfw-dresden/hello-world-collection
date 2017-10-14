
"""
This is a test module
"""


class ABC(object):
    """
    This is a dummy class.
    Each method of this class which starts with `test_` will be run
    automatically by the function `unittest.main()` (see below).
    """

    def __init__(self, a, b):
        """
        The constructor method.

        Parameters:
        a

        b
        """

        # nothing to do ...

        pass

    def do_important_things(self, x, y=0):
        """
        Method for performing important calculation. See [1] for details.

        Parameters

        x

        y


        [1]: Ostrom, Elinor; Hess, Charlotte (2007).
        Understanding knowledge as a commons: from theory to practice. Cambridge, Massachusetts: MIT Press
        """


def myfunction(i, j, k):
    """
    A functions that probably does something.

    Parameters:


    After description of the parameters typically there is more information
    on the documented function or method.
    """

    pass
