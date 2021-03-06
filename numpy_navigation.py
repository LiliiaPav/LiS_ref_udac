# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_heights=np.array(heights)
np_positions=np.array(positions)

# Heights of the goalkeepers: gk_heights
temp=(np_positions == 'GK')
gk_heights=np_heights[temp]


# Heights of the other players: other_heights
temp2=(np_positions != 'GK')
other_heights=np_heights[temp2]

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
