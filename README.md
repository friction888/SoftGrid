# SoftGrid

A modern, self-hosted dashboard application inspired by Speed Dial 2. Create and manage your favorite bookmarks, organize them into groups (displayed on the right sidebar), and customize your dashboard with widgets.

## Features

- 📌 **Favorites Management** - Add, edit, and delete your favorite bookmarks
- 📂 **Smart Groups** - Organize bookmarks into categories (displayed on the right sidebar)
- 🎨 **Modern Design** - Clean, responsive UI inspired by Speed Dial 2
- 🔧 **Customizable Widgets** - Add widgets to your dashboard for additional functionality
- ⚙️ **Settings** - Full customization options for appearance and behavior
- 🌐 **Self-Hosted** - Deploy on your own server and access from any browser
- 🔒 **User Accounts** - Multi-user support with authentication

## Tech Stack

- **Frontend:** React with Tailwind CSS
- **Backend:** Python with Flask/FastAPI
- **Database:** PostgreSQL
- **Containerization:** Docker

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 16+
- PostgreSQL 12+
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/friction888/SoftGrid.git
   cd SoftGrid
   ```

2. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```bash
   cd ../frontend
   npm install
   ```

4. Create a `.env` file in the backend directory with your configuration:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/softgrid
   JWT_SECRET=your_secret_key
   FLASK_ENV=development
   ```

5. Initialize the database:
   ```bash
   cd backend
   python manage.py db upgrade
   ```

6. Start the backend:
   ```bash
   python app.py
   ```

7. Start the frontend (in a new terminal):
   ```bash
   cd frontend
   npm start
   ```

Visit `http://localhost:3000` to access SoftGrid.

## Project Structure

```
SoftGrid/
├── backend/              # Python Flask/FastAPI backend
│   ├── app.py
│   ├── requirements.txt
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── migrations/
├── frontend/             # React frontend
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── tailwind.config.js
├── docker-compose.yml
└── README.md
```

## Docker Deployment

Build and run with Docker Compose:

```bash
docker-compose up -d
```

## Configuration

See the [CONFIGURATION.md](./CONFIGURATION.md) file for detailed configuration options.

## Contributing

This is a personal project. Feel free to fork and customize it for your needs!

## License

MIT License - See LICENSE file for details

## Support

For issues or feature requests, please open an issue on GitHub.
