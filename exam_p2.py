def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]
    HINT: https://stackoverflow.com/a/35340988/941742
    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]
    Example:
    process_file('yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]
    """
    
    folder = './babynames/' + file_name
    file = open(folder, 'r')
    line = file.readline()
    my_list = []
    for line in file:
        stats = line.split(',')
        stats[-1] = stats[-1].strip()
        my_list.append(stats)
    return my_list




def total_births(txt):
    """
    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """
    file_name = txt
    stats = process_file(file_name)
    total = 0
    for item in stats:
        num_of_birth = item[2]
        total += int(num_of_birth)
    return total



def proportion(name, gender, txt):
    """
    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a floating number, the proportion of babies with the given name to total births in given year
    """
    file_name = txt
    stats = process_file(file_name)
    this_total = 0
    for item in stats:
        baby_name = item[0]
        baby_gender = item[1]
        this_birth = item[2]
        if (name == baby_name) and (gender == baby_gender):
            this_total += int(this_birth)
    birth_prop = (this_total / total_births(txt)) * 100
    return birth_prop




def highest_year(name, gender):
    """
    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the proportions of the same name in different years)
    """
    #this doesn't work, but I tried my best, not too sure how to get it to sort through all the year files
    file_name = txt
    stats = process_file(file_name)
    my_dict = {}
    for item in stats:
        my_dict[item] = proportion(name, gender, txt)
    return max(my_dict, key=my_dict.get)


def main():
    print(process_file('yob2010.txt'))
    print(total_births('yob2010.txt'))
    print(proportion('David', 'M', 'yob2010.txt'))
    # print(highest_year('David', 'M'))


if __name__ == '__main__':
    main()