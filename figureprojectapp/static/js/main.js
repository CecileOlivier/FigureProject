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
		var total = 0;
		var img = $('img.oeuvre-max').width();
		console.log('image ='+img);
		var pres = $('.presentation').width();
		console.log('presentation ='+pres);
		var sousmenu = $('.sous-menu').width();
		console.log('sousmenu ='+sousmenu);
		var galerie = 0;
		$('.oeuvre-mini').each(function() {
			galerie += $(this).outerWidth();
			console.log('galerie ='+galerie);
		});
		total = img+pres+sousmenu+galerie;
		console.log('total ='+total);
		$('main.oeuvre').css('width', total+150);
		/*$('main.oeuvre').children().each(function() {
			total += $(this).outerWidth();
			console.log(total);
		});
		$("main.oeuvre").css("width", total+650);*/

		$(".lienvisible").click(function(event) {
			$(event.currentTarget).show();
			//$("div .annee").show();
		    var val_link = $(event.currentTarget).attr('href'); 
		    console.log('clic sur '+val_link);
		    $(val_link).show();
		    console.log("a[href="+val_link+"]");
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