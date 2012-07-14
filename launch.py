import sys
from PyQt4 import QtCore, QtGui, QtNetwork
from post import Ui_MainWindow

class MyApp(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
                self.ui.label.setText("Status...")
                QtCore.QObject.connect(self.ui.postbutton,QtCore.SIGNAL("clicked()"), self.post)
	def post(self):    
                from lxml import etree
		try:
                  self.ui.label.setText("Importing necessary modules...")
                  from wordpress_xmlrpc import Client, WordPressPost
                  status = 1  		
                except:
                  status = 0
                if(status==1):
                  from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
		  from wordpress_xmlrpc.methods.users import GetUserInfo
                  self.ui.label.setText("Imported modules...")
		  data = etree.parse("config.xml")
		  user = data.find("user").text	
		  url = data.find("url").text
		  pwd = data.find("pass").text
                  self.ui.label.setText("Imported data...")
                  try:  
                    wp = Client(url+"/xmlrpc.php", user, pwd)
	            	  
                  except:
                    status = 0
                  if (status == 1):  
                    post = WordPressPost()
		    post.content = str(self.ui.BodyEdit.toPlainText())
		    post.title = str(self.ui.TitleEdit.text())
                    post.content = post.content + "<br><small><i>via QuickPress</i></small></br>"
                    post.post_status = 'publish'
		    wp.call(NewPost(post))	
                    self.ui.label.setText("Published") 
                  else:
                    self.ui.label.setText("Check Internet Connection and try again...")
                else:
		  self.ui.label.setText("module(wordpress_xmlrpc) not found, you can install manually from terminal using pip install python-wordpress-xmlrpc")                
                                 
                
             
if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	myapp = MyApp()
	myapp.show()
	sys.exit(app.exec_())
