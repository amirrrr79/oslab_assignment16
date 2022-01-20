import sqlite3
from PySide6.QtCore import*
from PySide6.QtWidgets import*
from PySide6.QtGui import*
from PySide6.QtUiTools import*

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader=QUiLoader()
        self.ui=loader.load('untitled.ui')
        self.ui.show()
        self.conn=sqlite3.connect('my sql.db')
        self.my_cursor=self.conn.cursor()
        self.id=0
        self.load_data()
        self.ui.add_btn.clicked.connect(self.add)
        self.ui.delete_btn.clicked.connect(self.delete_all)
        self.ui.delete_btn_2.clicked.connect(self.delete)
           
    def load_data(self):
        self.my_cursor.execute('SELECT * FROM Person')
        result= self.my_cursor.fetchall() 
        for item in result:
            label=QLabel() 
            label.setText(str(item[0])+'-'+item[1]+' '+str(item[2])+' : '+str(item[4])+' ___ '+str(item[5]))
            self.ui.verticalLayout.addWidget(label)
    
    def add(self):
        name=self.ui.lineEdit.text()
        family=self.ui.lineEdit_2.text()
        mobile_number=self.ui.lineEdit_3.text()
        email=self.ui.lineEdit_4.text()  
        self.id +=1
        self.my_cursor.execute(f"INSERT INTO Person(id,name,family,mobile_number,email) VALUES('{self.id}','{name}','{family}','{mobile_number}','{email}')")
        self.conn.commit()
        label=QLabel()
        label.setText(str(self.id)+'-'+name+' '+str(family)+' : '+str(mobile_number)+' ___ '+str(email))
        self.ui.verticalLayout.addWidget(label)
    
    def delete_all(self):
            self.my_cursor.execute('DELETE FROM Person')
            self.conn.commit()
            for i in range(self.ui.verticalLayout.count()):
                self.ui.verticalLayout.itemAt(i).widget().deleteLater()
    
    def delete(self):
        name=self.ui.lineEdit_5.text()
        self.my_cursor.execute(f"DELETE FROM Person WHERE name =='{name}'")
        self.conn.commit()
        for i in range(self.ui.verticalLayout.count()):
              self.ui.verticalLayout.itemAt(i).widget().deleteLater()
        self.load_data()      
        
        
app=QApplication()
main_window=mainwindow()
app.exec()        



