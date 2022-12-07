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
    check50.run("./snackbar").stdout("\nWelcome to Beach Burger Shack!\nChoose from the following menu to order. Press enter when done.\n\nBurger: $9.50\nVegan Burger: $11.00\nHot Dog: $5.00\nCheese Dog: $7.00\nFries: $5.00\nCheese Fries: $6.00\nCold Pressed Juice: $7.00\nCold Brew: $3.00\nWater: $2.00\nSoda: $2.00\n\nEnter a food item: ").stdin("burger").stdin("fries").stdin("soda").stdin("\n").stdout("\nYour total cost is: $16.50").exit()

@check50.check(compiles)
def trinagle2():
    """cold brew, hot dog"""
    check50.run("./snackbar").stdin("cold brew").stdin("hot dog").stdin("\n").stdout("\nYour total cost is: $8.00").exit()
