import React, { useState } from "react";
import { useAuth } from "../auth/AuthProvider";
import { Link, useNavigate } from "react-router-dom";
import { toErrorMessage } from "../utils/error";

export default function Login() {
  const nav = useNavigate();
  const { login } = useAuth();
  const [username, setU] = useState("");
  const [password, setP] = useState("");
  const [err, setErr] = useState<string | null>(null);

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErr(null);
    if (!username || !password) return setErr("Please enter username and password.");
    try {
      await login(username, password);
      nav("/");
    } catch (e: any) {
      setErr(toErrorMessage(e));
    }
  };

  return (
    <div className="card">
      <div className="header">
        <h2>Sign in</h2>
        <p className="muted">Use your demo account</p>
      </div>
      <form onSubmit={onSubmit}>
        <label>Username</label>
        <input value={username} onChange={e => setU(e.target.value)} placeholder="ajay" />
        <label>Password</label>
        <input type="password" value={password} onChange={e => setP(e.target.value)} placeholder="••••••••" />
        <button type="submit">Sign In</button>
      </form>
      {err && <p className="error">{err}</p>}
      <p className="muted" style={{textAlign:'center', marginTop:12}}>
        No account? <Link className="link" to="/signup">Create one</Link>
      </p>
    </div>
  );
}
