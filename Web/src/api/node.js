import {apiClient, handleResponse, handleError} from "./api.js"

function get_nodes(data) {
  return apiClient.post("/get_nodes", data).then(handleResponse).catch(handleError)
}

const fileAPI = {
  get_nodes
}

export default fileAPI