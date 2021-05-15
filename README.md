# NLP - Text Classification

## Information

This project was prepared by Uroš Polanc ([up4472@student.uni-lj.si](mailto:up4472@student.uni-lj.si))
as part of the Natural Langage Processing (NLP) course at the Faculty of Computer Science and Information,
University of Ljubljana.

## Instructions

To run the project just import it into PyCharm, and make sure the following packages are installed
before running the project (the versions are the ones I was using) :

| Package       | Version   |
| :---          | :---      |
| sklearn       | 0.24.2    |
| numpy         | 1.19.5    |
| tensorflow    | 2.5.0     |
| pandas        | 1.2.4     |
| nltk          | 3.6.2     |
| matplotlib    | 3.4.0     |
| xlrd          | 2.0.1     |
| openpyxl      | 3.0.7     |
| wordcloud     | 1.8.1     |
| scipy         | 1.6.3     |
| transformers  | 4.6.0     |
| argparse      | 1.1       |

The packages can be installed in the python terminal with the following command :

```
pip install package-name
```

or you can run the following command that will install them all if your system can run .bat files :

```
pip_install_all
```

Note that the BERT uses tensorflow learning, which means it needs CUDA cores, or more specifically an NVidea GPU. If you
have an AMD GPU be prepered to wait a very long time before the process is done. But there are some solutions for that,
such as ROCm (https://rocmdocs.amd.com/en/latest/), look at that if you need.

## Repository structure

- ``` .\example\ ``` contains python code for some examples
- ``` .\reports\ ``` contains pdf reports
- ``` .\resources\ ``` contains all the necessary resources (.txt, .xlsx, .docx)
- ``` .\resources\models ``` contains all the necessary pretrained models (.bin, .json, .txt)
- ``` .\source\ ``` contains python source code

## Running

You can run full analysis of all possible results with the following command :

```
python main.py
```

or to run a more targeted analysis check the help of the command line by running :

```
python main.py --help
```
