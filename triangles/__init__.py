import check50
import check50.c
import re

@check50.check()
def exists():
    """triangles.c exists"""
    check50.exists("triangles.c")

@check50.check(exists)
def compiles():
    """triangles.c compiles"""
    # Check if student code compiles
    check50.c.compile("triangles.c", lcs50=True)

@check50.check(compiles)
def trinagle1():
    """Accepts a valid triangle 3, 4, 5"""
    check50.run("./triangles").stdin("3").stdin("4").stdin("5").stdout("Valid").exit()

@check50.check(compiles)
def trinagle2():
    """ Rejects an invalid triangle 2, 3, 5"""
    check50.run("./triangles").stdin("2").stdin("3").stdin("5").stdout("Invalid").exit()
    
@check50.check(compiles)
def trinagle3():
    """Rejects negative numbers -3, 4, 5"""
    check50.run("./triangles").stdin("-3").stdin("4").stdin("5").stdout("Invalid").exit()

@check50.check(compiles)
def trinagle4():
    """Rejects 0 0, 0, 0"""
    check50.run("./triangles").stdin("0").stdin("0").stdin("0").stdout("Invalid").exit()
