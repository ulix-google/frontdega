import { api } from './config';

export const API = {
  getMessage: async function () {
    const response = await api.request({
      url: `/getMessage`,
      method: 'GET'
    });

    return response.data;
  }
};
