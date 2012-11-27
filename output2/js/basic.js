/*
 * SimpleModal Basic Modal Dialog
 * http://www.ericmmartin.com/projects/simplemodal/
 * http://code.google.com/p/simplemodal/
 *
 * Copyright (c) 2010 Eric Martin - http://ericmmartin.com
 *
 * Licensed under the MIT license:
 *   http://www.opensource.org/licenses/mit-license.php
 *
 * Revision: $Id: basic.js 254 2010-07-23 05:14:44Z emartin24 $
 */

 jQuery(function ($) {
 	// Load dialog on click
 	$('.basic-modal').click(function (e) {
 		$('#basic-modal-content-'+$(this).val()).modal({
 			onOpen: function (dialog) {
 				dialog.overlay.fadeIn(200, function () {
 					dialog.container.fadeIn(200, function () {
 						dialog.data.fadeIn(200, function () {
 								});
 							});
 						});
 				},
			onClose: function (dialog) {				
				dialog.data.fadeOut(200, function () {
					dialog.container.fadeOut(200, function () {
						dialog.overlay.fadeOut(200, function () {
							$.modal.close(); // must call this!
							});
						});
					});
				}
		});
 		return false;
 	});
 });
