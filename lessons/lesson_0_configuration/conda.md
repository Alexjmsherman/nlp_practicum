
<img src="https://github.com/Alexjmsherman/ml_guild/blob/master/raw_data/images/conda_logo.png" alt="conda_logo" width="60px" height="30" />


"Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer. It was created for Python programs, but it can package and distribute software for any language.

Conda as a package manager helps you find and install packages. If you need a package that requires a different version of Python, you do not need to switch to a different environment manager, because conda is also an environment manager. With just a few commands, you can set up a totally separate environment to run that different version of Python, while continuing to run your usual version of Python in your normal environment."

	Source: https://conda.io/docs/

	Cheat Sheet: https://conda.io/docs/_downloads/conda-cheatsheet.pdf


### CONDA INSTALLATION
**Confirm that a Python environment variable is set**

	# start python
	python -i
	# exit python
	exit()
	# check if conda is installed (from git bash, not python)
	conda

	# if either of the above failed add the two following environment variables
	1. search 'edit the system environment variables'
	2. click 'Environment Variables...'
	3. under the system variables, edit the variables 'Path'
	4. Add the two following paths
		- C:\Users\alsherman\AppData\Local\Continuum\anaconda3\Scripts
		- C:\Users\alsherman\AppData\Local\Continuum\anaconda3

**add channels to specify from where to install python packages**

	conda config --add channels conda-forge
	conda config --add channels anaconda
	conda config --add channels jim-hart

** clean your environment (not required, but recommended to avoid install issues)

	conda clean --all --yes

**create a conda environment with specific packages from a requirements.txt**

	conda env create -f environment.yml

	# FYI - code if you want to create a environment.yml
	conda env export > environment.yml


### ENVIRONMENTS
**list conda environments**

	conda env list

**Remove an environment and everything in it**

	conda env remove --name [environment_name]
	# e.g. create a test env
	conda create --name test
	# remove the test env
	conda env remove --name test

<img src="https://github.com/Alexjmsherman/ml_guild/blob/master/raw_data/images/conda_envs.png" alt="conda_logo" width="200" height="200" />


### JUPYTER NOTEBOOK SETUP
**add new kernel to jupyer notebook to access kernel**

Type the following commands:

	source activate guild
		
	conda install nb_conda
		
	python -m ipykernel install --user --name guild --display-name "guild environment"

#### RESOLVE ERRORS
**identify which python version is running in Jupyter notebook**

	# start python
	python -i
	# import the system package
	import sys
	# check which version of python is running
	sys.executable
	# exit python
	exit()

##### if it is the correct python version, try the following
	conda install ipykernel --name Python3

	http://ipython.readthedocs.io/en/stable/install/kernel_install.html#kernels-for-different-environments
	
	https://stackoverflow.com/questions/37433363/link-conda-environment-with-jupyter-notebook


<img src="https://github.com/Alexjmsherman/ml_guild/blob/master/raw_data/images/conda_stack.png" alt="conda_logo" width="300" height="250" />


### RESOURCES:
conda vs pip vs virtualenv

	http://devopspy.com/python/conda-vs-pip/

Video: Managing python environments with conda

	https://www.youtube.com/watch?v=EGaw6VXV3GI

Effectively using open source with conda: 

	https://www.slideshare.net/teoliphant/effectively-using-open-source-with-conda

Create a virtual env with conda

	http://uoa-eresearch.github.io/eresearch cookbook/recipe/2014/11/20/conda/