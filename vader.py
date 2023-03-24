import requests
import os
import logging
import time
import subprocess
import sys

logger = logging.getLogger('vader')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def main():
    while True:
        logger.info('Querying for a job')
        res = requests.get('http://127.0.0.1:8000/api/jobs/next/')
        if not res.ok:
            logger.info('No available jobs, retrying in 10sec')
            time.sleep(10)
            continue

        job = res.json()
        logger.info('Starting job: %s', job['id'])
        script = job['script']
        proc = subprocess.run(['/bin/bash', '-c', script])
        logger.info('Job completed with exit code: %d', proc.returncode)
        requests.put(f'http://127.0.0.1:8000/api/jobs/{job["id"]}', json=job | {"status" : "done"})

if __name__=='__main__':
    main()