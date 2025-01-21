# python-start

Before we start, please, I know there are a few shortcuts and "not best practices" here.  The goal is 
simply to get people up and writing a piece of executable code and a test in Python in Visual Studio
Code.  Thanks.

## Overview

This is the companion repo to the "Getting Started" located in Confluence at
[Getting Started with Python and VSCode](https://mypizza.atlassian.net/wiki/spaces/IP1/pages/5501878367/Getting+Started+with+Python+and+VSCode).

I created this as close to the most basic project I could make that would:
* run in VSCode
* include source code and a test file
* have some of the most basic configurations.

This isn't necessarily how you'd write a normal repo. You would __NOT__ check in:
* an `.env` because typically it might hold access keys or other values that you don't want to check in.
* a `.vscode` folder because the person working on the project might not be using VSCode or might have their
  own preferred setup.
* a `*.code-workspace` file because, again, you might not be using VSCode

But, this is a repo to get you up and started in VSCode as soon as possible. In the future, you would:
* include `.env`, `.vscode/`, and `*.code-workspace` in the `.gitignore` file so that it isn't save to git.
* and then recreate these files in a manner of your choices that works with your IDE.

## Try it out.

There are four things that I intended. There are more elaborate instructions on the Confluence Page.

In the integrated terminal, try these:
```
# run the one test
pytest

# run the one executable
python src/intro/my_executable.py
```

Within the IDE, there are two things to try:

* In the testing tab, you should be able to click on test and debug or run it.
* If you open # djangocourse
