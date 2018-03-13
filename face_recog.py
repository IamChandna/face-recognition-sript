from urllib2 import Request, urlopen
import json

values = """
    {
     "image":"http://www.newscrab.com/wp-content/uploads/2017/11/ranveer-singh_148231652900.jpg",
     "subject_id" :"ranveer",
     "gallery_name":"gallery"
    }
"""

headers = {
    'Content-Type': 'application/json',
    'app_id': '6042f5ee',
    'app_key': 'a5820104fd5a6648672cc2a1e55ab403'
}
#register
request=Request('https://api.kairos.com/enroll',data=values,headers=headers)
rb = urlopen(request).read()
rb = json.loads(rb)
print rb
#print type(rb)
print rb['face_id']
print "Age: "+str(rb['images'][0]['attributes']['age'])
print "Status: "+str(rb['images'][0]['attributes']['gender']['type'])
print "Height: "+str(rb['images'][0]['transaction']['height'])


