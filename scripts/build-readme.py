# -*- coding: utf-8 -*-
"""Builds README.md from the dataset entries below. Run from the repo root:

    python3 scripts/build-readme.py

Draft of the generator anticipated by DEC-001: swap the ds() calls for the
datasets/*.yml cards once the card schema and controlled vocabularies settle.
licence='' means not verified, so the field is omitted rather than guessed."""
import io

PCOE = "https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/"
NOLIC = "no licence stated"   # NASA PCoE: no formal licence, citation requested

E = []
def ds(sec, name, url, tasks, size, modality, labels, origin, licence, source, body, cite=None):
    E.append(dict(sec=sec, name=name, url=url, tasks=tasks, size=size, modality=modality,
                  labels=labels, origin=origin, licence=licence, source=source,
                  body=body, cite=cite))

# ---------------------------------------------------------------- propulsion
ds("Propulsion", "Spacecraft Thruster Firing Tests",
   "https://www.kaggle.com/datasets/patrickfleith/spacecraft-thruster-firing-tests-dataset",
   ["regression"], "10.9 GB", "time series", True, ["synthetic"], "", "Patrick Fleith, 2022",
   ["Time series analysis and predictive modelling of engine thrust, mass flow rate, and performance degradation over time. The data is synthetic, partially based on the real-world physics of a chemical reaction control thruster, which makes it the closest public stand-in for RCS acceptance test data.",
    "Time series in .csv files."])

# -------------------------------------------------------------------- power
ds("Power", "Mars Express Power Challenge",
   "https://kelvins.esa.int/mars-express-power-challenge/home/",
   ["regression","forecasting"], "150 MB", "time series", True, ["real"], "", "ESA Advanced Concepts Team, 2021",
   ["Predict the average current consumption of 33 thermal power lines per hour of the mission's fourth Martian year, 2014-04-14 to 2016-03-01. Flight data from an operating interplanetary mission.",
    "Time series in .csv files."])
ds("Power", "NASA Battery",
   "https://www.kaggle.com/datasets/patrickfleith/nasa-battery-dataset",
   ["rul"], "210 MB", "time series", True, ["real"], NOLIC, "NASA Ames, 2007",
   ["A set of Li-ion batteries were run through different operational profiles (charge, discharge and impedance) at various temperatures. Impedance measurement was carried out through an electrochemical impedance spectroscopy frequency sweep. Repeated charge and discharge cycles accelerate ageing, while the impedance measurements give insight into the internal battery parameters that change as ageing progresses. The experiments stopped when the batteries reached end-of-life criteria.",
    "Usable for predicting both remaining charge for a given discharge cycle and remaining useful life. Batches of 6 experiments, in .mat files, with experiment details in an associated README.txt."],
   "B. Saha and K. Goebel (2007), Prognosis CoE, NASA Ames")
ds("Power", "Randomized Battery Usage",
   "https://www.kaggle.com/datasets/patrickfleith/nasa-randomized-battery-usage-dataset",
   ["rul"], "1.12 GB", "time series", True, ["real"], NOLIC, "NASA Ames",
   ["Batteries are continuously cycled with randomly generated current profiles, which is closer to real load than a constant-current test. Reference charging and discharging cycles are also performed after each fixed interval of randomized usage, to provide reference benchmarks for battery state of health.",
    "Download: section 11, `Randomized Battery Usage`, of the [NASA Prognostics Data Repository](%s)." % PCOE],
   "B. Bole, C. Kulkarni, and M. Daigle, NASA Ames Research Center")

# ------------------------------------------------- structures and mechanisms
ds("Structures and mechanisms", "CFRP Composites", PCOE,
   ["rul","anomaly-detection"], "4.5 GB", "time series", True, ["real"], NOLIC, "Stanford SACL and NASA Ames",
   ["Run-to-failure experiments on CFRP panels with periodic measurements to capture internal damage growth under tension-tension fatigue. Monitoring data consists of Lamb wave signals from a network of 16 piezoelectric (PZT) sensors and multiple triaxial strain gages. Periodic x-rays were taken to characterise internal damage as ground truth information. Three different layups were tested.",
    "Organised into three zipped folders, each containing data from coupons of a single layup type, a readme, and a folder with reports and papers published from this dataset. Download: section 2, `Carbon Fiber-Reinforced Polymer (CFRP) Composites`."],
   "Abhinav Saxena, Kai Goebel, Cecilia C. Larrosa, and Fu-Kuo Chang. Experiments conducted at Stanford Structures and Composites Laboratory (SACL) in collaboration with the Prognostic Center of Excellence (PCoE) of NASA Ames Research Center")
ds("Structures and mechanisms", "NASA Bearing",
   "https://www.kaggle.com/vinayak123tyagi/bearing-dataset",
   ["rul","anomaly-detection"], "6.08 GB", "time series", True, ["real"], "", "University of Cincinnati IMS",
   ["Four bearings were installed on a shaft. Three data sets are included in the data packet, and each one describes a test-to-failure experiment. Each data set consists of individual files that are 1-second vibration signal snapshots recorded at specific intervals. Each file consists of 20,480 points with the sampling rate set at 20 kHz.",
    "Data format is ASCII and .txt. The standard bearing degradation benchmark."],
   "University of Cincinnati, Center for Intelligent Maintenance Systems (IMS)")
ds("Structures and mechanisms", "FEMTO Bearings", PCOE,
   ["rul"], "2 GB", "time series", True, ["real"], NOLIC, "FEMTO-ST Institute",
   ["Experiments on bearings' accelerated life tests. A second bearing benchmark on a different rig, which makes it useful for checking whether a model trained on NASA Bearing transfers.",
    "Download the dataset by searching for section 10, `FEMTO Bearing`, in the NASA Prognostics Data Repository."],
   "P. Nectoux, R. Gouriveau, K. Medjaher, E. Ramasso, B. Morello, N. Zerhouni, C. Varnier, FEMTO-ST Institute, Besancon, France, and NASA Ames Research Center")
ds("Structures and mechanisms", "NASA Milling",
   "https://www.kaggle.com/datasets/vinayak123tyagi/milling-data-set-prognostic-data",
   ["regression"], "72.6 MB", "time series", True, ["real"], "", "UC Berkeley BEST lab, 2007",
   ["Can you predict the flank wear VB in mm, the wearing of the milling insert after some runs? Experiments on a milling machine for different speeds, feeds, and depths of cut, recording the wear of the milling insert.",
    "The dataset is in .mat format and has been zipped. A Readme.pdf provides details on the experimental protocol and the measurement techniques."],
   "A. Agogino and K. Goebel (2007), BEST lab, UC Berkeley")
ds("Structures and mechanisms", "NASA Airfoil Self-Noise",
   "https://archive.ics.uci.edu/dataset/291/airfoil+self+noise",
   ["regression"], "< 1 MB", "tabular", True, ["real"], "CC BY 4.0", "NASA",
   ["A series of aerodynamic and acoustic tests of two and three-dimensional airfoil blade sections, conducted in an anechoic wind tunnel. The span of the airfoil and the observer position were the same in all of the experiments. The objective is to predict the aerofoil noise, the scaled sound pressure level.",
    "Small enough to prototype a pipeline in minutes."],
   "Thomas F. Brooks, D. Stuart Pope and Michael A. Marcolini (NASA). Donor: Dr. Roberto Lopez")

# --------------------------------------------------- avionics and EEE parts
ds("Avionics and EEE parts", "MOSFET Thermal Overstress Aging", PCOE,
   ["rul"], "7.3 GB", "time series", True, ["real"], NOLIC, "NASA Ames",
   ["Run-to-failure experiments on power MOSFETs under thermal overstress. The data is in .mat format and has been zipped.",
    "Download: section 13, `Metal-Oxide-Semiconductor Field-Effect Transistor (MOSFET) Thermal Overstress Aging`. The DataSet reference document can be downloaded [here](http://ti.arc.nasa.gov/m/project/prognostic-repository/MOSFET%20Thermal%20Overstress%20Aging%20Document.pdf)."],
   "J. R. Celaya, A. Saxena, S. Saha, and K. Goebel, NASA Ames Research Center")
ds("Avionics and EEE parts", "Capacitor Electrical Stress", PCOE,
   ["rul"], "4.8 GB", "time series", True, ["real"], NOLIC, "NASA Ames",
   ["Capacitors were subjected to electrical stress under three voltage levels: 10 V, 12 V and 14 V. The data set contains EIS data as well as charge/discharge signal data, in .mat format, zipped.",
    "Download: section 12, `Capacitor Electrical Stress`. The DataSet reference document can be downloaded [here](http://ti.arc.nasa.gov/m/project/prognostic-repository/Description%20of%20Electrolytic%20Capacitors%20under%20Electrical%20Overstress%20Data%20Sets.pdf)."],
   "J. Renwick, C. Kulkarni, and J. Celaya, NASA Ames Research Center")

# ------------------------------------------------- operations and telemetry
ds("Operations and telemetry", "ESA Anomaly Dataset",
   "https://zenodo.org/records/15237121",
   ["anomaly-detection","novelty-detection"], "11.6 GB", "time series", True, ["real"], "CC BY 3.0 IGO", "K. Kotowski et al., 2024",
   ["A large-scale, real-life satellite telemetry dataset with curated anomaly annotations, originating from three ESA missions. The task is to detect anomalies in the telemetry time series. It is the largest labelled operational telemetry set available.",
    "The dataset is in compressed Pickle files with data, and CSVs with annotations."],
   "K. Kotowski et al., \"European Space Agency Benchmark for Anomaly Detection in Satellite Telemetry,\" 2024, http://arxiv.org/abs/2406.17826")
ds("Operations and telemetry", "Controlled Anomalies Time Series (CATS)",
   "https://zenodo.org/records/8338435",
   ["anomaly-detection","novelty-detection","outlier-detection"], "2.0 GB", "time series", True, ["synthetic"], "CC BY 4.0", "Patrick Fleith, Solenix, 2023",
   ["A large, multivariate time series dataset designed specifically for benchmarking anomaly detection algorithms. It contains 17 variables (sensors, control commands, and external stimuli) from a simulated complex system, with 5 million data points including 200 injected anomalies.",
    "Useful for evaluating and developing algorithms for anomaly detection in multivariate time series, supporting both semi-supervised (novelty detection) and unsupervised (outlier detection) approaches. Because the anomalies are injected, the ground truth is exact, which no real telemetry set can give you. The time series are in a .csv or .parquet file."],
   "Patrick Fleith. (2023). Controlled Anomalies Time Series (CATS) Dataset (Version 2) [Data set]. Solenix Engineering GmbH. https://doi.org/10.5281/zenodo.8338435")
ds("Operations and telemetry", "SMAP and MSL",
   "https://www.kaggle.com/datasets/patrickfleith/nasa-anomaly-detection-dataset-smap-msl",
   ["anomaly-detection","novelty-detection"], "~250 MB", "time series", True, ["real"], "", "NASA JPL, 2018",
   ["Expert-labeled telemetry anomaly data from the Soil Moisture Active Passive (SMAP) satellite and the Mars Science Laboratory (MSL) rover, Curiosity. Indications of telemetry anomalies can be found within Incident Surprise Anomaly (ISA) reports. All telemetry channels discussed in an individual ISA were reviewed to ensure that the anomaly was evident in the associated telemetry data, and specific anomalous time ranges were manually labeled for each channel. If multiple anomalous sequences and channels closely resembled each other, only one was kept, in order to create a diverse and balanced set.",
    "Anomalies were classified into two categories, point and contextual, to distinguish between anomalies that would likely be identified by properly-set alarms or distance-based methods that ignore temporal information (point anomalies), and those that require more complex methodologies such as LSTMs or Hierarchical Temporal Memory (contextual anomalies).",
    "**SMAP**: 55 TM channels, 429,735 total TM values, 69 anomalies. **MSL**: 27 TM channels, 66,709 total TM values, 36 anomalies. Data in .npy files."],
   "Kyle Hundman et al. 2018, NASA Jet Propulsion Laboratory")
ds("Operations and telemetry", "LASP Spacecraft Telemetry",
   "https://github.com/sapols/Satellite-Telemetry-Anomaly-Detection",
   ["outlier-detection"], "14 MB", "time series", False, ["real"], "", "Shawn Polson, LASP",
   ["This dataset can be used for visualisation and analysis of telemetry data that is built and maintained at the Laboratory for Atmospheric and Space Physics. There is no ground truth, so it suits unsupervised work only.",
    "Data in .csv files. Read more in [Unsupervised Machine Learning for Spacecraft Anomaly Detection in WebTCAD](https://github.com/sapols/Satellite-Telemetry-Anomaly-Detection/blob/master/Paper/Unsupervised%20Machine%20Learning%20for%20Spacecraft%20Anomaly%20Detection%20in%20WebTCAD.pdf)."],
   "Shawn Polson, Laboratory for Atmospheric and Space Physics")
ds("Operations and telemetry", "Satellite (ODDS)",
   "http://odds.cs.stonybrook.edu/satellite-dataset/",
   ["outlier-detection"], "< 1 MB", "tabular", True, ["real"], "", "Adapted from A. Srinivasan, 1993",
   ["The original Statlog (Landsat Satellite) dataset from the UCI machine learning repository is a multi-class classification dataset. Here, the training and test data are combined. The smallest three classes, 2, 4 and 5, are combined to form the outliers class, while all the other classes are combined to form an inlier class. A sanity check for a new detector before you point it at telemetry.",
    "Data in a .mat file. X = multi-dimensional point data, y = labels (1 = outliers, 0 = inliers)."],
   "Adapted from Ashwin Srinivasan (1993), University of Strathclyde")
ds("Operations and telemetry", "Satimage-2 (ODDS)",
   "http://odds.cs.stonybrook.edu/satimage-2-dataset/",
   ["outlier-detection"], "< 1 MB", "tabular", True, ["real"], "", "Adapted from A. Srinivasan, 1993",
   ["The original Statlog (Landsat Satellite) dataset from the UCI machine learning repository is a multi-class classification dataset. Here, the training and test data are combined, and class 2 is down-sampled to 71 outliers, while all the other classes are combined to form an inlier class. The modified dataset is referred to as Satimage-2. A harder imbalance than Satellite (ODDS).",
    "Data in a .mat file. X = multi-dimensional point data, y = labels (1 = outliers, 0 = inliers)."],
   "Adapted from Ashwin Srinivasan (1993), University of Strathclyde")
ds("Operations and telemetry", "Turbofan Engine Degradation (C-MAPSS)",
   "https://www.nasa.gov/content/prognostics-center-of-excellence-data-set-repository",
   ["rul"], "45.3 MB", "time series", True, ["synthetic"], NOLIC, "NASA Ames, 2008",
   ["Engine degradation simulation carried out using C-MAPSS. Four different sets were simulated under different combinations of operational conditions and fault modes. The data records several sensor channels to characterise fault evolution. An aero engine rather than spacecraft hardware, and the standard RUL benchmark that most published methods report against.",
    "The dataset is in text format and has been zipped, including a readme file and an original paper describing damage propagation modelling."],
   "A. Saxena and K. Goebel (2008), Prognostics CoE at NASA Ames")

# -------------------------------------------------- GNC and space debris
ds("GNC and space debris", "Pose Estimation Challenge 2021",
   "https://kelvins.esa.int/pose-estimation-2021/home/",
   ["pose-estimation","domain-adaptation"], "15.7 GB", "image", True, ["mixed"], "", "ESA ACT and Stanford SLAB, 2021",
   ["Can you predict the position and orientation of a spacecraft in realistic images while only being provided with labels from computer generated examples? SPEC2021 is explicitly designed to investigate the domain gap between synthetic labelled and realistic unlabelled images.",
    "The challenge sheds light on the next big question for spaceborne computer vision algorithms: how can one validate on-ground a pose estimation algorithm on spaceborne image targets that are simply unavailable prior to the mission? Unlike on Earth, autonomous driving in space prohibits habitual road tests and on-site debugging.",
    "Data provided are .json (filenames) and 8-bit monochrome images in jpeg format, at a resolution of 1920x1200 pixels. Only the synthetic images carry labels. You may also want to look at the dataset of the previous Pose Estimation Challenge from 2019, [here](https://kelvins.esa.int/satellite-pose-estimation-challenge/)."],
   "Advanced Concepts Team (ESA) and Space Rendezvous Laboratory (SLAB) of Stanford University, 2021")
ds("GNC and space debris", "spotGEO",
   "https://kelvins.esa.int/spot-the-geo-satellites/home/",
   ["object-detection","regression"], "4.2 GB", "image", True, ["real"], "", "ESA ACT and University of Adelaide, 2020",
   ["The goal is to detect orbiting objects in the geostationary ring from sequences of 5 consecutive frames imaging some unknown portion of the sky, provided by a low-cost ground based telescope. Can you learn how to cope with cloud cover, atmospheric and weather effects, light pollution, sensor noise and defects, and star occlusions?",
    "32,000 grayscale images of size 640x480 pixels, plus JSON files."],
   "Advanced Concepts Team (ESA) and University of Adelaide, 2020")
ds("GNC and space debris", "Space Debris: the origin",
   "https://kelvins.esa.int/space-debris-the-origin/home/",
   ["classification","regression"], "< 3 MB", "tabular", True, ["synthetic"], "", "ESA Advanced Concepts Team, 2021",
   ["Determine two things for each of the debris given: the id of the defunct satellite (classification task), and the value of the effective area over mass ratio Cr(A/m) of the debris (regression task).",
    "Data are in .dat files."],
   "Advanced Concepts Team, European Space Agency, 2021")
ds("GNC and space debris", "The Kessler Run (GTOC9)",
   "https://kelvins.esa.int/gtoc9-kessler-run/home/",
   ["optimisation"], "< 1 MB", "tabular", False, ["real"], "", "ESA Advanced Concepts Team, 2017",
   ["Design and optimise n missions able to cumulatively remove all the 123 orbiting debris. One mission is a multiple-rendezvous spacecraft trajectory where a subset of size N of the 123 orbiting debris is removed by the delivery and activation of N de-orbit packages. Optimisation rather than learning, so there are no labels.",
    "Data are orbital debris elements in .csv."],
   "Advanced Concepts Team, European Space Agency, 2017")
ds("GNC and space debris", "Planetary Defence Challenge",
   "https://kelvins.esa.int/planetary-defence/home/",
   ["regression"], "< 1 MB", "time series", True, ["synthetic"], "", "ESA Advanced Concepts Team, 2021",
   ["Several high-fidelity simulations of a kinetic impactor mission over a binary system have been produced. The lightcurves as observed from the Earth before and after the impact of each of the simulated scenarios are available. Estimate the beta-factor and a/c, the secondary and the ratio between the secondary major and minor axis.",
    "Data are in .dat files."],
   "Advanced Concepts Team, European Space Agency, 2021")

# ---------------------------------------------------------- payload imaging
ds("Payload imaging", "Mars Surface and Curiosity Image Set",
   "https://www.kaggle.com/brsdincer/mars-surface-and-curiosity-image-set-nasa",
   ["image-classification"], "3.24 GB", "image", True, ["real"], "", "A. Stanboli and K. L. Wagstaff, NASA",
   ["This data set consists of 6,691 images that were collected by the Mars Science Laboratory (MSL, Curiosity) rover by three instruments: Mastcam Right eye, Mastcam Left eye, and MAHLI. The proposed task is a multiple output classification model.",
    "An on-board classifier would make it possible to prioritise which images are sent back to Earth earlier than the others, which makes this a downlink budget problem as much as a vision one. 6,691 images of roughly 256x256 in .jpg format."],
   "Alice Stanboli and Kiri L. Wagstaff, NASA")
ds("Payload imaging", "Statlog (Landsat Satellite)",
   "https://archive.ics.uci.edu/ml/datasets/Statlog+(Landsat+Satellite)",
   ["classification"], "< 1 MB", "tabular", True, ["real"], "CC BY 4.0", "A. Srinivasan, 1993",
   ["The dataset consists of the multi-spectral values of pixels in 3x3 neighbourhoods in a satellite image, and the classification associated with the central pixel in each neighbourhood. The aim is to predict this classification, given the multi-spectral values. In the sample database, the class of a pixel is coded as a number.",
    "Two ASCII files, sat.trn and sat.tst. See also the two ODDS variants of this dataset under operations and telemetry."],
   "Ashwin Srinivasan (1993), University of Strathclyde")

# --------------------------------------------------------- space environment
ds("Space environment", "NASA and NOAA Solar Wind",
   "https://www.kaggle.com/arashnic/soalr-wind",
   ["forecasting","regression"], "898 MB", "time series", True, ["real"], "", "NASA and NOAA",
   ["The disturbance-storm-time index, or Dst, is a measure of the severity of a geomagnetic storm. The data is composed of solar wind measurements collected from two satellites: NASA's Advanced Composition Explorer (ACE) and NOAA's Deep Space Climate Observatory (DSCOVR).",
    "The goal is to develop models for forecasting Dst that push the boundary of predictive performance, under operationally viable constraints, using the real-time solar-wind (RTSW) data feeds from NOAA's DSCOVR and NASA's ACE satellites."],
   "NASA and NOAA")

# ---------------------------------------------------------- engineering text
ds("Engineering text", "Space systems corpora",
   "https://pureportal.strath.ac.uk/en/datasets/dataset-of-space-systems-corpora-thesis-data",
   ["pretraining"], "257 MB", "text", False, ["real"], "", "A. Berquand and A. Riccardi, 2021",
   ["Several corpora used to train the methods developed in the thesis \"Text Mining and Natural Language Processing for the Early Stages of Space Mission Design\". The dataset includes 4,991 articles published in Acta Astronautica, Advances in Space Research (ASR), and Aerospace Science and Technology (AST), 39 books related to space mission design, and 242 Wikipedia pages processed with a space domain-specific Natural Language Processing pipeline.",
    "Additional text sources are 27,016 parsed ECSS requirements extracted from 126 active standards. The mission requirements are extracted from two publicly available ESA documents, the SMOS mission System Requirement Document and MarcoPolo-R's Mission Requirement Document. The ECSS portion is the part most engineering teams want. Data in .txt and .json files."],
   "Audrey Berquand, Annalisa Riccardi (2021), University of Strathclyde")
ds("Engineering text", "Space News",
   "https://www.kaggle.com/datasets/patrickfleith/space-news-dataset",
   ["pretraining","text-classification"], "79 MB", "text", False, ["real"], "", "Patrick Fleith",
   ["The title, url, text content, author, publish date, and post excerpt of more than 20,700 English news articles related to the space industry. A total of more than 14 million words, which makes it suitable for training language models specific to the space industry ecosystem.",
    "It covers agency news, commercial, civil, launches, military, and also opinion articles from [SpaceNews](https://spacenews.com/). Data are in .csv files."])
ds("Engineering text", "Astro-MCQA",
   "https://huggingface.co/datasets/patrickfleith/Astro-mcqa",
   ["llm-eval"], "200 rows", "text", True, ["real"], "CC BY 4.0", "Patrick Fleith, 2024",
   ["The primary purpose of AstroMCQA is for application developers in the domain of space mission design and operations to comparatively assess LLM performance on the specific task of multiple-choice question-answering.",
    "It addresses questions such as: which LLM to use, and how does it perform in the different subdomains? It enables benchmarking of different models, different sizes, quantization methods, prompt engineering strategies, and the effectiveness of fine-tuning on the specific task of multiple-choice question-answering in space engineering."],
   "AstroMCQA (c) 2024 by Patrick Fleith, licensed under Creative Commons Attribution 4.0 International")
ds("Engineering text", "Aeronautics and Astronautics Abstracts",
   "https://www.kaggle.com/sylar68/aeronautics-astronautics-journal-abstracts",
   ["text-classification"], "< 1 MB", "text", True, ["real"], "", "Patrick Fleith, 2021",
   ["Titles and abstracts of about 493 papers published by AIAA either in the Journal of Propulsion and Power (JPP) or in the Journal of Thermophysics and Heat Transfer (JTHT), manually retrieved from https://arc.aiaa.org.",
    "The task is to build a classifier able to distinguish between abstracts and titles from each specific technical domain. The challenge lies in that both domains, propulsion and heat transfer, contain overlapping vocabulary such as combustion, exchange, thermal and fluid, which makes it harder to tell which journal a paper comes from. All in an excel file (.xls)."],
   "Patrick Fleith, 2021")
ds("Engineering text", "IAF congress abstracts",
   "https://www.iafastro.org/",
   ["pretraining"], "coming soon", "text", False, ["real"], "", "Patrick Fleith, 2022",
   ["More than 30,000 abstracts of congress articles submitted to the IAF (International Astronautical Federation). This is equivalent to over 6 million words.",
    "Not yet released. We are constantly working towards more NLP-for-space data."])

# ----------------------------------------------------------------- astronomy
ds("Astronomy", "G2Net 2: continuous gravitational waves",
   "https://www.kaggle.com/competitions/g2net-detecting-continuous-gravitational-waves/overview",
   ["classification","signal-processing"], "227.1 GB", "time series", True, ["mixed"], "", "G2Net",
   ["A follow-up competition to G2Net. The goal is to find continuous gravitational-wave signals. You will develop a model sensitive enough to detect weak yet long-lasting signals emitted by rapidly-spinning neutron stars within noisy data.",
    "Real detector noise with simulated signals injected."])
ds("Astronomy", "G2Net",
   "https://www.kaggle.com/c/g2net-gravitational-wave-detection/overview",
   ["classification","signal-processing"], "72 GB", "time series", True, ["mixed"], "", "European Gravitational Observatory",
   ["A training set of time series data containing simulated gravitational wave measurements from a network of 3 gravitational wave interferometers: LIGO Hanford, LIGO Livingston, and Virgo. Each time series contains either detector noise, or detector noise plus a simulated gravitational wave signal. The task is to identify when a signal is present from the mergers of binary black holes.",
    "Each data sample (.npy file) contains 3 time series, one for each detector. Each spans 2 seconds and is sampled at 2,048 Hz."],
   "European Gravitational Observatory (EGO), 2015")
ds("Astronomy", "Breakthrough Listen SETI",
   "https://www.kaggle.com/c/seti-breakthrough-listen/data",
   ["classification","signal-processing"], "62.0 GB", "image", True, ["real"], "", "Berkeley SETI Research Center, 2021",
   ["Detect candidate signatures of extraterrestrial technology in deep space signals (cadence snippets) taken by the Green Bank Telescope (GBT).",
    "NumPy float16 format of shape (6, 273, 256)."],
   "University of California, Berkeley SETI Research Center, 2021")
ds("Astronomy", "Kepler Exoplanet Search Results",
   "https://www.kaggle.com/nasa/kepler-exoplanet-search-results",
   ["eda"], "989 MB", "tabular", True, ["real"], "", "NASA",
   ["A cumulative record of all observed Kepler \"objects of interest\", which is all of the approximately 10,000 exoplanet candidates Kepler has taken observations on.",
    "Inspiration for analysis: how often are exoplanets confirmed in the existing literature disconfirmed by measurements from Kepler, and the other way round? What general characteristics about exoplanets can you derive from this dataset? Which exoplanets get assigned names in the literature? What is the distribution of confidence scores?",
    "You can access the original table [here](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=koi). More data from the Kepler mission is available from the same [source](https://exoplanetarchive.ipac.caltech.edu/docs/data.html)."])

SECTIONS = []
for e in E:
    if e["sec"] not in SECTIONS: SECTIONS.append(e["sec"])

BLURB = {
 "Operations and telemetry": "Housekeeping telemetry and its simulated equivalent. Spacecraft health monitoring work starts here.",
 "Astronomy": "Not spacecraft engineering, but the instruments are, and the signal processing transfers.",
}
TASKS_VOCAB = ["regression","forecasting","classification","image-classification",
    "text-classification","anomaly-detection","novelty-detection","outlier-detection",
    "rul","object-detection","pose-estimation","domain-adaptation","signal-processing",
    "pretraining","llm-eval","optimisation","eda"]

def anchor(h):
    return "#" + h.lower().replace(" ","-").replace("(","").replace(")","").replace(":","").replace(",","").replace(".","").replace("/","")

def tbadge(t):
    return "![%s](assets/badges/task-%s.svg)" % (t, t)

def lb(name, alt):
    return "![%s](assets/badges/%s.svg)" % (alt, name)

def meta_balanced(e):
    b = [lb("labels-yes" if e["labels"] else "labels-no",
            "labels: yes" if e["labels"] else "labels: no")]
    for o in e["origin"]:
        b.append(lb("origin-" + o, "origin: " + o))
    rest = [e["size"], e["modality"]]
    if e["licence"]: rest.append(e["licence"])
    rest.append(e["source"])
    return " ".join(b) + " · " + " · ".join(rest)

def meta_text(e):
    bits = [e["size"], e["modality"],
            "labelled" if e["labels"] else "unlabelled",
            " + ".join(e["origin"])]
    if e["licence"]: bits.append(e["licence"])
    bits.append(e["source"])
    return " · ".join(bits)

def meta_badges(e):
    b = [sb("size", e["size"], C["size"]),
         sb("modality", e["modality"], C["modality"]),
         sb("labels", "yes" if e["labels"] else "no", C["yes"] if e["labels"] else C["no"])]
    for o in e["origin"]:
        b.append(sb("origin", o, C[o]))
    if e["licence"]: b.append(sb("licence", e["licence"], C["licence"]))
    b.append(sb("source", e["source"], C["source"]))
    return " ".join(b)

def meta_plain(e):
    bits = [e["size"], e["modality"]]
    if e["licence"]: bits.append(e["licence"])
    bits.append(e["source"])
    return " · ".join(bits)

def badge_line(e):
    b = [tbadge(t) for t in e["tasks"]]
    b.append(lb("labels-yes" if e["labels"] else "labels-no",
                "labels: yes" if e["labels"] else "labels: no"))
    for o in e["origin"]:
        b.append(lb("origin-" + o, "origin: " + o))
    return " ".join(b)

o = []; w = o.append
w("# Awesome Spacecraft Engineering Datasets [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)")
w("")
w("Datasets for space vehicle engineering (spacecraft, rovers), for industry and research. Grouped by spacecraft subsystem.")
w("")
w("## Contents")
w("")
counts = {s: sum(1 for e in E if e["sec"] == s) for s in SECTIONS}
w(" · ".join("[%s](%s) (%d)" % (s, anchor(s), counts[s]) for s in SECTIONS))
w("")
w("[Index by ML/AI task](#index-by-mlai-task) lists the same datasets the other way round.")
w("")
w("---")
w("")
for s in SECTIONS:
    w("## %s" % s); w("")
    if s in BLURB: w(BLURB[s]); w("")
    for e in [x for x in E if x["sec"] == s]:
        w("#### [%s](%s)" % (e["name"], e["url"]))
        w("")
        w(meta_plain(e))
        w("")
        w(badge_line(e))
        w("")
        w("<details><summary>Description</summary>")
        w("")
        for para in e["body"]:
            w(para); w("")
        if e["cite"]:
            w("*%s*" % e["cite"]); w("")
        w("</details>")
        w("")
w("---")
w("")
w("## Index by ML/AI task"); w("")
w("A dataset carries every task it supports, so entries repeat here."); w("")
w("| Task | Datasets |"); w("|---|---|")
for t in TASKS_VOCAB:
    n = [e["name"] for e in E if t in e["tasks"]]
    if n: w("| `%s` | %s |" % (t, ", ".join(n)))
w("")
w("## Licences"); w("")
nolic = [e["name"] for e in E if not e["licence"]]
w("Licence is shown only where it is stated by the host and has been checked. %d entries have a verified licence." % (len(E)-len(nolic)))
w("")
w("The NASA Prognostics Data Repository states no formal licence, only that users acknowledge the repository and the data donors and employ the data at their own risk. Those entries are marked `no licence stated`.")
w("")
w("Still to verify: %s." % ", ".join(nolic))
w("")
w("## Contributing"); w("")
w("Propose a dataset with the [issue template](.github/ISSUE_TEMPLATE/dataset-submission.md). List every task it supports rather than the headline one, give the modality and the licence, and name the subsystem it comes from.")

io.open("README.md","w",encoding="utf-8").write("\n".join(o) + "\n")
print("entries:", len(E), "| licensed:", sum(1 for e in E if e["licence"]))
