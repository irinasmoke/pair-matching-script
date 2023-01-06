import random
import math
import random

def generate_pairs(names, disallowed_combinations):

  # Shuffle the list of names to ensure that the pairs are random
  random.shuffle(names)

  # Calculate the maximum number of pairs that can be created
  max_pairs = math.ceil(len(names) / 2)

  # Create a list to store the pairs
  pairs = []

  # Create a list to store the names that have not been paired yet
  unpaired_names = names.copy()

  # Iterate over the names, two at a time
  for i in range(0, len(names), 2):
    # If there are an odd number of names, the last pair will have one member (to be manually assigned by organizer to a pair)
    if i+1 < len(names):
      pair = (names[i], names[i+1])
    else:
      pair = (names[i],)

    # Check if the pair is in the list of disallowed combinations
    if pair in disallowed_combinations or (pair[::-1] in disallowed_combinations):
      # If the pair is disallowed, do not add it to the list
      continue
    pairs.append(pair)
    # Remove the paired names from the list of unpaired names
    unpaired_names.remove(pair[0])
    if len(pair) == 2:
      unpaired_names.remove(pair[1])

  # While there are more than one singleton in the list of pairs
  while len([pair for pair in pairs if len(pair) == 1]) > 1:
    # Shuffle the list of pairs to ensure that the pairing of singletons is random
    random.shuffle(pairs)

    # Find the first pair with a singleton
    for i, pair in enumerate(pairs):
      if len(pair) == 1:
        singleton = pair[0]
        # Find the next pair with a singleton
        for j, other_pair in enumerate(pairs[i+1:]):
          if len(other_pair) == 1:
            other_singleton = other_pair[0]
            # Check if the combination of the two singletons is disallowed
            if (singleton, other_singleton) in disallowed_combinations or ((other_singleton, singleton) in disallowed_combinations):
              # If the combination is disallowed, do not pair the singletons
              continue
            # Otherwise, pair the singletons and remove them from the list of pairs
            new_pair = (singleton, other_singleton)
            pairs.remove(pair)
            pairs[i+j] = new_pair
            break

  # If the maximum number of pairs has not been reached, try again
  # WARNING: Does not cover the case where it's not possible to reach the max number of pairs. If max # of pairs can't be reached due to too many conflicts, this will simply hang as it keeps re-trying.
  while len(pairs) < max_pairs:
    pairs = generate_pairs(names, disallowed_combinations)

  return pairs


# Test the function
names = ['Joey', 'Laurel','Giselle',  'Jake', 'Ben', 'JP', 'Sara', 'Jessica', 'Irina', 'Jin']
disallowed_combinations = [
    
    #Prior pairs, do not repeat
    ('Ben', 'Jake'), 
    ('Linzi', 'Irina'),

    #Managers should not be paired with reports
    ('JP', 'Irina'),
    ('JP', 'Linzi'),
    ('JP', 'Ben'),

    #Level Conflicts

      #Contractor/UXR I should not be paired with Senior or Principal
      ('Joey', 'Wei'),
      ('Joey', 'Jake'),
      ('Joey', 'Ben'),
      ('Joey', 'JP'),
      ('Joey', 'Sara'),
      ('Joey', 'Jessica'),

      ('Laurel', 'Wei'),
      ('Laurel', 'Jake'),
      ('Laurel', 'Ben'),
      ('Laurel', 'JP'),
      ('Laurel', 'Sara'),
      ('Laurel', 'Jessica'),

      ('Jin', 'Wei'),
      ('Jin', 'Jake'),
      ('Jin', 'Ben'),
      ('Jin', 'JP'),
      ('Jin', 'Sara'),
      ('Jin', 'Jessica'),

      #Principal should also not be paired with UXR II
      ('Jessica', 'Giselle'),
      ('Jessica', 'Irina'),
      ('Jessica', 'Linzi'),

]
print(generate_pairs(names, disallowed_combinations))
