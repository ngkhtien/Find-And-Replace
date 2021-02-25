"""Find and replace sheets name of selected sheet sets"""
__author__='NguyenKhanhTien - khtien0107@gmail.com'
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction
from rpw.ui.forms import TextInput, FlexForm, Label, ComboBox, TextBox,\
                         TaskDialog, Separator, Button, CheckBox
from pyrevit import revit, DB
from pyrevit import forms

doc = __revit__.ActiveUIDocument.Document

viewsheet = forms.select_sheets(button_name='Select Sheet Set')

component = [Label('Find:'),
                TextBox('textbox1', Text=""),
                Label('Replace:'),
                TextBox('textbox2', Text=""),
                Separator(),
                Label('Nguyen Khanh Tien - khtien0107@gmail.com'),
                Button('Select')]
form = FlexForm('Find And Replace Sheet Name',component)
form.show()
find = form.values['textbox1']
replace = form.values['textbox2']
prompt = ''
count = 0
t=Transaction(doc,"Find And Replace Sheet Name")
t.Start()

for sheet in viewsheet:
    custom_param=sheet.LookupParameter("Sheet Name")
    if find in custom_param.AsString():
       custom_param.Set(custom_param.AsString().replace(find, replace))
       number = sheet.LookupParameter("Sheet Number")
       count+=1
       prompt+= '\n' + "Sheet "+  number.AsString() + ': ' + custom_param.AsString() 

if count==0:
    prompt = 'No sheet found'
    print (prompt)
else:
    print ('Total sheets: ' + str(count))
    print (prompt)
t.Commit()

