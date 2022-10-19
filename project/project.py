import csv
import json
import argparse
import sys

class Categories:
    def __init__(self,json_file):
        with open(json_file) as file:
            self._dict = json.load(file)
        self.jsonfile = json_file
            
    @property
    def dict(self):
        return self._dict
    
    def add_category(self, category):
        self._dict.update({category:[]})
    
    def add_keyword(self, category, keyword):
        self._dict[category].append(keyword)
        
    def save_file(self):
        with open(self.jsonfile, "w") as outfile:
            json.dump(self.dict, outfile)
    
    def reset(self):
        empty = {"test":[]}
        with open(self.jsonfile, "w") as outfile:
            json.dump(empty, outfile)
        
class Operation:
    def __init__(self, Date, Type, Memo, Amount, Category=None):
        self.date = Date
        self.type = Type
        self.memo = Memo
        self.amount = Amount
        self.category = Category
    
    def __str__(self):
        return f"{self.date}, {self.type}, {self.memo}, {self.category}, {self.amount}"

def main():
    args = get_args()
    dict_json = f"util/{args.d}"
    categories = Categories(dict_json)
    #print (categories)
    operations_list = csv_to_list(args.f)
    if args.R:
        categories.reset()
        sys.exit()
    operations_list = clean_data(operations_list)
    categorised = learn(add_category(operations_list, categories.dict), categories)
    stats = get_stats(categorised, categories.dict)
    print (stats)
    
def csv_to_list(f):
    """
    data format: [{'date': '', 'Unique Id': '',...},{},{}]
    """
    money = []
    with open(f) as file:
        reader = csv.DictReader(file)
        for row in reader:
            money.append(row)
    return money

def get_args():
    parser = argparse.ArgumentParser(description="Get some statistics from a bank csv file")
    parser.add_argument("-f", help="csv file from the bank", type=str)
    parser.add_argument("-d", help="Json file for categories", type=str, default="categories.json")
    parser.add_argument("--R",action='store_true')
    return parser.parse_args()
    
def clean_data(l):
    """
    Function to clean the data entry: : some keys removed, key category added etc...
    : param f: list of operations (from csv file)
    : type f: list of dictionnaries
    : return: list operations, each operations passed through the Operation class
    """
    clean = []
    for row in l:
        row.pop('Unique Id')
        row.pop('Cheque Number')
        row.pop('Payee')
        row["Memo"] = row["Memo"].lower()
        row["Type"] = row.pop('Tran Type')
        row["Amount"] = float(row["Amount"])
        clean.append(Operation(**row))
    return clean

def add_category(l, categories):
    """
    add category in the row of the operation list (l argument) if it' s in the dictionnary provided (categories argument)
    """
    #print(categories)
    for row in l:
        if row.memo == "":  # set category to unknown if memo field is blank
            row.category = "unknown"
        for key in categories:
            for word in categories[key]:
                if word in row.memo:
                    row.category = key
    return l

def learn(l, c):
    """ 
    This function takes a list of dictionnaries (operations), a categories dictionnary and a json file to update 
    For operations without category, the user is prompt to choose one and add a Keyword associated to the dictionnary (idealy present in the memo of the operation)
    :param l: list of all operations [{},]
    :param c: instance of Categories class
    """
    for row in l:
        keys = list(c.dict.keys()) # keys from categories dictionnary
        add_category(l, c.dict)
        if not row.category: 
            print(f"\n{row}\n") 
            print("Please choose a category:\n",*keys,"\n", sep=" -- ")
            manual_category = input(f"categorie? \n")
            if manual_category and manual_category in keys:
                row.category = manual_category
                manual_keyword = input("Keyword? ")
                if manual_keyword != "":
                    c.add_keyword(manual_category,manual_keyword)
                    c.save_file()
            else:           
                while True:
                    prompt = input("not an existing category, do you want to add one? ").lower()
                    if prompt == "yes" or prompt == "y":
                        new_cat = input("New category: ")
                        c.add_category(new_cat)
                        c.add_keyword(new_cat, input("Keyword?: "))
                        c.save_file()
                        break
                    elif prompt == "no" or prompt == "n":
                        break
                    else:
                        continue                  
    return l

def get_stats(f, c):
    stats = {} 
    for key in c: # create dictionnary with same keys as the categories dictionnary and a list as value 
        stats[key] = []
    for row in f: # parse each row and add the amount in the list value of the category
        if row.category:
            stats[row.category].append(row.amount)
    for i in stats:
        stats[i] = "{:.2f}".format(sum(stats[i]))
    return stats
    
if __name__ == "__main__":
    main()