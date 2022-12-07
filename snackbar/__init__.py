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
