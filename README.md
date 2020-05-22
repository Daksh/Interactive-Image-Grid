# Interactive-Image-Grid
A python script, used to generate an interactive (image enlarges on mouse hover) image grid [HTML]

## Requirements
`python3`

## Steps
1. Put all the images in `images` directory
2. [Optional] Change the number of columns in the output grid, at [line 3 in the script](https://github.com/Daksh/Interactive-Image-Grid/blob/master/interactive_image_grid.py#L3)
3. Run `python3 interactive_image_grid.py`

The script generates two HTML files `image_grid_web.html`, `image_grid.html`. The first one, loads the data from this repository, and can be shared with anyone (without them having to save all the images locally). The second one loads faster, but needs the `images` directory present where the HTML file is.

NOTE: For you to use the `image_grid_web.html` file properly, you need to change [Line 91](https://github.com/Daksh/Interactive-Image-Grid/blob/master/interactive_image_grid.py#L91), and add the prefix URL where all your images are hosted :)

In our sample, we have taken the images from <https://www.kaggle.com/xhlulu/flickrfaceshq-dataset-nvidia-resized-256px> dataset.

## Demo Output
![](https://github.com/Daksh/Interactive-Image-Grid/raw/master/demo.gif)
