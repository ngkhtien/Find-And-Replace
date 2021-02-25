"""Find and replace views name of selected sheet sets"""
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
form = FlexForm('Find And Replace View Name',component)
form.show()
find = form.values['textbox1']
replace = form.values['textbox2']
prompt = ''
count = 0
divide = "----------------------------------------------------"
t=Transaction(doc,"Find And Replace View Name")
t.Start()

for sheet in viewsheet:
    for eid in sheet.GetAllPlacedViews():
        ev=doc.GetElement(eid)
        custom_param=ev.Name
        if find in custom_param:
            custom_param=custom_param.replace(find, replace)
            ev.Name=custom_param
            number = sheet.LookupParameter("Sheet Number")
            name = sheet.LookupParameter("Sheet Name")
            count+=1
            prompt+= '\n' + ev.Title
            prompt+= '\n' + "Sheet " + number.AsString() + ': ' + name.AsString()
            prompt+= '\n' + divide

if count==0:
    prompt = 'No view found'
    print (prompt)
else:
    print ('Total views: ' + str(count))
    print (prompt)
t.Commit()

