# Awesome Spacecraft Engineering Datasets [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)
A list of awesome and diverse datasets related to space vehicle engineering for industry and research.

### Engineering Datasets
- [**Spacecraft Thruster Firing Test Dataset**](https://www.kaggle.com/sylar68/spacecraft-thruster-firing-test-dataset) - 1 GB - Regression Task - Time series analysis and predictive modelling of engine thrust, mass flow rate, and performance degradation over time. This is a synthetic dataset based on the real-world physics of a chemical reaction control thruster. Time series data in .csv files, *(Patrick Fleith, 2021)*
- [**Mars Express Challenge**](https://kelvins.esa.int/mars-express-power-challenge/home/) - 150 MB - Regression Task - Predict the average current consumption of 33 thermal power lines per hour of the mission's fourth Martian year (2014-04-14 to 2016-03-01), Time series are in .csv files, *Advanced Concepts Team, European Space Agency, 2021*
- [**Mars Surface and Curiosity Image Set**](https://www.kaggle.com/brsdincer/mars-surface-and-curiosity-image-set-nasa) - 3.24 GB - Multioutput Image Classification - This data set consists of 6691 images that were collected by the Mars Science Laboratory (MSL, Curosity) rover by three instruments (Mastcam Right eye, Mastcam Left eye, and MAHLI). The proposed task is a multiple output classification model. An on-board classifier would make it possible to prioritise which images are sent back to Earth earlier than the others; 6691 images of roughly 256x256 in .jpg format, *Alice Stanboli and Kiri L. Wagstaff, NASA*
- [**NASA Airfoil Self-Noise Data Set**](https://archive.ics.uci.edu/ml/datasets/airfoil+self-noise) - < 1MB - Regression Task - The NASA data set is obtained from a series of aerodynamic and acoustic tests of two and three-dimensional airfoil blade sections conducted in an anechoic wind tunnel. The span of the airfoil and the observer position were the same in all of the experiments. The objective is to predict the aerofoil noise (the scale sound pressure level), *Thomas F. Brooks, D. Stuart Pope and Michael A. Marcolini (NASA), Donor: Dr. Roberto Lopez*
- [**NASA Bearing Dataset**](https://www.kaggle.com/vinayak123tyagi/bearing-dataset) - 6.08 GB - Prognosis for Predictive/Preventive Maintenance - Four bearings were installed on a shaft. Three (3) data sets are included in the data packet. Each data set describes a test-to-failure experiment. Each data set consists of individual files that are 1-second vibration signal snapshots recorded at specific intervals. Data fromat is in ASCII and txt. Each file consists of 20,480 points with the sampling rate set at 20 kHz - *University of Cincinnati., Center for Intelligent Maintenance Systems (IMS)*

### Aerospace Text Data for NLP applications
- [**Aeronautics & Astronautics Abstracts**](https://www.kaggle.com/sylar68/aeronautics-astronautics-journal-abstracts) - < 1MB - Text Classification - The Aeronautics & Astronautics Abstracts dataset includes titles and abstracts of about 493 papers published by AIAA either in the journal of propulsion and power (JPP), or in the journal of thermophysics and heat transfers (JTHT) which were manually retrieved from https://arc.aiaa.org. The task is to build a classifier that is able to distinguish between abstracts and/or titles from each specific technical domain. The challenge lies in that both domains (propulsion, heat transfers) contains vocabulary that overlaps such as (combustion, exchange, thermal, fluid, etc…) which makes it harder to distinguish which journal it comes from. All is in an excel file (.xls), *(Patrick Fleith, 2021)*
- More NLP data to come

### Space Environment
- [**NASA and NOAA Solar Wind Dataset**](https://www.kaggle.com/arashnic/soalr-wind) - 898 MB - Regression - The disturbance-storm-time index, or Dst, is a measure of the severity of the geomagnetic storm. The data is composed of solar wind measurements collected from two satellites: NASA's Advanced Composition Explorer (ACE) and NOAA's Deep Space Climate Observatory (DSCOVR).The goal is to develop models for forecasting Dst that push the boundary of predictive performance, under operationally viable constraints, using the real-time solar-wind (RTSW) data feeds from NOAA’s DSCOVR and NASA’s ACE satellites, *NASA+NOAA*.

### Astrodynamics
- [**Space Debris: the origin**](https://kelvins.esa.int/space-debris-the-origin/home/) - < 3 MB - Multi-Task: Classification + Regression - To determine two things for each of the debris given: the id of the defunct satellite (Classification Task) + the value of the effective area over mass ratio Cr(A/m) of the debris (Regression Task) - Data are in .dat files - *Advanced Concepts Team, European Space Agency, 2021*
- [**Planetary defence challenge**](https://kelvins.esa.int/planetary-defence/home/) - < 1 MB - Regression Task - Several high-fidelity simulations of a kinetic impactor mission over a binary system have been produced. The lightcurves as observed from the Earth before and after the impact of each of the simulated scenarios are available. To estimate the beta-factor and a/c (the secondary and the ratio between the secondary major and minor axis)., data are in .dat files, *Advanced Concepts Team, European Space Agency, 2021*

### Astronomy Data Sets
- [**Breakthough Listen SETI**](https://www.kaggle.com/c/seti-breakthrough-listen/data) - 62.0 GB - Binary Classification task to detect candidate signatures of extraterrestrial technology in Deep Space Signals (cadence snippet) taken by the Green Bank Telescope (GBT), numpy float16 format of shape (6, 273, 256), *(University of California, Berkeley SETI Research Center., 2021)*.

- [**Kepler Exoplanet Search Results**](https://www.kaggle.com/nasa/kepler-exoplanet-search-results) - 989 MB - Exploratory Data Analysis - This dataset is a cumulative record of all observed Kepler "objects of interest" — basically, all of the approximately 10,000 exoplanet candidates Kepler has taken observations on. You can access the original table [here](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=koi):  More data from the Kepler mission is available from the same [source](https://exoplanetarchive.ipac.caltech.edu/docs/data.html). Inspiration for anlysis: How often are exoplanets confirmed in the existing literature disconfirmed by measurements from Kepler? How about the other way round? What general characteristics about exoplanets (that we can find) can you derive from this dataset? What exoplanets get assigned names in the literature? What is the distribution of confidence scores?

- [**Grav2Net**](https://www.kaggle.com/c/g2net-gravitational-wave-detection/overview) - 72 GB - Binary Classification - You are provided with a training set of time series data containing simulated gravitational wave measurements from a network of 3 gravitational wave interferometers (LIGO Hanford, LIGO Livingston, and Virgo). Each time series contains either detectornoise or detector noise plus a simulated gravitational wave signal. The task is to identify when a signal is present from the mergers of binary black holes; Each data sample (npy file) contains 3 time series (1 for each detector) and each spans 2 sec and is sampled at 2,048 Hz. *European Gravitational Observatory - EGO, 2015*
