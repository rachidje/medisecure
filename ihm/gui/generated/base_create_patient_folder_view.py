# Form implementation generated from reading ui file 'ihm/gui/qt_designer_files/create_patient_folder_view.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(989, 554)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(30, 20, 941, 521))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.firstname_input = QtWidgets.QLineEdit(parent=self.widget)
        self.firstname_input.setObjectName("firstname_input")
        self.gridLayout.addWidget(self.firstname_input, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lastname_input = QtWidgets.QLineEdit(parent=self.widget)
        self.lastname_input.setObjectName("lastname_input")
        self.gridLayout.addWidget(self.lastname_input, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.email_input = QtWidgets.QLineEdit(parent=self.widget)
        self.email_input.setObjectName("email_input")
        self.gridLayout.addWidget(self.email_input, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.date_of_birth_input = QtWidgets.QDateEdit(parent=self.widget)
        self.date_of_birth_input.setObjectName("date_of_birth_input")
        self.gridLayout.addWidget(self.date_of_birth_input, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.consent_checkbox = QtWidgets.QCheckBox(parent=self.widget)
        self.consent_checkbox.setObjectName("consent_checkbox")
        self.gridLayout.addWidget(self.consent_checkbox, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.guardian_consent_checkbox = QtWidgets.QCheckBox(parent=self.widget)
        self.guardian_consent_checkbox.setObjectName("guardian_consent_checkbox")
        self.gridLayout.addWidget(self.guardian_consent_checkbox, 5, 1, 1, 1)
        self.create_folder_btn = QtWidgets.QPushButton(parent=self.widget)
        self.create_folder_btn.setObjectName("create_folder_btn")
        self.gridLayout.addWidget(self.create_folder_btn, 6, 2, 1, 1)
        self.cancel_create_folder_btn = QtWidgets.QPushButton(parent=self.widget)
        self.cancel_create_folder_btn.setObjectName("cancel_create_folder_btn")
        self.gridLayout.addWidget(self.cancel_create_folder_btn, 6, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Firstname"))
        self.label_2.setText(_translate("Form", "Lastname"))
        self.label_3.setText(_translate("Form", "Email"))
        self.label_4.setText(_translate("Form", "Date of birth"))
        self.label_5.setText(_translate("Form", "Consent"))
        self.consent_checkbox.setText(_translate("Form", "Consented"))
        self.label_6.setText(_translate("Form", "Guardian Consent"))
        self.guardian_consent_checkbox.setText(_translate("Form", "Consented"))
        self.create_folder_btn.setText(_translate("Form", "Create"))
        self.cancel_create_folder_btn.setText(_translate("Form", "Cancel"))
