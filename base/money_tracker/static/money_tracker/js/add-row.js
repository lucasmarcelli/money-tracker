
$(function() {
  $("#add-row-daily").click(
    function () {
      $("#daily-body tr:last").after('<tr><td class="company"></td><td class="item"></td><td class="amount-in"></td><td class="amount-out"></td><td class="reason"></td><td class="unnecessary"><input type="checkbox" class="unnecessary-box"></input></td><td class="pk" style="display:none">-1</td></tr>');

    });
});
