Get-CimInstance -ClassName Win32_Desktop | out-file info_escritorio.txt
Get-CimInstance -ClassName Win32_BIOS | out-file info_BIOS.txt
Get-CimInstance -ClassName Win32_Processor | Select-Object -ExcludeProperty "CIM*" | out-file info_procesador.txt
Get-CimInstance -ClassName Win32_ComputerSystem | out-file info_modelo.txt
Get-CimInstance -ClassName Win32_QuickFixEngineering | out-file info_versiones_instaladas.txt
Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object -Property Build*,OSType,ServicePack* | out-file info_version.txt
Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object -Property *user* | out-file info_usuarios.txt
Get-CimInstance -ClassName Win32_LogicalDisk -Filter "DriveType=3" | out-file info_discos.txt
Get-CimInstance -ClassName Win32_LogonSession | out-file info_logon.txt
