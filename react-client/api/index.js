export const fetchWithBearer = async (url, options = {}) => {
  const token = localStorage.getItem('token');

  let response = await fetch(url, {
    ...options,
    headers: {
      ...options.headers,
      'Authorization': `Bearer ${token}`
  }});

  if (response.status === 401) {
    const resp = await response.json();

    if (resp.message === 'Token expired') {
      const refreshToken = localStorage.getItem('refreshToken');
      const tokenResponse = await fetch('http://localhost:8000/api/token/refresh/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ refresh: refreshToken })
      });
      
      if (tokenResponse.ok) {
        tokenResp = await tokenResponse.json();

        localStorage.setItem("token", tokenResp.access);
        localStorage.setItem("refreshToken", tokenResp.refresh);

        response = await fetch(url, ...options, headers);
      } else {
        // TODO Not sure appropriate handler yet
        console.log("REFRESH_FAILED");
      }
    }
  }

  return response;
};
