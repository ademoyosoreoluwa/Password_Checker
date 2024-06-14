from PIL import Image

base_width = 500
img = Image.open('/Users/eagleseyes/Desktop/web server/web server/static/assets/images/work1.png')
wpercent = (base_width / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)  # fixed syntax error here
img.save('/Users/eagleseyes/Desktop/web server/web server/static/assets/images/work-a.png')


# Equal Image size


from PIL import Image

base_width = 500
base_height = 500

img = Image.open('/Users/eagleseyes/Desktop/password checker.png')

wpercent = base_width / float(img.size[0])
hpercent = base_height / float(img.size[1])

if wpercent < hpercent:
    new_width = base_width
    new_height = int((float(img.size[1]) * float(wpercent)))
else:
    new_width = int((float(img.size[0]) * float(hpercent)))
    new_height = base_height

img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

img.save('/Users/eagleseyes/Desktop/web server/web server/static/assets/images/work-b.png')
