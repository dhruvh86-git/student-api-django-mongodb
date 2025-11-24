#!/bin/bash

echo "🚀 Setting up MongoDB in Codespace..."

# Import MongoDB public GPG key
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -

# Create a list file for MongoDB
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

# Reload local package database
sudo apt-get update

# Install MongoDB packages
sudo apt-get install -y mongodb-org

# Create data directory
sudo mkdir -p /data/db
sudo chown -R $USER:$USER /data/db

# Start MongoDB
sudo systemctl start mongod
sudo systemctl enable mongod

# Check status
sudo systemctl status mongod

echo "✅ MongoDB installation complete!"
echo "MongoDB is running on localhost:27017"
