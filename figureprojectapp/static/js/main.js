$(document).ready(function() {
	$(".lienvisible").click(function(event) {
		$(event.currentTarget).show();
	    var val_link = $(event.currentTarget).attr('href'); 
	    console.log(val_link);
	    $(val_link).toggle();
	});
	// si un hash est présent, on simule le clic sur le lien correspondant
    var hash = window.location.hash;
    if(hash) {
        var lien = $('[href="'+hash+'"]')
        console.log(lien);
        lien.click();
    }
	if ($(window).width() < 360) {
		console.log('petit');
		$(".hide").hide(); 
	}
	else if ($(window).width() < 1024) {
		console.log('moyen');
		$("#menu-principal").removeClass("hide");
		$("#oeuvres").addClass("hide");
		$(".hide").hide(); 
	}
	else {
		console.log('grand');
		// jquery.mousewheel.min.js pour le scroll horizontal
		$('html, body, *').on('mousewheel', function(e, delta) {
			this.scrollLeft -= (delta * 40);
			e.preventDefault();
		});
		// custom scrollbar
		/*$("#note").mCustomScrollbar({
    		theme:"rounded-dark",
    		scrollButtons:{
     		 	enable: true // on choisit d'afficher les flèches haut et bas
    		}
		});*/
		$("#note").removeClass("hide");
		$("#menu-principal").removeClass("hide");
		$("#oeuvres").removeClass("hide");
		$("#calendrier").removeClass("hide");
		$("#diffusion").addClass("hide");
		$("a[href=#note]").css("display:none;");
		$(".hide").hide(); 
	}
	/* tester avec un if et un else, puis un autre if */
});