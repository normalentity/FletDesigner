import json


def create_new_file (file_path:str):
    content = {
        "page_props": {
            "bgcolor": "black",
            "control_counter_number": 0
        },
        "widgets": {}
    }

    open(file_path, "w+", encoding="utf-8").write(json.dumps(content, indent=4))