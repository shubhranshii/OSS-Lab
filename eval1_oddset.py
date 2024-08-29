shopping_list=["eggs"]

def add_item(item: str):
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.")

def remove_item(item: str):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' is not in your shopping list.")

def search_item(item: str):
    return item in shopping_list

def binary_search(item:str) ->str :
    left=0
    right= len(shopping_list)-1
    shopping_list.sort()
    while(left<=right):
        mid= (int)((left+right)/2)
        if(item== shopping_list[mid]):
            return item[::-1]
        elif(item<shopping_list[mid]):
            high=mid-1
        else:
            low=mid+1
    return "Item is not present"

def display_list():
    if shopping_list:
        print("Current shopping list is:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print("Shopping list is empty.")

if __name__ == "__main__":
    choice='0'
    while(choice!='6'):
        print("CHOOSE AN OPTION. ENTER 6 TO EXIT.")
        print("1. add_item(item: str): Add a new item to the shopping list.")
        print("2. remove_item(item: str): Remove an item from the list by its name.")
        print("3. search_item(item: str) -> bool: Check if an item is on the list and return True if it is")
        print("4. display_list(): Display the current shopping list.")
        print("5. binary search an item")
        choice= input("Enter your choice")
        
        if(choice=='1'):
            item=input("Enter item to be added. ")
            add_item(item)
        elif(choice=='2'):
            item=input("Enter item to be removed. ")
            remove_item(item)

        elif(choice=='3'):
            item=input("Enter item to be searched. ")
            search_item(item)
        
        elif(choice=='4'):
            display_list()

        elif(choice=='5'):
            item=input("Enter item to be searched. ")
            print(binary_search(item))

        
