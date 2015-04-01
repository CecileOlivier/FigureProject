$(document).ready(function() {
	$(".lienvisible").click(function(event) {
		$(event.currentTarget).show();
	    var val_link = $(event.currentTarget).attr('href'); 
	    console.log('clic sur '+val_link);
	    $(val_link).toggle();
	    //$("a h2").removeClass('active');
	    //$("a h2").css("color", "#3D3D3F");
	    $("a").removeClass('active');
	    //$("a h2:after").css("color", "#3E3D3F");
	    //$("a[href="+val_link+"] > h2").addClass('active');
	    //$("a[href="+val_link+"] > h2").css("color", "#E1001A");
	    $("a[href="+val_link+"]").addClass('active');
	    console.log("a[href="+val_link+"]");
	});
	/* simulation du clic pour les couleurs */
	var chemin = window.location.pathname;
	var chemin2 = chemin.replace(/^.(\s+)?/, '');
	var chemin3 = chemin2.replace(/(\s+)?.$/, '');
    console.log('le chemin est  '+chemin3);
    if(chemin) {
    	console.log(chemin3);
    	//$("li a[href='biographie]").addClass('active');
    	$('li a[href="{% url '+chemin3+' %}]').addClass('active');
    }
    /* media queries */
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
			console.log('je fais qqchose');
			e.preventDefault();
		});
		// custom scrollbar
		$("#note").mCustomScrollbar({
    		theme:"rounded-dark",
    		scrollButtons:{
     		 	enable: true // affichage flèches haut et bas
    		}
		});
		$("#note").removeClass("hide");
		$("#menu-principal").removeClass("hide");
		$("#oeuvres").removeClass("hide");
		$("#calendrier").removeClass("hide");
		$("#diffusion").addClass("hide");
		$("a[href=#note] > h2").css("display", "none");
		$(".hide").hide(); 
	}
});