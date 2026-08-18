import subprocess

task_name = "LifeNote_Daily_Reminder"
ps_cmd = f'''
$Action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-WindowStyle Hidden -Command "[void][System.Reflection.Assembly]::LoadWithPartialName(\\\"System.Windows.Forms\\\"); $n = New-Object System.Windows.Forms.NotifyIcon; $n.Icon = [System.Drawing.SystemIcons]::Information; $n.Visible = $true; $n.ShowBalloonTip(5000, \\\"Life Note 일기 작성 시간 ✨\\\", \\\"오늘 하루의 소중한 순간들을 라이프 노트에 기록해 보세요.\\\", [System.Windows.Forms.ToolTipIcon]::Info)"'
$Trigger = New-ScheduledTaskTrigger -Daily -At 9:00PM
Register-ScheduledTask -TaskName "{task_name}" -Action $Action -Trigger $Trigger -Description "Life Note 매일 일기 알림" -Force
Write-Host "Daily reminder scheduled successfully!"
'''

with open('c:\\Users\\김용남\\Desktop\\난중일기\\register_reminder.ps1', 'w', encoding='utf-8-sig') as f:
    f.write(ps_cmd)

try:
    subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', 'c:\\Users\\김용남\\Desktop\\난중일기\\register_reminder.ps1'], check=True)
    print("Scheduled task registered successfully!")
except Exception as e:
    print("Scheduled task note:", e)
