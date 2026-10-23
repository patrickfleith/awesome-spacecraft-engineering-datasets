# Awesome Spacecraft Engineering Datasets [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

Datasets for space vehicle engineering (spacecraft, rovers), for industry and research. Grouped by spacecraft subsystem.

## Contents

[Propulsion](#propulsion) (1) · [Power](#power) (3) · [Structures and mechanisms](#structures-and-mechanisms) (5) · [Avionics and EEE parts](#avionics-and-eee-parts) (2) · [Operations and telemetry](#operations-and-telemetry) (7) · [GNC and space debris](#gnc-and-space-debris) (5) · [Payload imaging](#payload-imaging) (2) · [Space environment](#space-environment) (1) · [Engineering text](#engineering-text) (5) · [Astronomy](#astronomy) (4)

[Index by ML/AI task](#index-by-mlai-task) lists the same datasets the other way round.

---

## Propulsion

#### [Spacecraft Thruster Firing Tests](https://www.kaggle.com/datasets/patrickfleith/spacecraft-thruster-firing-tests-dataset)

10.9 GB · time series · Patrick Fleith, 2022

![regression](assets/badges/task-regression.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: synthetic](assets/badges/origin-synthetic.svg)

<details><summary>Description</summary>

Time series analysis and predictive modelling of engine thrust, mass flow rate, and performance degradation over time. The data is synthetic, partially based on the real-world physics of a chemical reaction control thruster, which makes it the closest public stand-in for RCS acceptance test data.

Time series in .csv files.

</details>

## Power

#### [Mars Express Power Challenge](https://kelvins.esa.int/mars-express-power-challenge/home/)

150 MB · time series · ESA Advanced Concepts Team, 2021

![regression](assets/badges/task-regression.svg) ![forecasting](assets/badges/task-forecasting.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

Predict the average current consumption of 33 thermal power lines per hour of the mission's fourth Martian year, 2014-04-14 to 2016-03-01. Flight data from an operating interplanetary mission.

Time series in .csv files.

</details>

#### [NASA Battery](https://www.kaggle.com/datasets/patrickfleith/nasa-battery-dataset)

210 MB · time series · no licence stated · NASA Ames, 2007

![rul](assets/badges/task-rul.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

A set of Li-ion batteries were run through different operational profiles (charge, discharge and impedance) at various temperatures. Impedance measurement was carried out through an electrochemical impedance spectroscopy frequency sweep. Repeated charge and discharge cycles accelerate ageing, while the impedance measurements give insight into the internal battery parameters that change as ageing progresses. The experiments stopped when the batteries reached end-of-life criteria.

Usable for predicting both remaining charge for a given discharge cycle and remaining useful life. Batches of 6 experiments, in .mat files, with experiment details in an associated README.txt.

*B. Saha and K. Goebel (2007), Prognosis CoE, NASA Ames*

</details>

#### [Randomized Battery Usage](https://www.kaggle.com/datasets/patrickfleith/nasa-randomized-battery-usage-dataset)

1.12 GB · time series · no licence stated · NASA Ames

![rul](assets/badges/task-rul.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

Batteries are continuously cycled with randomly generated current profiles, which is closer to real load than a constant-current test. Reference charging and discharging cycles are also performed after each fixed interval of randomized usage, to provide reference benchmarks for battery state of health.

Download: section 11, `Randomized Battery Usage`, of the [NASA Prognostics Data Repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/).

*B. Bole, C. Kulkarni, and M. Daigle, NASA Ames Research Center*

</details>

## Structures and mechanisms

#### [CFRP Composites](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)

4.5 GB · time series · no licence stated · Stanford SACL and NASA Ames

![rul](assets/badges/task-rul.svg) ![anomaly-detection](assets/badges/task-anomaly-detection.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

Run-to-failure experiments on CFRP panels with periodic measurements to capture internal damage growth under tension-tension fatigue. Monitoring data consists of Lamb wave signals from a network of 16 piezoelectric (PZT) sensors and multiple triaxial strain gages. Periodic x-rays were taken to characterise internal damage as ground truth information. Three different layups were tested.

Organised into three zipped folders, each containing data from coupons of a single layup type, a readme, and a folder with reports and papers published from this dataset. Download: section 2, `Carbon Fiber-Reinforced Polymer (CFRP) Composites`.

*Abhinav Saxena, Kai Goebel, Cecilia C. Larrosa, and Fu-Kuo Chang. Experiments conducted at Stanford Structures and Composites Laboratory (SACL) in collaboration with the Prognostic Center of Excellence (PCoE) of NASA Ames Research Center*

</details>

#### [NASA Bearing](https://www.kaggle.com/vinayak123tyagi/bearing-dataset)

6.08 GB · time series · University of Cincinnati IMS

![rul](assets/badges/task-rul.svg) ![anomaly-detection](assets/badges/task-anomaly-detection.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

Four bearings were installed on a shaft. Three data sets are included in the data packet, and each one describes a test-to-failure experiment. Each data set consists of individual files that are 1-second vibration signal snapshots recorded at specific intervals. Each file consists of 20,480 points with the sampling rate set at 20 kHz.

Data format is ASCII and .txt. The standard bearing degradation benchmark.

*University of Cincinnati, Center for Intelligent Maintenance Systems (IMS)*

</details>

#### [FEMTO Bearings](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)

2 GB · time series · no licence stated · FEMTO-ST Institute

![rul](assets/badges/task-rul.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

Experiments on bearings' accelerated life tests. A second bearing benchmark on a different rig, which makes it useful for checking whether a model trained on NASA Bearing transfers.

Download the dataset by searching for section 10, `FEMTO Bearing`, in the NASA Prognostics Data Repository.

*P. Nectoux, R. Gouriveau, K. Medjaher, E. Ramasso, B. Morello, N. Zerhouni, C. Varnier, FEMTO-ST Institute, Besancon, France, and NASA Ames Research Center*

</details>

#### [NASA Milling](https://www.kaggle.com/datasets/vinayak123tyagi/milling-data-set-prognostic-data)

72.6 MB · time series · UC Berkeley BEST lab, 2007

![regression](assets/badges/task-regression.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

Can you predict the flank wear VB in mm, the wearing of the milling insert after some runs? Experiments on a milling machine for different speeds, feeds, and depths of cut, recording the wear of the milling insert.

The dataset is in .mat format and has been zipped. A Readme.pdf provides details on the experimental protocol and the measurement techniques.

*A. Agogino and K. Goebel (2007), BEST lab, UC Berkeley*

</details>

#### [NASA Airfoil Self-Noise](https://archive.ics.uci.edu/dataset/291/airfoil+self+noise)

< 1 MB · tabular · CC BY 4.0 · NASA

![regression](assets/badges/task-regression.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

A series of aerodynamic and acoustic tests of two and three-dimensional airfoil blade sections, conducted in an anechoic wind tunnel. The span of the airfoil and the observer position were the same in all of the experiments. The objective is to predict the aerofoil noise, the scaled sound pressure level.

Small enough to prototype a pipeline in minutes.

*Thomas F. Brooks, D. Stuart Pope and Michael A. Marcolini (NASA). Donor: Dr. Roberto Lopez*

</details>

## Avionics and EEE parts

#### [MOSFET Thermal Overstress Aging](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)

7.3 GB · time series · no licence stated · NASA Ames

![rul](assets/badges/task-rul.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

Run-to-failure experiments on power MOSFETs under thermal overstress. The data is in .mat format and has been zipped.

Download: section 13, `Metal-Oxide-Semiconductor Field-Effect Transistor (MOSFET) Thermal Overstress Aging`. The DataSet reference document can be downloaded [here](http://ti.arc.nasa.gov/m/project/prognostic-repository/MOSFET%20Thermal%20Overstress%20Aging%20Document.pdf).

*J. R. Celaya, A. Saxena, S. Saha, and K. Goebel, NASA Ames Research Center*

</details>

#### [Capacitor Electrical Stress](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)

4.8 GB · time series · no licence stated · NASA Ames

![rul](assets/badges/task-rul.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

Capacitors were subjected to electrical stress under three voltage levels: 10 V, 12 V and 14 V. The data set contains EIS data as well as charge/discharge signal data, in .mat format, zipped.

Download: section 12, `Capacitor Electrical Stress`. The DataSet reference document can be downloaded [here](http://ti.arc.nasa.gov/m/project/prognostic-repository/Description%20of%20Electrolytic%20Capacitors%20under%20Electrical%20Overstress%20Data%20Sets.pdf).

*J. Renwick, C. Kulkarni, and J. Celaya, NASA Ames Research Center*

</details>

## Operations and telemetry

Housekeeping telemetry and its simulated equivalent. Spacecraft health monitoring work starts here.

#### [ESA Anomaly Dataset](https://zenodo.org/records/15237121)

11.6 GB · time series · CC BY 3.0 IGO · K. Kotowski et al., 2024

![anomaly-detection](assets/badges/task-anomaly-detection.svg) ![novelty-detection](assets/badges/task-novelty-detection.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

A large-scale, real-life satellite telemetry dataset with curated anomaly annotations, originating from three ESA missions. The task is to detect anomalies in the telemetry time series. It is the largest labelled operational telemetry set available.

The dataset is in compressed Pickle files with data, and CSVs with annotations.

*K. Kotowski et al., "European Space Agency Benchmark for Anomaly Detection in Satellite Telemetry," 2024, http://arxiv.org/abs/2406.17826*

</details>

#### [Controlled Anomalies Time Series (CATS)](https://zenodo.org/records/8338435)

2.0 GB · time series · CC BY 4.0 · Patrick Fleith, Solenix, 2023

![anomaly-detection](assets/badges/task-anomaly-detection.svg) ![novelty-detection](assets/badges/task-novelty-detection.svg) ![outlier-detection](assets/badges/task-outlier-detection.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: synthetic](assets/badges/origin-synthetic.svg)

<details><summary>Description</summary>

A large, multivariate time series dataset designed specifically for benchmarking anomaly detection algorithms. It contains 17 variables (sensors, control commands, and external stimuli) from a simulated complex system, with 5 million data points including 200 injected anomalies.

Useful for evaluating and developing algorithms for anomaly detection in multivariate time series, supporting both semi-supervised (novelty detection) and unsupervised (outlier detection) approaches. Because the anomalies are injected, the ground truth is exact, which no real telemetry set can give you. The time series are in a .csv or .parquet file.

*Patrick Fleith. (2023). Controlled Anomalies Time Series (CATS) Dataset (Version 2) [Data set]. Solenix Engineering GmbH. https://doi.org/10.5281/zenodo.8338435*

</details>

#### [SMAP and MSL](https://www.kaggle.com/datasets/patrickfleith/nasa-anomaly-detection-dataset-smap-msl)

~250 MB · time series · NASA JPL, 2018

![anomaly-detection](assets/badges/task-anomaly-detection.svg) ![novelty-detection](assets/badges/task-novelty-detection.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

Expert-labeled telemetry anomaly data from the Soil Moisture Active Passive (SMAP) satellite and the Mars Science Laboratory (MSL) rover, Curiosity. Indications of telemetry anomalies can be found within Incident Surprise Anomaly (ISA) reports. All telemetry channels discussed in an individual ISA were reviewed to ensure that the anomaly was evident in the associated telemetry data, and specific anomalous time ranges were manually labeled for each channel. If multiple anomalous sequences and channels closely resembled each other, only one was kept, in order to create a diverse and balanced set.

Anomalies were classified into two categories, point and contextual, to distinguish between anomalies that would likely be identified by properly-set alarms or distance-based methods that ignore temporal information (point anomalies), and those that require more complex methodologies such as LSTMs or Hierarchical Temporal Memory (contextual anomalies).

**SMAP**: 55 TM channels, 429,735 total TM values, 69 anomalies. **MSL**: 27 TM channels, 66,709 total TM values, 36 anomalies. Data in .npy files.

*Kyle Hundman et al. 2018, NASA Jet Propulsion Laboratory*

</details>

#### [LASP Spacecraft Telemetry](https://github.com/sapols/Satellite-Telemetry-Anomaly-Detection)

14 MB · time series · Shawn Polson, LASP

![outlier-detection](assets/badges/task-outlier-detection.svg) ![labels: no](assets/badges/labels-no.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

This dataset can be used for visualisation and analysis of telemetry data that is built and maintained at the Laboratory for Atmospheric and Space Physics. There is no ground truth, so it suits unsupervised work only.

Data in .csv files. Read more in [Unsupervised Machine Learning for Spacecraft Anomaly Detection in WebTCAD](https://github.com/sapols/Satellite-Telemetry-Anomaly-Detection/blob/master/Paper/Unsupervised%20Machine%20Learning%20for%20Spacecraft%20Anomaly%20Detection%20in%20WebTCAD.pdf).

*Shawn Polson, Laboratory for Atmospheric and Space Physics*

</details>

#### [Satellite (ODDS)](http://odds.cs.stonybrook.edu/satellite-dataset/)

< 1 MB · tabular · Adapted from A. Srinivasan, 1993

![outlier-detection](assets/badges/task-outlier-detection.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

The original Statlog (Landsat Satellite) dataset from the UCI machine learning repository is a multi-class classification dataset. Here, the training and test data are combined. The smallest three classes, 2, 4 and 5, are combined to form the outliers class, while all the other classes are combined to form an inlier class. A sanity check for a new detector before you point it at telemetry.

Data in a .mat file. X = multi-dimensional point data, y = labels (1 = outliers, 0 = inliers).

*Adapted from Ashwin Srinivasan (1993), University of Strathclyde*

</details>

#### [Satimage-2 (ODDS)](http://odds.cs.stonybrook.edu/satimage-2-dataset/)

< 1 MB · tabular · Adapted from A. Srinivasan, 1993

![outlier-detection](assets/badges/task-outlier-detection.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

The original Statlog (Landsat Satellite) dataset from the UCI machine learning repository is a multi-class classification dataset. Here, the training and test data are combined, and class 2 is down-sampled to 71 outliers, while all the other classes are combined to form an inlier class. The modified dataset is referred to as Satimage-2. A harder imbalance than Satellite (ODDS).

Data in a .mat file. X = multi-dimensional point data, y = labels (1 = outliers, 0 = inliers).

*Adapted from Ashwin Srinivasan (1993), University of Strathclyde*

</details>

#### [Turbofan Engine Degradation (C-MAPSS)](https://www.nasa.gov/content/prognostics-center-of-excellence-data-set-repository)

45.3 MB · time series · no licence stated · NASA Ames, 2008

![rul](assets/badges/task-rul.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: synthetic](assets/badges/origin-synthetic.svg)

<details><summary>Description</summary>

Engine degradation simulation carried out using C-MAPSS. Four different sets were simulated under different combinations of operational conditions and fault modes. The data records several sensor channels to characterise fault evolution. An aero engine rather than spacecraft hardware, and the standard RUL benchmark that most published methods report against.

The dataset is in text format and has been zipped, including a readme file and an original paper describing damage propagation modelling.

*A. Saxena and K. Goebel (2008), Prognostics CoE at NASA Ames*

</details>

## GNC and space debris

#### [Pose Estimation Challenge 2021](https://kelvins.esa.int/pose-estimation-2021/home/)

15.7 GB · image · ESA ACT and Stanford SLAB, 2021

![pose-estimation](assets/badges/task-pose-estimation.svg) ![domain-adaptation](assets/badges/task-domain-adaptation.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: mixed](assets/badges/origin-mixed.svg)

<details><summary>Description</summary>

Can you predict the position and orientation of a spacecraft in realistic images while only being provided with labels from computer generated examples? SPEC2021 is explicitly designed to investigate the domain gap between synthetic labelled and realistic unlabelled images.

The challenge sheds light on the next big question for spaceborne computer vision algorithms: how can one validate on-ground a pose estimation algorithm on spaceborne image targets that are simply unavailable prior to the mission? Unlike on Earth, autonomous driving in space prohibits habitual road tests and on-site debugging.

Data provided are .json (filenames) and 8-bit monochrome images in jpeg format, at a resolution of 1920x1200 pixels. Only the synthetic images carry labels. You may also want to look at the dataset of the previous Pose Estimation Challenge from 2019, [here](https://kelvins.esa.int/satellite-pose-estimation-challenge/).

*Advanced Concepts Team (ESA) and Space Rendezvous Laboratory (SLAB) of Stanford University, 2021*

</details>

#### [spotGEO](https://kelvins.esa.int/spot-the-geo-satellites/home/)

4.2 GB · image · ESA ACT and University of Adelaide, 2020

![object-detection](assets/badges/task-object-detection.svg) ![regression](assets/badges/task-regression.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

The goal is to detect orbiting objects in the geostationary ring from sequences of 5 consecutive frames imaging some unknown portion of the sky, provided by a low-cost ground based telescope. Can you learn how to cope with cloud cover, atmospheric and weather effects, light pollution, sensor noise and defects, and star occlusions?

32,000 grayscale images of size 640x480 pixels, plus JSON files.

*Advanced Concepts Team (ESA) and University of Adelaide, 2020*

</details>

#### [Space Debris: the origin](https://kelvins.esa.int/space-debris-the-origin/home/)

< 3 MB · tabular · ESA Advanced Concepts Team, 2021

![classification](assets/badges/task-classification.svg) ![regression](assets/badges/task-regression.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: synthetic](assets/badges/origin-synthetic.svg)

<details><summary>Description</summary>

Determine two things for each of the debris given: the id of the defunct satellite (classification task), and the value of the effective area over mass ratio Cr(A/m) of the debris (regression task).

Data are in .dat files.

*Advanced Concepts Team, European Space Agency, 2021*

</details>

#### [The Kessler Run (GTOC9)](https://kelvins.esa.int/gtoc9-kessler-run/home/)

< 1 MB · tabular · ESA Advanced Concepts Team, 2017

![optimisation](assets/badges/task-optimisation.svg) ![labels: no](assets/badges/labels-no.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

Design and optimise n missions able to cumulatively remove all the 123 orbiting debris. One mission is a multiple-rendezvous spacecraft trajectory where a subset of size N of the 123 orbiting debris is removed by the delivery and activation of N de-orbit packages. Optimisation rather than learning, so there are no labels.

Data are orbital debris elements in .csv.

*Advanced Concepts Team, European Space Agency, 2017*

</details>

#### [Planetary Defence Challenge](https://kelvins.esa.int/planetary-defence/home/)

< 1 MB · time series · ESA Advanced Concepts Team, 2021

![regression](assets/badges/task-regression.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: synthetic](assets/badges/origin-synthetic.svg)

<details><summary>Description</summary>

Several high-fidelity simulations of a kinetic impactor mission over a binary system have been produced. The lightcurves as observed from the Earth before and after the impact of each of the simulated scenarios are available. Estimate the beta-factor and a/c, the secondary and the ratio between the secondary major and minor axis.

Data are in .dat files.

*Advanced Concepts Team, European Space Agency, 2021*

</details>

## Payload imaging

#### [Mars Surface and Curiosity Image Set](https://www.kaggle.com/brsdincer/mars-surface-and-curiosity-image-set-nasa)

3.24 GB · image · A. Stanboli and K. L. Wagstaff, NASA

![image-classification](assets/badges/task-image-classification.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

This data set consists of 6,691 images that were collected by the Mars Science Laboratory (MSL, Curiosity) rover by three instruments: Mastcam Right eye, Mastcam Left eye, and MAHLI. The proposed task is a multiple output classification model.

An on-board classifier would make it possible to prioritise which images are sent back to Earth earlier than the others, which makes this a downlink budget problem as much as a vision one. 6,691 images of roughly 256x256 in .jpg format.

*Alice Stanboli and Kiri L. Wagstaff, NASA*

</details>

#### [Statlog (Landsat Satellite)](https://archive.ics.uci.edu/ml/datasets/Statlog+(Landsat+Satellite))

< 1 MB · tabular · CC BY 4.0 · A. Srinivasan, 1993

![classification](assets/badges/task-classification.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

The dataset consists of the multi-spectral values of pixels in 3x3 neighbourhoods in a satellite image, and the classification associated with the central pixel in each neighbourhood. The aim is to predict this classification, given the multi-spectral values. In the sample database, the class of a pixel is coded as a number.

Two ASCII files, sat.trn and sat.tst. See also the two ODDS variants of this dataset under operations and telemetry.

*Ashwin Srinivasan (1993), University of Strathclyde*

</details>

## Space environment

#### [NASA and NOAA Solar Wind](https://www.kaggle.com/arashnic/soalr-wind)

898 MB · time series · NASA and NOAA

![forecasting](assets/badges/task-forecasting.svg) ![regression](assets/badges/task-regression.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

The disturbance-storm-time index, or Dst, is a measure of the severity of a geomagnetic storm. The data is composed of solar wind measurements collected from two satellites: NASA's Advanced Composition Explorer (ACE) and NOAA's Deep Space Climate Observatory (DSCOVR).

The goal is to develop models for forecasting Dst that push the boundary of predictive performance, under operationally viable constraints, using the real-time solar-wind (RTSW) data feeds from NOAA's DSCOVR and NASA's ACE satellites.

*NASA and NOAA*

</details>

## Engineering text

#### [Space systems corpora](https://pureportal.strath.ac.uk/en/datasets/dataset-of-space-systems-corpora-thesis-data)

257 MB · text · A. Berquand and A. Riccardi, 2021

![pretraining](assets/badges/task-pretraining.svg) ![labels: no](assets/badges/labels-no.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

Several corpora used to train the methods developed in the thesis "Text Mining and Natural Language Processing for the Early Stages of Space Mission Design". The dataset includes 4,991 articles published in Acta Astronautica, Advances in Space Research (ASR), and Aerospace Science and Technology (AST), 39 books related to space mission design, and 242 Wikipedia pages processed with a space domain-specific Natural Language Processing pipeline.

Additional text sources are 27,016 parsed ECSS requirements extracted from 126 active standards. The mission requirements are extracted from two publicly available ESA documents, the SMOS mission System Requirement Document and MarcoPolo-R's Mission Requirement Document. The ECSS portion is the part most engineering teams want. Data in .txt and .json files.

*Audrey Berquand, Annalisa Riccardi (2021), University of Strathclyde*

</details>

#### [Space News](https://www.kaggle.com/datasets/patrickfleith/space-news-dataset)

79 MB · text · Patrick Fleith

![pretraining](assets/badges/task-pretraining.svg) ![text-classification](assets/badges/task-text-classification.svg) ![labels: no](assets/badges/labels-no.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

The title, url, text content, author, publish date, and post excerpt of more than 20,700 English news articles related to the space industry. A total of more than 14 million words, which makes it suitable for training language models specific to the space industry ecosystem.

It covers agency news, commercial, civil, launches, military, and also opinion articles from [SpaceNews](https://spacenews.com/). Data are in .csv files.

</details>

#### [Astro-MCQA](https://huggingface.co/datasets/patrickfleith/Astro-mcqa)

200 rows · text · CC BY 4.0 · Patrick Fleith, 2024

![llm-eval](assets/badges/task-llm-eval.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

The primary purpose of AstroMCQA is for application developers in the domain of space mission design and operations to comparatively assess LLM performance on the specific task of multiple-choice question-answering.

It addresses questions such as: which LLM to use, and how does it perform in the different subdomains? It enables benchmarking of different models, different sizes, quantization methods, prompt engineering strategies, and the effectiveness of fine-tuning on the specific task of multiple-choice question-answering in space engineering.

*AstroMCQA (c) 2024 by Patrick Fleith, licensed under Creative Commons Attribution 4.0 International*

</details>

#### [Aeronautics and Astronautics Abstracts](https://www.kaggle.com/sylar68/aeronautics-astronautics-journal-abstracts)

< 1 MB · text · Patrick Fleith, 2021

![text-classification](assets/badges/task-text-classification.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

Titles and abstracts of about 493 papers published by AIAA either in the Journal of Propulsion and Power (JPP) or in the Journal of Thermophysics and Heat Transfer (JTHT), manually retrieved from https://arc.aiaa.org.

The task is to build a classifier able to distinguish between abstracts and titles from each specific technical domain. The challenge lies in that both domains, propulsion and heat transfer, contain overlapping vocabulary such as combustion, exchange, thermal and fluid, which makes it harder to tell which journal a paper comes from. All in an excel file (.xls).

*Patrick Fleith, 2021*

</details>

#### [IAF congress abstracts](https://www.iafastro.org/)

coming soon · text · Patrick Fleith, 2022

![pretraining](assets/badges/task-pretraining.svg) ![labels: no](assets/badges/labels-no.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

More than 30,000 abstracts of congress articles submitted to the IAF (International Astronautical Federation). This is equivalent to over 6 million words.

Not yet released. We are constantly working towards more NLP-for-space data.

</details>

## Astronomy

Not spacecraft engineering, but the instruments are, and the signal processing transfers.

#### [G2Net 2: continuous gravitational waves](https://www.kaggle.com/competitions/g2net-detecting-continuous-gravitational-waves/overview)

227.1 GB · time series · G2Net

![classification](assets/badges/task-classification.svg) ![signal-processing](assets/badges/task-signal-processing.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: mixed](assets/badges/origin-mixed.svg)

<details><summary>Description</summary>

A follow-up competition to G2Net. The goal is to find continuous gravitational-wave signals. You will develop a model sensitive enough to detect weak yet long-lasting signals emitted by rapidly-spinning neutron stars within noisy data.

Real detector noise with simulated signals injected.

</details>

#### [G2Net](https://www.kaggle.com/c/g2net-gravitational-wave-detection/overview)

72 GB · time series · European Gravitational Observatory

![classification](assets/badges/task-classification.svg) ![signal-processing](assets/badges/task-signal-processing.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: mixed](assets/badges/origin-mixed.svg)

<details><summary>Description</summary>

A training set of time series data containing simulated gravitational wave measurements from a network of 3 gravitational wave interferometers: LIGO Hanford, LIGO Livingston, and Virgo. Each time series contains either detector noise, or detector noise plus a simulated gravitational wave signal. The task is to identify when a signal is present from the mergers of binary black holes.

Each data sample (.npy file) contains 3 time series, one for each detector. Each spans 2 seconds and is sampled at 2,048 Hz.

*European Gravitational Observatory (EGO), 2015*

</details>

#### [Breakthrough Listen SETI](https://www.kaggle.com/c/seti-breakthrough-listen/data)

62.0 GB · image · Berkeley SETI Research Center, 2021

![classification](assets/badges/task-classification.svg) ![signal-processing](assets/badges/task-signal-processing.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

Detect candidate signatures of extraterrestrial technology in deep space signals (cadence snippets) taken by the Green Bank Telescope (GBT).

NumPy float16 format of shape (6, 273, 256).

*University of California, Berkeley SETI Research Center, 2021*

</details>

#### [Kepler Exoplanet Search Results](https://www.kaggle.com/nasa/kepler-exoplanet-search-results)

989 MB · tabular · NASA

![eda](assets/badges/task-eda.svg) ![labels: yes](assets/badges/labels-yes.svg) ![origin: real](assets/badges/origin-real.svg)

<details><summary>Description</summary>

A cumulative record of all observed Kepler "objects of interest", which is all of the approximately 10,000 exoplanet candidates Kepler has taken observations on.

Inspiration for analysis: how often are exoplanets confirmed in the existing literature disconfirmed by measurements from Kepler, and the other way round? What general characteristics about exoplanets can you derive from this dataset? Which exoplanets get assigned names in the literature? What is the distribution of confidence scores?

You can access the original table [here](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=koi). More data from the Kepler mission is available from the same [source](https://exoplanetarchive.ipac.caltech.edu/docs/data.html).

</details>

---

## Index by ML/AI task

A dataset carries every task it supports, so entries repeat here.

| Task | Datasets |
|---|---|
| `regression` | Spacecraft Thruster Firing Tests, Mars Express Power Challenge, NASA Milling, NASA Airfoil Self-Noise, spotGEO, Space Debris: the origin, Planetary Defence Challenge, NASA and NOAA Solar Wind |
| `forecasting` | Mars Express Power Challenge, NASA and NOAA Solar Wind |
| `classification` | Space Debris: the origin, Statlog (Landsat Satellite), G2Net 2: continuous gravitational waves, G2Net, Breakthrough Listen SETI |
| `image-classification` | Mars Surface and Curiosity Image Set |
| `text-classification` | Space News, Aeronautics and Astronautics Abstracts |
| `anomaly-detection` | CFRP Composites, NASA Bearing, ESA Anomaly Dataset, Controlled Anomalies Time Series (CATS), SMAP and MSL |
| `novelty-detection` | ESA Anomaly Dataset, Controlled Anomalies Time Series (CATS), SMAP and MSL |
| `outlier-detection` | Controlled Anomalies Time Series (CATS), LASP Spacecraft Telemetry, Satellite (ODDS), Satimage-2 (ODDS) |
| `rul` | NASA Battery, Randomized Battery Usage, CFRP Composites, NASA Bearing, FEMTO Bearings, MOSFET Thermal Overstress Aging, Capacitor Electrical Stress, Turbofan Engine Degradation (C-MAPSS) |
| `object-detection` | spotGEO |
| `pose-estimation` | Pose Estimation Challenge 2021 |
| `domain-adaptation` | Pose Estimation Challenge 2021 |
| `signal-processing` | G2Net 2: continuous gravitational waves, G2Net, Breakthrough Listen SETI |
| `pretraining` | Space systems corpora, Space News, IAF congress abstracts |
| `llm-eval` | Astro-MCQA |
| `optimisation` | The Kessler Run (GTOC9) |
| `eda` | Kepler Exoplanet Search Results |

## Licences

Licence is shown only where it is stated by the host and has been checked. 12 entries have a verified licence.

The NASA Prognostics Data Repository states no formal licence, only that users acknowledge the repository and the data donors and employ the data at their own risk. Those entries are marked `no licence stated`.

Still to verify: Spacecraft Thruster Firing Tests, Mars Express Power Challenge, NASA Bearing, NASA Milling, SMAP and MSL, LASP Spacecraft Telemetry, Satellite (ODDS), Satimage-2 (ODDS), Pose Estimation Challenge 2021, spotGEO, Space Debris: the origin, The Kessler Run (GTOC9), Planetary Defence Challenge, Mars Surface and Curiosity Image Set, NASA and NOAA Solar Wind, Space systems corpora, Space News, Aeronautics and Astronautics Abstracts, IAF congress abstracts, G2Net 2: continuous gravitational waves, G2Net, Breakthrough Listen SETI, Kepler Exoplanet Search Results.

## Contributing

Propose a dataset with the [issue template](.github/ISSUE_TEMPLATE/dataset-submission.md). List every task it supports rather than the headline one, give the modality and the licence, and name the subsystem it comes from.
