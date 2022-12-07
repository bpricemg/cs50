import check50
import check50.c

@check50.check()
def exists():
    """initials.c exists."""
    check50.exists("initials.c")

@check50.check(exists)
def compiles():
    """initials.c compiles."""
    check50.c.compile("initials.c", lcs50=True)

@check50.check(compiles)
def uppercase():
    """Outputs BAP for Brandon Alexander Price"""
    check50.run("./initials").stdin("Brandon Alexander Price", prompt=False).stdout("BAP").exit(0)

@check50.check(compiles)
def lowercase():
    """Outputs BAP for brandon alexander price"""
    check50.run("./initials").stdin("brandon alexander price", prompt=False).stdout("BAP").exit(0)

@check50.check(compiles)
def mixed_case():
    """Outputs BP for brandon Price"""
    check50.run("./initials").stdin("brandon Price", prompt=False).stdout("BP").exit(0)

@check50.check(compiles)
def all_uppercase():
    """Outputs B for BRANDON"""
    check50.run("./initials").stdin("BRANDON", prompt=False).stdout("B").exit(0)
