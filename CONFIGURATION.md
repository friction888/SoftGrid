# SoftGrid Configuration Guide

## Backend Configuration

### Environment Variables

Create a `.env` file in the `backend/` directory:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/softgrid

# JWT Authentication
JWT_SECRET=your_secret_key_here
JWT_EXPIRATION=86400  # 24 hours in seconds

# Flask Settings
FLASK_ENV=development  # or production
FLASK_DEBUG=False
SECRET_KEY=your_flask_secret_key

# CORS Settings
ALLOWED_ORIGINS=http://localhost:3000,http://yourdomain.com

# Server Settings
HOST=0.0.0.0
PORT=5000
```

## Frontend Configuration

Create a `.env` file in the `frontend/` directory:

```env
REACT_APP_API_URL=http://localhost:5000
REACT_APP_API_TIMEOUT=30000
```

## Database Setup

The application uses PostgreSQL. Make sure to:

1. Create a database:
   ```bash
   createdb softgrid
   ```

2. Run migrations:
   ```bash
   python manage.py db upgrade
   ```

## Widget Configuration

Widgets can be configured in the user settings. Available widget types:

- **Weather** - Display weather information
- **Calendar** - Show calendar with events
- **Notes** - Quick notes widget
- **Clock** - Digital or analog clock
- **RSS Feed** - Display RSS feeds
- **Custom** - Embed custom content via iframe

## User Settings

Users can customize:

- **Theme** - Light/Dark mode
- **Layout** - Grid size, spacing
- **Sidebar** - Position, width, collapsible
- **Auto-save** - Enable/disable auto-save
- **Import/Export** - Backup and restore settings

## Deployment

### Self-Hosted on Linux/Unix

1. Install dependencies
2. Configure environment variables
3. Run migrations
4. Start the application with a process manager (systemd, supervisor, etc.)
5. Set up a reverse proxy (nginx, Apache)

### Docker Deployment

See the main README for Docker Compose setup.

### HTTPS Setup

Use a reverse proxy like nginx with Let's Encrypt for SSL/TLS:

```nginx
server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    location / {
        proxy_pass http://localhost:3000;
    }

    location /api {
        proxy_pass http://localhost:5000;
    }
}
```

## Performance Tuning

- Increase PostgreSQL connection pool
- Enable Redis caching for frequently accessed data
- Optimize React bundle size
- Use CDN for static assets
