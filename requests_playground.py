r = requests.get('https://api.github.com/events')
print(r.text)
print(r)
r = requests.get('http://httpbin.org/get')
print(r.headers['Access-Control-Allow-Credentials'])
print(r.headers['Access-Control-Allow-Origin'])
print(r.headers['CONNECTION'])
print(r.headers['content-length'])
print(r.headers['Content-Type'])
print(r.headers['Date'])
print(r.headers['server'])
print(r.headers['via'])


r = requests.get('http://httpbin.org/get')
print(r.headers['Access-Control-Allow-Credentials'])
print(r.headers['Access-Control-Allow-Origin'])
print(r.headers['CONNECTION'])
print(r.headers['content-length'])
print(r.headers['Content-Type'])
print(r.headers['Date'])
print(r.headers['server'])
print(r.headers['via'])


print(r)
print(r.text)
print(r.headers['Accept'])
print(r.headers)
print(r.headers['Server','Content-Length]])
print(r.headers['Server','Content-Length'])
print(r.headers['Server'])
response = r.json()
print(r.json())
print(response)
print(response['args'])
print(response['headers'])



payload = {'user_name': 'admin', 'password': 'password'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)>>> print(r.text)