# PHAST Temperature Dispersion Analyser

A tool for analysing temperature data from PHAST dispersion reports.
Useful for cryogenic risk assessments where you want to find the maximum downwind distance to a temperature of interest.

## Installation

1. Clone this repository
2. Install in development mode:
```bash
pip install -e .
```

## Usage

Run the application:
```bash
python -m src.main
```

## Features

- Process multiple Excel files containing PHAST dispersion data
- Support for both vapour and liquid temperature analysis
- Multiple interpolation methods (Linear, Cubic Spline, Quadratic, Nearest Neighbor)
- Export results to Excel with customizable decimal places
- Progress tracking and logging 
