import React, { useState } from 'react';

function Sidebar({ groups }) {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <aside className={`bg-white shadow-lg transition-all duration-300 ${collapsed ? 'w-20' : 'w-64'} p-4`}>
      <button
        onClick={() => setCollapsed(!collapsed)}
        className="w-full mb-6 p-2 bg-gray-200 hover:bg-gray-300 rounded-lg transition"
      >
        {collapsed ? '→' : '←'}
      </button>

      {!collapsed && (
        <div>
          <h2 className="font-bold text-lg mb-4 text-gray-800">Groups</h2>
          <div className="space-y-2">
            {groups && groups.map((group) => (
              <div
                key={group.id}
                className="p-3 rounded-lg hover:bg-gray-100 cursor-pointer transition"
                style={{ borderLeft: `4px solid ${group.color}` }}
              >
                <p className="text-sm font-medium text-gray-700">{group.name}</p>
              </div>
            ))}
          </div>
        </div>
      )}
    </aside>
  );
}

export default Sidebar;
