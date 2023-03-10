from flask import Flask, request, redirect
import re

app = Flask(__name__)

UNSAFE_REGEX = re.compile("(www|beta).example.com/")
SAFE_REGEX = re.compile(r"(www|beta)\.example\.com/")

@app.route('/some/path/bad')
def unsafe(request):
    target = request.args.get('target', '')
    if UNSAFE_REGEX.match(target):
        return redirect(target)

@app.route('/some/path/good')
def safe(request):
    target = request.args.get('target', '')
    if SAFE_REGEX.match(target):
        return redirect(target)

@app.route("/command1")
def command_injection1():
    files = request.args.get('files', '')
    # Don't let files be `; rm -rf /`
    os.system("ls " + files) # $result=BAD    

# FP reported in https://github.com/github/codeql/issues/3712
# This does not define a regex (but could be used by other code to do so)
escaped = re.escape("https://www.humblebundle.com/home/library")


# Add something
