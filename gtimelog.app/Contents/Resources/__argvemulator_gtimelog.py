import argvemulator, os, sys

argvemulator.ArgvCollector().mainloop()

gtimelog_dir = os.path.join(os.path.split(__file__)[0], "gtimelog")
gtimelog_dir = os.path.abspath(gtimelog_dir)
sys.path.insert(0, gtimelog_dir)

import gtimelog
gtimelog.main()
