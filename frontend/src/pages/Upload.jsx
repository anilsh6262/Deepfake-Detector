@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        print("UPLOAD HIT")

        if 'file' not in request.files:
            return jsonify({"error": "No file received"}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"error": "Empty file"}), 400

        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

        file.save(upload_path)

        return jsonify({
            "message": "Upload success",
            "filename": file.filename
        }), 200

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500