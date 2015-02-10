$(document).ready(function() {

	if (window.matchMedia("(min-width: 320px) and (max-width: 765px)").matches) {
		console.log('je fonctionne en petit');		
		//$("a[href=#oeuvres]").attr("href", "oeuvre.html");
		$(".hide").hide(); 
		$(".lienvisible").click(function(event) {
			console.log('je fais toujours qqchose');
	        $(event.currentTarget).show();
	        console.log(event.currentTarget);
	        // on récupère le lien
	        var val_link = $(event.currentTarget).attr('href'); 
	        console.log(val_link);
	        // on affiche le lien
	        $(val_link).toggle();
		});
	}
	else if (window.matchMedia("(min-width: 768px) and (max-width: 1023px)").matches) {
		$("#menu-principal").removeClass("hide");
		$("#oeuvres").addClass("hide");
		$(".hide").hide(); 
		$(".lienvisible").click(function(event) {
	        $(event.currentTarget).show();
	        var val_link = $(event.currentTarget).attr('href'); 
	        $(val_link).toggle();
		});
		console.log('je fonctionne en tablette et +');
	}
	else { 
		// plugin jquery.mousewheel.min.js pour le scroll horizontal
		$('html, body, *').mousewheel(function(e, delta) {
			this.scrollLeft -= (delta * 40);
			e.preventDefault();
		});
		// custom scrollbar
		$("#note").mCustomScrollbar({
    		theme:"rounded-dark",
    		scrollButtons:{
     		 	enable: true // on choisit d'afficher les flèches haut et bas
    		}
		});
		console.log('je fonctionne en desktop');
		$("#note").removeClass("hide");
		$("#menu-principal").removeClass("hide");
		$("#oeuvres").addClass("hide");
		$("a[href=#note]").css("display:none;");
		$(".hide").hide(); 
		$(".lienvisible").click(function(event) {
	        $(event.currentTarget).show();
	        var val_link = $(event.currentTarget).attr('href'); 
	        $(val_link).toggle();
		});
	}
});