# Python process count by Mackerel custom metrics

clone this repo

Add /etc/mackerel-agent/mackerel-agent.conf

```
[plugin.metrics.vmstat]
command = [ "python3", "/path/to/mackerel-python-process/vmstat-metrics.py" ]
```
