import React, { useState } from "react";
import { useAuth } from "../auth/AuthProvider";
import { useNavigate, Link } from "react-router-dom";
import { toErrorMessage } from "../utils/error";

export default function Signup() {
  const nav = useNavigate();
  const { signup } = useAuth();
  const [username, setU] = useState("");
  const [password, setP] = useState("");
  const [fullName, setF] = useState("");
  const [err, setErr] = useState<string | null>(null);

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErr(null);
    if (!username || username.length < 3) return setErr("Username must be at least 3 characters.");
    if (!password || password.length < 6) return setErr("Password must be at least 6 characters.");
    try {
      await signup(username, password, fullName);
      nav("/");
    } catch (e: any) {
      setErr(toErrorMessage(e));
    }
  };

  return (
    <div className="card">
      <div className="header">
        <h2>Create account</h2>
        <p className="muted">It’s quick and secure</p>
      </div>
      <form onSubmit={onSubmit}>
        <label>Username</label>
        <input value={username} onChange={e => setU(e.target.value)} placeholder="ajay" />
        <label>Full name (optional)</label>
        <input value={fullName} onChange={e => setF(e.target.value)} placeholder="Ajay Sai Ram" />
        <label>Password</label>
        <input type="password" value={password} onChange={e => setP(e.target.value)} placeholder="••••••••" />
        <button type="submit">Create Account</button>
      </form>
      {err && <p className="error">{err}</p>}
      <p className="muted" style={{textAlign:'center', marginTop:12}}>
        Have an account? <Link className="link" to="/login">Sign in</Link>
      </p>
    </div>
  );
}
