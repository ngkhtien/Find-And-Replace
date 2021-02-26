"""Find and replace rooms name in project"""
__author__='NguyenKhanhTien - khtien0107@gmail.com'
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction
from rpw.ui.forms import TextInput, FlexForm, Label, ComboBox, TextBox,\
                         TaskDialog, Separator, Button, CheckBox
from pyrevit import revit, DB
from pyrevit import forms

doc = __revit__.ActiveUIDocument.Document

#viewsheet = forms.select_sheets(button_name='Select Sheet Set')
rooms= FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms)\
                    .WhereElementIsNotElementType()\
                    .ToElements()

component = [Label('Find:'),
                TextBox('textbox1', Text=""),
                Label('Replace:'),
                TextBox('textbox2', Text=""),
                Separator(),
                Label('Nguyen Khanh Tien - khtien0107@gmail.com'),
                Button('Select')]
form = FlexForm('Find And Replace Room Name',component)
form.show()
find = form.values['textbox1']
replace = form.values['textbox2']
prompt = ''
count = 0
divide = " -- "
t=Transaction(doc,"Find And Replace Room Name")
t.Start()

for room in rooms:
    custom_param=room.LookupParameter("Name")
    tam=custom_param.AsString()
    if find in custom_param.AsString():
       custom_param.Set(custom_param.AsString().replace(find, replace))
       #number = sheet.LookupParameter("Sheet Number")
       count+=1
       prompt+= '\n' + tam + divide + custom_param.AsString()
       #prompt+= '\n' + "Sheet "+  number.AsString() + ': ' + custom_param.AsString() 

if count==0:
    prompt = 'No room found'
    print (prompt)
else:
    print ('Total rooms: ' + str(count))
    print (prompt)
t.Commit()

