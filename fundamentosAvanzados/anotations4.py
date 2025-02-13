from typing import Optional

def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:
    """
    Busca un ID de empleado en una lista de IDs y devuelve el valor si existe.

    Args:
        employee_ids (list[int]): lista de IDs de empleados 
        employee_id (int): ID a buscar 

    Returns:
        Optional[int]: El ID encontrado o None si no existe en la lista
    """
    if employee_id in employee_ids:
        return employee_id
    return None