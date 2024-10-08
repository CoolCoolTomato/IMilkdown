from sdk.sdk import *
from flask import Flask, request, jsonify
from model import Node

app = Flask(__name__)

@app.route('/read_file', methods=['POST'])
def api_read_file():
    data = request.json
    path = data.get('path')
    try:
        content = read_file(path)
        return jsonify({'content': content}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/write_file', methods=['POST'])
def api_write_file():
    data = request.json
    path = data.get('path')
    content = data.get('content')
    try:
        write_file(path, content)
        return jsonify({'message': 'File written successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/get_files', methods=['POST'])
def api_get_files():
    data = request.json
    path = data.get('path')
    try:
        files = get_files(path)
        return jsonify({'files': files}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/get_folders', methods=['POST'])
def api_get_folders():
    data = request.json
    path = data.get('path')
    try:
        folders = get_folders(path)
        return jsonify({'folders': folders}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/create_file', methods=['POST'])
def api_create_file():
    data = request.json
    path = data.get('path')
    try:
        create_file(path)
        return jsonify({'message': 'File created successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/create_folder', methods=['POST'])
def api_create_folder():
    data = request.json
    path = data.get('path')
    try:
        create_folder(path)
        return jsonify({'message': 'Folder created successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/rename_file', methods=['POST'])
def api_rename_file():
    data = request.json
    old_path = data.get('old_path')
    new_path = data.get('new_path')
    try:
        rename_file(old_path, new_path)
        return jsonify({'message': 'File renamed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/rename_folder', methods=['POST'])
def api_rename_folder():
    data = request.json
    old_path = data.get('old_path')
    new_path = data.get('new_path')
    try:
        rename_folder(old_path, new_path)
        return jsonify({'message': 'Folder renamed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/delete_file', methods=['POST'])
def api_delete_file():
    data = request.json
    path = data.get('path')
    try:
        delete_file(path)
        return jsonify({'message': 'File deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/delete_folder', methods=['POST'])
def api_delete_folder():
    data = request.json
    path = data.get('path')
    try:
        delete_folder(path)
        return jsonify({'message': 'Folder deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/get_nodes')
def api_get_nodes():
    data = request.json
    path = data.get('path')

    root_node = Node(path=path, name=path.split("/")[-1], is_folder=True)
    try:
        root_node.build_node()
        return jsonify({'nodes': root_node}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)