# Network Pharmacology Analysis for Myotonic Dystrophy Type 1 (DM1)

This repository contains code and data for a network pharmacology analysis aimed at identifying potential repurposed drugs for Myotonic Dystrophy type 1 (DM1).

## Project Overview

Myotonic dystrophy type 1 is a multisystem disorder caused by a CTG repeat expansion in the DMPK gene. This project uses protein-protein interaction (PPI) networks to identify key genes and potential drug targets.

## Initial Findings

An initial analysis using degree centrality identified several hub genes that may serve as potential drug targets. The top-ranked genes include:
- **DMPK** (the disease-causing gene)
- **MBNL1** (a key splicing regulator)
- **CELF1** (another splicing factor)

## Repository Structure

- `analyze_network.py`: Main script that loads a PPI network and computes centrality metrics.
- `data/`: Contains sample network data (not included in this repo for size reasons).
- `results/`: Output files with centrality scores and visualizations.

## Getting Started

1. Clone this repository.
2. Install dependencies: `pip install networkx pandas matplotlib`
3. Run the analysis: `python analyze_network.py`

## Future Work

- Incorporate betweenness centrality for improved identification of regulatory bottlenecks.
- Integrate drug-target interaction databases to suggest repurposable compounds.
- Validate predictions using in vitro models.