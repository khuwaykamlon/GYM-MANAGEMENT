import csv

@app.route('/generate_report')
def generate_report():
    members = Member.query.all()
    with open('members_report.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Username", "RFID Tag"])
        for member in members:
            writer.writerow([member.id, member.username, member.rfid_tag])
    
    return "Report generated!"
