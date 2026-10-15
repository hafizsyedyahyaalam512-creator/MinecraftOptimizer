# 🎮 Minecraft Optimizer Pro

Minecraft 1.8.9 PvP ke liye all-in-one optimization tool. Network, Java, Windows, aur in-game settings ko optimize karo!

## Features

✅ **Network Optimization**
- TCP settings auto-configure
- RSS (Multi-core network processing) enable
- DNS flushing
- Latency reduction

✅ **Packet Optimization (NEW!)**
- TCP window size reduced
- MTU optimized for Minecraft
- TCP pacing enabled
- Faster packet delivery
- Better hit registration

✅ **Java Arguments**
- G1GC garbage collector optimized
- Memory management improved
- FPS drops minimize

✅ **Windows Optimization**
- Game Mode disable
- Power plan setup
- Audio service optimization
- DNS cache flush

✅ **Minecraft Settings Guide**
- Render distance optimization
- Particle settings
- GUI scaling
- Performance tips

## Requirements

- Windows 10/11
- Python 3.7+
- **Admin Rights** (for network/system optimizations)

## Installation

### Option 1: Using Python

```bash
# Python already installed hona chahiye
python minecraft_optimizer.py
```

### Option 2: Standalone EXE (Make it yourself)

```bash
pip install pyinstaller
pyinstaller --onefile --windowed minecraft_optimizer.py
```

Exe `dist` folder mein milega.

## How to Use

### 1. Network Optimization
- Tab: "Network" kholo
- Checkboxes select karo (sabhi recommended hain)
- "Apply Network Optimizations" button dabao
- ⚠️ **Admin Rights required!**

### 2. Java Arguments
- Tab: "Java Arguments" kholo
- Text box se copy karo (or manually select)
- "Copy to Clipboard" button dabao
- Launcher kholo → Settings → JVM Arguments
- Paste karo

### 3. Windows Settings
- Tab: "Windows Settings" kholo
- Options select karo
- "Apply Windows Optimizations" button dabao
- **Restart dena padh sakta hai**

### 4. Minecraft Settings
- Tab: "Minecraft Settings" kholo
- In-game settings manually configure karo
- Ya **OptiFine** use karo auto-optimization ke liye

## Recommended Settings

### Network (All enabled)
```
RSS: Enabled
Autotune: Normal
Timestamps: Disabled
```

### Java Arguments (Paste in Launcher)
```
-XX:+UseG1GC
-XX:+UnlockExperimentalVMOptions
-XX:MaxGCPauseMillis=100
-XX:+DisableExplicitGC
-XX:TargetSurvivorRatio=90
-XX:G1NewSizePercent=50
-XX:G1MaxNewSizePercent=80
-XX:G1HeapRegionSize=16m
-XX:InitiatingHeapOccupancyPercent=10
-XX:G1ReservePercent=15
-Dfml.earlyProgressWindow=false
```

### Minecraft In-Game
- Render Distance: 8
- Particles: Minimal (0)
- GUI Scale: Small
- View Bobbing: Off
- Simulation Distance: 8
- VSync: Off
- Fullscreen: On

### Mouse Settings
- DPI: 400-800
- In-game Sensitivity: 0.5-1.0
- Windows Pointer Speed: 6/11

## Tips for Better Hit Registration

1. **Mods use karo (Legit):**
   - OptiFine
   - Sodium (Fabric)
   - BadLion Client

2. **Practice:**
   - W-tapping practice
   - Combo drills
   - Sensitivity adjustment

3. **Hardware:**
   - Ethernet use karo (WiFi se better)
   - Wired mouse use karo
   - Big mousepad lo

4. **Network:**
   - Stable connection ensure karo
   - Background downloads off karo
   - VPN use karo (agar ISP throttle kar raha hai)

## Troubleshooting

### "Admin Rights required"
- Right-click → "Run as administrator"

### Settings not applying
- Restart Windows
- Check if antivirus block kar rahe hai

### Lag issues persist
- Server ping check karo (multiplayer screen mein)
- Render distance reduce karo further
- OptiFine install karo

## Performance Impact

Expected improvements after optimization:
- **Latency:** 5-15ms reduction
- **FPS:** 20-50 FPS improvement (depends on PC)
- **Hitboxes:** Better registration (network optimizations se)

## Disclaimer

- Backups lelo before major changes
- Some optimizations require restart
- Ban nahi hote (sirf performance optimize hai)
- Server rules check karo (mods ke liye)

## Version

**v1.1** - October 2026 - Packet Optimization Added

---

Made for Minecraft 1.8.9 PvP players 🎯
