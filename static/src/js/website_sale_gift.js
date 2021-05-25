'use strict';
odoo.define('website_sale_gift.checkout', function (require) {

    require('web.dom_ready');
    var ajax = require('web.ajax');
    var core = require('web.core');
    var _t = core._t;

    var $gift_button = $('#o_gift_form');

    var _onGiftClick = function(ev) {
        gift_id = $(ev.currentTarget).is(':checked');
        var values = {'gift_id': gift_id};
        ajax.jsonRpc('/shop/update_gift', 'call', values).then(_onGiftUpdateAnswer);
    };

    var _onGiftUpdateAnswer = function(result) {
        console.log('Gift Change');
        console.log(result);
    };

    var $gift = $("#gift_method input[name='gift_id']");
    $gift.click(_onGiftClick);

});
