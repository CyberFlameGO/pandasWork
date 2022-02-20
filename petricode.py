# -*- coding: utf-8 -*-
import os
import json
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

data = {}
times = []

with open('transcripts.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

for x in data['messages']:
    times.append(x['timestamp'][:10])

z = {i:times.count(i) for i in set(times)}
sorted_dict = {key: value for key, value in sorted(z.items())}

print(sorted_dict)
