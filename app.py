
@application.route('upload.html',methods = ['POST'])
def upload_route_summary():
    if request.method == 'POST':
  # Create variable for uploaded file
     f = request.files['fileupload']
 #store the file contents as a string
     fstring = f.read()
 #create list of dictionaries keyed by header row
     csv_dicts = [{k: v for k, v in row.items()} for row in
     csv.DictReader(fstring.splitlines(), skipinitialspace=True)]
 #do something list of dictionaries
     return ("success")
