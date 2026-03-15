"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.
    """
    azara_coordinate = azara_record[1]
    
    rui_coord_1 = rui_record[1][0]
    rui_coord_2 = rui_record[1][1]
    rui_coordinate = f"{rui_coord_1}{rui_coord_2}"
    
    return azara_coordinate == rui_coordinate

def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.
    """

    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    else:
        return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.
    """

    result = ""
    
    for treasure, _, location, coordinate, quadrant in combined_record_group:
        result += f"{(treasure, location, coordinate, quadrant)}\n"
        
    return result
           
