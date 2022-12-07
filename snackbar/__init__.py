import check50
import check50.c
import re

@check50.check()
def exists():
    """snackbar.c exists"""
    check50.exists("snackbar.c")

@check50.check(exists)
def compiles():
    """snackbar.c compiles"""
    # Check if student code compiles
    check50.c.compile("snackbar.c", lcs50=True)

@check50.check(compiles)
def trinagle1():
    """burger, fries, soda"""
    check50.run("./snackbar").stdin("burger").stdin("fries").stdin("soda").stdin("\n").stdout("Your total cost is: $16.50").exit()

@check50.check(compiles)
def trinagle2():
    """cold brew, hot dog"""
    check50.run("./snackbar").stdin("cold brew").stdin("hot dog").stdin("\n").stdout("Your total cost is: $8.00").exit()
