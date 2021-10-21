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
def emma():
    """responds to name Emma"""
    check50.run("./hello").stdin("Emma").stdout("Emma").exit()

@check50.check(compiles)
def rodrigo():
    """responds to name Rodrigo"""
    check50.run("./hello").stdin("Rodrigo").stdout("Rodrigo").exit()
