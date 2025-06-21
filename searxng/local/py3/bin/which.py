#!/home/cra88y/proj/searxng-custom-theme/searxng/local/py3/bin/python
# -*- coding: utf-8 -*-
import re
import sys
from fspath._which import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
