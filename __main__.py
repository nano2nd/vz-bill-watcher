#!/usr/bin/env python3

import verizon_bill_tracker.program as program
import os

_cwd = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


if __name__ == "__main__":
    program.start(_cwd)
