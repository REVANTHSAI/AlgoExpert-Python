def underscorifySubstring(string, substring):
    locations = get_locations(string,substring)
    print(locations)
    compress_string_locations(locations)
    print(locations)
    return populateUnderScores(string,locations)

def get_locations(string,substring):
    i = 0
    locations = []
    while i + len(substring) <= len(string):
        j = i+len(substring)-1
        if string[i:j+1] == substring:
            locations.append([i,j])
        i+=1
    return locations

def compress_string_locations(substring_locations):
    i = 0
    while i < len(substring_locations)-1:
        if (substring_locations[i][1]+1 == substring_locations[i+1][0]) or (substring_locations[i][1] == substring_locations[i+1][0]):
            updated_location = [substring_locations[i][0],substring_locations[i+1][1]]
            substring_locations[i] = updated_location
            del substring_locations[i+1]
        else:
            i += 1

def populateUnderScores(string,substring_locations):
    string_list = list(string)
    locations = []
    insert_offset = 0
    for location in substring_locations:
        locations.extend(location)
    print(locations)
    for i in range(len(substring_locations)):
        first_insert_loc = substring_locations[0]
        second_insert_loc = substring_locations[1]
        current_insert_loc = first_insert_loc
        if locations[i] == 0:
            string_list = ['_']+string_list
            insert_offset += 1
        elif locations[i] == len(string)-1:
            string_list = string_list+['_']
        else:
            insert_index = locations[i]+insert_offset
            if i%2 == 0:
                string_list = string_list[:insert_index]+['_']+string_list[insert_index:]
            else:
                string_list = string_list[:insert_index+1]+['_']+string_list[insert_index+1:]
            insert_offset += 1
    return ''.join(string_list)

if __name__ == '__main__':
    string = 'ababababa'
    subString = 'a'
    print(underscorifySubstring(string,subString))
