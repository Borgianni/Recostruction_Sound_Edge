# Sound at the Edge

This repository provides the implementation of the framework described in the paper:
**"Reconstructing the Sound at the Edge: A Low-Latency Framework for NMP with Autotuned Local Synthesis"**

## 🧩 Overview

This system allows ultra-low-latency interaction in networked music performance (NMP) by sending minimal control messages (like MIDI) over the network, and reconstructing sound locally with synthesis using SuperCollider.

## 📁 Contents

- `midi_udp_sender.py`: Python script to read incoming MIDI and send OSC messages via UDP.
- `edge.scd`: SuperCollider script that receives OSC messages and synthesizes sound in real-time.

## 🚀 How to Run

### 1. SuperCollider (on receiver side)

- Open `edge.scd`
- Boot the server
- Run the script to start listening for OSC messages.

### 2. Python MIDI Sender (on controller side)

Install requirements:
```bash
pip install python-rtmidi python-osc
```

Then run:
```bash
python midi_udp_sender.py
```

## 🎥 Demo

Watch the system in action:

https://github.com/user-attachments/assets/7858616d-1097-4fbf-84b3-34ef08d5676a

> **Note**: If you're viewing this on GitHub, the video should play directly above. If it doesn't load, you can [click here to view it directly](https://github.com/user-attachments/assets/7858616d-1097-4fbf-84b3-34ef08d5676a).


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.


