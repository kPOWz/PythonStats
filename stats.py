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


class Stats:
  def __init__(self, min_max_population_array: list[tuple[int, int]]):
    self.min_max_population_array = min_max_population_array

  def less(self, n: int):
    stats_lookup_min_max = self.min_max_population_array[n];
    stats_lookup_index_min = stats_lookup_min_max[0];
    count_items_less_than_n = stats_lookup_index_min;
    return count_items_less_than_n;
