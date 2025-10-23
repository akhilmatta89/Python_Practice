import React from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "./auth/AuthProvider";

const Protected: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { accessToken } = useAuth();
  if (!accessToken) return <Navigate to="/login" replace />;
  return <>{children}</>;
};

export default Protected;
