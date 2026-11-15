; Inno Setup script: the Windows installer for ChumpMan 11D.
; Built by .github/workflows/release.yml from PyInstaller's dist\ChumpMan11D folder:
;   iscc /DAppVersion=1.0.0 packaging\chumpman11d.iss
; Installs for the current user only (no administrator rights), adds a Start-menu
; entry and an uninstaller (Settings > Apps).

#ifndef AppVersion
  #define AppVersion "0.0.0"
#endif

[Setup]
AppId={{E0583D45-0DA3-5628-9D7C-CA4EED37930E}
AppName=ChumpMan 11D
AppVersion={#AppVersion}
AppPublisher=Zachary Klaas
AppPublisherURL=https://github.com/zklaas/chumpman11d
DefaultDirName={localappdata}\Programs\ChumpMan11D
DefaultGroupName=ChumpMan 11D
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
OutputDir=..\release
OutputBaseFilename=ChumpMan11D-Setup-Windows
SetupIconFile=..\icons\chumpman11d.ico
UninstallDisplayIcon={app}\ChumpMan11D.exe
LicenseFile=..\LICENSE
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64compatible

[Files]
Source: "..\dist\ChumpMan11D\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs ignoreversion

[Icons]
Name: "{group}\ChumpMan 11D"; Filename: "{app}\ChumpMan11D.exe"
Name: "{userdesktop}\ChumpMan 11D"; Filename: "{app}\ChumpMan11D.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; Flags: unchecked

[Run]
Filename: "{app}\ChumpMan11D.exe"; Description: "Start ChumpMan 11D"; Flags: nowait postinstall skipifsilent
