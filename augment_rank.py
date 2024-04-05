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
    current_rank = 1
    skip_ranks = 0
    previous_freq = None
    location_ranks = {}
    for location, freq in sorted_locations:
        if freq == previous_freq:  # Tie condition
            location_ranks[location] = current_rank
            skip_ranks += 1  # Increase skip for next rank due to the tie
        else:
            current_rank += skip_ranks  # Apply skipped ranks if any
            location_ranks[location] = current_rank
            skip_ranks = 1  # Reset skip ranks for next potential tie
            current_rank = current_rank  # Update current rank for next
        previous_freq = freq

    # No need for adjustment outside the loop

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
    current_rank = 1
    skip_ranks = 0
    previous_freq = None
    nature_ranks = {}
    for nature, freq in sorted_natures:
        if freq == previous_freq:  # Tie condition
            nature_ranks[nature] = current_rank
            skip_ranks += 1  # Increase skip for next rank due to the tie
        else:
            current_rank += skip_ranks  # Apply skipped ranks if any
            nature_ranks[nature] = current_rank
            skip_ranks = 1  # Reset skip ranks for next potential tie
            current_rank = current_rank  # Update current rank for next
        previous_freq = freq


    # Update incidents with nature ranks
    for incident in incidents:
        incident["nature_rank"] = nature_ranks[incident["nature"]]