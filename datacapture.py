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
        self.raw_data_condensed = []

  def add(self, n: int):
    self.raw_data[n] = n
    return self.raw_data

  def build_stats(self):
    for n in self.raw_data:
        if(n != None):
            self.raw_data_condensed.append(n)
            self.raw_data[n] = len(self.raw_data_condensed) - self.zero_base_array_adjustment_factor
    return self.raw_data_condensed

  def less(self, n: int):
    stats_lookup_index = self.raw_data[n];
    return stats_lookup_index + 1 - stats_lookup_index;
