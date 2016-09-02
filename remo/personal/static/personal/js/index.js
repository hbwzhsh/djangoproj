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
      title: "Guanabara",
      latitude: -22.9307,
      longitude: -43.1467,
      imageURL: "http://s23.postimg.org/3o5tplts7/PNBOIA_1.png",
      width: 32,
      height: 32,
      label: "02/09/2016 16h h \n Int. Vento: 10 m/s \n Dir.Vento 100 deg \n Hs: 2.5 m \n Tp: 10.2 s \n Dp: 2.5 m",
      labelPosition: "right",
      
               
    },{
      zoomLevel: 5,
      scale: 0.5,
      title: "Santos",
      latitude: -25.2707,
      longitude: -44.9273,
      imageURL: "http://s23.postimg.org/3o5tplts7/PNBOIA_1.png",
      width: 32,
      height: 32,
      label: "02/09/2016 16h h \n Int. Vento: 10 m/s \n Dir.Vento 100 deg \n Hs: 2.5 m \n Tp: 10.2 s \n Dp: 2.5 m",
      labelPosition: "right"
    },{      
      zoomLevel: 5,
      scale: 0.5,
      title: "Recife",
      latitude: -8.1557,
      longitude: -34.5633,
      imageURL: "http://s23.postimg.org/3o5tplts7/PNBOIA_1.png",
      width: 32,
      height: 32,
      label: "02/09/2016 16h h \n Int. Vento: 10 m/s \n Dir.Vento 100 deg \n Hs: 2.5 m \n Tp: 10.2 s \n Dp: 2.5 m",
      labelPosition: "right"
      
    },{
      zoomLevel: 5,
      scale: 0.5,
      title: "Porto Seguro",
      latitude: -15.9958,
      longitude: -37.9362,
      imageURL: "http://s23.postimg.org/3o5tplts7/PNBOIA_1.png",
      width: 32,
      height: 32,
      label: "02/09/2016 16h h \n Int. Vento: 10 m/s \n Dir.Vento 100 deg \n Hs: 2.5 m \n Tp: 10.2 s \n Dp: 2.5 m",
      labelPosition: "right"
    },{
      zoomLevel: 5,
      scale: 0.5,
      title: "Santa Catarina",
      latitude: -28.5175,
      longitude: -47.3905,
      imageURL: "http://s23.postimg.org/3o5tplts7/PNBOIA_1.png",
      width: 32,
      height: 32,
      label: "02/09/2016 16h h \n Int. Vento: 10 m/s \n Dir.Vento 100 deg \n Hs: 2.5 m \n Tp: 10.2 s \n Dp: 2.5 m",
      labelPosition: "right"
    },{
      zoomLevel: 5,
      scale: 0.5,
      title: "Rio Grande",
      latitude: -31.5747,
      longitude: -49.8713,
      imageURL: "http://s23.postimg.org/3o5tplts7/PNBOIA_1.png",
      width: 32,
      height: 32,
      label: "02/09/2016 16h h \n Int. Vento: 10 m/s \n Dir.Vento 100 deg \n Hs: 2.5 m \n Tp: 10.2 s \n Dp: 2.5 m",
      labelPosition: "right"
    }
  
            
            ]
  },

} );

map.addListener("positionChanged", updateCustomMarkers);
