import apiAxios from '@utils/api.axios';

const isAuthorized = async () => {
  const response = await apiAxios.get('/pokeapi/is_authorized');
  return response?.data;
}

const getAuthUrl = async () => {
  const response = await apiAxios.get('/pokeapi/get_auth_url');
  return response?.data;
}

const saveAuthCode = async (code) => {
  const response = await apiAxios.post('/pokeapi/save_token', { code });
  return response?.data;
}

const getConfig = async () => {
  const response = await apiAxios.get('/pokeapi/get_config');
  return response?.data;
}

const PokeAPIService = {
  isAuthorized,
  getAuthUrl,
  saveAuthCode,
  getConfig
};

export default PokeAPIService;
