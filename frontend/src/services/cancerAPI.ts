import axios from 'axios';

export const getCharts = async (features: string[], chartTypes: string[]) => {
  const response = await axios.post('/api/charts', {
    features,
    chartTypes,
  });
  return response.data;
};

export const getPredictions = async (features: { [key: string]: string }) => {
  const response = await axios.post('/api/prediction', {
    ...features,
  });
  return response.data;
};
