import {apiClient, handleResponse, handleError} from "./api.js"

function read_file(data) {
  return apiClient.post("/read_file", data).then(handleResponse).catch(handleError)
}

function write_file(data) {
  return apiClient.post("/write_file", data).then(handleResponse).catch(handleError)
}

function get_files(data) {
  return apiClient.post("/get_files", data).then(handleResponse).catch(handleError)
}

function create_file(data) {
  return apiClient.post("/create_file", data).then(handleResponse).catch(handleError)
}

function rename_file(data) {
  return apiClient.post("/rename_file", data).then(handleResponse).catch(handleError)
}

function delete_file(data) {
  return apiClient.post("/delete_file", data).then(handleResponse).catch(handleError)
}

const fileApi = {
  read_file,
  write_file,
  get_files,
  create_file,
  rename_file,
  delete_file
}

export default fileApi