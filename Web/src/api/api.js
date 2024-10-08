import axios from 'axios'
import config from '@/config/config.js'

export const apiClient = axios.create({
  baseURL: config.apiUrl,
  withCredentials: false,
  headers: {
      Accept: 'application/json',
  }
})

apiClient.interceptors.request.use(config => {
  config.headers['Content-Type'] = 'application/json'
  return config
})

export const handleResponse = (response) => {
  return response.data
}

export const handleError = (error) => {
  console.error('API call error:', error)
  throw error
}