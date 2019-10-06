// funzione per gestire la creazione del grafico a istogramma
google.charts.load('current', {packages: ['corechart', 'bar']});
let globalMsg = {};

function drawStacked() {
  const data = google.visualization.arrayToDataTable([
    ['', '', { role: 'style' }],
    ['Angry', globalMsg['Angry'] * 100, 'color: #000000'],
    ['Happy', globalMsg['Happy'] * 100, 'color: #FF6900'],
    ['Excited', globalMsg['Excited'] * 100, 'color: #FF0000'],
    ['Fear', globalMsg['Fear'] * 100, 'color: #1C677E'],
    ['Sad', globalMsg['Sad'] * 100, 'color: #AAAAAA'],
    ['Bored', globalMsg['Bored'] * 100, 'color: #9F19B5'],
  ]);
  
  const options = {
    title: '',
    legend: {position: 'none'},
    chartArea: {width: '50%'},
    isStacked: true
  };
  const chart = new google.visualization.BarChart(document.getElementById('chart_div'));
  chart.draw(data, options);
}

// funzione per effettuare l'analisi del testo
$(document).ready(function() {
  $("#bottone").click(function() {
    $("#bottone").attr("disabled", true);
    const lang = $("#lang").val();
    const text = $("#text").val();
    $.ajax({
      type: "POST",
      url: "/get_emotions",
      data: "lang=" + lang + "&" + "text=" + text,
      dataType: "html",
      success: function(msg)
      {
        //alert(msg)
        console.log(msg);
        $("#bottone").attr("disabled", false);
        globalMsg = JSON.parse(msg)["emotion"];
        google.charts.setOnLoadCallback(drawStacked);
      },
      error: function()
      {
        alert("Chiamata fallita, si prega di riprovare...");
        $("#bottone").attr("disabled", false);
      }
    });
  });
});