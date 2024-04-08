from typing import Callable
import re
def generator_numbers(text: str):
    for el in re.finditer(r' \d*\.\d+ ', text):
        # print(el)
        yield float(el.group())
        

def sum_profit(text: str, func:Callable):
    total_sum = 0
    for el in func(text):
        total_sum += el
    return total_sum


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
