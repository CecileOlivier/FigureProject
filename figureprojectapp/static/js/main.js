$(document).ready(function() {
	if ($(window).width() < 360) {
		console.log('petit');
		$(".hide").hide(); 
		$(".lienvisible").click(function(event) {
	        var val_link = $(event.currentTarget).attr('href'); 
	        console.log(val_link);
	        $(val_link).toggle();
		});
	}
	else if ($(window).width() < 1024) {
		console.log('moyen');
		$("#menu-principal").removeClass("hide");
		$("#oeuvres").addClass("hide");
		$(".hide").hide(); 
		$(".lienvisible").click(function(event) {
	        $(event.currentTarget).show();
	        var val_link = $(event.currentTarget).attr('href'); 
	        $(val_link).toggle();
		});
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
		$("#oeuvres").addClass("hide");
		$("#calendrier").addClass("hide");
		$("#diffusion").addClass("hide");
		$("a[href=#note]").css("display:none;");
		$(".hide").hide(); 
		$(".lienvisible").click(function(event) {
	        var val_link = $(event.currentTarget).attr('href'); 
	        $(val_link).toggle();
		});
		$(".lienvisiblemenu").click(function(event) {
	        var val_link_menu = $(event.currentTarget).attr('href'); 
	        var val_link_menu2 = val_link_menu.substring(1);
	        $(val_link_menu2).toggle();
		});
	}
});