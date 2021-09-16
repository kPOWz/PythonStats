# capture = DataCapture()
 
# capture.add(3)
# capture.add(9)
# capture.add(3)
# capture.add(4)
# capture.add(6)
 
# stats = capture.build_stats()
 
# stats.less(4) # should return 2 (only two values 3, 3 are less than 4)
 
# stats.between(3, 6) # should return 4 (3, 3, 4 and 6 are between 3 and 6)
 
# stats.greater(4) # should return 2 (6 and 9 are the only two values greater than 4)
from stats import Stats

class DataCapture:
  max_integer = 1000 + 1;
  zero_base_array_adjustment_factor = 1;
  def __init__(self):
    self.raw_data = [None for n in range(self.max_integer)]
    self.raw_data_ascending_condensed = []

  def add(self, n: int):
    current_value = self.raw_data[n]
    if current_value is None:
      self.raw_data[n] = n
    else:
      self.raw_data[n] = current_value + n     
       
    return self.raw_data

  def build_stats(self):
    for idx, n in enumerate(self.raw_data):
        if(n != None):
            min_index = len(self.raw_data_ascending_condensed)
            n_denormalized = int(n/idx); 

            self.raw_data_ascending_condensed.extend([idx for n in range(n_denormalized)])
            
            max_index =  len(self.raw_data_ascending_condensed) - self.zero_base_array_adjustment_factor
            min_max = (min_index, max_index)
            self.raw_data[idx] = min_max

    # odd for the two classes to share all the base/sample data, but probably odder still to make Stats a DataCapture given the requirement that a DataCapture function return a Stats instance
    return Stats(self.raw_data, self.raw_data_ascending_condensed)
