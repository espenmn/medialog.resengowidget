(function(){var k=function(a,c,d,b){if(a.getElementById(d)){if(b){var e=100;var f=function(){setTimeout(function(){e--;if(window.RESENGO_WIDGET_SCRIPT_LOADED)b();else if(0<e)f();else throw Error("resengo script failed to load");},100)};f()}}else{var g=a.getElementsByTagName(c)[0];a=a.createElement(c);a.id=d;a.src="https://resengocomgeneralpurpose.blob.core.windows.net/resengowidget/resengo-widget.base.js";b&&(a.onload=b);g.parentNode.insertBefore(a,g)}},h=function(){return k(document,"script","resengo-flow-widget-script",function(){RESENGO_WIDGET({companyId:"1755231",language:"NL"})})};
window.attachEvent?window.attachEvent("onload",h):window.addEventListener("load",h,!1)})();