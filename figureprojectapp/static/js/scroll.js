$(document).ready(function() {
	// jquery.mousewheel.min.js pour le scroll horizontal
	console.log('scroll horizontal ok...');
	//if ($(window).width() > 1024) {
		$('html, body, *').on('mousewheel', function(e, delta) {
			this.scrollLeft -= (delta * 40);
			console.log('je fonctionne');
			e.preventDefault();
		});
	//});
});