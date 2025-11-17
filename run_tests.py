# run_tests.py
# Simple pytest launcher for Pythonista
#
# This script uses the built-in pytest module in Pythonista
# and runs all tests under the current directory.

import pytest  # Use built-in pytest in Pythonista

if __name__ == "__main__":
    # Run all tests in the current directory (recursively)
    # -q: quiet mode (less verbose output)
    pytest.main(["-q"])  # Execute pytest from Python script
