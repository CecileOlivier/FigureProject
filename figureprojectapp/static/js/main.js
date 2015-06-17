$(document).ready(function() {
	console.log('js actif');

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
    // MEDIA QUERIES
	if ($(window).width() < 360) {
		var isVisible = $( "ul#menu-principal" ).is( ":visible" );
		var isHidden = $( "ul#menu-principal" ).is( ":hidden" );

        $("menu-principal").hide(); 
        $('div.menu a').css("background-image", "url('../static/icones/menu-ouv.png')");
		$('.menu').click(function(){
			$(".menu-principal").toggle();
			$('div.menu a').css("background-image", "url('../static/icones/menu-fer.png')");
		});
		if ($( "ul#menu-principal:visible")) {
	    	console.log('menu ouvert');
	    }
	    else if ($( "ul#menu-principal:hidden")) {
			console.log('menu fermé');
	    }

		/*$("a[href=#menu-principal]").click(function(){
        	$("ul#menu-principal").toggle();
        	console.log('toogle');
        	if ($( "ul#menu-principal:visible")) {
	    		$('div.menu a').addClass('open');
	    		$('div.menu a').removeClass('close');
	    	}
	    	else if ($( "ul#menu-principal:hidden")) {
				$('div.menu a').removeClass('open');
				$('div.menu a').addClass('close');
	    	}
        	//$('div.menu a').addClass('open');
        	//$('div.menu a').removeClass('open');
        	//$('div.menu a').css("background-image", "url('../icones/menu-ferm.png')");
    	});*/
	}
	else if ($(window).width() < 1024) {
		$("#menu-principal").removeClass("hide");
		$("#oeuvres").addClass("hide");
		$(".hide").hide(); 
	}
	else {
		// CALCUL DE LA TAILLE DES ÉLÉMENTS
		$(window).load(function() {
			console.log('window load')
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
			$('main.oeuvre').width(total + 150);
		});

		$(".lienvisible").click(function(event) {
			$(event.currentTarget).show();
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