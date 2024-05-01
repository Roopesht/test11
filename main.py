@app.route('/first_record', methods=['GET'])
def get_first_record():
    first_record = ProvisioningReqHistory.query.first()
    if first_record:
        return jsonify(first_record.__dict__)
    else:
        return jsonify(message="No records found"), 404

if __name__ == '__main__':
    app.run(debug=True)
