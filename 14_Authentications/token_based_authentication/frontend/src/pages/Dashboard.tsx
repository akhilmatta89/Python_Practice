import React, { useEffect, useState } from "react";
import api from "../api";
import { useAuth } from "../auth/AuthProvider";

type Profile = { username: string; full_name?: string | null };

export default function Dashboard() {
  const { logout } = useAuth();
  const [me, setMe] = useState<Profile | null>(null);
  const [err, setErr] = useState<string | null>(null);

  useEffect(() => {
    api.get<Profile>("/me").then(r => setMe(r.data)).catch(() => setErr("Failed to load profile."));
  }, []);

  return (
    <div className="card">
      <div className="header">
        <h2>Dashboard</h2>
        <p className="muted">Protected route</p>
      </div>
      {me ? (
        <p>Welcome, <strong>{me.full_name ?? me.username}</strong>!</p>
      ) : err ? (
        <p className="error">{err}</p>
      ) : (
        <p className="muted">Loading…</p>
      )}
      <button onClick={() => logout()} style={{marginTop:16}}>Logout</button>
    </div>
  );
}
