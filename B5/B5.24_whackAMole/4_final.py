# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Whack A Mole - GAMEPLAY (FINAL)
# I did not copy anyone

import time
from datetime import datetime

startTime = datetime.now()
print(startTime)
time.sleep(2)
stopTime = datetime.now()
print(stopTime)

diff = (stopTime - startTime).total_seconds()
print(diff)
