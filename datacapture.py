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
            
            for nn in range(n_denormalized):
              self.raw_data_ascending_condensed.append(idx)
            
            max_index =  len(self.raw_data_ascending_condensed) - self.zero_base_array_adjustment_factor
            min_max = (min_index, max_index)
            self.raw_data[idx] = min_max

    return self.raw_data_ascending_condensed

  def less(self, n: int):
    stats_lookup_min_max = self.raw_data[n];
    stats_lookup_index_min = stats_lookup_min_max[0];
    count_items_less_than_n = stats_lookup_index_min;
    return count_items_less_than_n;
