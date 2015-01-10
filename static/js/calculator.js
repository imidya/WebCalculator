var result = '';
var formula = '';

$(document).ready(function() {

    var update = function() {
        $('#result-float').html('');
        $('#result-int').html(formula);
    }

    var enter = function(text) {
        formula += text;
        update();
    }
    
    $('#btn-0').click(function() {
        enter('0');
    });
    $('#btn-1').click(function() {
        enter('1');
    });
    $('#btn-2').click(function() {
        enter('2');
    });
    $('#btn-3').click(function() {
        enter('3');
    });
    $('#btn-4').click(function() {
        enter('4');
    });
    $('#btn-5').click(function() {
        enter('5');
    });
    $('#btn-6').click(function() {
        enter('6');
    });
    $('#btn-7').click(function() {
        enter('7');
    });
    $('#btn-8').click(function() {
        enter('8');
    });
    $('#btn-9').click(function() {
        enter('9');
    });
    $('#btn-dot').click(function() {
        console.log('->' + formula)
        if (formula.indexOf('.') <= -1) {
            enter('.');
        }
    });
    $('#btn-add').click(function() {
        var lastOperator
        if (formula.length > 3) {
            lastOperator = formula.substr(formula.length - 3);
        }
        if (lastOperator != ' + ' && lastOperator != ' - ' && lastOperator != ' x ' && lastOperator != ' ÷ ') {
            enter(' + ');
        }
    });
    $('#btn-minus').click(function() {
        var lastOperator
        if (formula.length > 3) {
            lastOperator = formula.substr(formula.length - 3);
        }
        if (lastOperator != ' + ' && lastOperator != ' - ' && lastOperator != ' x ' && lastOperator != ' ÷ ') {
            enter(' - ');
        }
    });
    $('#btn-times').click(function() {
        var lastOperator
        if (formula.length > 3) {
            lastOperator = formula.substr(formula.length - 3);
        }
        if (lastOperator != ' + ' && lastOperator != ' - ' && lastOperator != ' x ' && lastOperator != ' ÷ ') {
            enter(' x ');
        }
    });
    $('#btn-divided').click(function() {
        var lastOperator
        if (formula.length > 3) {
            lastOperator = formula.substr(formula.length - 3);
        }
        if (lastOperator != ' + ' && lastOperator != ' - ' && lastOperator != ' x ' && lastOperator != ' ÷ ') {
            enter(' ÷ ');
        }
    });
    $('#btn-equal').click(function() {
        formula = formula.replace('x', '*').replace('÷', '/');

        $.ajax({
            url: '/cal',
            data: {'formula': formula},
            type: 'POST',
            success: function(data, message) {
                if (data.result % 1 === 0) {
                    $('#result-int').html(data.result);
                } else {
                    resultAll = data.result + '';
                    var resultInt = resultAll.split('.')[0];
                    var resultFloat = resultAll.split('.')[1];
                    $('#result-int').html(resultInt);
                    $('#result-float').html('.' + resultFloat);
                }
                $('#formula').html(formula);
                formula = data.result;
            }
        });
    });
    $('#btn-clear').click(function() {
        $('#result-int').html('0');
        $('#result-float').html('');
        $('#formula').html('');
        formula = '';
        result = '';
    });
});