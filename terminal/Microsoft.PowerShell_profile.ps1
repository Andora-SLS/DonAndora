oh-my-posh init pwsh --config 'C:\Users\strat\AppData\Local\Programs\oh-my-posh\themes\andora.omp.json' | Invoke-Expression
#oh-my-posh init pwsh --config 'C:\Users\strat\AppData\Local\Programs\oh-my-posh\themes\emodipt-extend.omp.json' | Invoke-Expression

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

function pcode() {
    code 'C:\Users\strat\Documents\PowerShell\Microsoft.PowerShell_profile.ps1'
}

function christitustool() {
    iwr -useb https://christitus.com/win | iex
}
