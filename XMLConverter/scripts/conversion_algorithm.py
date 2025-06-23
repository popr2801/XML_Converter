import os,sys

if getattr(sys,'frozen',False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

index_xml_path = os.path.join(base_path,"assets","index.xml")
invoice_xml_path = os.path.join(base_path,"assets","invoiceLine.xml")

def find_word(file_path):
    dict = {}
    with open(file_path,"r",encoding = "utf-8") as file:
        lines = file.readlines()
        for line_num,line in enumerate(lines,1):
                if "=" in line:
                    results = line.split("=")
                    dict[results[0].strip()] = results[1].strip()
    return dict

def invoice_line(id,name,tax,price,amount,total):
    with open(invoice_xml_path,"r",encoding="utf-8") as base:
        content = base.read()
        content = content.replace("tax",tax)
        content = content.replace("total",total)
        content = content.replace("price",price)
        content = content.replace("name",name)
        content = content.replace("amount",amount)
        content = content.replace("id",id)
        
    return content

def read_table(file_path):
    print(f"Trying to open file {file_path}")
    with open(file_path,"r",encoding="utf-8") as text:
        content = text.read()
        parts = content.split("_TotalHT_")
        content = parts[1]
        parts = content.split("For")
        content = parts[0]
    return "\n".join([line for line in content.splitlines() if line.strip()])


def select_data_from_chunks(string):
    result = ""
    lines = string.splitlines()
    index = 1
    for i in range(0,len(lines)-5,5):
        result += invoice_line(str(index),lines[i],lines[i+1],lines[i+2],lines[i+3],lines[i+4])
        index+=1
    return result

def convert_file(file_to_convert,destination):
    dict = find_word(file_to_convert)
    with open(index_xml_path,"r",encoding="utf-8") as xmlfile,open(destination,"w",encoding="utf-8") as results:
        content = xmlfile.read()
        content = content.replace("object_date_creation",dict["object_date_creation"])
        content = content.replace("object_date_limit",dict["object_date_limit"])
        for key,value in dict.items():
            if key in content:
                content = content.replace(key,value)
        content = content.replace("invoiceline",select_data_from_chunks(read_table(file_to_convert)))
        results.write(content)
