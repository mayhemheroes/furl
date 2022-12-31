#!/usr/bin/env python3
import random

import atheris
import sys
import fuzz_helpers
import random

with atheris.instrument_imports():
    from furl import furl

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        f = furl(fdp.ConsumeRemainingString())
        f.query.encode()
    except ValueError:
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
