# Virtual Environment

Virtual environments in python offers logical seperation of environemnts and is almost similar to VM's in the concpet of virtualization of servers using hypervisors.
Instad of creating multiple VM's to satisfy the requirements, we can simply create virtual environments and switch in between them with respect to the requirements.
`Environment` - A space containing all the required packages of specific versions to execute a piece of code and deliver the result.
For example, we can't install two versions of a same package in the same machine. So, if we create different virtual environments, we can install different versions of the same package into different virtual environments.
To install virtual environments, download the package from pip using `pip install virtualenv`
After installing, simply type `python -m venv <venv_name>`. For example, `python -m venv demo_project`
Do `ls -al`. 
Just switch into the venv using `source <venv_name>/bin/activate` and enter into that virtual environments.
For exmaple, `source demo_venv/bin/activate`
Simply type `deactivate` in the CLI to exit from the virtual environments.

Similarly, we can create any number of virtual environments with respect to the requirements and resource availability.