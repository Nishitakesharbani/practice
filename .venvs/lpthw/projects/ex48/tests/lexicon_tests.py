from nose.tools import*
import ex48 import lexicon

def setup():
    print("SETUP")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I Ran!",end='')