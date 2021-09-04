import json
from os import name

schema_file = 'sample_schema.json'



def create_instruction_stack(instruction) : 
    return [instruction.strip() for instruction in instruction.split(">")] 

def get_model_object_command(sub_instruction) :

    model, obj = sub_instruction.split(":")
    return model.strip(), obj.strip()

def display_list(l, delimiter=", ") : 
    d_l  = [item["name"] for item in l]
    print(delimiter.join(d_l))
         


def find(model, obj, cursor) : 

    if type(cursor) == list :

        for i, c in enumerate(cursor) : 

            if obj=="" : 
                return c[model]

            else : 

                for o in c[model]: 
                    if o["name"] == obj: 
                        return o

    elif type(cursor) == dict : 
        return cursor[model]

    else : 
        raise ValueError("Could not ascertain this type {} for model {} object {}".format(type(cursor[model]), model, obj))

    raise ValueError("The given object {} could not be found.".format(obj))


def parse(instruction, delimiter=", ") : 

    instruction_stack = create_instruction_stack(instruction)
    print("instruction_stack : " , instruction_stack)

    with open(schema_file, 'r') as f:
        cursor = json.load(f)
    
    for sub_instruction in instruction_stack :

        print("working on sub_instruction: ", sub_instruction)

        model, obj =  get_model_object_command(sub_instruction)
        

        if obj == "" : 
            cursor = find(model, obj, cursor)
            display_list(cursor, delimiter)

        else : 

            cursor = find(model, obj, cursor)

if __name__ == "__main__": 

    instruction = "schemas:General Attack>steps:"
    parse(instruction, delimiter="\n")
    selected_step = input("Which step do you select? Please note, in some terminals you may need to wrap the option in quotes. \n")
    instruction += selected_step+">participants:"
    parse(instruction, delimiter=", ")

    









