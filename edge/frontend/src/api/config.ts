import axios from 'axios';

const host = () : string => {
  if (process.env.NODE_ENV === 'development') {
    return 'http://localhost:8000';
  }
  return '/api';
}

export const api = axios.create({
  baseURL: host()
});
