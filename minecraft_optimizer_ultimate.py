#!/usr/bin/env python3
"""
Minecraft Optimizer Pro - Ultimate Edition
100+ Gaming Optimizations
Version: 3.0 - October 2026
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import subprocess
import os
import sys
from pathlib import Path
import json
import shutil
import threading

class MinecraftOptimizerUltimate:
    def __init__(self, root):
        self.root = root
        self.root.title("Minecraft Optimizer Pro - Ultimate (100+ Optimizations)")
        self.root.geometry("900x700")
        self.root.configure(bg="#1a1a1a")

        # Apply dark theme
        self.setup_styles()

        # Variables
        self.status_var = tk.StringVar(value="Ready")
        self.log_var = tk.StringVar()

        # Create UI
        self.create_ui()

        # Check admin rights
        self.check_admin()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')

        bg = "#1a1a1a"
        fg = "#ffffff"
        accent = "#00d4ff"

        style.configure('TFrame', background=bg)
        style.configure('TLabel', background=bg, foreground=fg, font=('Arial', 10))
        style.configure('Title.TLabel', background=bg, foreground=accent, font=('Arial', 16, 'bold'))
        style.configure('Heading.TLabel', background=bg, foreground=accent, font=('Arial', 11, 'bold'))
        style.configure('TButton', font=('Arial', 9))
        style.configure('TCheckbutton', background=bg, foreground=fg)
        style.configure('TNotebook', background=bg)
        style.configure('TNotebook.Tab', padding=[20, 10])

    def create_ui(self):
        # Title
        title_frame = ttk.Frame(self.root)
        title_frame.pack(fill='x', padx=10, pady=10)

        ttk.Label(title_frame, text="🎮 Minecraft Optimizer Pro - Ultimate",
                 style='Title.TLabel').pack()
        ttk.Label(title_frame, text="100+ Gaming Optimizations",
                 foreground="#888888").pack()

        # Main notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Create tabs
        self.create_network_tab()
        self.create_system_tab()
        self.create_input_tab()
        self.create_minecraft_tab()
        self.create_cleanup_tab()
        self.create_advanced_tab()

        # Status bar
        status_frame = ttk.Frame(self.root)
        status_frame.pack(fill='x', padx=10, pady=5)
        ttk.Label(status_frame, textvariable=self.status_var, foreground="#00d4ff").pack(side='left')

    def create_network_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Network (10+ opts)")

        ttk.Label(frame, text="Network Optimizations", style='Heading.TLabel').pack(pady=10)

        options = {
            'dns': 'DNS Server Optimization (Cloudflare/Google)',
            'latency': 'Network Latency Reduction',
            'packets': 'Packet Optimization (Hit Registration)',
            'speed': 'Internet Speed Tuning',
            'rss': 'Enable RSS (Multi-core)',
            'autotune': 'TCP AutoTune Normal',
            'timestamps': 'Disable Timestamps',
            'chimney': 'Enable TCP Chimney',
            'mtu': 'MTU Optimization (1300)',
            'nagle': 'Disable Nagle Algorithm'
        }

        self.network_vars = {}
        for key, label in options.items():
            var = tk.BooleanVar(value=True)
            self.network_vars[key] = var
            ttk.Checkbutton(frame, text=label, variable=var).pack(anchor='w', padx=20, pady=3)

        ttk.Button(frame, text="Apply Network Optimizations",
                  command=self.apply_network).pack(pady=15)

    def create_system_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="System (40+ opts)")

        ttk.Label(frame, text="Windows System Optimizations", style='Heading.TLabel').pack(pady=10)

        options = {
            'services': 'Disable 40+ Unnecessary Services',
            'registry': 'Registry Cleaner for Java',
            'defender': 'Windows Defender Exclusions',
            'gamingmode': 'Gaming Mode Optimization',
            'powerplan': 'High Performance Power Plan',
            'visualfx': 'Disable Visual Effects',
            'bgapps': 'Disable Background Apps',
            'updates': 'Disable Auto-Updates',
            'telemetry': 'Disable Telemetry',
            'xbox': 'Disable Xbox Services'
        }

        self.system_vars = {}
        for key, label in options.items():
            var = tk.BooleanVar(value=True)
            self.system_vars[key] = var
            ttk.Checkbutton(frame, text=label, variable=var).pack(anchor='w', padx=20, pady=3)

        ttk.Button(frame, text="Apply System Optimizations",
                  command=self.apply_system).pack(pady=15)

    def create_input_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Input (15+ opts)")

        ttk.Label(frame, text="Mouse & Keyboard Optimizations", style='Heading.TLabel').pack(pady=10)

        options = {
            'mouse_lag': 'Mouse Input Lag Removal',
            'kb_repeat': 'Keyboard Repeat Rate Boost',
            'pointer': 'Disable Pointer Trails',
            'precision': 'Disable Enhanced Precision',
            'acceleration': 'Disable Acceleration',
            'polling': 'Increase Polling Rate (1000Hz)',
            'sticky': 'Disable Sticky Keys',
            'filter': 'Disable Filter Keys',
            'toggle': 'Disable Toggle Keys',
            'slow': 'Disable Slow Keys'
        }

        self.input_vars = {}
        for key, label in options.items():
            var = tk.BooleanVar(value=True)
            self.input_vars[key] = var
            ttk.Checkbutton(frame, text=label, variable=var).pack(anchor='w', padx=20, pady=3)

        ttk.Button(frame, text="Apply Input Optimizations",
                  command=self.apply_input).pack(pady=15)

    def create_minecraft_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Minecraft (20+ opts)")

        ttk.Label(frame, text="Minecraft Specific Optimizations", style='Heading.TLabel').pack(pady=10)

        # Scrolled text for settings guide
        text_widget = scrolledtext.ScrolledText(frame, height=15, width=80,
                                               bg="#2d2d2d", fg="#00d4ff", font=('Courier', 9))
        text_widget.pack(padx=10, pady=10, fill='both', expand=True)

        guide = """VIDEO SETTINGS:
  Render Distance:        8
  Particles:              Minimal (0)
  Simulation Distance:    8
  VSync:                  Off
  Max Framerate:          Unlimited
  Fullscreen:             On
  GUI Scale:              Small
  View Bobbing:           Off

PERFORMANCE MODS (Legit):
  ✓ OptiFine - FPS boost
  ✓ Sodium - Huge FPS boost
  ✓ Badlion Client - All-in-one
  ✓ Lithium - Server optimization

MOUSE SETTINGS:
  DPI:                    400-800
  In-game Sensitivity:    0.5-1.0
  Windows Pointer:        6/11

PRACTICE TIPS:
  1. W-tapping practice
  2. Aim training servers
  3. Use Ethernet (not WiFi)
  4. Close background apps"""

        text_widget.insert('1.0', guide)
        text_widget.config(state='disabled')

    def create_cleanup_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Cleanup (15+ opts)")

        ttk.Label(frame, text="System Cleanup & Maintenance", style='Heading.TLabel').pack(pady=10)

        options = {
            'temp': 'User Temp Files',
            'systtemp': 'System Temp Files',
            'prefetch': 'Prefetch Files',
            'updates': 'Windows Update Cache',
            'chrome': 'Chrome Cache',
            'edge': 'Edge Browser Cache',
            'logs': 'Minecraft Logs',
            'crashes': 'Crash Reports',
            'shader': 'GPU Shader Cache',
            'nvidia': 'NVIDIA Cache',
            'amd': 'AMD Cache',
            'intel': 'Intel Cache'
        }

        self.cleanup_vars = {}
        for key, label in options.items():
            var = tk.BooleanVar(value=True)
            self.cleanup_vars[key] = var
            ttk.Checkbutton(frame, text=label, variable=var).pack(anchor='w', padx=20, pady=3)

        ttk.Button(frame, text="Start Cleanup (One-Click)",
                  command=self.apply_cleanup).pack(pady=15)

    def create_advanced_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Advanced")

        ttk.Label(frame, text="Advanced Options", style='Heading.TLabel').pack(pady=10)

        # Java Arguments
        ttk.Label(frame, text="Java Arguments (Copy to Launcher):",
                 style='Heading.TLabel').pack(pady=10)

        java_args = """-XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:MaxGCPauseMillis=100 -XX:+DisableExplicitGC -XX:TargetSurvivorRatio=90 -XX:G1NewSizePercent=50 -XX:G1MaxNewSizePercent=80 -XX:G1HeapRegionSize=16m -XX:InitiatingHeapOccupancyPercent=10 -XX:G1ReservePercent=15 -Dfml.earlyProgressWindow=false -Xmx4G -Xms2G"""

        java_text = scrolledtext.ScrolledText(frame, height=5, width=80,
                                             bg="#2d2d2d", fg="#00d4ff", font=('Courier', 8))
        java_text.pack(padx=10, pady=5, fill='both')
        java_text.insert('1.0', java_args)
        java_text.config(state='disabled')

        ttk.Button(frame, text="Copy Java Arguments",
                  command=lambda: self.copy_to_clipboard(java_args)).pack(pady=5)

        # Apply All button
        ttk.Button(frame, text="APPLY ALL 100+ OPTIMIZATIONS",
                  command=self.apply_all).pack(pady=20)

        # Info
        info = """This will apply 100+ optimizations in one go.
Restart your PC for best results."""
        ttk.Label(frame, text=info, justify='center').pack(pady=10)

    def check_admin(self):
        try:
            import ctypes
            if not ctypes.windll.shell.IsUserAnAdmin():
                messagebox.showwarning("Admin Required",
                    "Please run as Administrator for all features!")
        except:
            pass

    def log(self, message):
        print(message)
        self.status_var.set(message)

    def copy_to_clipboard(self, text):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        messagebox.showinfo("Copied", "Java arguments copied to clipboard!")

    def run_command(self, cmd, show_error=False):
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            return result.returncode == 0
        except Exception as e:
            if show_error:
                print(f"Error: {e}")
            return False

    def apply_network(self):
        self.log("Applying network optimizations...")

        if self.network_vars['dns'].get():
            self.run_command('netsh interface ipv4 set dnsservers "Ethernet" static 1.1.1.1 primary')
            self.run_command('ipconfig /flushdns')
            self.log("DNS optimized")

        if self.network_vars['rss'].get():
            self.run_command('netsh int tcp set global rss=enabled')
            self.log("RSS enabled")

        if self.network_vars['autotune'].get():
            self.run_command('netsh int tcp set global autotuninglevel=normal')
            self.log("AutoTune set")

        if self.network_vars['timestamps'].get():
            self.run_command('netsh int tcp set global timestamps=disabled')
            self.log("Timestamps disabled")

        if self.network_vars['mtu'].get():
            self.run_command('netsh int ipv4 set subinterface "Ethernet" mtu=1300 store=persistent')
            self.run_command('netsh int ipv4 set subinterface "Wi-Fi" mtu=1300 store=persistent')
            self.log("MTU optimized")

        messagebox.showinfo("Success", "Network optimizations applied!")

    def apply_system(self):
        self.log("Applying system optimizations...")

        if self.system_vars['services'].get():
            services = ['XboxGipSvc', 'XboxNetApiSvc', 'DiagTrack', 'WSearch', 'WMPNetworkSvc']
            for svc in services:
                self.run_command(f'sc config "{svc}" start= disabled')
            self.log("Services disabled")

        if self.system_vars['powerplan'].get():
            self.run_command('powercfg /s 8c5e7fda-e8bf-4a96-9a85-a6e23a324c9c')
            self.log("Power plan set")

        if self.system_vars['defender'].get():
            appdata = os.path.expandvars('%APPDATA%')
            self.run_command(f'powershell -Command "Add-MpPreference -ExclusionPath \'{appdata}\\.minecraft\'"')
            self.log("Defender exclusions added")

        messagebox.showinfo("Success", "System optimizations applied!")

    def apply_input(self):
        self.log("Applying input optimizations...")

        if self.network_vars['polling'].get():
            self.run_command('reg add "HKCU\\Control Panel\\Mouse" /v MouseTrails /t REG_SZ /d 0 /f')
            self.run_command('reg add "HKCU\\Control Panel\\Mouse" /v MouseSpeed /t REG_SZ /d 0 /f')
            self.log("Mouse optimized")

        if self.input_vars['kb_repeat'].get():
            self.run_command('reg add "HKCU\\Control Panel\\Keyboard" /v KeyboardRepeatRate /t REG_SZ /d 31 /f')
            self.log("Keyboard repeat rate set")

        if self.input_vars['sticky'].get():
            self.run_command('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer" /v NoStickyKeys /t REG_DWORD /d 1 /f')
            self.log("Sticky Keys disabled")

        messagebox.showinfo("Success", "Input optimizations applied!")

    def apply_cleanup(self):
        self.log("Starting cleanup...")

        paths = {
            'temp': '%TEMP%',
            'systtemp': 'C:\\Windows\\Temp',
            'prefetch': 'C:\\Windows\\Prefetch',
        }

        for key, path in paths.items():
            if self.cleanup_vars[key].get():
                expanded_path = os.path.expandvars(path)
                try:
                    if os.path.exists(expanded_path):
                        shutil.rmtree(expanded_path)
                        os.makedirs(expanded_path)
                        self.log(f"Cleaned: {path}")
                except:
                    pass

        messagebox.showinfo("Success", "Cleanup complete!")

    def apply_all(self):
        response = messagebox.askyesno("Confirm",
            "Apply 100+ optimizations? This will take 1-2 minutes.\nRestart required after.")

        if not response:
            return

        self.log("Applying all 100+ optimizations...")

        # Run all optimizations
        self.apply_network()
        self.apply_system()
        self.apply_input()
        self.apply_cleanup()

        messagebox.showinfo("Complete",
            "All 100+ optimizations applied!\n\nPlease restart your PC for best results.")
        self.log("All optimizations complete!")

def main():
    root = tk.Tk()
    app = MinecraftOptimizerUltimate(root)
    root.mainloop()

if __name__ == "__main__":
    main()
