document.addEventListener("DOMContentLoaded", function() {
  const calendar = document.getElementById("calendar");
  const currentDate = new Date();
  let selectedDate = new Date();

  renderCalendar(currentDate.getFullYear(), currentDate.getMonth());

  function renderCalendar(year, month) {
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const firstDayIndex = new Date(year, month, 1).getDay();
    
    const monthNames = [
      "January", "February", "March", "April", "May", "June", "July",
      "August", "September", "October", "November", "December"
    ];

    calendar.innerHTML = `
      <div class="calendar-header">
        <button onclick="prevYear()">&#10094;</button>
        <button onclick="prevMonth()">&#10094;</button>
        <h2>${monthNames[month]} ${year}</h2>
        <button onclick="nextMonth()">&#10095;</button>
        <button onclick="nextYear()">&#10095;</button>
      </div>
      <div class="calendar-days">
        <div class="day">Sun</div>
        <div class="day">Mon</div>
        <div class="day">Tue</div>
        <div class="day">Wed</div>
        <div class="day">Thu</div>
        <div class="day">Fri</div>
        <div class="day">Sat</div>
        ${renderDays(firstDayIndex, daysInMonth)}
      </div>
    `;
  }

  function renderDays(firstDayIndex, daysInMonth) {
    let days = "";

    for (let i = 0; i < firstDayIndex; i++) {
      days += `<div class="day"></div>`;
    }

    for (let i = 1; i <= daysInMonth; i++) {
      const dayClass = (i === currentDate.getDate() && currentDate.getMonth() === selectedDate.getMonth() && currentDate.getFullYear() === selectedDate.getFullYear()) ? "today" : (i === selectedDate.getDate()) ? "selected" : "";
      days += `<div class="day ${dayClass}" onclick="selectDate(${i})">${i}</div>`;
    }

    return days;
  }

  window.prevYear = function() {
    selectedDate.setFullYear(selectedDate.getFullYear() - 1);
    renderCalendar(selectedDate.getFullYear(), selectedDate.getMonth());
  }

  window.nextYear = function() {
    selectedDate.setFullYear(selectedDate.getFullYear() + 1);
    renderCalendar(selectedDate.getFullYear(), selectedDate.getMonth());
  }

  window.prevMonth = function() {
    selectedDate.setMonth(selectedDate.getMonth() - 1);
    renderCalendar(selectedDate.getFullYear(), selectedDate.getMonth());
  }

  window.nextMonth = function() {
    selectedDate.setMonth(selectedDate.getMonth() + 1);
    renderCalendar(selectedDate.getFullYear(), selectedDate.getMonth());
  }

  window.selectDate = function(day) {
    selectedDate.setDate(day);
    renderCalendar(selectedDate.getFullYear(), selectedDate.getMonth());
  }
});
