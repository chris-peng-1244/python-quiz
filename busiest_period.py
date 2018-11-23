def busiest_period(entries):
    period = (None, None)
    num_people, max_num_people = 0, 0

    # Sort the entries by timestamp
    sorted_entries = sorted(entries, key = lambda e: e["timestamp"])

    # Keep track of the number of people at each entry.
    for i, entry in enumerate(sorted_entries):
        if entry["type"] == "enter":
            num_people += entry["count"]
        else:
            num_people -= entry["count"]

        if num_people > max_num_people:
            max_num_people = num_people
            period = (entry["timestamp"], sorted_entries[i+1]["timestamp"])
    
    return period