from PIL import Image

base_width = 500
img = Image.open('/Users/eagleseyes/Desktop/web server/web server/static/assets/images/work1.png')
wpercent = (base_width / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)  # fixed syntax error here
img.save('/Users/eagleseyes/Desktop/web server/web server/static/assets/images/work-a.png')