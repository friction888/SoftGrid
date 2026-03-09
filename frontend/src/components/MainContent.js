import React from 'react';

function MainContent({ bookmarks, widgets }) {
  return (
    <main className="flex-1 overflow-auto p-8">
      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-6">
        {bookmarks && bookmarks.map((bookmark) => (
          <a
            key={bookmark.id}
            href={bookmark.url}
            target="_blank"
            rel="noopener noreferrer"
            className="bg-white rounded-lg shadow-md hover:shadow-lg transition-all hover:scale-105 p-4 text-center group"
          >
            {bookmark.icon && (
              <img src={bookmark.icon} alt="" className="w-12 h-12 mx-auto mb-2" />
            )}
            <p className="text-sm font-medium text-gray-800 group-hover:text-blue-600">{bookmark.title}</p>
          </a>
        ))}
      </div>

      {widgets && widgets.length > 0 && (
        <div className="mt-12">
          <h2 className="text-2xl font-bold mb-6 text-gray-800">Widgets</h2>
          <div className="grid gap-6">
            {widgets.map((widget) => (
              <div key={widget.id} className="bg-white rounded-lg shadow-md p-6">
                <h3 className="font-bold text-lg text-gray-800 mb-2">{widget.widget_type}</h3>
                <p className="text-gray-600">Widget configuration: {JSON.stringify(widget.config)}</p>
              </div>
            ))}
          </div>
        </div>
      )}
    </main>
  );
}

export default MainContent;
