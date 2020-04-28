# this is probably the best way to make gui, because each option should have its own setting
import json

fp = open("options.js", "r")
options = fp.read()
fp.close()
options = options[options.find('{'):options.find('}')+1]
options = json.loads(options)

html = ""
keys = list(options.keys())
i = 0
while i != len(keys):
    key = keys[i]
    #print(key + ": " + str(options[key]))
    if type(options[key]) == int or type(options[key]) == float:
        html += "<div id=\"option" + str(i+1) + "\">\n\t<p>" + key + "</p>\n\t"
        init_val = options[key]
        print("what would you like to do with key value \"" + key + "\"?")
        print("""
options: 
1: range slider
2: textbox input for numbers
""")
        num = input("> ")
        if num.isnumeric:
            num = int(num)
            if num == 1: # range slider
                min = input("min value? > ")
                max = input("max value? > ")
                change_val = input("change initial value? (y/n): ")
                # if an empty string both if statements will fail
                if change_val:
                    change_val = change_val[0].lower() == "y"
                # if n is given this if statement will fail
                if change_val:
                    init_val = input("initial value: > ")
                html += '<input type="range" min="'+min+'" max="'+max+'" value="'+str(init_val)+'" class="slider" id="slider'+str(i+1)+'">\n'
            else: # textbox input for numbers
                print("not implemented yet...")
            html += "</div>\n"
        else:
            print("error! should be a number.")
    else:
        print("this option is an invalid type: " + type(options[key]))
        i -= 1
    i += 1
    fp = open("render.html", "w")
    fp.write(html)
    fp.close()
