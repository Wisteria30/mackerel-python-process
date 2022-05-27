import os
import subprocess
import sys
import time
from subprocess import PIPE

if os.environ.get("MACKEREL_AGENT_PLUGIN_META") == "1":
    import json

    meta = {
        "graphs": {
            "python.process": {
                "label": "Python process",
                "unit": "integer",
                "metrics": [
                    {"name": "count", "label": "Process num"},
                ],
            }
        }
    }

    print("# mackerel-agent-plugin")
    print(json.dumps(meta))
    sys.exit(0)

command = f'ps aux | grep "python" | grep -v "\(root\|grep\)" | grep -v "{os.path.basename(__file__)}" | wc -l'
proc = subprocess.run(command, shell=True, stdout=PIPE, stderr=PIPE, text=True)
if proc.returncode != 0:
    print("error: " + proc.stderr)
    sys.exit(1)

cnt = proc.stdout.strip()
print("\t".join(map(str, ["python.process.count", cnt, int(time.time())])))
