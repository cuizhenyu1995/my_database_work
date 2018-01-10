/**
 * Bootstrap Table Chinese translation
 * Author: Zhixin Wen<wenzhixin2010@gmail.com>
 */
(function ($) {
    'use strict';

    $.fn.bootstrapTable.locales['zh-CN'] = {
        formatLoadingMessage: function () {
            return 'æ­£åœ¨åŠªåŠ›åœ°åŠ è½½æ•°æ®ä¸­ï¼Œè¯·ç¨å€™â€¦â€¦';
        },
        formatRecordsPerPage: function (pageNumber) {
            return 'æ¯é¡µæ˜¾ç¤º ' + pageNumber + ' æ¡è®°å½•';
        },
        formatShowingRows: function (pageFrom, pageTo, totalRows) {
            return 'æ˜¾ç¤ºç¬¬ ' + pageFrom + ' åˆ°ç¬¬ ' + pageTo + ' æ¡è®°å½•ï¼Œæ€»å…± ' + totalRows + ' æ¡è®°å½•';
        },
        formatSearch: function () {
            return 'æœç´¢';
        },
        formatNoMatches: function () {
            return 'æ²¡æœ‰æ‰¾åˆ°åŒ¹é…çš„è®°å½•';
        },
        formatPaginationSwitch: function () {
            return 'éšè—/æ˜¾ç¤ºåˆ†é¡µ';
        },
        formatRefresh: function () {
            return 'åˆ·æ–°';
        },
        formatToggle: function () {
            return 'åˆ‡æ¢';
        },
        formatColumns: function () {
            return 'åˆ—';
        },
        formatExport: function () {
            return 'å¯¼å‡ºæ•°æ®';
        },
        formatClearFilters: function () {
            return 'æ¸…ç©ºè¿‡æ»¤';
        }
    };

    $.extend($.fn.bootstrapTable.defaults, $.fn.bootstrapTable.locales['zh-CN']);

})(jQuery);
