// src/components/TopBar.jsx
import React from 'react';

const TopBar = () => {
  const handleMenuToggle = () => {
    const sidebar = document.querySelector('.sidebar');
    if (sidebar) {
      sidebar.classList.toggle('hidden');
    }
  };

  return (
    <header className="bg-white shadow-sm">
      <div className="flex items-center justify-between p-4">
        <div className="flex items-center md:hidden">
          <button className="text-gray-600" onClick={handleMenuToggle}>
            <i className="fas fa-bars text-xl"></i>
          </button>
        </div>
        <div className="hidden md:block">
          <h1 className="text-xl font-semibold text-gray-800">Tableau de bord</h1>
        </div>
        <div className="flex items-center">
          <div className="relative mr-4">
            <span className="absolute inset-y-0 left-0 flex items-center pl-3">
              <i className="fas fa-search text-gray-400"></i>
            </span>
            <input
              type="text"
              className="pl-10 pr-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"
              placeholder="Rechercher..."
            />
          </div>
          <div className="relative mr-4">
            <i className="fas fa-bell text-gray-600 text-xl"></i>
            <span className="absolute top-0 right-0 w-2 h-2 bg-red-500 rounded-full"></span>
          </div>
        </div>
      </div>
    </header>
  );
};

export default TopBar;