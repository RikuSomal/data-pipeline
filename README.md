# data-pipeline

Lightweight ETL pipeline for processing and transforming datasets.

## Features
- Extract data from CSV, JSON, or REST APIs
- Transform and clean datasets
- Load to database or output files

## Install
```bash
pip install -r requirements.txt
```

## Usage
```python
from pipeline import Pipeline

p = Pipeline()
p.extract("data/input.csv")
p.transform()
p.load("output/result.csv")
```

## License
MIT
