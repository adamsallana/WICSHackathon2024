

from distutils.log import debug 
from fileinput import filename 
# from flask_ngrok import run_with_ngrok 
from flask import *  


app = Flask(__name__)   


# #home page 
# @app.route('/')   
# def main():   
#     return render_template("index.html")   

#user email
@app.route('/', methods=['GET', 'POST'])   

def upload():   
    render_template("frontPage.html")
    if request.method == 'POST':
        # Then get the data from the form
            email = request.form['email']

            #MAKE SURE USER EMAIL ENDS IN EDU?

            # Generate just a boring response
            return render_template("PRODUCTPAGE")


    else:   
        return render_template('frontPage.html')


#which product do they need
@app.route('/whichproduct')   
def upload():   
    return render_template("HTMLHERE") 

#how many items
@app.route('/quantity')   
def upload():   
    return render_template("HTMLHERE") 

#timeline page
@app.route('/timeline')   
def upload():   
    return render_template("HTMLHERE") 

#user information
@app.route('/userinfo')   
def upload():   
    return render_template("HTMLHERE") 


#educational resources
@app.route('/education resources')   
def upload():   
    return render_template("HTMLHERE") 



# @app.route('/success', methods = ['POST'])   
# def success():   
#     if request.method == 'POST':   
#         f = request.files['file'] 
#         f.save('documents/'+f.filename)   
#         return render_template("totesdidit.html", name = f.filename)   

# import os


# # def results():   
# #         folderPath = r"C:\Users\Allana\Dev\PearlHacks24\PearlHacks24\PearlHacks24-1\documents"
# #         documentsList = []
# #         for x in os.scandir(folderPath):
# #              documentsList.append[x.name]
# #         return render_template("searchnotes-res.html", names = documentsList)   


# @app.route('/search')   
# def getFiles():
#     # folderPath = r"C:\Users\Allana\PearlHacks24\documents"
#     folderPath = r"./documents"
#     def fObjFromScan(x):
#         # return file information for rendering
        
#         return {'name': x.name,
#                 'relPath': os.path.relpath(x.path, folderPath).replace("\\", "/")}
#     fileObjs = [fObjFromScan(x) for x in os.scandir(folderPath)]

#     return render_template('searchnotes-res.html', data={'files': fileObjs})

# from flask import make_response

# # @app.route('/reports/', defaults={'reqPath': ''})
# # @app.route('/reports/<path:reqPath>')
# # def getFiles(reqPath):
#     # Join the base and the requested path
#     # could have done os.path.join, but safe_join ensures that files are not fetched from parent folders of the base folder
#     # absPath = safe_join(FolderPath, reqPath)

#     # # Return 404 if path doesn't exist
#     # if not os.path.exists(absPath):
#     #     return abort(404)

#     # # Check if path is a file and serve
#     # if os.path.isfile(absPath):
#     #     return send_file(absPath)

# # @app.route('/getPdf/<path:reqPath>')
# # # @app.route('/search/<id>')
# # def get_pdf(reqPath=None):
# #     if reqPath is not None:
# #         # fileName =  reqPath
# #         folderPath = r"C:\Users\Allana\PearlHacks24\documents"
# #         data = open(folderPath + "\\" + reqPath)
# #         # data = get_binary_pdf_data_from_database(id=id)
# #         response = make_response(data)
# #         response.headers['Content-Type'] = 'application/pdf'
# #         response.headers['Content-Disposition'] = \
# #             'inline; filename=%s.pdf' % 'yourfilename'
# #         return response


if __name__ == '__main__':   
    app.run(debug=True)

