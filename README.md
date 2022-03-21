# Arup COMPAS Workshop

In this workshop, we will explore the core functionality of the COMPAS framework,
and apply some of this functionality to a small structural design project.

Basic knowledge of Python and Rhino are highly recommended.

## Requirements

Please install the following software.

* Anaconda (https://www.anaconda.com/products/individual)
* Rhino 7 (https://www.rhino3d.com/download/)
* VS Code (https://code.visualstudio.com/)
* VS Code Python and Pylance extension from Microsoft (https://code.visualstudio.com/docs/editor/extension-marketplace)

Use the recommended settings during each of the installation processes!

## Install COMPAS

To install COMPAS, we will use `conda`, the package manager of Anaconda.
`conda` is a command line tool.
On Mac, you can use it directly from the Terminal app.
On Windows, **please use the Anaconda Prompt** instead of the default Command Prompt.

In both case, install COMPAS with the following command.

```bash
conda create -n arup -c conda-forge python=3.9 compas --yes 
```

To verify the installation, activate the `arup` environment and run the main COMPAS package (`compas`) as a python module.

```bash
conda activate arup
python -m compas
```

```none
Yay! COMPAS is installed correctly!

COMPAS: 1.14.1
Python: 3.9.10 (CPython)
```

## Join us on Slack

For questions and technical assistance, before, during and after the workshop...

https://join.slack.com/t/arupmarch2022/shared_invite/zt-15bpawx3q-31apqIYiB4atG9YPx5_dLg
