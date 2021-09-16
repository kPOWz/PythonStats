class Stats:
  def __init__(self, min_max_population_array: list[tuple[int, int]], integer_count: int):
    self.min_max_population_array = min_max_population_array
    self.integer_count = integer_count

  def less(self, n: int):
    stats_lookup_min_max = self.min_max_population_array[n];
    stats_lookup_index_min = stats_lookup_min_max[0];
    count_items_less_than_n = stats_lookup_index_min;
    return count_items_less_than_n;

  def greater(self, n: int):
    stats_lookup_min_max = self.min_max_population_array[n];
    stats_lookup_index_max = stats_lookup_min_max[1];
    count_items_greater_than_n = self.integer_count - stats_lookup_index_max - 1;
    return count_items_greater_than_n;

  def between(self, n: int, m: int):
    return self.integer_count - self.less(n) - self.greater(m)
