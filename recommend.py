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
        "\nFrom which style period would you like to find composers?\nType the first few letters and then hit Enter to search.\n"
    )).lower()
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
    if len(matching_styles) == 1:
        select_style = str(input(
            "\nThe only matching style period from your search is " + matching_styles[0].title() + ". \nDo you want to see a list of " + matching_styles[0].title() + " composers? Enter y for yes or N for no.\n"
        )).lower()
    ##after finding the selected style period, retrieve composer data here
        if select_style == 'y':
            selected_style = matching_styles[0]
            print("Selected Style Period: " + selected_style)
            composer_list_head = composer_list.get_head_node()
            while composer_list_head is not None:
                sublist_head = composer_list_head.get_valu().get_head_node()
                if sublist_head.get_value()[0] == selected_style:
                    while sublist_head.get_next_node() is not None:
                        print("-_-_-_-_-_-_-_-_-_-_-")
                        print("Name: " + sublist_head.get_value()[1])
                        print("Dates: " + sublist_head.get_value()[2])
                        print("Country: " + sublist_head.get_value()[3])
                        print("-_-_-_-_-_-_-_-_-_-_-")
                        sublist_head = sublist_head.get_next_node()
                composer_list_head = composer_list_head.get_next_node()
    ##ask user if they want to search for other restraunts

            repeat = str(input("\nDo you want to see composers from a different style period? Enter y for yes or n for no.\n")).lower()
            if repeat == 'y':
                selected_style_period = ""
