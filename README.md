# python logger
this is just a simple logger for python programs, nothing fancy

## usage
```python
from logger import *

set_logging(3)

log('this is some info!', 1)
log('this is a warning!', 2)
log('this is an error!', 3)
```
output:
```
[INFO] this is some info!
[WARNING] this is a warning!
[ERROR] this is an error!
```
