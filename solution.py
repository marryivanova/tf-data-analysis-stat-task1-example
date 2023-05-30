import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    
    # Найдём точечную оценку для среднего значения выборки
    x_mean = x.mean()
    
    # Найдём стандартную ошибку среднего
    stderr = stats.sem(x)
    
    # Вычислим квантиль t-распределения
    t = abs(stats.t.ppf(0.025, len(x) - 1))
    
    # Найдём границы доверительного интервала
    lower_bound = x_mean - t * stderr
    upper_bound = x_mean + t * stderr
    
    # Выведем на экран доверительный интервал и вернём точечную оценку
    print("Confidence interval: [{:.2f}, {:.2f}]".format(lower_bound, upper_bound))
    return x_mean
