var cor = ""
var map = AmCharts.makeChart("mapa", {
  type: "map",
  theme: "chalk",
   path: "http://www.amcharts.com/lib/3/",

  imagesSettings: {
    labelRollOverColor: "#7E7EFC",
    labelPosition: "bottom"
  },
  areasSettings: {
    rollOverOutlineColor: "#FFFFFF",
    rollOverColor: "#7E7EFC",
    alpha: 0.8,
    //unlistedAreasColor: "#15A892"
    
  },
   zoomControl: {
        buttonFillColor: "#7E7EFC"
    },
  
  dataProvider: {
    map: "brazilHigh",
    zoomLevel: 0.5,
    zoomLongitude: -10, 
    zoomLatitude: -40,
    images: [ {
      
      zoomLevel: 5,
      scale: 0.5,
      title: "BMOBR-06",
      latitude: -22.9307,
      longitude: -43.1467,
      imageURL: "http://s23.postimg.org/3o5tplts7/PNBOIA_1.png",
      width: 32,
      height: 32,
      label: "02/09/2016 16h h \n Int. Vento: 10 m/s \n Dir.Vento 100 deg \n Hs: 2.5 m \n Tp: 10.2 s \n Dp: 2.5 m",
      labelPosition: "right",         
    },
            ]
  },
} );

map.addListener("positionChanged", updateCustomMarkers);
