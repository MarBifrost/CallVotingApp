(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();

    // // Calendar Date & Time Range Selector
    // $('#calender').datetimepicker({
    //     inline: true,
    //     format: 'L',
    //     sideBySide: true,
    //     // Enable range selection
    //     calendarWeeks: true,
    //     viewMode: 'days'
    // });
    //
    // // Function to highlight the selected time range
    // $('#showResults').click(function () {
    //     var enteredNumber = $('input[name="called_number"]').val(); // Get the entered number
    //     var selectedDate = $('#calender').datetimepicker('viewDate').format('YYYY-MM-DD'); // Get the selected date
    //     var timeRangeStart = $('#calender').datetimepicker('getDate').startOf('day').format('YYYY-MM-DD HH:mm:ss');
    //     var timeRangeEnd = $('#calender').datetimepicker('getDate').endOf('day').format('YYYY-MM-DD HH:mm:ss');
    //
    //     // Highlight the selected time range on the page
    //     highlightTimeRange(timeRangeStart, timeRangeEnd);
    //
    //     // Perform an AJAX request to get the call count based on the number and selected date/range
    //     $.ajax({
    //         url: '{% url "calls:get_calls_count" %}',  // Define your backend URL
    //         type: 'GET',
    //         data: {
    //             called_number: enteredNumber,
    //             selected_date: selectedDate,
    //             time_range_start: timeRangeStart,
    //             time_range_end: timeRangeEnd
    //         },
    //         success: function (response) {
    //             // Update the result on the page
    //             $('.result_show').text(response.calls_count);
    //         },
    //         error: function () {
    //             alert("Error retrieving call count.");
    //         }
    //     });
    // });
    //
    // // Function to visually highlight the selected time range
    // function highlightTimeRange(start, end) {
    //     // Parse the start and end times into Date objects
    //     var startDate = new Date(start);
    //     var endDate = new Date(end);
    //
    //     // Convert the start and end time into human-readable strings
    //     var startTime = startDate.toLocaleString();
    //     var endTime = endDate.toLocaleString();
    //
    //     // Create a new div element for the range and append it to the page
    //     var rangeDiv = $('<div class="time-range-highlight"></div>');
    //     rangeDiv.text('Selected time range: ' + startTime + ' to ' + endTime);
    //
    //     // Style the div (you can customize the styles)
    //     rangeDiv.css({
    //         'background-color': 'rgba(0, 123, 255, 0.3)', // Light blue color
    //         'padding': '10px',
    //         'margin-top': '20px',
    //         'border-radius': '5px',
    //         'font-size': '14px'
    //     });
    //
    //     // Append the range div to a specific container (e.g., an element with class "container-fluid")
    //     $('.container-fluid').append(rangeDiv);
    // }

})(jQuery);

