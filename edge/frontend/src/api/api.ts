import { api } from './config';

export const API = {
  getTotalPullUps: async function () {
    const response = await api.request({
      url: `/totalPullUps`,
      method: 'GET'
    });

    return response.data;
  }
};
