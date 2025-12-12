# Network Troubleshooting Guide

## Issue: Wi-Fi Not Connecting

### Symptoms
- Device cannot connect to Wi-Fi.
- Error message: "Unable to join network."
- Internet works on other devices but not this one.

### Possible Causes
- Incorrect Wi-Fi password.
- Router or modem issues.
- Device network settings misconfigured.
- IP conflict or DHCP failure.

### Step-by-Step Solution
1. **Restart Router and Device**
   - Turn off the router and device.
   - Wait 30 seconds, then turn them back on.

2. **Verify Wi-Fi Password**
   - Ensure you are entering the correct password.
   - Check if Caps Lock is on.

3. **Forget and Reconnect to Network**
   - Go to Wi-Fi settings.
   - Forget the network and reconnect by entering the password again.

4. **Check IP Settings**
   - Ensure DHCP is enabled.
   - If using static IP, verify correct configuration.

5. **Update Network Drivers**
   - On Windows, update drivers via Device Manager.
   - On Mac, ensure system updates are installed.

6. **Reset Network Settings**
   - On mobile devices, reset network settings to default.
   - On PC, use `netsh winsock reset` (Windows).
