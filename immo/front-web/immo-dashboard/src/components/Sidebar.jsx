// src/components/Sidebar.jsx
import React from 'react';
import { useAuth } from '../hooks/useAuth';

const Sidebar = () => {
  const { user } = useAuth();

  return (
    <div className="sidebar bg-indigo-800 text-white w-64 flex-shrink-0 hidden md:block">
      <div className="p-4">
        <h2 className="text-2xl font-semibold">ImmoBoard</h2>
        <p className="text-xs opacity-70">Dashboard Agent Immobilier</p>
      </div>
      <nav className="mt-8">
        <a href="#" className="flex items-center py-3 px-4 bg-indigo-900 text-white">
          <i className="fas fa-tachometer-alt mr-3"></i>
          <span>Tableau de bord</span>
        </a>
        <a href="#" className="flex items-center py-3 px-4 text-white hover:bg-indigo-700">
          <i className="fas fa-home mr-3"></i>
          <span>Biens immobiliers</span>
        </a>
        {user?.role === 'directeur' && (
        <a href="/settings/commission-rates" className="flex items-center py-3 px-4 text-white hover:bg-indigo-700">
            <i className="fas fa-cog mr-3"></i>
            <span>Paramètres de l'Agence</span>
        </a>)}
        {/* Ajoute les autres liens ici */}
      </nav>
      <div className="absolute bottom-0 w-64 p-4">
        <div className="flex items-center">
          <img src={user?.avatarUrl || "/api/placeholder/40/40"} className="rounded-full mr-3" alt="Avatar" />
          <div>
            <p className="font-semibold">{user?.name || "Sophie Martin"}</p>
            <p className="text-xs opacity-70">{user?.role || "Agent Senior"}</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;