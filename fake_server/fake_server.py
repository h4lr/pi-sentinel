1. **Prepare the Raspberry Pi with Raspberry Pi OS Lite**  
   Standard setup instructions for Raspberry Pi OS Lite.

2. **Install Python**  
   Ensure Python 3 is installed:
   ```bash
   sudo apt update
   sudo apt install python3
   ```

3. **Run the Server**  
   Navigate to the project directory and run the script:
   ```bash
   python3 fake_server.py
   ```

4. (optional) - **SSH Access **: To access your Pi remotely, enable SSH from the `raspi-config` menu or via the terminal:
     ```bash
     sudo raspi-config
     ```
     Select **Interfacing Options > SSH > Enable**.
