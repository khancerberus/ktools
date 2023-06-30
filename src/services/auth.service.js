import jwtDecode from 'jwt-decode';

import apiAxios from '@utils/api.axios';

const login = async (code) => {
  const response = await apiAxios.post('/auth/login', {
    code
  });

  if (response?.data?.access_token) {
    localStorage.setItem('access_token', response?.data?.access_token);
  }

  return response?.data;
}

const logout = () => {
  localStorage.removeItem('access_token');
}

const getUserFromToken = () => {
  const token = localStorage.getItem('access_token');

  if (!token) return null;

  try {
    const decodedToken = jwtDecode(token);
    return decodedToken?.user;

  } catch (error) {
    return null;
  }
}

const AuthService = {
  login,
  logout,
  getUserFromToken
};

export default AuthService;
