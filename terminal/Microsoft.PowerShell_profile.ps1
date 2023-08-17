oh-my-posh init pwsh --config 'C:\Users\strat\AppData\Local\Programs\oh-my-posh\themes\andora.omp.json' | Invoke-Expression

Import-Module Terminal-Icons
Import-Module PSReadLine
Set-PSReadLineKeyHandler -Key Tab -Function Complete
Set-PSReadLineOption -PredictionViewStyle ListView

#Functions
function whereis ($command) {
    Get-Command -Name $command -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Path -ErrorAction SilentlyContinue
}

function hclear () {
    Remove-Item (Get-PSReadlineOption).HistorySavePath
}

function hcode () {
    code 'C:\Users\strat\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt'
}

function Leauge () {
    start "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\League of Legends.lnk"
}

function YouTube() {
    start https://youtube.com/
}