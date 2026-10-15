# 🎮 Minecraft Optimizer Pro

All-in-one optimization tool for Minecraft 1.8.9 PvP. Optimize Network, Java, Windows, and in-game settings!

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
- FPS drops minimized

✅ **Windows Optimization**
- Game Mode disable
- Power plan setup
- Audio service optimization
- DNS cache flush

✅ **Mouse & Input Optimization**
- Input lag removal
- 1000Hz polling rate
- Disable pointer trails
- Enhanced precision disabled

✅ **System Cleanup**
- Temp files cleaner
- Shader cache cleaner
- Browser cache cleanup
- Minecraft logs cleanup

✅ **Minecraft Settings Guide**
- Render distance optimization
- Particle settings
- GUI scaling
- Performance tips

## 100+ Optimizations Included

### Network (10+)
- DNS Server (Cloudflare/Google)
- Network Latency Reduction
- Packet Optimization
- Internet Speed Tuning
- RSS, AutoTune, Timestamps
- MTU Optimization
- Nagle Algorithm Disabled

### System (40+)
- Disable 40+ Unnecessary Services
- Registry Cleaner for Java
- Windows Defender Exclusions
- Gaming Mode Optimization
- High Performance Power Plan
- Disable Visual Effects
- Background Apps Disabled
- Telemetry Disabled
- Xbox Services Disabled

### Input (15+)
- Mouse Input Lag Removal
- Keyboard Repeat Rate Boost
- Disable Pointer Trails
- Disable Enhanced Precision
- Disable Acceleration
- 1000Hz Polling Rate
- Disable Sticky/Filter/Toggle Keys

### Cleanup (15+)
- User Temp Files
- System Temp Files
- Prefetch Files
- Browser Caches
- GPU Shader Cache
- Minecraft Logs & Crash Reports

## Requirements

- Windows 10/11
- Python 3.7+ (for GUI versions)
- **Administrator Rights** (required for network/system optimizations)

## Installation

### Option 1: Python GUI (Recommended)

```bash
# Install Python first if not installed
python minecraft_optimizer_pro.py
```

### Option 2: Batch Script

```bash
# Just run as Administrator
minecraft_optimizer_ultimate.bat
```

### Option 3: Standalone EXE

```bash
pip install pyinstaller
pyinstaller --onefile --windowed minecraft_optimizer_pro.py
```

The exe will be in the `dist` folder.

## How to Use

### Option 1: Modern GUI (Best Experience)
```
Run: python minecraft_optimizer_pro.py
- Select optimizations from sidebar
- Click "Apply" buttons
- Restart PC when done
```

### Option 2: Batch Script (Fastest)
```
1. Right-click minecraft_optimizer_ultimate.bat
2. Click "Run as administrator"
3. Choose option 20 for "Apply All"
4. Restart PC
```

### Option 3: Individual Features
```
1. Run the tool
2. Choose specific category from menu
3. Apply individual optimizations
4. Restart if required
```

## Recommended Settings

### Network (All enabled)
```
RSS: Enabled
Autotune: Normal
Timestamps: Disabled
MTU: 1300
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
-Xmx4G -Xms2G
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

1. **Use Legit Mods:**
   - OptiFine
   - Sodium (Fabric)
   - Badlion Client

2. **Practice:**
   - W-tapping practice
   - Combo drills
   - Sensitivity adjustment

3. **Hardware:**
   - Use Ethernet (better than WiFi)
   - Use wired mouse
   - Use big mousepad

4. **Network:**
   - Ensure stable connection
   - Turn off background downloads
   - Use VPN if ISP is throttling

## Troubleshooting

### "Admin Rights required"
- Right-click → "Run as administrator"

### Settings not applying
- Restart Windows
- Check if antivirus is blocking

### Lag issues persist
- Check server ping (in multiplayer screen)
- Reduce render distance further
- Install OptiFine

## Performance Impact

Expected improvements after optimization:
- **Latency:** 5-15ms reduction
- **FPS:** 20-50 FPS improvement (depends on PC)
- **Hit Registration:** Significantly better
- **Input Delay:** Reduced by 5-10ms

## Files Included

```
MinecraftOptimizer/
├── minecraft_optimizer_ultimate.bat (Ultimate - 100+ features)
├── minecraft_optimizer_ultimate.py  (GUI - 100+ features)
└── README.md                        (This file)
```

## Disclaimer

- Take backups before major changes
- Some optimizations require restart
- This is performance optimization only (no cheats)
- Check server rules for allowed mods

## Version

**v3.0** - October 2026 - 100+ Optimizations Added

---

Made for Minecraft 1.8.9 PvP players 🎯
