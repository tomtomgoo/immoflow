import React, { useEffect, useState } from "react";
import { useAuth } from "../hooks/useAuth";
import axios from 'axios';
import Sidebar from './Sidebar.jsx';
import TopBar from './TopBar.jsx';

const Dashboard = () => {
  const { user, loading } = useAuth();  // ← add this
  const [data, setData] = useState(null);

  useEffect(() => {
    if (user) {
      axios.get("http://127.0.0.1:8000/agent/kpis", {
        headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` }
      })
        .then(response => {
          setData(response.data);
        })
        .catch(error => {
          console.error("Erreur lors de la récupération des KPI :", error);
        });
    }
  }, [user]);

  // console.log(user)  ← remove or comment out

  if (loading) {
    return <div className="flex items-center justify-center h-screen">Chargement...</div>;
  }

  if (!data) {
    return <div className="flex items-center justify-center h-screen">Chargement des KPI...</div>;
  }

  return (
    <div className="flex w-screen min-h-screen bg-white">
      <Sidebar />
      <div className="flex-1 overflow-auto bg-white">
        <TopBar />
        <main className="p-6">
          {/* Cartes KPI */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
            <div className="bg-white rounded-lg shadow-sm p-6 border-l-4 border-indigo-500">
              <p className="text-sm font-medium text-gray-500">Biens en gestion</p>
              <p className="text-2xl font-semibold text-gray-800">{data.biens_en_gestion}</p>
              <p className="text-xs text-green-500 flex items-center mt-1">
                <i className="fas fa-arrow-up mr-1"></i> +8% ce mois
              </p>
            </div>
            <div className="bg-white rounded-lg shadow-sm p-6 border-l-4 border-green-500">
              <p className="text-sm font-medium text-gray-500">Ventes finalisées</p>
              <p className="text-2xl font-semibold text-gray-800">{data.ventes_finalisees}</p>
              <p className="text-xs text-green-500 flex items-center mt-1">
                <i className="fas fa-arrow-up mr-1"></i> +2% ce mois
              </p>
            </div>
            <div className="bg-white rounded-lg shadow-sm p-6 border-l-4 border-blue-500">
              <p className="text-sm font-medium text-gray-500">Prospects actifs</p>
              <p className="text-2xl font-semibold text-gray-800">{data.prospects_actifs}</p>
              <p className="text-xs text-red-500 flex items-center mt-1">
                <i className="fas fa-arrow-down mr-1"></i> -3% ce mois
              </p>
            </div>
            <div className="bg-white rounded-lg shadow-sm p-6 border-l-4 border-yellow-500">
              <p className="text-sm font-medium text-gray-500">Commissions (€)</p>
              <p className="text-2xl font-semibold text-gray-800">{Number(data.commission_annuelle ?? 0).toFixed(2)}</p>
              <p className="text-xs text-green-500 flex items-center mt-1">
                <i className="fas fa-arrow-up mr-1"></i> +12% ce mois
              </p>
            </div>
          </div>

          {/* Autres sections du dashboard (ex: graphiques, rendez-vous, etc.) */}
          <div>
            {/* Tu pourras ajouter ici d'autres composants ou sections */}
          </div>
        </main>
      </div>
    </div>
  );
};

export default Dashboard;