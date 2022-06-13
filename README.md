# Awesome Spacecraft Engineering Datasets [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)
A list of awesome and diverse datasets related to space vehicle engineering for industry and research.

## Engineering Datasets for Regression
- [**Spacecraft Thruster Firing Test Dataset**](https://www.kaggle.com/sylar68/spacecraft-thruster-firing-test-dataset) - **1 GB - Regression Task**
  - Time series analysis and predictive modelling of engine thrust, mass flow rate, and performance degradation over time. This is a synthetic dataset based on the real-world physics of a chemical reaction control thruster. Time series data in .csv files, *(Patrick Fleith, 2021)*
 
- [**Mars Express Challenge**](https://kelvins.esa.int/mars-express-power-challenge/home/) - **150 MB - Regression Task**
  - Predict the average current consumption of 33 thermal power lines per hour of the mission's fourth Martian year (2014-04-14 to 2016-03-01), Time series are in .csv files, *Advanced Concepts Team, European Space Agency, 2021*
  
- [**NASA Airfoil Self-Noise Data Set**](https://archive.ics.uci.edu/ml/datasets/airfoil+self-noise) - **< 1MB - Regression Task**
  - The NASA data set is obtained from a series of aerodynamic and acoustic tests of two and three-dimensional airfoil blade sections conducted in an anechoic wind tunnel. The span of the airfoil and the observer position were the same in all of the experiments. The objective is to predict the aerofoil noise (the scale sound pressure level), *Thomas F. Brooks, D. Stuart Pope and Michael A. Marcolini (NASA), Donor: Dr. Roberto Lopez*

## Engineering Datasets for Classification

- [**Mars Surface and Curiosity Image Set**](https://www.kaggle.com/brsdincer/mars-surface-and-curiosity-image-set-nasa) - **3.24 GB - Multioutput Image Classification**
  - This data set consists of 6691 images that were collected by the Mars Science Laboratory (MSL, Curosity) rover by three instruments (Mastcam Right eye, Mastcam Left eye, and MAHLI). The proposed task is a multiple output classification model. An on-board classifier would make it possible to prioritise which images are sent back to Earth earlier than the others; 6691 images of roughly 256x256 in .jpg format, *Alice Stanboli and Kiri L. Wagstaff, NASA*

- [**Statlog (Landsat Satellite) Data Set**](https://archive.ics.uci.edu/ml/datasets/Statlog+(Landsat+Satellite)) - **< 1MB - Classification**
  - The dataset consists of the multi-spectral values of pixels in 3x3 neighbourhoods in a satellite image, and the classification associated with the central pixel in each neighbourhood. The aim is to predict this classification, given the multi-spectral values. In the sample database, the class of a pixel is coded as a number. - 2 ASCII files sat.trn and sat.tst - *Ashwin Srinivasan (1993), University of Strathclyde*

## Engineering Datasets for Outliers & Anomalies Detection

- [**SMAP & MSL Dataset**](https://www.kaggle.com/patrickfleith/datasets) - **~ 250 MB - Anomaly/Novelty Detection COMING SOON** 
  - This dataset contains expert-labeled telemetry anomaly data from the Soil Moisture Active Passive (SMAP) satellite and the Mars Science Laboratory (MSL) rover, Curiosity. Indications of telemetry anomalies can be found within previously mentioned ISA reports.
All telemetry channels discussed in an individual ISA were reviewed to ensure that the anomaly was evident in the associated telemetry data, and specific anomalous time ranges were manually labeled for each channel. If multiple anomalous sequences and channels closely resembled each other, only one was kept for the experiment in order to create a diverse and balanced set. Anomalies were classified into two categories, point and contextual, to distinguish between anomalies that would likely be identified by properly-set alarms or distance-based methods that ignore tem- poral information (point anomalies) and those that require more complex methodologies such as LSTMs or Hierarchical Temporal Memory (HTM) approaches to detect (contextual anomalies), **SMAP**: TM Channels (55), Total TM values (429,735), Total anomalies (69), **MSL**: TM Channels (27), Total TM values (66,709), Total anomalies (36)- Data in .npy files - *Kyle Hundman et al. 2018, NASA Jet Propulsion Laboratory*

- [**LASP Spacecraft Telemtry**](https://github.com/sapols/Satellite-Telemetry-Anomaly-Detection) - **14 MB - Outliers Detection**
  - This dataset can be used for visualization and analysis of telemetry data that is built and maintained at the Laboratory for Atmospheric and Space Physics. Read more [here](https://github.com/sapols/Satellite-Telemetry-Anomaly-Detection/blob/master/Paper/Unsupervised%20Machine%20Learning%20for%20Spacecraft%20Anomaly%20Detection%20in%20WebTCAD.pdf) - Data in .csv files, no ground truth - *Shawn Polson, Laboratory for Atmospheric and Space Physics*

- [**Satellite dataset (from Statlog)**](http://odds.cs.stonybrook.edu/satellite-dataset/) - **< 1MB - Outliers Detection**
  - The original Statlog (Landsat Satellite) dataset from UCI machine learning repository is a multi-class classification dataset. Here, the training and test data are combined. The smallest three classes, i.e. 2, 4, 5 are combined to form the outliers class, while all the other classes are combined to form an inlier class, - Data in .mat file, X = Multi-dimensional point data, y = labels (1 = outliers, 0 = inliers), *Adapted from Ashwin Srinivasan (1993),
University of Strathclyde*

- [**satimage-2 dataset (from Statlog)**](http://odds.cs.stonybrook.edu/satimage-2-dataset/) - **< 1MB - Outliers Detection**
  - The original Statlog (Landsat Satellite) dataset from UCI machine learning repository is a multi-class classification dataset. Here, the training and test data are combined. Class 2 is down-sampled to 71 outliers, while all the other classes are combined to form an inlier class. The modified dataset is referred to as Satimage-2. Data in .mat file, X = Multi-dimensional point data, y = labels (1 = outliers, 0 = inliers), *Adapted from Ashwin Srinivasan (1993),
University of Strathclyde*

## Engineering Datasets for Prognosis

- [**NASA Bearing Dataset**](https://www.kaggle.com/vinayak123tyagi/bearing-dataset) - **6.08 GB - Prognosis for Predictive / Preventive Maintenance**
  - Four bearings were installed on a shaft. Three (3) data sets are included in the data packet. Each data set describes a test-to-failure experiment. Each data set consists of individual files that are 1-second vibration signal snapshots recorded at specific intervals. Data fromat is in ASCII and txt. Each file consists of 20,480 points with the sampling rate set at 20 kHz - *University of Cincinnati., Center for Intelligent Maintenance Systems (IMS)*

- [**NASA Battery Dataset**](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#battery) - **210 MB - Regression / Remaining Usefull Life Estimation (RUL)**
  - A set of Li-ion batteries were run through different operational profiles (charge, discharge and impedance) at various temperatures. Impedance measurement was carried out through an electrochemical impedance spectroscopy (EIS) frequency. Repeated charge and discharge cycles result in accelerated aging of the batteries while impedance measurements provide insight into the internal battery parameters that change as aging progresses. The experiments were stopped when the batteries reached end-of-life (EOL) criteria. These datasets can be used for the prediction of both remaining charge (for a given discharge cycle) and remaining useful life (RUL). Data are in Batch of 6 experiments, data provided in .mat files with experiment details in associated READEME.txt - *B. Saha and K. Goebel (2007), Prognosis CoE, NASA Ames*

- [**NASA Milling Dataset**](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#milling) - **72.6 MB - Regression / Prognosis**
  - Can you predict the flank wear VB [mm], i.e. the wearing of the miling insert after sone runs? Experiments on a milling machine for different speeds, feeds, and depth of cut. Records the wear of the milling insert, VB. The dataset is in .mat format and has been zipped. A Readme.pdf provides details on the experimental protocol and the measurement technics. *A. Agogino and K. Goebel (2007). BEST lab, UC Berkeley*

- [**CFRP Composites Dataset**](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#composites) - **4.5 GB - Expected End-of-life Prediction**
  - Run-to-failure experiments were run on CFRP panels with periodic measurements to capture internal damage growth under tension-tension fatigue. Monitoring data consist of lamb wave signals from a network of 16 piezoelectric (PZT) sensors and multiple triaxial strain gages. Additionally, periodic x-rays were taken to characterize internal damage as ground truth information. Three different layups were tested. Dataset is organized into three zipped folders each containing data from coupons of single layup type and includes a readme file, and a folder with reports and papers published from this dataset. *Abhinav Saxena, Kai Goebel, Cecilia C. Larrosa, and Fu-Kuo Chang. Experiments were conducted at Stanford Structures and Composites Laboratory (SACL) in collaboration with the Prognostic Center of Excellence (PCoE) of NASA Ames Research Center.*

- [**Turbofan Engine Degradation Simulation Data Set**](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#turbofan) - **45.3 MB - Prognosis**
  - Engine degradation simulation was carried out using C-MAPSS. Four different were sets simulated under different combinations of operational conditions and fault modes. Records several sensor channels to characterize fault evolution. The dataset is in text format and has been zipped including a readme file, and an original paper describing damage propagation modeling. *A. Saxena and K. Goebel (2008), Prognostics CoE at NASA Ames.*

- [**Turbofan Engine Degradation Simulation Dataset-2**](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#turbofan-2) - **14.8 GB - Prognosis**
  - The generation of data-driven prognostics models requires the availability of datasets with run-to-failure trajectories. In order to contribute to the development of these methods, the dataset provides a new realistic dataset of run-to-failure trajectories for a small fleet of aircraft engines under realistic flight conditions. The damage propagation modelling used for the generation of this synthetic dataset builds on the modeling strategy from previous work . The dataset was generated with the Commercial Modular Aero-Propulsion System Simulation (C-MAPSS) dynamical model. The data set is been provided by the Prognostics CoE at NASA Ames in collaboration with ETH Zurich and PARC. Readme file for the dataset describing the experimetal details and data can be found [here](https://ti.arc.nasa.gov/m/project/prognostic-repository/Run_to_Failure_Simulation_Under_Real_Flight_Conditions_Dataset.pdf). The dataset is in csv format and has been zipped. A python code to unzip the files can be found [here](https://ti.arc.nasa.gov/m/project/prognostic-repository/N-CMAPSS_Example_data_loading_and_exploration.ipynb). *M. Chao, C.Kulkarni, K. Goebel and O. Fink (2021), NASA Ames and ETH Zurich*

- [**FEMTO Bearing Dataset**](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#femto) - **1.1 GB - Prognosis**
  - Experiments on bearings' accelerated life tests, *P. Nectoux, R. Gouriveau, K. Medjaher, E. Ramasso, B. Morello, N. Zerhouni, C. Varnier, FEMTO-ST Institute, Besançon, France, NASA Ames Research Center*

- [**Randomized Battery Usage Dataset**](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#batteryrnddischarge) **1.12 GB  - Prognosis**
  - Batteries are continuously cycled with randomly generated current profiles. Reference charging and discharging cycles are also performed after a fixed interval of randomized usage in order to provide reference benchmarks for battery state of health. *B. Bole, C. Kulkarni, and M. Daigle, NASA Ames Research Center*

- [**Small Satellite Power Simulation Dataset**](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#smallsat) - **5 MB - Prognosis**
  - Data collected from the simulated experiments on small satellite BP930 batteries using the MACCOR system. Reference document can be dowloaded [here](https://ti.arc.nasa.gov//m/project/prognostic-repository/Description_of_Simulated_Small_Satellite_Operation_Data_Sets.pdf). The power cycle reference sheet can be dowloaded [here](https://ti.arc.nasa.gov//m/project/prognostic-repository/Simulated_Current_Draw_Profile.xlsx). MATLAB file (.mat) and excel spreadsheet (.xlsx), *Z. Cameron, C. Kulkarni , A. Guarneros, K. Goebel, S. Poll, NASA Ames*

- [**Capacitor Electrical Stress Data Set**](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#escapacitor) - **4.8 GB - Prognosis**
  - Capacitors were subjected to electrical stress under three voltage levels i.e 10V, 12V and 14V. Data Set contains EIS data as well as Charge/Discharge Signal data. DataSet Reference document can be downloaded [here](http://ti.arc.nasa.gov/m/project/prognostic-repository/Description%20of%20Electrolytic%20Capacitors%20under%20Electrical%20Overstress%20Data%20Sets.pdf), The dataset is in .mat format and has been zipped. *J. Renwick, C. Kulkarni, and J Celaya, NASA Ames Research Center*

- [**Capacitor Electrical Stress Data Set - 2**](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#eoscapacitor) - **1 kB - Prognosis**
  - Capacitors were subjected to electrical stress at 10V. DataSet Reference document can be downloaded [here](http://ti.arc.nasa.gov/m/project/prognostic-repository/Electrolytic%20Capacitors%20under%20Electrical%20Overstress%20Data%20Sets.pdf), The dataset is in .mat format and has been zipped. *J. Celaya, C. Kulkarni, G. Biswas, and K. Goebel, NASA Ames Research Center*

- [**MOSFET Thermal Overstress Aging Data Set**](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/#mosfet) - **7.3 GB - Prognosis**
  - Run-to-failure experiments on Power MOSFETs under thermal overstress. DataSet Reference document can be downloaded [here](http://ti.arc.nasa.gov/m/project/prognostic-repository/MOSFET%20Thermal%20Overstress%20Aging%20Document.pdf), The dataset is in .mat format and has been zipped. *J. R. Celaya, A. Saxena, S. Saha, and K. Goebel, NASA Ames Research Center*
  
## Aerospace Text Data for NLP applications

- [**Dataset of space systems corpora**](https://pureportal.strath.ac.uk/en/datasets/dataset-of-space-systems-corpora-thesis-data) - **257 MB - Natural Language Processing**
  - The dataset contains several corpora used to train the methods developed in the thesis "Text Mining and Natural Language Processing for the Early Stages of Space Mission Design". The dataset includes 4,991 articles published in the Acta Astronautica, the Advance in Space Research (ASR), and the Aerospace Science and Technology (AST) journals, 39 books related to space mission design and 242 Wikipedia pages processed with a space domain-specific Natural Language Processing pipeline. Additional text sources are 27,016 parsed ECSS requirements extracted from 126 active standards. The mission requirements are extracted from two ESA documents, publicly available, the SMOS mission System Requirement Document and MarcoPolo-R's Mission Requirement Document - Data in .txt and .json files - *Audrey Berquand, Annalisa Riccardi (2021), University of Strathclyde*

- [**Space News Dataset**](https://www.kaggle.com/datasets/patrickfleith/space-news-dataset) - **79 MB - Natural Language Processing**
  - This dataset contains the title, url, text content, author, publish data, and post excerpt of more than 17,400 english news articles related to the space industry, a total of 13.1 million tokens (words) which makes it perfect to train language models specific to the space industry ecosystem. It covers agency news, commercial, civil, launches, military, and also opinion articles from [spacenews](https://spacenews.com/) - Data are in .csv files.

- [**International Astronatucial Federation**](https://www.iafastro.org/) - **COMING SOON**
  - This dataset contains more than 30,000 abstracts of congress articles submitted to the IAF (International Astronautical Federation). This is equivalent to (>6 million words), *(Patrick Fleith, 2022)*

- [**Aeronautics & Astronautics Abstracts**](https://www.kaggle.com/sylar68/aeronautics-astronautics-journal-abstracts) - **< 1MB - Text Classification**
  - The Aeronautics & Astronautics Abstracts dataset includes titles and abstracts of about 493 papers published by AIAA either in the journal of propulsion and power (JPP), or in the journal of thermophysics and heat transfers (JTHT) which were manually retrieved from https://arc.aiaa.org. The task is to build a classifier that is able to distinguish between abstracts and/or titles from each specific technical domain. The challenge lies in that both domains (propulsion, heat transfers) contains vocabulary that overlaps such as (combustion, exchange, thermal, fluid, etc…) which makes it harder to distinguish which journal it comes from. All is in an excel file (.xls), *(Patrick Fleith, 2021)*

- We are constantly working towards more NLP4space data

## Astrodynamics
- [**Pose Estimation Challenge 2021**](https://kelvins.esa.int/pose-estimation-2021/home/) - **15.7 GB - Regression Task**
  - Can you predict the position and orientation of our spacecraft in realistic images while only being provided with labels from computer generated examples? The new challenge SPEC2021 is explicitly designed to investigate the domain gap between synthetic labelled and realistic unlabelled images. Conducting this challenge will shed more light on the next big question for spaceborne computer vision algorithms: how can one validate on-ground the pose estimation algorithm on spaceborne image targets that are simply unavailable prior to the mission? After all, unlike on Earth, autonomous driving in space prohibits habitual road tests and on-site debugging. You may also want to look at the dataset of the previous Pose Estimation Challenge from 2019 ([here](https://kelvins.esa.int/satellite-pose-estimation-challenge/)) - Data provided are .json (filenames) and images 8 bit monochrome in jpeg format, with a resolution of 1920×1200 pixels - *Advanced Concepts Team (ESA) + Space Rendezvous Laboratory (SLAB) of Stanford University, 2021*

- [**Space Debris: the origin**](https://kelvins.esa.int/space-debris-the-origin/home/) - **< 3 MB - Multi-Task: Classification + Regression**
  - To determine two things for each of the debris given: the id of the defunct satellite (Classification Task) + the value of the effective area over mass ratio Cr(A/m) of the debris (Regression Task) - Data are in .dat files - *Advanced Concepts Team, European Space Agency, 2021*

- [**Planetary defence challenge**](https://kelvins.esa.int/planetary-defence/home/) - **< 1 MB - Regression Task**
  - Several high-fidelity simulations of a kinetic impactor mission over a binary system have been produced. The lightcurves as observed from the Earth before and after the impact of each of the simulated scenarios are available. To estimate the beta-factor and a/c (the secondary and the ratio between the secondary major and minor axis)., data are in .dat files, *Advanced Concepts Team, European Space Agency, 2021*

- [**spotGEO**](https://kelvins.esa.int/spot-the-geo-satellites/home/) - **4.2 GB - Classification + Regression Task**
  - The goal is to detect orbiting objects in the geostationary ring from sequences of 5 consecutive frames imaging some (unknown) portion of the sky and provided by a low-cost ground based telescope. Can you learn on how to cope with cloud cover, atmospheric/weather effects, light pollution, sensor noise/defects, star occlusions and more?; 32,000 grayscale images of size 640x480 pixels + JSON files; *Advanced Concepts Team (ESA) + University of Adelaide, 2020*

- [**The Kessler Run**](https://kelvins.esa.int/gtoc9-kessler-run/home/) - **< 1 MB - Trajectory Optimisation**
  - Design and optimize n missions able to cumulatively remove all the 123 orbiting debris. One mission is a multiple-rendezvous spacecraft trajectory where a subset of size N of the 123 orbiting debris is removed by the delivery and activation of N de-orbit packages. Data are Orbital debris elements in .csv - *Advanced Concepts Team, European Space Agency, 2017*

## Space Environment
- [**NASA and NOAA Solar Wind Dataset**](https://www.kaggle.com/arashnic/soalr-wind) - **898 MB - Regression**
  - The disturbance-storm-time index, or Dst, is a measure of the severity of the geomagnetic storm. The data is composed of solar wind measurements collected from two satellites: NASA's Advanced Composition Explorer (ACE) and NOAA's Deep Space Climate Observatory (DSCOVR).The goal is to develop models for forecasting Dst that push the boundary of predictive performance, under operationally viable constraints, using the real-time solar-wind (RTSW) data feeds from NOAA’s DSCOVR and NASA’s ACE satellites, *NASA+NOAA*.

## Astronomy Data Sets
- [**Breakthough Listen SETI**](https://www.kaggle.com/c/seti-breakthrough-listen/data) - **62.0 GB - Binary Classification task** 
  - to detect candidate signatures of extraterrestrial technology in Deep Space Signals (cadence snippet) taken by the Green Bank Telescope (GBT), numpy float16 format of shape (6, 273, 256), *(University of California, Berkeley SETI Research Center., 2021)*.

- [**Kepler Exoplanet Search Results**](https://www.kaggle.com/nasa/kepler-exoplanet-search-results) - **989 MB - Exploratory Data Analysis** 
  - This dataset is a cumulative record of all observed Kepler "objects of interest" — basically, all of the approximately 10,000 exoplanet candidates Kepler has taken observations on. You can access the original table [here](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=koi):  More data from the Kepler mission is available from the same [source](https://exoplanetarchive.ipac.caltech.edu/docs/data.html). Inspiration for anlysis: How often are exoplanets confirmed in the existing literature disconfirmed by measurements from Kepler? How about the other way round? What general characteristics about exoplanets (that we can find) can you derive from this dataset? What exoplanets get assigned names in the literature? What is the distribution of confidence scores?

- [**Grav2Net**](https://www.kaggle.com/c/g2net-gravitational-wave-detection/overview) - **72 GB - Binary Classification** 
  - You are provided with a training set of time series data containing simulated gravitational wave measurements from a network of 3 gravitational wave interferometers (LIGO Hanford, LIGO Livingston, and Virgo). Each time series contains either detectornoise or detector noise plus a simulated gravitational wave signal. The task is to identify when a signal is present from the mergers of binary black holes; Each data sample (npy file) contains 3 time series (1 for each detector) and each spans 2 sec and is sampled at 2,048 Hz. *European Gravitational Observatory - EGO, 2015*
