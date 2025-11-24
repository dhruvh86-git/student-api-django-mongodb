#!/bin/bash

echo "🚀 Starting Student API Setup..."
echo

# Check if MongoDB is running
if ! pgrep -x "mongod" > /dev/null; then
    echo "📦 Starting MongoDB..."
    sudo mkdir -p /data/db
    sudo chown -R $USER:$USER /data/db
    mongod --dbpath /data/db --fork --logpath /data/db/mongodb.log
    sleep 2
    echo "✅ MongoDB started"
else
    echo "✅ MongoDB is already running"
fi

echo

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

echo "📦 Installing dependencies..."
source venv/bin/activate
pip install -q -r requirements.txt

echo "✅ Dependencies installed"
echo

echo "📦 Running migrations..."
python manage.py migrate --no-input

echo "✅ Migrations completed"
echo

echo "🎉 Setup complete!"
echo
echo "To start the server, run:"
echo "  python manage.py runserver"
echo
echo "Or run in background:"
echo "  nohup python manage.py runserver > server.log 2>&1 &"
echo
echo "API will be available at: http://127.0.0.1:8000/students/"
