/* Mini-game in index-page */
const ball = document.querySelector("#ball");


/* Dropping additional information about player in roster-page */

const players = document.querySelectorAll(".player");

for(let player of players) {
    player.addEventListener("click", function() {
        let currentPlayer = player;
        if( ! currentPlayer.classList.contains('show-info') ) {
            players.forEach(function(item) {
                item.classList.remove('show-info');
            });

            currentPlayer.classList.add('show-info');
        }
        else {
            currentPlayer.classList.remove('show-info');
        }
    });
}


/* Roster table sorting */

function sortTableByNameColumn(table, column = 1, asc = true) {
    const dirModifier = asc ? 1 : -1;
    const tBody = table.querySelector(".roster-table-body");
    const rows = Array.from(tBody.querySelectorAll("tr"));
    const rows1 = [];
    for(let i = 0; i < rows.length; i += 2) {
        rows1.push(rows.slice(i, i + 2));
    }
    const sortedRows = rows1.sort((a, b) => {
        const aColText = a[0].querySelector(".name-column").textContent;
        const bColText = b[0].querySelector(".name-column").textContent;
        return aColText > bColText ? (1 * dirModifier) : (-1 * dirModifier);
    });

    while(tBody.firstChild) {
        tBody.removeChild(tBody.firstChild);
    }

    for (let i = 0; i < sortedRows.length; i++) {
        tBody.append(...sortedRows[i]);
    }

    table.querySelectorAll("th").forEach(th => th.classList.remove("th-sort-asc", "th-sort-desc"));
    table.querySelector(`th:nth-child(${ column + 1 })`).classList.toggle("th-sort-asc", asc);
    table.querySelector(`th:nth-child(${ column + 1 })`).classList.toggle("th-sort-desc", !asc);
}

function sortTableByNumberColumn(table, column, asc = true) {
    const dirModifier = asc ? 1 : -1;
    const tBody = table.querySelector(".roster-table-body");
    const rows = Array.from(tBody.querySelectorAll("tr"));
    const rows1 = [];
    for(let i = 0; i < rows.length; i += 2) {
        rows1.push(rows.slice(i, i + 2));
    }
    const sortedRows = rows1.sort((a, b) => {
        const aColText = Number(a[0].querySelector(`td:nth-child(${ column + 2 })`).textContent);
        const bColText = Number(b[0].querySelector(`td:nth-child(${ column + 2 })`).textContent);
        return aColText > bColText ? (-1 * dirModifier) : (1 * dirModifier);
    });

    while(tBody.firstChild) {
        tBody.removeChild(tBody.firstChild);
    }

    for (let i = 0; i < sortedRows.length; i++) {
        tBody.append(...sortedRows[i]);
    }

    table.querySelectorAll("th").forEach(th => th.classList.remove("th-sort-asc", "th-sort-desc"));
    table.querySelector(`th:nth-child(${ column + 1 })`).classList.toggle("th-sort-asc", asc);
    table.querySelector(`th:nth-child(${ column + 1 })`).classList.toggle("th-sort-desc", !asc);

}

try {
    document.querySelector(".points-column").classList.add('th-sort-asc');
} catch(err) {
}

document.querySelectorAll(".roster-table th").forEach(headerCell => {
    headerCell.addEventListener("click", () => {
        const tableElement = headerCell.parentElement.parentElement.parentElement;
        const headerIndex = Array.prototype.indexOf.call(headerCell.parentElement.children, headerCell);
        const currentIsAscending = headerCell.classList.contains("th-sort-asc");

        if (headerIndex == 0) {
            sortTableByNameColumn(tableElement, 0, !currentIsAscending);
        } else {
            sortTableByNumberColumn(tableElement, headerIndex, !currentIsAscending);
        }
    });
});