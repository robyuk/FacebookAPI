import requests
import os
import json

def getgraph(token, id='me',fields=''):
  '''Returns a text string containing the fields from the facebook graph API'''
  url=f"https://graph.facebook.com/v14.0/{id}?fields={fields}&access_token={token}"
  return requests.get(url).text

#Must have a current session token
token=os.getenv("token")

#With id='me' and no fields, prints the User Name and ID
print(getgraph(token))

#This prints the user ID, Name, and all posts
#print(getgraph(token=token, #fields="id%2Cname%2Cposts"))
#exit(0)

#To get just one post, put the ID of the post in the url
id='10225265298997417_10208033512573526'
fields='id%2Cmessage'
print(getgraph(token=token, id=id, fields=fields))
#['posts']) #['data'][0]['message'])

# To get all the fields, set fields to null or remove the fields parameter from the url:
id='10225265298997417_10207621523194049'
fields=''
print(getgraph(token, id))
#
# To get a list of photos:
id='me/photos/uploaded'
#print(getgraph(token, id))

# Get a link to the page for a photo:
print(getgraph(token, id='10208033512013512',fields='link'),'\n')

# get the links to the image
text=getgraph(token, id='10208033512013512',fields='images')
#print(text)
# The response from the Facebook Graph API is a JSON text string.  To get a particular field we have to convert the string to a python type
data=json.loads(text)
#data is now a list of dicts, each dict containing a url to the image. 
imageUrl=data['images'][0]['source']
#So now we can download the actual image data
imageBytes=requests.get(imageUrl).content
#and write to a file
with open('image.jpg', 'wb') as file:
  file.write(imageBytes)