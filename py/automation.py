import pyautogui as gui


def open_file(path):

    with open(path) as f:
        l = f.readlines()

    return l


def sai_define_tools(tools_path):
    
    tools_u_v = open_file(tools_path)
    # print(tools_u_v)

    tools_memory = []

    for i in range(len(tools_u_v)):
        item = str(tools_u_v[i])
        item_rm = item.replace('\n', '')
        
        # print(item_rm)
        tools_memory.append(item_rm)
    
    return tools_memory


def sai_define_pos(pos_path):

    pos_u_v = open_file(pos_path)
    # print(pos_u_v)

    pos_memory = []

    for i in range(len(pos_u_v)):
        item = str(pos_u_v[i])
        item_rm = item.replace('\n', '')
        
        # print(item_rm)
        pos_memory.append(item_rm)
    
    return pos_memory


def click_tool(tools_list):

    # print(gui.size())

    for i in range(len(tools_list)):
        tmp_t = tools_list[i]

        if "uv_tool" in tmp_t:

            # print(tmp)
            tmp_t_sp = tmp_t.split(",")
            n_t, u_t, v_t = tmp_t_sp

            # print(int(u_t), int(v_t))
            # gui.moveTo(1, 1)
            # gui.move(100, 100) 
            gui.moveTo(int(u_t), int(v_t))
            gui.click(int(u_t), int(v_t))

            print(int(u_t), int(v_t))
            # print(gui.position())


            ### Magic Number (MBP 13)
            # magic_number = [625, 115]
            # gui.moveTo(magic_number[0], magic_number[1])
            # gui.click()


            print("Select Pen Tool")




def click_color(tools_list, color_id):

    for i in range(len(tools_list)):
        tmp_c = tools_list[i]

        set_clr = "uv_color_{}".format(color_id)

        if set_clr in tmp_c:
            # print(tmp)
            tmp_c_sp = tmp_c.split(",")
            n_c, u_c, v_c = tmp_c_sp

            # print(u_c, v_c)
            
            gui.moveTo(int(u_c), int(v_c))
            gui.click()

            print("Set Color")



def draw_line(tools_list, pos_list):

    ### Operate Pos List
    c_pos = pos_list.split(",")

    ### Select Pen Tool
    click_tool(tools_list)

    ### Select Color
    click_color(tools_list, c_pos[0])
    print(c_pos[0])


    ### Draw Line
    print("Draw Curve")

    count = int((len(c_pos) - 1) * 0.5)
    # print(count)

    for i in range(count):
        uu = c_pos[(i*2) + 1]
        vv = c_pos[(i*2) + 2]

        
        gui.moveTo(int(uu), int(vv))
        gui.click()

        # print(uu, vv)
        # print(gui.position())

    gui.press(keys = "Enter")


def draw_lines(tools_list, pos_list):

    yn_tool = input("Tool Position ok? (y/n) :")
    if yn_tool == "y" or "Y":

        for i in range(len(pos_list)):

            if i == 0:
                draw_line(tools_list, pos_list[i])

            else:
                yn_c = input("Continue? (y/n) :")
                if yn_c == "y" or "Y":
                    draw_line(tools_list, pos_list[i])


def run():

    print("Tajima Automation Tool (ver0)\n\n")

    ### Input Date
    # tools_path = input("TOOLS : ")
    # tools_path = r"C:\Users\yoshioca\Documents\Tajima_Sai_Automation\data\tools.txt"
    tools_path = r"C:\Users\ysoky\Documents\Tajima_Sai_Automation\data\tools.txt"
    
    # pos_path = input("POS : ")
    # pos_path = r"C:\Users\yoshioca\Documents\Tajima_Sai_Automation\data\pos_1.txt"
    pos_path = r"C:\Users\ysoky\Documents\Tajima_Sai_Automation\data\pos_1.txt"

    

    ### file to memory
    tools_list = sai_define_tools(tools_path)
    pos_list = sai_define_pos(pos_path)
    # print(tools_list)
    # print(pos_list)

    ### Test
    click_tool(tools_list)
    # click_color(tools_list, 7)
    # draw_line(tools_list, pos_list[1])

    draw_lines(tools_list, pos_list)



run()

