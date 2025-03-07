def check_update(update, rules):
    count_applied_rules = 0
    count_not_ignored_rules = 0
    for j in range(len(rules)):
        rule = rules[j]
        if rule[0] in update and rule[1] in update:
            count_not_ignored_rules += 1
            if update.index(rule[0]) < update.index(rule[1]):
                count_applied_rules += 1
    return count_applied_rules == count_not_ignored_rules

def sort_update(to_update, rules):

    
    for rule in rules:
        i,j = to_update.index(rule[0]), to_update.index(rule[1])
        if i > j:
            to_update[i], to_update[j] = to_update[j], to_update[i]
            
    if not check_update(to_update, rules):
        sort_update(to_update, rules)
    return to_update
    
def task_1(path):
    with open(path, 'r') as f:
        data =  f.read().split('\n')
        
    rules = []
    i = 0
    while data[i] != '':
        rules.append(list(map(int,data[i].split('|'))))
        i += 1
    i += 1
    
    updates = []
    for j in range(i, len(data)):
        updates.append(list(map(int,data[j].split(','))))
        
        
    sum_of_middle_pages = 0
    for i in range(len(updates)):
        update = updates[i]                       
        if check_update(update, rules):
            sum_of_middle_pages += update[len(update)//2]                
            
    print(sum_of_middle_pages)
    return None


def task_2(path):
    with open(path, 'r') as f:
        data =  f.read().split('\n')
        
    rules = []
    i = 0
    while data[i] != '':
        rules.append(list(map(int,data[i].split('|'))))
        i += 1
    i += 1
    
    updates = []
    for j in range(i, len(data)):
        updates.append(list(map(int,data[j].split(','))))
        
        
    sum_of_middle_pages = 0
    for i in range(len(updates)):
        update = updates[i]                       
        if not check_update(update, rules):
            to_update = update[:]
            needed_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
            sorted_update = sort_update(to_update, needed_rules)
            
            sum_of_middle_pages += sorted_update[len(update)//2]                
            
    print(sum_of_middle_pages)
    return None


if __name__ == '__main__':
    task_2('order.txt')

