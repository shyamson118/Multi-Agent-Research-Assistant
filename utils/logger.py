import logging
import os
from datetime import datetime

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger("cogni-research")
    logger.setLevel(logging.INFO)
    
    fh = logging.FileHandler(f"logs/app_{datetime.now().strftime('%Y%m%d')}.log")
    fh.setLevel(logging.INFO)
    
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    return logger