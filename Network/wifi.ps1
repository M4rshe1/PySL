function Set-CultureWin([System.Globalization.CultureInfo] $culture) {
    [System.Threading.Thread]::CurrentThread.CurrentUICulture = $culture
    [System.Threading.Thread]::CurrentThread.CurrentCulture = $culture
}
Set-CultureWin en-US ; [system.threading.thread]::currentthread.currentculture
$profile_names = ((netsh wlan show profiles).split("`n") | where-object { $_.contains(" : ") }) -replace ".*: ", "" | ForEach-Object { $_.trim() }

$profiles = @()

$profile_names | ForEach-Object {
    $profile = (netsh wlan show profile name = $_ key = clear).split("`n") | where-object { $_.contains(" : ") }
    $ProfileObject = [PSCustomObject]@{ }
    $profile | ForEach-Object {
#        replce special characters and umlauts


        $key = $_.split(":")[0].trim().ToLower().replace("ü", "ue").replace("ä", "ae").replace("ö", "oe").replace("ß", "ss")
        $value = $_.split(":")[1].trim()
        $ProfileObject | Add-Member -MemberType NoteProperty -Name $key -Value $value -Force
    }

    $ProfileObject | ConvertTo-Json -Depth 100

    $profiles += [PSCustomObject]@{
        SSID = $ProfileObject.Name
        Key = $ProfileObject.$("schlüsselinhalt")
    }
}

$profiles | ConvertTo-Json -Depth 100
