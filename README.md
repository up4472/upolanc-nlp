# NLP - Text Classification

## Information

This project was prepared by Uroš Polanc ([up4472@student.uni-lj.si](mailto:up4472@student.uni-lj.si))
as part of the Natural Langage Processing (NLP) course at the Faculty of Computer Science and Information,
University of Ljubljana.

## Repository structure

- ``` .\example\ ``` contains python code for some examples
- ``` .\reports\ ``` contains pdf reports
- ``` .\resources\ ``` contains all the necessary resources (.txt, .xlsx, .docx)
- ``` .\resources\models ``` contains all the necessary pretrained models (.bin, .json, .txt)
- ``` .\source\ ``` contains python source code

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

Note that wordcloud package might fail if you do not have Microsoft Visual C++ Build Tools, this can be solved by downloading
and installing it from https://visualstudio.microsoft.com/visual-cpp-build-tools/.

Note that the BERT uses tensorflow learning, which means it needs CUDA cores, or more specifically an NVidea GPU. If you
have an AMD GPU be prepered to wait a very long time before the process is done. But there are some solutions for that,
such as ROCm (https://rocmdocs.amd.com/en/latest/), look at that if you need.

After the packages have been installed, we need to download the pretrained BERT models. The base english conversation
model can be found at http://docs.deeppavlov.ai/en/master/features/pretrained_vectors.html. Download the Conversational
BERT pythorch version, then extract and save all the files into the ``` .\resources\models\pretrained\english\ ```
folder.

Unless you want to train the database yourself you will also need our pretrained models, which can be found at
https://mega.nz/file/dsgm1SIa#KUFvVSIMooJFr9aR7y7xSjc1Uv06lolol5y9FQiD2AE and should be extracted to the ``` .\resources\models\pretrained\custom\ ``` folder.

The final structure should look exactly like this :
```
.\resources
    +-- models
        +-- pretrained
            +-- english
                +-- config.json
                +-- pytorch_model.bin
                +-- vocab.txt
            +-- custom
                +-- bookid3
                    +-- config.json
                    +-- pytorch_model.bin
                    +-- vocab.txt
                +-- codepreliminary9
                    +-- config.json
                    +-- pytorch_model.bin
                    +-- vocab.txt
                +-- codepreliminary16
                    +-- config.json
                    +-- pytorch_model.bin
                    +-- vocab.txt
                +-- topic3
                    +-- config.json
                    +-- pytorch_model.bin
                    +-- vocab.txt
```

After all packages have been instaled and all models have been downloaded, we can run the project.

## Running

You can run full analysis of all possible results with the following command (with pretrained it takes around 45 min
on CPU) :

```
python main.py
```

or to run a more targeted analysis check the help of the command line by running :

```
python main.py --help
```
