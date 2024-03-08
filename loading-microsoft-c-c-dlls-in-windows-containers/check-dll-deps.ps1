# Define an array of DLL filenames to check
$dllNames = @(
    'MSVCP140.dll',
    'VCRUNTIME140_1.dll',
    'VCRUNTIME140.dll',
    'api-ms-win-crt-runtime-l1-1-0.dll',
    'KERNEL32.dll'
)

# Define the system directory to check in, typically System32 for system DLLs
$systemDir = [System.Environment]::SystemDirectory

# Iterate over each DLL name in the array
foreach ($dllName in $dllNames) {
    # Construct the full path to where the DLL should be located
    $fullPath = Join-Path -Path $systemDir -ChildPath $dllName
    
    # Check if the file exists
    if (Test-Path -Path $fullPath) {
        Write-Output "$dllName exists."
    } else {
        Write-Output "$dllName does NOT exist."
    }
}