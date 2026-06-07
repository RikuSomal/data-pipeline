import logging
from pipeline import Pipeline

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    p = Pipeline()
    p.run()
