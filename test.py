import httplib,os

requrl = "https://n.cg.163.com/api/v2/sign-today"
headerdata = {"Authorization":os.environ["cg163_data"]}

conn = httplib.HTTPConnection("n.cg.163.com")

conn.request(method="POST",url=requrl,body="",headers = headerdata)

response = conn.getresponse()

res= response.read()

print res