def rank_locations(incidents):
    # Count the frequency of each location
    location_freq = {}
    for incident in incidents:
        location = incident["location"]
        if location in location_freq:
            location_freq[location] += 1
        else:
            location_freq[location] = 1

    # Sort locations by frequency, preserving ties
    sorted_locations = sorted(location_freq.items(), key=lambda x: x[1], reverse=True)

    # Assign ranks with ties properly handled so the next rank is incremented after ties
    actual_rank = 0
    previous_freq = None
    location_ranks = {}
    for location, freq in sorted_locations:
        actual_rank += 1 

        if freq == previous_freq:  # Tie condition
            location_ranks[location] = prev_rank
        else:
            location_ranks[location] = actual_rank
            prev_rank = actual_rank
    
        previous_freq = freq

    # Update incidents with location ranks
    for incident in incidents:
        incident["location_rank"] = location_ranks[incident["location"]]

def rank_nature(incidents):
    # Count the frequency of each nature
    nature_freq = {}
    for incident in incidents:
        nature = incident["nature"]
        if nature in nature_freq:
            nature_freq[nature] += 1
        else:
            nature_freq[nature] = 1

    # Sort natures by frequency, preserving ties
    sorted_natures = sorted(nature_freq.items(), key=lambda x: x[1], reverse=True)

    # Assign ranks with ties properly handled so the next rank is incremented after ties
    actual_rank = 0
    previous_freq = None
    nature_ranks = {}
    for nature, freq in sorted_natures:
        actual_rank += 1 

        if freq == previous_freq:  # Tie condition
            nature_ranks[nature] = prev_rank
        else:
            nature_ranks[nature] = actual_rank
            prev_rank = actual_rank
    
        previous_freq = freq

    # Update incidents with nature ranks
    for incident in incidents:
        incident["nature_rank"] = nature_ranks[incident["nature"]]