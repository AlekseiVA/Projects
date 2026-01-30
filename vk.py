# Требуемая библиотека pip install psutil

import time
import psutil
import winreg
from pathlib import Path

CHECK_INTERVAL = 60  # 1 минута
TOTAL_CHECKS = 5    # 5 минут


def get_steam_path():
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Valve\Steam"
        )
        steam_path, _ = winreg.QueryValueEx(key, "SteamPath")
        return Path(steam_path)
    except Exception:
        return None


def get_active_download_game(steam_path: Path):
    """
    Пытаемся определить активную загрузку по логам Steam
    """
    log_file = steam_path / "logs" / "content_log.txt"
    if not log_file.exists():
        return "Неизвестно"

    try:
        with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()[-200:]
            for line in reversed(lines):
                if "Downloading" in line or "Starting download" in line:
                    return line.strip()
    except Exception:
        pass

    return "Игра не определена"


def get_steam_network_speed():
    """
    Считаем сетевую активность steam.exe
    """
    steam_procs = []
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and "steam" in proc.info['name'].lower():
            steam_procs.append(proc)

    if not steam_procs:
        return 0

    bytes_recv_1 = 0
    for p in steam_procs:
        try:
            io = p.net_io_counters()
            if io:
                bytes_recv_1 += io.bytes_recv
        except Exception:
            pass

    time.sleep(1)

    bytes_recv_2 = 0
    for p in steam_procs:
        try:
            io = p.net_io_counters()
            if io:
                bytes_recv_2 += io.bytes_recv
        except Exception:
            pass

    speed_bytes_per_sec = bytes_recv_2 - bytes_recv_1
    speed_mbps = (speed_bytes_per_sec * 8) / (1024 * 1024)

    return max(speed_mbps, 0)


def is_download_paused(speed_mbps):
    return speed_mbps < 0.1


def main():
    steam_path = get_steam_path()
    if not steam_path:
        print("Steam не найден в реестре.")
        return

    print(f"Steam найден: {steam_path}")
    print("Начинаю мониторинг загрузок...\n")

    for i in range(TOTAL_CHECKS):
        game_info = get_active_download_game(steam_path)
        speed = get_steam_network_speed()

        if is_download_paused(speed):
            status = "Пауза или нет активной загрузки"
        else:
            status = "Загрузка активна"

        print(f"[{i+1}/5]")
        print(f"Игра: {game_info}")
        print(f"Скорость загрузки: {speed:.2f} Mbps")
        print(f"Статус: {status}")
        print("-" * 50)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()