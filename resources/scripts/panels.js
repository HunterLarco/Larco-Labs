(function(){
	
	window.addEventListener('load', Init);

	function Init(){
		BindParallax();
	}

	function BindParallax(){
		window.addEventListener('scroll', UpdateParallax);
		UpdateParallax();
	}
	function UpdateParallax(){
		var panels = document.querySelectorAll('.panel');
	
		for(var i=0,panel; panel=panels[i++];)
			panel.style.top = CalculatePanelTop(panel);
	}
	function CalculatePanelTop(panel){
		var y = window.scrollY,
				height = window.innerHeight;
	
		var diff = (panel.offsetTop) - (y);
				percent = diff / height;

		if(percent < -panel.offsetHeight/height || percent > 1) return;
	
		panel.querySelector('.img').style.top = percent*250 + 'px';
	}
	
})();