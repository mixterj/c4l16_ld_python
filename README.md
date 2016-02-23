CODE4Lib 2016 Python RDF Parser
===============
This Python code demonstrates how to load a URI into a graph in memory and conduct queries on it for specific Schema.org properties.

Instructions:
===============

The Python code assumes 2 variables by default. The first is the URI to load and query. The second is a set of Schema.org properties to query for. 

Below are instructions on how to install Python on Mac and Windows as well as how to pull the GitHub Repo and use the code.

Mac:
------

1) Make sure Python is installed (is packaged with Mac OS X). If not install Python (https://www.python.org/downloads/)

2) From the Terminal install Pip: 

    sudo easy_install pip

	
Windows:
------

1) Download Python 2.7.11 (https://www.python.org/downloads/windows/). Pip is already packaged with the install.

6) Set Python Path for Windows

    Windows 7 - http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7
    Windows 8 and 10 - http://stackoverflow.com/questions/21372637/installing-python-2-7-on-windows-8
	
Using the Python code:
------

1) Clone the GitHub project

2) Run the setup.py installation to include the Python dependencies
    
    python setup.py install

3) Run the script using these parameters.
  
    parsegraph

4) You can override the default settings by inlcuding these parameters

    parsegraph -u <URI to be loaded and parsed> -p <predicates to query for>

5) The acceptable predicates are

    name - Name of the URI resource
    description - Description of the URI resource
    creator - Name of the creator of the URI resource (if no name, the URI for the creator will be returned)
    about - Name of the subjects of the URI resource (if no name, the URI for the subject will be returned)

