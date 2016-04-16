import os
def gen_html(argv):
	if len(argv)<4:
		print 'please input the base dir and two video path'
		return
	#path=[]
	sub_fds = argv[2:4]
	base_dir = argv[1]
	
	top_n=5
	col_name = ('googlenet','c3d')
	path = []
	path.append(base_dir + '/' + sub_fds[0])
	path.append(base_dir + '/' + sub_fds[1])
	fds = [fd for fd in os.listdir(path[0]) if os.path.isdir(os.path.join(path[0],fd))]
	#title = path.split('/')[-1]
	#render head
	split=5
	per_page = len(fds)/split+1
	for p in xrange(split):
		start = p*per_page
		final = min((p+1)*per_page,len(fds))
		page = open(base_dir+'/r'+str(p)+'.html','w')
		page.write('<hr><h2>Comparison of %s and %s</h2>' % col_name)
		for f in fds[start:final]:
			page.write('<div style=\'border: 2px solid; width:166px; height:360px; display:inline-table\'>')
			page.write('<video width="162" height = "288" controls src=\'%s/%s/source.mp4\'></video><br> <hr><label>Source</label></div>' % (sub_fds[0],f))
			
			for i in xrange(top_n):
				page.write('<div style=\'border: 2px solid; width:166px; height:360px; display:inline-table\'>')		
				page.write('<video width = "162" height = "288" controls src = \'%s/%s/top%d.mp4\'> </video> <br> <hr> <label>%s top-%d</label></div>' % (sub_fds[0], f,i,col_name[0], i+1))
			page.write('<br>')

			page.write('<div style=\'border: 2px solid; width:166px; height:360px; display:inline-table\'></div>')
			
			for i in xrange(top_n):
				page.write('<div style=\'border: 2px solid; width:166px; height:360px; display:inline-table\'>')		
				page.write('<video width = "162" height = "288" controls src = \'%s/%s/top%d.mp4\'> </video> <br> <hr> <label>%s top-%d</label></div>' % (sub_fds[1], f,i,col_name[1], i+1))
			page.write('<br>')

		page.write('<hr>')
		page.close()
if __name__ == '__main__':
	import sys
	gen_html(sys.argv)
