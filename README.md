# Real Python PDF
![Tests](https://github.com/oleksis/real-python-pdf/workflows/Tests/badge.svg)

# Motivation
Real Python is an excellent site to learn Python, it has a large number of articles, 
from a basic to advanced level on different topics. During a certain time you can 
collect the list of articles of your interest and organize/structure them in a 
__Table of Contents__ (TOC) and then create a PDF (Python CookBook 👨🏾‍🍳🧾📖🐍) and 
access its Off-Line reading.

# Requirements
* [Selenium](https://selenium-python.readthedocs.io/installation.html)
* [PyPDF2](https://pythonhosted.org/PyPDF2/)

# Usage
You can create a __Table of Contents__ (TOC) by following the Links syntax in 
[Markdown](https://guides.github.com/features/mastering-markdown/)

When run `main.py` it reads the __TOC__ block from this `README.md`, it creates the 
list of links to download the __PDF__ version of each article and save it in the `pdfs` 
folder. When finished, merge all the pdfs passing the __Outlines/Bookmarks__ and save 
the final pdf as `Real_Python.pdf` in the root directory.

```bash
python main.py
```

# Table of Contents

<!-- toc starts -->

##	Basic

* [Python Strings](https://realpython.com/python-strings/)
* [Python String Split Concatenate Join](https://realpython.com/python-string-split-concatenate-join/)
* [Python f Strings](https://realpython.com/python-f-strings/)
* [Python String Formatting](https://realpython.com/python-string-formatting/)
* [Python Exceptions](https://realpython.com/python-exceptions/)
* [Python Modules Packages](https://realpython.com/python-modules-packages/)
* [Python Namespaces Scope](https://realpython.com/python-namespaces-scope/)
* [Python Command Line Arguments](https://realpython.com/python-command-line-arguments/)
* [Python Keywords](https://realpython.com/python-keywords/)
* [How To Implement Python Stack](https://realpython.com/how-to-implement-python-stack/)
* [Python Lambda](https://realpython.com/python-lambda/)
* [Python Main Function](https://realpython.com/python-main-function/)
* [Python3 Object Oriented Programming](https://realpython.com/python3-object-oriented-programming/)
* [Absolute Vs Relative Python Imports](https://realpython.com/absolute-vs-relative-python-imports/)
* [Working With Files In Python](https://realpython.com/working-with-files-in-python/)
* [Python CSV](https://realpython.com/python-csv/)
* [Python JSON](https://realpython.com/python-json/)
* [Python Time Module](https://realpython.com/python-time-module/)

##	Intermediate

* [Python Interface](https://realpython.com/python-interface/)
* [Inheritance Composition Python](https://realpython.com/inheritance-composition-python/)
* [Python Thinking Recursively](https://realpython.com/python-thinking-recursively/)
* [Intro To Python Threading](https://realpython.com/intro-to-python-threading/)
* [List Comprehension Python](https://realpython.com/list-comprehension-python/)
* [Linked Lists Python](https://realpython.com/linked-lists-python/)
* [Python Data Structures](https://realpython.com/python-data-structures/)
* [Sorting Algorithms Python](https://realpython.com/sorting-algorithms-python/)
* [Binary Search Python](https://realpython.com/binary-search-python/)
* [Python Defaultdict](https://realpython.com/python-defaultdict/)

* [Python Debugging Pdb](https://realpython.com/python-debugging-pdb/)
* [Python Testing](https://realpython.com/python-testing/)
* [Pytest Python Testing](https://realpython.com/pytest-python-testing/)
* [Python Code Quality](https://realpython.com/python-code-quality/)
* [Python Type Checking](https://realpython.com/python-type-checking/)
* [Pyinstaller Python](https://realpython.com/pyinstaller-python/)
* [Python Logging Source Code](https://realpython.com/python-logging-source-code/)

##	Advanced

* [Python GIL](https://realpython.com/python-gil/)
* [Python Concurrency](https://realpython.com/python-concurrency/)
* [Python Sockets](https://realpython.com/python-sockets/)
* [Python Async Features](https://realpython.com/python-async-features/)
* [Async IO Python](https://realpython.com/async-io-python/)
* [Python Web Scraping Practical Introduction](https://realpython.com/python-web-scraping-practical-introduction/)

* [Creating Modifying PDF](https://realpython.com/creating-modifying-pdf/)
* [Python Memory Management](https://realpython.com/python-memory-management/)
* [The Model View Controller MVC Paradigm Summarized With Legos](https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/)
* [Python Refactoring](https://realpython.com/python-refactoring/)
* [Python Continuous Integration](https://realpython.com/python-continuous-integration/)
* [Pypi Publish Python Package](https://realpython.com/pypi-publish-python-package/)
* [Python Wheels](https://realpython.com/python-wheels/)
* [Advanced Git For Pythonistas](https://realpython.com/advanced-git-for-pythonistas/)
* [Prevent Python SQL Injection](https://realpython.com/prevent-python-sql-injection/)

<!-- toc ends -->

# Contributing
You can contribute to the project by making a [Pull Request](https://github.com/oleksis/real-python-pdf/pulls) 
or by sending new links to the __Table of Contents__ [Issues](https://github.com/oleksis/real-python-pdf/issues). Any feedbacks is welcome!

# License
[MIT](LICENSE)
