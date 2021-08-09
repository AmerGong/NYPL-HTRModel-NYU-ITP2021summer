## Handwritten Text Recognition (HTR) for NYPL 
### NYU-Information Technology Projects-2021 Summer-NYPL Group
#### Group memeber: Anci Hu, Ke Shi, Vipul Goyal, Yuze Gong

Handwritten Text Recognition (HTR) system implemented using [TensorFlow 2.x](https://www.tensorflow.org/) and trained on the NYPL offline HTR datasets. This Neural Network model recognizes the text contained in the images of segmented texts lines.

Data partitioning (train, validation, test) was performed following the methodology of each dataset. The project implemented the HTRModel abstraction model (inspired by [CTCModel](https://github.com/ysoullard/CTCModel)) as a way to facilitate the development of HTR systems.

This model is an improved version of [HTRModel](https://github.com/arthurflor23/handwritten-text-recognition) 's NYPL

## Datasets supported

a. [NYPL](https://colab.research.google.com/drive/1i5NSBPGxkoUDxAIRThoGksHUPuot7TKN?usp=sharing)

b. [Bentham](http://www.transcriptorium.eu/~tsdata/)

c. [IAM](http://www.fki.inf.unibe.ch/databases/iam-handwriting-database)

d. [Rimes](http://www.a2ialab.com/doku.php?id=rimes_database:start)

e. [Saint Gall](https://fki.tic.heia-fr.ch/databases/saint-gall-database)

f. [Washington](https://fki.tic.heia-fr.ch/databases/washington-database)


## Requirements

- Python 3.x
- OpenCV 4.x
- editdistance
- TensorFlow 2.x

## Sample

NYPL sample with default parameters in the **[tutorial](https://github.com/AmerGong/NYPL-HTRModel-NYU-ITP2021summer/blob/main/src/tutorial.ipynb)** file.

1. Preprocessed image (network input)
2. TE_L: Ground Truth Text (label)
3. TE_P: Predicted text (network output)

<img src="https://github.com/AmerGong/NYPL-HTRModel-NYU-ITP2021summer/blob/main/doc/image/NYPL_example.png?raw=true">

## Tutorial
#### Step1.Access to date
A Jupyter Notebook is available to access to NYPL data, check out the **[NYPL_API](https://github.com/AmerGong/NYPL-HTRModel-NYU-ITP2021summer/blob/main/NYPL_API.ipynb)**.

### Step2.Make the NYPL dataset
**[NYPL_dataset](https://drive.google.com/file/d/1wxeNjSUdID2FFUPOsFKkygIKnoWTjg0B/view?usp=sharing)** \
We made the data set ourselves. Use **[Readcoop](https://readcoop.eu/)** to get the ground truth. And use the picture editing tool to cut the images into lines. Process the cut pictures through the **[imageresize.py](https://github.com/AmerGong/NYPL-HTRModel-NYU-ITP2021summer/blob/main/imageresize.py)** file.

### Step3.Clone the project to local
```
git clone https://github.com/AmerGong/NYPL-HTRModel-NYU-ITP2021summer.git
```
###Step4.Open it locally
It is strongly recommended to use PyCharm.

###Step5.


A Jupyter Notebook is available to demo run, check out the **[tutorial](https://github.com/AmerGong/NYPL-HTRModel-NYU-ITP2021summer/blob/main/src/tutorial.ipynb)** on Google Colab/Drive.
