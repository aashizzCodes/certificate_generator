# public imports
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from docxtpl import DocxTemplate
from pathlib import Path
import datetime
import uuid


app = FastAPI()
template = DocxTemplate(Path(r'template\template.docx'))

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=['*'],
                   allow_headers=['*'])



# function to recive data from the client 
# trigger function
@app.post('/send')
async def recive(data:dict):
    # save the data into new varible
    recived_data = data
    # construct the data for template 
    changes = _construct_data(recived_data)
    # render the template
    file_path = render_template(changes)


# function to create an file name
# format:  roll_uuid
def _get_file_name(roll:str) -> str:
    return str(f'{roll}_{uuid.uuid4().hex[:8]}')


# function to construct data --helper Function
def _construct_data(datas:dict) -> dict:

    # make an dict for detilals to change in template from the data recived
    changes = {
        "full_name": str(datas['first_name'] + ' ' + datas['middle_name'] + ' ' + datas['surname']),
        "subject":str(datas['selected_subject']),
        "roll_number":str(datas['roll_number']),
        "teacher":None,
        "name_surname":str(datas['first_name'] + ' ' + datas['surname']),
    }
    return changes
    

# function to render the template
def render_template(render_params) -> Path:

    # render the template using the parms
    template.render(render_params)
    # get file name as na path object 
    file_name = Path(r'output' ) / f"{_get_file_name(render_params['roll_number'])}.docx"
    # save the rendered file
    template.save(file_name)
    # return the file path
    return file_name


# function to convert the docx file to pdf
# def convert_file(path:Path) -> Path:
    # return  

# function to collect the data from the client
def collect_data(data:dict):

    # open the file
    file = Path(r'backend\students.json')

    with open(file ,'r') as read_file:
        collected_data = json.load(read_file)
     
    
    