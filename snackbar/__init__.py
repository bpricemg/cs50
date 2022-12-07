import check50
import check50.c

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
def test1():
    """burger, fries, soda"""
    check50.run("./snackbar").stdin("burger").stdin("fries").stdin("soda").stdin("").stdout("\nYour total cost is: $16.50\n")

@check50.check(compiles)
def test2():
    """cold brew, hot dog"""
    check50.run("./snackbar").stdin("cold brew").stdin("hot dog").stdin("").stdout("\nYour total cost is: $8.00\n")
