# # from Tkinter import *
# # from Tkinter import Tk, Label, BOTH
# # from PIL import Image, ImageTk
# #
# #
# # from ttk import Frame, Style
# #
# # root = Tk()
# #
# # m1 = PanedWindow(root)
# # m1.pack(fill=BOTH, expand=1)
# #
# # opp_name = Label(m1, text="Operator Name :")
# # opp_value = Label(m1, text=" Saloni")
# #
# # app_name = Label(m1, text="Application Name :")
# # app_value = Label(m1, text=" BIocon")
# #
# # site_name = Label(m1, text="Site Name :")
# # site_value = Label(m1, text=" Sector 1")
# #
# # opp_name.pack()
# # opp_value.pack()
# # app_name.pack()
# # app_value.pack()
# # site_name.pack()
# # site_value.pack()
# #
# # Style().configure("TFrame", background="#333")
# #
# # bard = Image.open("/Users/salonibindra/Desktop/download.jpeg")
# # bardejov = ImageTk.PhotoImage(bard)
# # bardejov.pack()
# #
# # #label1 = Label( image=bardejov)
# # # label1.image = bardejov
# # # label1.place(x=20, y=20)
# # #
# # # m1.add(opp_name)
# # # m1.add(opp_value)
# # # m1.add(app_name)
# # # m1.add(app_value)
# # # m1.add(site_name)
# # # m1.add(site_value)
# # #
# # # m2 = PanedWindow(m1, orient=VERTICAL)
# # # m1.add(m2)
# # #
# # # top = Label(m2, text="top pane")
# # # m2.add(top)
# # #
# # # bottom = Label(m2, text="bottom pane")
# # # m2.add(bottom)
# #
# # root.geometry("500x150")
# # #m1.winfo_geometry(500)
# # mainloop()
#
#
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import mlab
# import Pyclustering as pc
# from sklearn.cluster import KMeans
#
#
# # make fake user data
# users = np.random.normal(0, 10, (20, 5))
#
# # cluster
# clusterid, error, nfound = pc.kcluster(users, nclusters=3, transpose=0,
#                                        npass=10, method='a', dist='e')
# centroids, _ = pc.clustercentroids(users, clusterid=clusterid)
#
# # reduce dimensionality
# users_pca = mlab.PCA(users)
# cutoff = users_pca.fracs[1]
# users_2d = users_pca.project(users, minfrac=cutoff)
# centroids_2d = users_pca.project(centroids, minfrac=cutoff)
#
# # make a plot
# colors = ['red', 'green', 'blue']
# plt.figure()
# plt.xlim([users_2d[:,0].min() - .5, users_2d[:,0].max() + .5])
# plt.ylim([users_2d[:,1].min() - .5, users_2d[:,1].max() + .5])
# plt.xticks([], []); plt.yticks([], []) # numbers aren't meaningful
#
# show the centroids
# plt.scatter(centroids_2d[:,0], centroids_2d[:,1], marker='o', c=colors, s=100)
#
# # show user numbers, colored by their cluster id
# for i, ((x,y), kls) in enumerate(zip(users_2d, clusterid)):
#     plt.annotate(str(i), xy=(x,y), xytext=(0,0), textcoords='offset points',
#                  color=colors[kls])
#
import Tkinter
from Tkinter import Tk
tk=Tk()
from tkFileDialog import askopenfilenames
import tkMessageBox
tk.withdraw()
from tkinter.filedialog import askopenfilename


def fileupload():
    while True:
        uploadedfilenames = askopenfilenames(multiple=True)
        if uploadedfilenames == '':
            tkMessageBox.showinfo(message="File Upload has been cancelled program will stop")
            return
        uploadedfiles = tk.splitlist(uploadedfilenames)
        return uploadedfiles

print (fileupload())

#fileupload()


name = askopenfilename( title = "Choose a file.")
print (name)
#name = "('/Users/salonibindra/Desktop/images.gif',)"
name = name.strip("(,',)")
print (name)


print("how to make tkinter speak to ")