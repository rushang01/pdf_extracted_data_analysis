def set_EMSSTAT_to_false(incident):
    incident["EMSSTAT"] = False

def process_emsstat(incidents):
    for i in range(len(incidents)):
        current_incident = incidents[i]
        if current_incident['incident_ori'] == 'EMSSTAT':
            current_incident['EMSSTAT'] = True
            # Look ahead at incidents to check for same time and location
            j = i
            while j < len(incidents) - 1:
                next_incident = incidents[j+1]
                j = j+1
                if  next_incident['date_time'] == current_incident['date_time'] and \
                    next_incident['location'] == current_incident['location']:
                    next_incident['EMSSTAT'] = True
                else:
                    break

            # Look behind at incidents to check for same time and location
            j = i
            while j > 0:
                previous_incident = incidents[j-1]
                j = j-1
                if  previous_incident['date_time'] == current_incident['date_time'] and \
                    previous_incident['location'] == current_incident['location']:
                    previous_incident['EMSSTAT'] = True
                else:
                    break

    return incidents