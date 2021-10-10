import numpy as np
import matplotlib.pyplot as plt
import glob
from PIL import Image

""" x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)
x4 = np.random.uniform(14,20, 10000)

x = [x1, x2, x3, x4]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey = True)

ax = [ax1, ax2, ax3, ax4]

axis1 = [-7.5, 2.5, 0, 0.6]
axis2 = [0, 10, 0, 0.6]
axis3 = [7, 17, 0, 0.6]
axis4 = [12, 22, 0, 0.6]
axis = [axis1, axis2, axis3, axis4]

bins1 = np.arange(-7.5, 2.5, 0.2)
bins2 = np.arange(0, 10, 0.2)
bins3 = np.arange(7, 17, 0.2)
bins4 = np.arange(12, 22, 0.2)
bins = [bins1, bins2, bins3, bins4]

titles = ['x1 Normal', 'x2 Gamma', 'x3 Exponential', 'x4 Normed Frequency']
color = ['#b5ef10', '#1b0045', '#cc0000', '#333333']

for i in range(len(ax)):
	#ax[i].cla()
	ax[i].hist(x[i],  density= True, bins = bins[i], color = color[i])
	ax[i].axis(axis[i])
	ax[i].set_title(titles[i])
	ax[i].set_ylabel('Normed Frequency')
	ax[i].set_xlabel('Value')
	plt.tight_layout()

	plt.savefig("/home/sebastian/Dev/python-exercises/hackerrank/d_fotos_armenia/%s.png" % (titles[i]))
 """
#--------- CREATE GIF ---------
imgs = glob.glob("/home/sebastian/Dev/python-exercises/hackerrank/d_fotos_armenia/*x*.jpeg")#Save all imagen in file
# Create the framesso
imgs.sort(key=lambda s: s[-6])
#imgsorted = sorted(imgs, key=lambda s: s[-6])
frames = []
#imgs = glob.glob("/mnt/d/SebasUbuntu/Documentos/Graficas/*x*.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

 
# Save into a GIF file that loops forever
frames[0].save('/home/sebastian/Dev/python-exercises/hackerrank/d_fotos_armenia/d.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=1000, loop=0)
