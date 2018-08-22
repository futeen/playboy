from PIL import ImageGrab

'''
    get capture, the first two num is starting capturing point,
    the last two num is size of capture
'''
def capture():
    bbox = (760, 0, 1160, 1080)
    im = ImageGrab.grab(bbox)
    im.save('/Users/futeen/desktop/a.png')
    im.shwo()
