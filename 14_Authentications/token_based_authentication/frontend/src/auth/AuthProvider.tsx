import React, { createContext, useContext, useEffect, useState } from "react";
import { jwtDecode } from "jwt-decode"; // <-- named import
import api, { setAccessToken } from "../api";

type User = { username: string; full_name?: string | null };
type AuthCtx = {
  user: User | null;
  accessToken: string | null;
  login: (u: string, p: string) => Promise<void>;
  signup: (u: string, p: string, f?: string) => Promise<void>;
  logout: () => Promise<void>;
  refresh: () => Promise<void>;
};

const Ctx = createContext<AuthCtx>(null!);
export const useAuth = () => useContext(Ctx);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [accessToken, _setAT] = useState<string | null>(null);

  const setAT = (t: string | null) => {
    _setAT(t);
    setAccessToken(t);
  };

  const fetchMe = async () => {
    const { data } = await api.get<User>("/me");
    setUser(data);
  };

  const login = async (username: string, password: string) => {
    const body = new URLSearchParams({ username, password });
    const { data } = await api.post("/auth/login", body, {
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
    });
    setAT(data.access_token);
    await fetchMe();
  };

  const signup = async (username: string, password: string, full_name?: string) => {
    await api.post("/auth/signup", { username, password, full_name });
    await login(username, password);
  };

  const refresh = async () => {
    try {
      const { data } = await api.post("/auth/refresh");
      setAT(data.access_token);
    } catch {
      // No active session yet — ignore 401 on first load
    }
  };

  const logout = async () => {
    await api.post("/auth/logout");
    setAT(null);
    setUser(null);
  };

  // proactive refresh ~60s before expiry
useEffect(() => {
  if (!accessToken) return;
  const { exp } = jwtDecode<{ exp: number }>(accessToken);
  const msLeft = exp * 1000 - Date.now();
  const early = Math.max(msLeft - 5_000, 0); // refresh 5s before expiry (for testing)
  console.log("⏳ Token expires in", msLeft / 1000, "seconds");
  const id = setTimeout(() => {
    console.log("🔄 Auto-refreshing token now...");
    refresh().catch(() => logout());
  }, early);
  return () => clearTimeout(id);
}, [accessToken]);

  // session resume on first load
  useEffect(() => { refresh().then(() => user ?? fetchMe().catch(() => {})); }, []);

  return (
    <Ctx.Provider value={{ user, accessToken, login, signup, logout, refresh }}>
      {children}
    </Ctx.Provider>
  );
};
