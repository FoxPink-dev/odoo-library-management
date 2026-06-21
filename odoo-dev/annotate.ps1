$DIR = "$env:TEMP\odoo_screenshots"
$OUT = "$DIR\annotated"
$TMP = "$env:TEMP\odoo_annotate_tmp"
New-Item -ItemType Directory -Path $OUT -Force | Out-Null
New-Item -ItemType Directory -Path $TMP -Force | Out-Null

$MAGICK = "C:\ImageMagick\magick.exe"
$FONT = "C:\Windows\Fonts\arial.ttf"

$files = @(
    @{
        File = "01_wizard_form.png"
        Annots = @(
            @{x=250; y=110; w=280; h=35; num=1; label="From Date"},
            @{x=550; y=110; w=280; h=35; num=2; label="To Date"},
            @{x=250; y=180; w=600; h=35; num=3; label="Products"},
            @{x=250; y=215; w=280; h=35; num=4; label="Category"},
            @{x=550; y=215; w=280; h=35; num=5; label="Warehouse/Location"},
            @{x=300; y=300; w=140; h=35; num=6; label="Generate"},
            @{x=460; y=300; w=140; h=35; num=7; label="Print PDF"}
        )
    },
    @{
        File = "02_list_view.png"
        Annots = @(
            @{x=230; y=95; w=200; h=25; num=1; label="Product"},
            @{x=680; y=95; w=100; h=25; num=2; label="In/Out Qty"},
            @{x=870; y=95; w=100; h=25; num=3; label="Balance Qty"},
            @{x=1050; y=95; w=120; h=25; num=4; label="Unit Cost"},
            @{x=1180; y=95; w=140; h=25; num=5; label="Valuation"}
        )
    },
    @{
        File = "03_graph_view.png"
        Annots = @(
            @{x=300; y=200; w=800; h=400; num=1; label="Chart area"},
            @{x=250; y=550; w=600; h=80; num=2; label="Measure/Group By"},
            @{x=190; y=120; w=80; h=200; num=3; label="Date axis"}
        )
    },
    @{
        File = "04_pivot_view.png"
        Annots = @(
            @{x=230; y=95; w=200; h=30; num=1; label="Row: Product"},
            @{x=600; y=95; w=400; h=30; num=2; label="Col: Date"},
            @{x=500; y=150; w=450; h=350; num=3; label="Measures area"}
        )
    },
    @{
        File = "05_menu_location.png"
        Annots = @(
            @{x=10; y=48; w=210; h=25; num=1; label="Inventory menu"},
            @{x=10; y=310; w=210; h=20; num=2; label="Reporting section"},
            @{x=10; y=330; w=210; h=25; num=3; label="Stock Card Report"}
        )
    }
)

function New-DrawScript {
    param($annots)
    $lines = @()
    $lines += "push defs"
    
    foreach ($a in $annots) {
        $x = $a.x; $y = $a.y; $w = $a.w; $h = $a.h
        $cx = $x - 10; $cy = $y - 10
        $label = $a.label
        $num = $a.num
        
        # Rectangle
        $lines += "stroke red stroke-width 3 fill none"
        $lines += "rectangle $x,$y $(($x+$w)),$(($y+$h))"
        
        # Red circle
        $lines += "fill red stroke red stroke-width 2"
        $lines += "circle $cx,$cy $(($cx+14)),$cy"
        
        # White inner circle
        $lines += "fill white stroke none"
        $lines += "circle $cx,$cy $(($cx+11)),$cy"
        
        # Number text
        $lines += "fill red stroke none"
        $lines += "text $($cx-5),$($cy+5) '$num'"
        
        # Label text
        $lines += "fill red stroke none"
        $lines += "text $($cx+22),$($cy+5) '$label'"
    }
    
    $lines += "pop defs"
    return $lines -join "`n"
}

foreach ($f in $files) {
    $inputFile = "$DIR\$($f.File)"
    $outputFile = "$OUT\$($f.File)"
    
    if (-not (Test-Path $inputFile)) {
        Write-Host "SKIP: $($f.File) not found"
        continue
    }
    
    Write-Host "Annotating: $($f.File) ... " -NoNewline
    
    # Write draw script to temp file
    $drawScript = New-DrawScript $f.Annots
    $scriptFile = "$TMP\$($f.File -replace 'png','txt')"
    Set-Content -Path $scriptFile -Value $drawScript -Encoding ASCII
    
    # Run ImageMagick
    & $MAGICK convert "`"$inputFile`"" -font "`"$FONT`"" -pointsize 14 -draw "@$scriptFile" "`"$outputFile`"" 2>&1 | Out-Null
    
    $sz = (Get-Item $outputFile).Length
    Write-Host "DONE ($([math]::Round($sz/1KB,0)) KB)"
}

# Cleanup
Remove-Item $TMP -Recurse -Force -ErrorAction SilentlyContinue

Write-Host "`n=== Annotated files ==="
Get-ChildItem $OUT | Select-Object Name, @{N='KB';E={[math]::Round($_.Length/1KB,0)}}
