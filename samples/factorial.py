#
#
#

import sys

#sys.path.insert(0, "../lib")

from phidias.Types  import *
from phidias.Main import *
from phidias.Lib import *


class fact(Procedure): pass

def_vars("Acc", "N")
fact(N) >> [ fact(N, 1) ]
fact(1, Acc) >> [ show_line("the resulting factorial is = ", Acc) ]
fact(N, Acc) >> \
    [
        "Acc = N * Acc",
        "N = N - 1",
        fact(N, Acc)
    ]

PHIDIAS.run()
PHIDIAS.shell(globals())

