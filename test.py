#!/usr/bin/env python

import sys
import doctest

import pari_utils
import pari_utils.args
import pari_utils.paths
import pari_utils.ret

num_failed = 0
for mod in [pari_utils, pari_utils.args, pari_utils.paths, pari_utils.ret]:
    res = doctest.testmod(mod, verbose=True)
    num_failed += res.failed
sys.exit(num_failed)
