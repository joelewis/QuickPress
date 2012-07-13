import sys
from lxml import etree
from PyQt4 import QtCore, QtGui
from post import Ui_MainWindow
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
data = etree.parse("config.xml")
user = data.find("user").text
url = data.find("url").text
pwd = data.find("pass").text
class MyApp(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
                QtCore.QObject.connect(self.ui.postbutton,QtCore.SIGNAL("clicked()"), self.post)
	def post(self):
                wp = Client(url+"/xmlrpc.php", user, pwd)
		post = WordPressPost()
		post.content = str(self.ui.BodyEdit.toPlainText())
		post.title = str(self.ui.TitleEdit.text())
                post.post_status = 'publish'
		wp.call(NewPost(post))	
                self.ui.label.setText("Published") 

                                 
                
             
if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	myapp = MyApp()
	myapp.show()
	sys.exit(app.exec_())
