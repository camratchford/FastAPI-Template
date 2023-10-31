



$Body = @"
{"email": "king.arthur@camelot.bt", "first_name": "Cam", "last_name": "ratchford"}
"@

$Params = @{

    Method      = "GET"
    Body = $Body
    StatusCodeVariable = "SCV"
    ErrorAction = "SilentlyContinue"

}
$Sess
$Result = Invoke-RestMethod -Uri "http://127.0.0.1:8080/auth/register" -Body $Body -Headers $Headers -Method Post -ContentType "application/json" -WebSession $sess -SessionVariable $sessipconfig
