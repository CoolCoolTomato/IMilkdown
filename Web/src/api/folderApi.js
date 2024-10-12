import {apiClient, handleResponse, handleError} from "./api.js"

function get_folders(data) {
  return apiClient.post("/get_folders", data).then(handleResponse).catch(handleError)
}

function create_folder(data) {
  return apiClient.post("/create_folder", data).then(handleResponse).catch(handleError)
}

function rename_folder(data) {
  return apiClient.post("/rename_folder", data).then(handleResponse).catch(handleError)
}

function delete_folder(data) {
  return apiClient.post("/delete_folder", data).then(handleResponse).catch(handleError)
}

const folderApi = {
  get_folders,
  create_folder,
  rename_folder,
  delete_folder
}

export default folderApi