from flask import Flask,render_template,request,send_file
from face_search import get_info
import openpyxl
import os
app=Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("main.html")


@app.route("/download_excel",methods=['POST'])
def get_excel():
    if request.method == 'POST':
        
        # if 'video' not in request.files:
        #     return render_template('upload.html', message='No file part')

        video_file = request.files['video']

        # if video_file.filename == '':
        #     return render_template('upload.html', message='No selected file')

        if video_file:
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_file.filename)
            video_file.save(video_path)
    urls=get_info(video_path)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    count=0
    print(urls)
    for url in urls:
        count+=1
        colum=0
        for i in url:
            colum+=1
            print(i,colum,count)
            sheet.cell(row=count, column=colum, value=i)

    
    filename = 'example.xlsx'
    workbook.save(filename)

    return send_file(filename, as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)