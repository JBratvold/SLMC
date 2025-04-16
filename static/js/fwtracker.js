document.addEventListener('DOMContentLoaded', () => {
    const getCellValue = (tr, idx) => tr.children[idx].innerText || tr.children[idx].textContent;

    const classificationOrder = {
        "Frontline": 0,
        "Command Ops": 1,
        "Rearguard": 2
    };

    const comparer = (idx, asc, isClassification = false) => (a, b) => {
        let v1 = getCellValue(asc ? a : b, idx);
        let v2 = getCellValue(asc ? b : a, idx);

        if (isClassification) {
            return classificationOrder[v1] - classificationOrder[v2];
        }

        return !isNaN(parseFloat(v1)) && !isNaN(parseFloat(v2)) 
            ? parseFloat(v1) - parseFloat(v2)
            : v1.toString().localeCompare(v2);
    };

    const headers = document.querySelectorAll('th');
    headers.forEach((th, index) => {
        th.classList.add('sortable');
        th.addEventListener('click', () => {
            const table = th.closest('table');
            const isClassification = th.textContent.trim() === "Classification";

            const asc = !th.classList.contains('asc');
            headers.forEach(h => h.classList.remove('asc', 'desc'));
            th.classList.add(asc ? 'asc' : 'desc');

            Array.from(table.querySelectorAll('tbody tr'))
                .sort(comparer(index, asc, isClassification))
                .forEach(tr => table.querySelector('tbody').appendChild(tr));
        });
    });
});