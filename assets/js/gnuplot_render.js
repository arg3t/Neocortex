
function GnuplotRenderer() {};

GnuplotRenderer.render = function(img, script){
  let gnuplot = new Gnuplot(gnuplot_link);
  let settings = GnuplotRenderer.terminalSettingsLight;
  if (localStorage.getItem('theme') == "dark"){
    settings = GnuplotRenderer.terminalSettingsDark;
  }
  gnuplot.run(settings + script, function(e) {
    gnuplot.getFile('out.svg', function(e) {
        if (!e.content) {
                 console.error("Output file out.svg not found!");
                 return;
             }
             try {
          var ab = new Uint8Array(e.content);
          var blob = new Blob([ab], {"type": "image\/svg+xml"});
          window.URL = window.URL || window.webkitURL;
          img.src = window.URL.createObjectURL(blob);
             } catch (err) { // in case blob / URL missing, fallback to data-uri
                  var rstr = '';
                for (var i = 0; i < e.content.length; i++)
                  rstr += String.fromCharCode(e.content[i]);
                img.src = 'data:image\/svg+xml;base64,' + btoa(rstr);
             }
         });
    });
}

GnuplotRenderer.renderPage = function(el){
  for(let container of document.querySelectorAll(".gnuplot")){
    let img = container.querySelector(".output");
    let script = container.querySelector(".code").innerHTML;
    GnuplotRenderer.render(img, script)
  }
}

GnuplotRenderer.terminalSettingsLight = `
set terminal svg size 400,300 enhanced fname 'arial'  fsize 10 butt solid
set output 'out.svg'

set xzeroaxis
set yzeroaxis
set zzeroaxis

set border 0
set xtics axis
set ytics axis

set xtics add ("" 0)
set ytics add ("" 0)

set tics scale 0.4

set style line 50 lt 1 lc rgb "black" lw 1
set key textcolor rgb "black"

set border ls 50
set xzeroaxis ls 50
set yzeroaxis ls 50
`

GnuplotRenderer.terminalSettingsDark = `
set terminal svg size 400,300 enhanced fname 'arial'  fsize 10 butt solid
set output 'out.svg'

set xzeroaxis
set yzeroaxis
set zzeroaxis

set border 0
set xtics axis
set ytics axis

set xtics add ("" 0)
set ytics add ("" 0)

set tics scale 0.4

set style line 50 lt 1 lc rgb "white" lw 1
set key textcolor rgb "white"

set border ls 50
set xzeroaxis ls 50
set yzeroaxis ls 50
`
