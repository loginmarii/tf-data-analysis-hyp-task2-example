import pandas as pd
import numpy as np


chat_id = 1676035524 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    from scipy.stats import ks_2samp
    stat, p = ks_2samp(x, y)
    if p <= 0.08:
        b = True
    else:
        b = False
    return b # Ваш ответ, True или False
