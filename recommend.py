from data import *
from linkedlist import LinkedList

##write code to insert style periods into a linked list from data.py
def insert_style_periods():
    style_period_list = LinkedList()
    for period in style_periods:
        style_period_list.insert_beginning(period)
    return style_period_list

##write code to insert composer data into a linked list of linked lists
def insert_composer_data():
    composer_data_list = LinkedList()
    for period in style_periods:
        composer_sublist = LinkedList()
        for composer in composer_data:
            if composer[0] == period:
                composer_sublist.insert_beginning(composer)
        composer_data_list.insert_beginning(composer_sublist)
    return composer_data_list

style_list = insert_style_periods()
composer_list = insert_composer_data()

selected_style_period = ""

##write code for user interaction
while len(selected_style_period) == 0:
    user_input = str(input(
        "\nFrom which style period would you like to find composers?\nType the first few letters and then hit Enter to search.\n".lower()
    ))
    ##search for user_input in style period data structures
    matching_styles = []
    style_list_head = style_list.get_head_node()
    while style_list_head is not None:
        if str(style_list_head.get_value()).startswith(user_input):
            matching_styles.append(style_list_head.get_value())
        style_list_head = style_list_head.get_next_node()

    ##print list of matching style names here
    for period in matching_styles:
        print(period)

    ##check if only one type of style name was found, as if user would like to stick with this input
    
    ##after finding the selected style period, retrieve composer data here

    ##ask user if they want to search for other restraunts
