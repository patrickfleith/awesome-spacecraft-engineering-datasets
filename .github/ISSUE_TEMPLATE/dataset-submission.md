---
name: Dataset submission
about: Propose a dataset for the list, or park one you found while scouting
title: "[DATASET]: "
labels: ''
assignees: ''

---

Fill in what you know. Blank or "not sure" is fine on any field. A partial submission still beats a lost link.

**Name and link**
The name, and a URL that reaches the data or its download page.

**Subsystem**
Where the data comes from, which decides the section it lands in: Propulsion, Power, Structures and mechanisms, Avionics and EEE parts, Operations and telemetry, GNC and space debris, Payload imaging, Space environment, Engineering text, Astronomy. Say so if none of them fit.

**Tasks**
Every task the data supports, not only the headline one. Existing badges: `regression`, `forecasting`, `classification`, `image-classification`, `text-classification`, `anomaly-detection`, `novelty-detection`, `outlier-detection`, `rul`, `object-detection`, `pose-estimation`, `domain-adaptation`, `signal-processing`, `pretraining`, `llm-eval`, `optimisation`, `eda`.

**Origin**
`real` if measured from hardware or a flying mission, `synthetic` if generated from a model or a simulator, `mixed` if real recordings carry injected synthetic signals. This is the first thing that tells a reader whether a result transfers, so say which one and how you know.

**Download size**
Size of the full download, with the unit.

**Description**
Two or three sentences. What a model predicts or finds in this data, where the data comes from, and why it earns a place next to what is already listed.

**Data format**
One line, such as "time series in CSV" or "zipped MAT files, one per experiment, with a README PDF".

**Access**
Free download, account needed, request form, or a licence that restricts use. Note any step between the link and the files.

**Author and citation**
Authors and year, or the full reference to cite.

**Checks**

- [ ] It is not in the README already
- [ ] The link works today and the data is public
- [ ] It covers spacecraft, rovers, launch vehicles or the engineering behind them, and is not a downstream Earth observation application
- [ ] I read the facts above off the source page rather than recalling or generating them
