def prepare_checklist(description,date_time,location,evidence):
    items=[]
    if description.strip(): items.append("Write a factual, chronological description without guesses.")
    else: items.append("Record what happened, including who/what/when/where, using factual language.")
    items.append("Record the date and approximate time; note uncertainty if exact time is unknown.")
    items.append("Record the location or online platform/account involved.")
    items.append("Preserve original evidence: screenshots, messages, URLs, emails, files, transaction records, or call details where relevant.")
    items.append("Keep copies of evidence in a safe place and avoid altering originals.")
    items.append("List relevant witnesses or accounts only if known.")
    items.append("For formal reporting, check the current official procedure for your jurisdiction or institution rather than relying on this demo.")
    if evidence.strip(): items.insert(0,"Evidence noted for this draft: " + evidence.strip()[:300])
    return {"title":"Complaint-preparation checklist","items":items,"disclaimer":"This tool prepares information; it is not a police, legal, or emergency service and does not submit a complaint."}
