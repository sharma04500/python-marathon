# Packages

Packages are the collection of modules, which can be stored a remote repository called `pypi` and are reused basing on the requirements. pypi is almost similar to docker hub or artifact hub of helm. 
`pypi = python package index`
`pip` is the command line tool to access the pypi. The command structure to download packages from pypi using pip is `pip install <package_name>`.      `pip install boto3` is an example.
`pip list` to see the list of packages. combine with `grep` to filter out specific packages to check their versions.
Simply, A collection of multiple python files bundled together to to perform a task or to build a microservice is called a `package`.