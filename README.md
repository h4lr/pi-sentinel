# Raspberry Pi-based responder and defense setup

This project sets up a **fake HTTP server** on a Raspberry Pi for educational purposes. The server logs incoming requests to simulate basic network interactions without exposing the Raspberry Pi to vulnerabilities.

## Compatibility with Raspberry Pi 2

While this project can be run on various Raspberry Pi models being 3 and 4 best, i'll be using a **Raspberry Pi 2**

### Key Considerations for the Raspberry Pi 2

1. **Performance**  
   The Raspberry Pi 2 has limited processing power and 1 GB of RAM.
2. **Networking**  
   The Pi 2 includes a 100 Mbps Ethernet port but lacks built-in Wi-Fi.
3. **Operating System**  
   Using **Raspberry Pi OS Lite** (the minimal version) is recommended for efficiency.

### Setting Up the Fake Server

1. **Prepare the Raspberry Pi with Raspberry Pi OS Lite**  
   Follow the standard setup instructions for Raspberry Pi OS Lite.

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
