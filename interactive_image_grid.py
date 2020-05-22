import os

NUM_COL = 50
img_names = set()

# remove the files with file size below 100 bytes
for fn in os.listdir('images'):
	fn = os.path.join('images',fn)
	if os.path.getsize(fn)>100:
		img_names.add(fn)

print("Non Empty images:",len(img_names))
print("Total images:",len(os.listdir('images')))

html_pre_text = """<!DOCTYPE html>
<html>
<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Arial;
}

.header {
  text-align: center;
  padding: 32px;
}

.row {
  display: -ms-flexbox; /* IE10 */
  display: flex;
  -ms-flex-wrap: wrap; /* IE10 */
  flex-wrap: wrap;
  padding: 0 0px;
}

/* Create four equal columns that sits next to each other */
.column {
  -ms-flex: 25%; /* IE10 */
  flex: 25%;
  max-width: 25%;
  padding: 0 0px;
}

.column img {
  margin-top: 0px;
  vertical-align: middle;
  width: 100%;
}

img:hover {
  transform: scale(3); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
}

/* Responsive layout - makes a two column-layout instead of four columns */
@media screen and (max-width: 800px) {
  .column {
	-ms-flex: 50%;
	flex: 50%;
	max-width: 50%;
  }
}

/* Responsive layout - makes the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 600px) {
  .column {
	-ms-flex: 100%;
	flex: 100%;
	max-width: 100%;
  }
}
</style>
<body>

<!-- Photo Grid -->
<div class="row"> 
"""

new_p = str(1/NUM_COL * 100)+'%'
html_pre_text = html_pre_text.replace('25%',new_p)

html_post_text="""</div>

</body>
</html>
"""

for url,suffix in [('<img src="https://raw.githubusercontent.com/Daksh/Interactive-Image-Grid/master/','_web'),('<img src="','')]:
	html_mid_text = ""
	img_names = list(img_names)
	for col in range(NUM_COL):
		html_mid_text = html_mid_text + '  <div class="column">\n'
		for row in range(NUM_COL):
			if col*NUM_COL + row < len(img_names):
				html_mid_text = html_mid_text +url+img_names[col*NUM_COL + row]+'" style="width:100%" loading="lazy">\n'
		html_mid_text = html_mid_text + '  </div>\n'
	with open("output/image_grid"+suffix+".html",'w') as f:
		f.write(html_pre_text)
		f.write(html_mid_text)
		f.write(html_post_text)

## References
# 1. https://www.w3schools.com/howto/howto_css_image_grid_responsive.asp
