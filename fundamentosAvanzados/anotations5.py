from typing import Union

def process_salary(salary: Union[int,float]) -> float:
    """
    Procesa un salario que puede ser entero o flotante y lo devuelve como flotante.

    Args:
        salary (Union[int,float]): Un salario que puede ser un entero o flotante.
    Returns:
        float: El salario convertido a flotante. 
    """
    return float(salary)