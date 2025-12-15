import check50
import check50.c
import re

@check50.check()
def exists():
    """digitsum.c exists"""
    check50.exists("digitsum.c")

@check50.check(exists)
def compiles():
    """digitsum.c compiles"""
    # Check if student code compiles
    check50.c.compile("digitsum.c", lcs50=True)

@check50.check(compiles)
def positive1():
    """digit sum of 1234"""
    check50.run("./digitsum").stdin("1234").stdout("10").exit()

@check50.check(compiles)
def positive2():
    """digit sum of 1"""
    check50.run("./digitsum").stdin("1").stdout("1").exit()
    
@check50.check(compiles)
def negative():
    """digit sum of -5391"""
    check50.run("./digitsum").stdin("-5391").stdout("-18").exit()
