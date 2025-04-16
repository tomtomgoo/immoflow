import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { useAuth } from './hooks/useAuth';
import Dashboard from './components/Dashboard';
import Login from './pages/Login';

export default function App() {
  const { user, loading } = useAuth();

  // Tant que l'auth se charge, on affiche un loader
  if (loading) return <div className="p-10">Chargement...</div>;

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          path="/*"
          element={user ? <Dashboard /> : <Navigate to="/login" replace />}
        />
      </Routes>
    </BrowserRouter>
  );
}