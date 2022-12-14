try:
    import urllib.request as urllib
except ImportError:
    import urllib
import io
import zipfile

import matplotlib.pyplot as plt 
import networkx as nx

url = "http://www-personal.umich.edu/~mejn/netdata/football.zip"

sock = urllib.urlopen(url)# open URL
s = io.BytesIO(sock.read()) # read into BytesIO "file"
sock.close()

zf = zipfile.ZipFile(s) # zipfile object
txt = zf.read('football.txt').decode()  # read info file
gml = zf.read('football.gml').decode()  # read gml data
# throw away bogus first line with # from mejn files
gml = gml.split('\n')[1:]
G = nx.parse_gml(gml)   # parse gml data

print(txt)
# print degree for each team - number of games
for n, d in G.degree():
    print('%s %d' % (n, d))

options = {
    'node_color': 'black',
    'node_size': 50,
    'line_color': 'grey',
    'linewidths': 0,
    'width': 0.1,
}

nx.draw(G, **options)
plt.show()