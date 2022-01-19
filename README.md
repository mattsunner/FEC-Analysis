# FEC Analysis

## About This Repository

This repository hold EDA and pipeline code for the analysis of current and historical Federal Election Commission (FEC) data. All data for this project was gathered from [fec.gov](https://fec.gov) and is available freely to anyone wishing to download the information. Data pulls were completed on 2022/01/19. 

## Repository Contents

- `/notebooks`: Contains all .ipynb notebook files for EDA & pipeline testing purposes
- `/src`: Contains all source code for the analysis project, including pipeline code, visualizations and feature engineering
- `/env`: Contains environment files for setup and deployement
- `/data`: Contains all data, both raw and cleaned, separated out by sub-folder
    - `/data/raw`: Raw data and source files
    - `/data/intermediate`: In process data sources
    - `/data/reporting`: Clean and final data for reporting purposes