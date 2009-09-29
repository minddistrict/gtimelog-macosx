import argvemulator, os, sys

# Don't know what ArgvCollector does, but on Snow Leopard it is broken but
# it seems to be not necessary
#argvemulator.ArgvCollector().mainloop()

gtimelog_dir = os.path.join(os.path.split(__file__)[0], "gtimelog")
gtimelog_dir = os.path.abspath(gtimelog_dir)
sys.path.insert(0, gtimelog_dir)

import gtimelog
gtimelog.main()
