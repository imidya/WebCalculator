var result = '';
var formula = '';

$(document).ready(function() {

    var update = function() {
        $('#result-int').html(formula);
    }
    
    $('#btn-0').click(function() {
        formula += '0';
        update();
    });
    $('#btn-1').click(function() {
        formula += '1';
        update();
    });
    $('#btn-2').click(function() {
        formula += '2';
        update();
    });
    $('#btn-3').click(function() {
        formula += '3';
        update();
    });
    $('#btn-4').click(function() {
        formula += '4';
        update();
    });
    $('#btn-5').click(function() {
        formula += '5';
        update();
    });
    $('#btn-6').click(function() {
        formula += '6';
        update();
    });
    $('#btn-7').click(function() {
        formula += '7';
        update();
    });
    $('#btn-8').click(function() {
        formula += '8';
        update();
    });
    $('#btn-9').click(function() {
        formula += '9';
        update();
    });
    $('#btn-add').click(function() {
        formula += ' + ';
        update();
    });
    $('#btn-minus').click(function() {
        formula += ' - ';
        update();
    });
    $('#btn-times').click(function() {
        formula += ' × ';
        update();
    });
    $('#btn-divided').click(function() {
        formula += ' ÷ ';
        update();
    });
    $('#btn-equal').click(function() {
        $('#formula').html(formula);
    });
    $('#btn-clear').click(function() {
        $('#result-int').html('0');
        $('#result-float').html('');
        $('#formula').html('');
        formula = '';
        result = '';
    });
});