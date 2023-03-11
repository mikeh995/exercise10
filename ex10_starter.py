
"""IMPORTING LIBS"""
"""This allows us to use function from the operating system or external libraries"""
import sys
import glob
import os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
# Setting your home directory
    hdir = os.environ['HOME']

# The pattern is using the home directory and the * symbol to indicate we want all files in the home directory
pattern = os.path.join(hdir, '*.html')

# list of filenames
thelist = (glob.glob(pattern))
print(thelist)


# file size
for name in thelist:
    size = os.path.getsize(name)


# only print if size greater than zero (changed to 70 as all files have size even empty)

    if size > 70:
        print(name, size)
    else:
        print(name, "is less than 70 in size")



# remove directory filename

    print(os.path.basename(name))




