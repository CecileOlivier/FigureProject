$(document).ready(function() {
	$(".lienvisible").click(function(event) {
		$(".hide").hide();
		$(event.currentTarget).show();
	    var val_link = $(event.currentTarget).attr('href'); 
	    console.log('clic sur '+val_link);
	    $(val_link).show();
	    $("a").removeClass('active');
	    $("a[href="+val_link+"]").addClass('active');
	    console.log("a[href="+val_link+"]");
	});
    // media queries 
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
		// affichage du calendrier
		//$("div .annee").hide();
		$(".lienvisible").click(function(event) {
			$(event.currentTarget).show();
			//$("div .annee").show();
		    var val_link = $(event.currentTarget).attr('href'); 
		    console.log('clic sur '+val_link);
		    $(val_link).show();
		    console.log("a[href="+val_link+"]");
		});
		// jquery.mousewheel.min.js pour le scroll horizontal
		$('html, body, *').on('mousewheel', function(e, delta) {
			this.scrollLeft -= (delta * 40);
			console.log('je fais qqchose');
			e.preventDefault();
		});
		// custom scrollbar
		$("#note").mCustomScrollbar({
    		theme:"rounded-dark",
    		scrollButtons:{
     		 	enable: true
    		}
		});
		$("#note").removeClass("hide");
		$("#menu-principal").removeClass("hide");
		$("#oeuvres").removeClass("hide");
		//$("#calendrier").removeClass("hide");
		$("#diffusion").addClass("hide");
		$("a[href=#note] > h2").css("display", "none");
		$(".hide").hide(); 
	}
});