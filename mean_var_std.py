import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  else:
    calculations = {'mean': [],
                    'variance': [],
                    'standard deviation': [],
                    'max': [],
                    'min': [],
                    'sum': []}

    array = np.array(list)
    matrix = np.reshape(array, (3,3))

    axis1_calc = np.mean(matrix, axis = 0).tolist()
    axis2_calc = np.mean(matrix, axis = 1).tolist()
    flattened_mean = np.mean(matrix)

    calculations['mean'] = [axis1_calc, axis2_calc, flattened_mean]

    axis1_calc = np.var(matrix, axis = 0).tolist()
    axis2_calc = np.var(matrix, axis = 1).tolist()
    flattened_var = np.var(matrix)

    calculations['variance'] = [axis1_calc, axis2_calc, flattened_var]

    axis1_calc = np.std(matrix, axis = 0).tolist()
    axis2_calc = np.std(matrix, axis = 1).tolist()
    flattened_std = np.std(matrix)

    calculations['standard deviation'] = [axis1_calc, axis2_calc, flattened_std]
    
    axis1_calc = np.max(matrix, axis = 0).tolist()
    axis2_calc = np.max(matrix, axis = 1).tolist()
    flattened_max = np.max(matrix)

    calculations['max'] = [axis1_calc, axis2_calc, flattened_max]

    axis1_calc = np.min(matrix, axis = 0).tolist()
    axis2_calc = np.min(matrix, axis = 1).tolist()
    flattened_min = np.min(matrix)

    calculations['min'] = [axis1_calc, axis2_calc, flattened_min]

    axis1_calc = np.sum(matrix, axis = 0).tolist()
    axis2_calc = np.sum(matrix, axis = 1).tolist()
    flattened_sum = np.sum(matrix)

    calculations['sum'] = [axis1_calc, axis2_calc, flattened_sum]
    return calculations