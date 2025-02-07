@app.route('/admin_dashboard')
def admin_dashboard():
    # Get member count, class bookings, etc.
    total_members = Member.query.count()
    total_classes = Class.query.count()
    return render_template('admin_dashboard.html', total_members=total_members, total_classes=total_classes)
