
import os
import sys
import glob

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
print("# Construct a portable wildcard pattern")
pattern = os.path.join(hdir, '*.*')
print(pattern)

# Use the glob.glob() function to obtain the list of filenames
filenames = glob.glob(pattern)
print(filenames)

# Use os.path.getsize to find each file's size
for f in filenames:
    print(f, os.path.getsize(f))

# Add a test to only display files that do not have a size of zero
for f in filenames:
    if os.path.getsize(f) > 0:
        print(os.path.basename(f), os.path.getsize(f))





