import os
def gen_html(argv):
	if len(argv)<2:
		print 'please input the video path'
		return
	path = argv[1]
	top_n=5
	fds = [fd for fd in os.listdir(path) if os.path.isdir(os.path.join(path,fd))]
	title = path.split('/')[-1]
	#render head
	page = open('index.html','w')
	page.write('<hr><h2>%s</h2>' % title)
	for f in fds:
		page.write('<div style=\'border: 2px solid; width:166px; height:360px; display:inline-table\'>')
		page.write('<video width="162" height = "288" controls src=\'%s/%s/source.mp4\'></video><br> <hr><label>Source</label></div>' % (path,f))
		for i in xrange(top_n):
			page.write('<div style=\'border: 2px solid; width:166px; height:360px; display:inline-table\'>')		
			page.write('<video width = "162" height = "288" controls src = \'%s/%s/top%d.mp4\'> </video> <br> <hr> <label>top-%d</label></div>' % (path, f,i,i+1))
		page.write('<br>')
	page.write('<hr>')
	page.close()
if __name__ == '__main__':
	import sys
	gen_html(sys.argv)
