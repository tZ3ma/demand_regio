# DemandRegio

This project aims at setting up both a database and a python toolkit called `disaggregator` for
- temporal and
- spatial disagregation

of demands of 
- electricity,
- heat and
- natural gas

of the final energy sectors
- private households,
- commerce, trade & services (CTS) and
- industry.


## Downloading the Repo to Your Machine

This is an updated version for non-admin windows user via the windows console or ide consoles like vs-code.

First, get the contents of this repo on your machine. To do that you can either use git for windows:

```bash
$ git clone https://github.com/tZ3ma/dm_regio_debug.git
```

or download and extract the zip folder:

    https://github.com/tZ3ma/dm_regio_debug/archive/refs/heads/main.zip


## Setting up the Virtualenvironment

Create a new virtualenvironment using your default python interpreter. This was tested with 3.10.11:

```bash
$ python -m venv demand_regio ALIAS_FOR_YOUR_FOLDER_LOCATION
```

`ALIAS_FOR_YOUR_FOLDER_LOCATION` could thereby be something like `~\Documents\python_venvs` or if you want to have a folder created in your current working directory.

## Installation Using pip

Since script activation is likely prohibited on non-admin windows users, you have to manually state the new python interpretor for installing the requirements:

```bash
$ PATH_TO_MY_INTERPRETER -m pip install -r requirements.txt
```

This will use the newly created venv interpreter to install all requirements using pip, which is reading the requirements.txt file.

On my machine this would look like:

```bash
$ ~\Code\Virtualenvironments\demand_regio\Scripts\python.exe -m pip install -r requirements.txt
```
which installs all required packages. 

## How to start

Since we can activate our virtualenv using bash, we start the correct jupyter notebook kernel by using:
Once the environment is activated, you can start a Jupyter Notebook from there

```bash
$ PATH_TO_MY_INTERPRETER -m jupyter notebook
```

so in my case:

```bash
$ ~\Code\Virtualenvironments\demand_regio\Scripts\python.exe -m jupyter notebook
```

From here on, the orignal documentation can be followed as usual.

As soon as the Jupyter Notebook opens in your browser, click on the `01_Demo_data-and-config.ipynb` file to start with a demonstration:

![Jupyter_View][img_01]

[img_01]: img/jupyter_notebook.png "Jupyter Notebook View"

## Results

![Jupyter_View][img_02]

[img_02]: img/spatial_elc_by_household_sizes.png "Year Electricity Consumption of Private Households"

## How does it work?

For each of the three sectors 'private households', 'commerce, trade & services' and 'industry' the spatial and temporal disaggregation is accomplished through application of various functions. These functions take input data from a database and return the desired output as shwon in the diagram. There are four Demo-Notebooks to present these functions and demonstrate their execution.

![Jupyter_View][img_03]

[img_03]: img/model_overview.png "Schematic diagram of modelling approach"

## Acknowledgements

The development of disaggregator was part of the joint [DemandRegio-Project](https://www.ffe.de/en/topics-and-methods/production-and-market/736-harmonization-and-development-of-methods-for-a-spatial-and-temporal-resolution-of-energy-demands-demandregio) which was carried out by

- Forschungszentrum Jülich GmbH (Simon Burges, Bastian Gillessen, Fabian Gotzens)
- Forschungsstelle für Energiewirtschaft e.V. (Tobias Schmid)
- Technical University of Berlin (Stephan Seim, Paul Verwiebe)

## License

Current version of software written and maintained by Paul A. Verwiebe (TUB)

Original version of software written by Fabian P. Gotzens (FZJ), Paul A. Verwiebe (TUB), Maike Held (TUB), 2019/20.

disaggregator is released as free software under the [GPLv3](http://www.gnu.org/licenses/gpl-3.0.en.html), see [LICENSE](LICENSE) for further information.
