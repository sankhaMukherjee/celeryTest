# celeryTest

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

You will need to have a valid Python installation on your system. This has been tested with Python 3.6. It does not assume a particulay version of python, however, it makes no assertions of proper working, either on this version of Python, or on another. 

## Installing

The folloiwing installations are for \*nix-like systems. These have been tried on macOS Sierra (Version 10.12.6) before. 

1. Clone the program to your computer. 
2. type `make firstRun`. This should do the following
    2.1. generate a virtual environment in folder `env`
    2.2. install a number of packages
    2.3. generate a new `requirements.txt` file
    2.4. generate an initial git repository
3. change to the `src` folder
4. run the command `make run`. This should run the small test program
5. Generate your documentation folder by running `make doc`. 
6. Check whether all the tests pass with the command `make test`. This uses py.test for running tests. 

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

 - Python 3.6

## Contributing

Please send in a pull request.

## Authors

Sankha Mukherjee - Initial work (2019)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

```
Things to change:

0. bin/vEnv.sh
    import celery into the new module ------------------------------------------------[DONE]
1. Makefile
    allow for an easy start for celery workers ---------------------------------------[DONE]
    check whether celery workers are working properly ... ----------------------------[]
    check whether the Redis server is working properly -------------------------------[]
2. lib:
    2.1. celery (a whole new library) ------------------------------------------------[DONE]
    2.2. celery (documentation for the library) --------------------------------------[]
    2.3. Example library worker ... --------------------------------------------------[DONE]
    2.4. Documentation for example library worker ... --------------------------------[]
    2.5. Example of new module that uses this celery instance ------------------------[]
    2.6. Make sure that everything is working properly -------------------------------[]

3. config
    3.1. celery.json --> This is a new file that needs to configure celery -----------[DONE]
4. bin
    4.1. the log libraries are in a separate file that starts with `celery_`. These are separately created.
    4.2. The makefile is updated to make sure that the log files for celery can be read properly 

database libraries
3. lib.databaseIO.pgIO: allow the libraries to have multiple attempts on a fail

json config files:
    `import jsonref` instead of `import json`
```


## Acknowledgments

 - Hat tip to anyone who's code was used
 - Inspiration
 - etc.
 