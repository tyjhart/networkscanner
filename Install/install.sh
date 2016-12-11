# Copyright 2016, Manito Networks, LLC. All rights reserved.
# Install script for Mikrotik device scanner

# Ensure we have the permissions we need to execute scripts
chmod -R +x ..

# Copy example config_default.py to real config_options.py
echo "Copy example config_default.py to real config.py"
cp $(pwd)/Python/config_default.py $(pwd)/Python/config.py

# Install Python dependencies
echo "Install Python dependencies"
pip install -r ./Install/requirements.txt