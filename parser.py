
from math import sqrt

def variance (vals):
    if not len(vals):
        return 0
    avg = sum(vals)/max(float(len(vals)),1)
    return sqrt(sum((val-avg)**2 for val in vals)/len(vals))
    
    
with open('monitor_new_johnny/results.out', 'r') as f:
    results = []
    result_keys = None
    for line in f.readlines():
        line = line.strip()
        if line[:5] == 'START':
            start = int(line.split(' ')[1])
        elif line[:4] == 'DONE':
            end = int(line.split(' ')[1])
        else:
            split = line.split(' ')
            if not result_keys:
                result_keys = split
            else:
                result = {}
                for i, key in enumerate(result_keys):
                    result[key] = split[i]
                results.append(result)
'''for result in results:
    print result['results'], result['first_time'], result['total_time']'''
    
    
    
with open('monitor_new_johnny/monitor.csv', 'r') as f:
    monitors = []
    monitor_keys = None
    for line in f.readlines():
        line = line.strip()
        split = line.split(',')
        if not monitor_keys:
            monitor_keys = split
        else:
            result = {}
            for i, key in enumerate(monitor_keys):
                if key == 'cpu(%)':
                    result[key] = float(split[i])
                else:
                    result[key] = int(split[i])
            time = int(result['timestamp(ms)'])
            if time > start and time < end:
                monitors.append(result)

cpu = [monitor['cpu(%)'] for monitor in monitors]
mem = [monitor['mem(b)'] for monitor in monitors]
avg = sum(cpu)/float(len(monitors))
med = sorted(cpu)[len(monitors)/2]
var = variance(cpu)
print avg, med, var


