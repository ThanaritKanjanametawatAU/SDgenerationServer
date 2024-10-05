# ''' A template for a handler file. '''

# import runpod

# def handler(job):
#     '''
#     This is the handler function for the job.
#     '''
#     job_input = job['input']
#     name = job_input.get('name', 'World')
#     return f"Hello, {name}!"

# runpod.serverless.start({"handler": handler})

import runpod
import requests

def get_my_ip(job):
    response = requests.get('https://httpbin.org/ip')
    return f"Your public IP address is: {response.json()['origin']}"


runpod.serverless.start({"handler": get_my_ip})