x = 5
y = 17
print(__name__)

# it only runs if this is the file that is run by the user
# if it gets imported, it's name is just the filename
# if you run it, it's name gets set to __main__
if __name__ == '__main__':
    print('this should always run, right? ')
    # require all of your code to be inside of this if statement

# AVOID AT ALL COSTS: def main():
