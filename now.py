import py_instagram_dl as pyigdl
import sys

# run script by providing username as command line argument
# usage : python script_name.py username

try:
    pyigdl.download(sys.argv[1], wait_between_requests=4)
except Exception as e:
    print(e)