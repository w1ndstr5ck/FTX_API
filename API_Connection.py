import time
import hmac
from requests import Request

ts = int(time.time() * 1000)
request = Request('GET', '<api_endpoint>')
prepared = request.prepare()
signature_payload = f'{ts}{prepared.method}{prepared.path_url}'
if prepared.body:
    signature_payload += prepared.body
signature_payload = signature_payload.encode()
signature = hmac.new('uWvzGWbXJca5EKwqk8gq-geNnx8Jw6wqT2Q05CRK'.encode(), signature_payload, 'sha256').hexdigest()

request.headers['FTX-KEY'] = 'SkSSj9W6chZtWyqsJ7aqbUg0z8EWKuTQeDE8t5tU'
request.headers['FTX-SIGN'] = signature
request.headers['FTX-TS'] = str(ts)
