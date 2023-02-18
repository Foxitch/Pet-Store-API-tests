a = [{"id":1010,"category":{"id":0,"name":"sheep"},"name":"lamb","photoUrls":["kid"],"tags":[{"id":0,"name":"string"}],"status":"pending"},{"id":760,"category":{"id":0,"name":"<categoryname>"},"name":"man","photoUrls":["woman"],"tags":[{"id":0,"name":"<tag>"}],"status":"pending"}]



for obj in a:
    print(obj['status'])