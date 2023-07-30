################### Scope ####################

# Local scope
enemies = 1

def increase_enemies():
  # This variable appear to be the first variable enemies, and now its been modified but make no mistake this is wrong this is a new variable within the scope of the function "The local scope"
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
# This wil print 1 because the variable was never modified 
print(f"enemies outside function: {enemies}")


# Global scope
enemies = 1

def increase_enemies():
  # Now in this example we are actually modified the first variable by explicitly telling to python that the global variable enemies is been modified.
  global enemies
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
# Right here two will be printed like inside the fucntion
print(f"enemies outside function: {enemies}")


# Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@epazos"

# By convention the variable that are constants must be all upper case


