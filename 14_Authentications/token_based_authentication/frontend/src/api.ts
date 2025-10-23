import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE,
  withCredentials: true, // send/receive refresh cookie
});

let accessToken: string | null = null;
let isRefreshing = false;
let queue: Array<(t: string) => void> = [];

export const setAccessToken = (t: string | null) => { accessToken = t; };

api.interceptors.request.use(cfg => {
  if (accessToken) {
    cfg.headers = cfg.headers ?? {};
    (cfg.headers as any).Authorization = `Bearer ${accessToken}`;
  }
  return cfg;
});

api.interceptors.response.use(
  res => res,
  async err => {
    const original = err.config;
    if (err.response?.status !== 401 || original._retried) {
      throw err;
    }

    if (!isRefreshing) {
      isRefreshing = true;
      original._retried = true;
      try {
        const { data } = await api.post("/auth/refresh"); // cookie supplies refresh
        setAccessToken(data.access_token);
        queue.forEach(fn => fn(data.access_token));
        queue = [];
        original.headers = original.headers ?? {};
        (original.headers as any).Authorization = `Bearer ${data.access_token}`;
        return api(original);
      } catch (e) {
        queue = [];
        setAccessToken(null);
        window.location.assign("/login");
        throw e;
      } finally {
        isRefreshing = false;
      }
    }

    return new Promise(resolve => {
      queue.push((newTok) => {
        original.headers = original.headers ?? {};
        (original.headers as any).Authorization = `Bearer ${newTok}`;
        resolve(api(original));
      });
    });
  }
);

export default api;
