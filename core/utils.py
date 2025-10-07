import json
import subprocess


def get_disks_info():
    ps_command = "Get-PhysicalDisk | Select-Object FriendlyName, MediaType, SerialNumber | ConvertTo-Json"
    result = subprocess.run(
        ["powershell", "-Command", ps_command],
        capture_output=True,
        text=True
    )
    try:
        disks = json.loads(result.stdout)
    except json.JSONDecodeError:
        return []
    if isinstance(disks, dict):
        disks = [disks]
    formatted_disks = []
    for d in disks:
        formatted_disks.append({
            "model": d.get("FriendlyName", ""),
            "serial": d.get("SerialNumber", ""),
            "type": d.get("MediaType", "Unknown")
        })
    return formatted_disks
