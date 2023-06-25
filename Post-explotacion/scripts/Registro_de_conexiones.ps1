$hostname = hostname
$logs = get-eventlog system -ComputerName $hostname -source Microsoft-Windows-Winlogon -After (Get-Date).AddDays(-90);
$res = @(); ForEach ($log in $logs) {if($log.instanceid -eq 7001) {$type = "Logon"} Elseif ($log.instanceid -eq 7002){$type="Logoff"} Else {Continue} $res += New-Object PSObject -Property @{Time = $log.TimeWritten; "Event" = $type; User = (New-Object System.Security.Principal.SecurityIdentifier $Log.ReplacementStrings[1]).Translate([System.Security.Principal.NTAccount])}};
$res | Export-Csv -Path .\Info_login_sessions.csv -NoTypeInformation