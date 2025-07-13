# midi_udp_sender.py

import rtmidi
from pythonosc import udp_client
import time

# CONFIGURATION
SERVER_IP = "192.168.10.3"       # Replace with SuperCollider machine IP
SERVER_PORT = 57120              # SuperCollider OSC port
OSC_ADDRESS = "/midi"            # OSC address used in edge.scd

# Create OSC client
client = udp_client.SimpleUDPClient(SERVER_IP, SERVER_PORT)

# Set up MIDI input
midiin = rtmidi.MidiIn()
ports = midiin.get_ports()

if not ports:
    print("❌ No MIDI input ports found.")
    exit()

print("✅ Available MIDI ports:")
for i, port in enumerate(ports):
    print(f"{i}: {port}")

print(f"🎹 Using MIDI input: {ports[0]}")
midiin.open_port(0)

def midi_to_frequency(midi_note):
    """Convert MIDI note to frequency in Hz"""
    return 440.0 * (2.0 ** ((midi_note - 69) / 12.0))

print(f"🚀 Sending OSC messages to {SERVER_IP}:{SERVER_PORT}{OSC_ADDRESS}")
print("▶️ Play MIDI notes... (Ctrl+C to exit)")

try:
    while True:
        msg = midiin.get_message()
        if msg:
            message, deltatime = msg
            status = message[0] & 0xF0
            if status == 0x90 and message[2] > 0:  # Note ON
                client.send_message(OSC_ADDRESS, [1, message[1]])
            elif status == 0x80 or (status == 0x90 and message[2] == 0):  # Note OFF
                client.send_message(OSC_ADDRESS, [0, message[1]])
except KeyboardInterrupt:
    print("🛑 Stopped by user")
