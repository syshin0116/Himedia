<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>jQuery UI Datepicker - Select a Date Range</title>
<link rel="stylesheet"
	href="//code.jquery.com/ui/1.13.1/themes/base/jquery-ui.css">
<link rel="stylesheet" href="/resources/demos/style.css">
<script src="https://code.jquery.com/jquery-3.6.0.js"></script>
<script src="https://code.jquery.com/ui/1.13.1/jquery-ui.js"></script>
  <style>
    .ui-controlgroup-vertical {
      width: 150px;
    }
    .ui-controlgroup.ui-controlgroup-vertical > button.ui-button,
    .ui-controlgroup.ui-controlgroup-vertical > .ui-controlgroup-label {
      text-align: center;
    }
    #car-type-button {
      width: 120px;
    }
    .ui-controlgroup-horizontal .ui-spinner-input {
      width: 20px;
    }
  </style>
<script>
  $( function() {
	  $( "#accordion" ).accordion();
	  $( "input" ).checkboxradio();
	  $( ".controlgroup" ).controlgroup()
	    $( ".controlgroup-vertical" ).controlgroup({
	      "direction": "vertical"
	    });
	  var spinner = $( "#spinner" ).spinner();
	  
	    $( "#disable" ).on( "click", function() {
	      if ( spinner.spinner( "option", "disabled" ) ) {
	        spinner.spinner( "enable" );
	      } else {
	        spinner.spinner( "disable" );
	      }
	    });
	    $( "#destroy" ).on( "click", function() {
	      if ( spinner.spinner( "instance" ) ) {
	        spinner.spinner( "destroy" );
	      } else {
	        spinner.spinner();
	      }
	    });
	    $( "#getvalue" ).on( "click", function() {
	      alert( spinner.spinner( "value" ) );
	    });
	    $( "#setvalue" ).on( "click", function() {
	      spinner.spinner( "value", 5 );
	    });
	 
	    $( "button" ).button();
    var dateFormat = "mm/dd/yy",
      from = $( "#from" )
        .datepicker({
          defaultDate: "+1w",
          changeMonth: true,
          numberOfMonths: 3
        })
        .on( "change", function() {
          to.datepicker( "option", "minDate", getDate( this ) );
        }),
      to = $( "#to" ).datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 3
      })
      .on( "change", function() {
        from.datepicker( "option", "maxDate", getDate( this ) );
      });
 
    function getDate( element ) {
      var date;
      try {
        date = $.datepicker.parseDate( dateFormat, element.value );
      } catch( error ) {
        date = null;
      }
 
      return date;
    }
  } );
  </script>
</head>
<body>
	<div id="accordion">
		<h3>Section 1</h3>
		<div>
			<label for="from">시작일:</label> <input type="text" id="from"
				name="from"> <label for="to">종료일:</label> <input type="text"
				id="to" name="to">
		</div>
		<h3>Section 2</h3>
		<div>
			<div class="widget">
  <h1>Checkbox and radio button widgets</h1>
 
  <h2>Radio Group</h2>
  <fieldset>
    <legend>Select a Location: </legend>
    <label for="radio-1">New York</label>
    <input type="radio" name="radio-1" id="radio-1">
    <label for="radio-2">Paris</label>
    <input type="radio" name="radio-1" id="radio-2">
    <label for="radio-3">London</label>
    <input type="radio" name="radio-1" id="radio-3">
  </fieldset>
 
  <h2>Checkbox</h2>
  <fieldset>
    <legend>Hotel Ratings: </legend>
    <label for="checkbox-1">2 Star</label>
    <input type="checkbox" name="checkbox-1" id="checkbox-1">
    <label for="checkbox-2">3 Star</label>
    <input type="checkbox" name="checkbox-2" id="checkbox-2">
    <label for="checkbox-3">4 Star</label>
    <input type="checkbox" name="checkbox-3" id="checkbox-3">
    <label for="checkbox-4">5 Star</label>
    <input type="checkbox" name="checkbox-4" id="checkbox-4">
  </fieldset>
 
  <h2>Checkbox nested in label</h2>
  <fieldset>
    <legend>Bed Type: </legend>
    <label for="checkbox-nested-1">2 Double
      <input type="checkbox" name="checkbox-nested-1" id="checkbox-nested-1">
    </label>
    <label for="checkbox-nested-2">2 Queen
      <input type="checkbox" name="checkbox-nested-2" id="checkbox-nested-2">
    </label>
    <label for="checkbox-nested-3">1 Queen
      <input type="checkbox" name="checkbox-nested-3" id="checkbox-nested-3">
    </label>
    <label for="checkbox-nested-4">1 King
      <input type="checkbox" name="checkbox-nested-4" id="checkbox-nested-4">
    </label>
  </fieldset>
</div>
		</div>
		<h3>Section 3</h3>
		<div>
			<div class="widget">
  <h1>Controlgroup</h1>
  <fieldset>
    <legend>Rental Car</legend>
    <div class="controlgroup">
      <select id="car-type">
        <option>Compact car</option>
        <option>Midsize car</option>
        <option>Full size car</option>
        <option>SUV</option>
        <option>Luxury</option>
        <option>Truck</option>
        <option>Van</option>
      </select>
      <label for="transmission-standard">Standard</label>
      <input type="radio" name="transmission" id="transmission-standard">
      <label for="transmission-automatic">Automatic</label>
      <input type="radio" name="transmission" id="transmission-automatic">
      <label for="insurance">Insurance</label>
      <input type="checkbox" name="insurance" id="insurance">
      <label for="horizontal-spinner" class="ui-controlgroup-label"># of cars</label>
      <input id="horizontal-spinner" class="ui-spinner-input">
      <button>Book Now!</button>
    </div>
  </fieldset>
  <br>
  <fieldset>
    <legend>Rental Car</legend>
    <div class="controlgroup-vertical">
      <select>
        <option>Compact car</option>
        <option>Midsize car</option>
        <option>Full size car</option>
        <option>SUV</option>
        <option>Luxury</option>
        <option>Truck</option>
        <option>Van</option>
      </select>
      <label for="transmission-standard-v">Standard</label>
      <input type="radio" name="transmission-v" id="transmission-standard-v">
      <label for="transmission-automatic-v">Automatic</label>
      <input type="radio" name="transmission-v" id="transmission-automatic-v">
      <label for="insurance-v">Insurance</label>
      <input type="checkbox" name="insurance" id="insurance-v">
      <label for="vertical-spinner" class="ui-controlgroup-label"># of cars</label>
      <input id="vertical-spinner" class="ui-spinner-input">
      <button id="book">Book Now!</button>
    </div>
  </fieldset>
</div>
		</div>
		<h3>Section 4</h3>
		<div>
			<p>
  <label for="spinner">Select a value:</label>
  <input id="spinner" name="value">
</p>
 
<p>
  <button id="disable">Toggle disable/enable</button>
  <button id="destroy">Toggle widget</button>
</p>
 
<p>
  <button id="getvalue">Get value</button>
  <button id="setvalue">Set value to 5</button>
</p>
		</div>
	</div>

</body>
</html>