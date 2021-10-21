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
    check50.c.compile("trinagles.c", lcs50=True)

@check50.check(compiles)
def trinagle1():
    """3, 4, 5"""
    check50.run("./hello").stdin("3").stdin("4").stdin("5").stdout("Valid").exit()

@check50.check(compiles)
def trinagle2():
    """2, 3, 5"""
    check50.run("./hello").stdin("2").stdin("3").stdin("5").stdout("Invalid").exit()
    
@check50.check(compiles)
def trinagle3():
    """-3, 4, 5"""
    check50.run("./hello").stdin("-3").stdin("4").stdin("5").stdout("Invalid").exit()
