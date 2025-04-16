// src/pages/Login.jsx
import React, { useState } from 'react';
import { useAuth } from '../hooks/useAuth';

export default function Login() {
  const { login } = useAuth();
  const [email, setEmail]       = useState('');
  const [password, setPassword] = useState('');
  const [error, setError]       = useState('');

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await login({ email, password });
      // redirection vers le dashboard
      window.location.href = '/';
    } catch {
      setError('Identifiants invalides');
    }
  };

  return (
    <div className="max-w-md mx-auto mt-20 p-6 bg-white rounded shadow">
      <h2 className="text-xl mb-4">Se connecter</h2>
      {error && <p className="text-red-500">{error}</p>}
      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="email" placeholder="Email"
          value={email} onChange={e => setEmail(e.target.value)}
          className="w-full p-2 border rounded"
        />
        <input
          type="password" placeholder="Mot de passe"
          value={password} onChange={e => setPassword(e.target.value)}
          className="w-full p-2 border rounded"
        />
        <button type="submit"
          className="w-full p-2 bg-indigo-600 text-white rounded">
          Connexion
        </button>
      </form>
    </div>
  );
}