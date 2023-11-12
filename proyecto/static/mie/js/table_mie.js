let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ] },
        {searchable:false,targets: [0, 8, 9, 10, 11, 12] }

    ],
    pageLength: 10,
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await initMiembros();

    dataTable = $("#datatable-miembros").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const initMiembros = async () => {
    try {
        const response = await fetch(listMieUrl);
        const data = await response.json();

        let content = ``;
        data.miembros.forEach((miembro, index) => {
            const nombreNacionalidad = miembro.nacionalidad ? data.nation.find(n => n.id === miembro.nacionalidad).nombre : '';
            const nombreEstadoCivil = miembro.estadocivil ? data.civil.find(c => c.id === miembro.estadocivil).nombre : '';
            const nombreGenero = miembro.genero ? data.gene.find(g => g.id === miembro.genero).nombre : '';
            content += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${miembro.id || ''}</td>
                    <td>${miembro.nombre || ''}</td>
                    <td>${miembro.apellido || ''}</td>
                    <td>${miembro.edad || ''}</td>   
                    <td>${nombreNacionalidad || ''}</td>
                    <td>${nombreEstadoCivil || ''}</td>
                    <td>${nombreGenero || ''}</td>
                    <td>${miembro.di || ''}</td>
                    <td>${miembro.direccion || ''}</td>
                    <td>${miembro.telefono || ''}</td>
                    <td>${miembro.correo || ''}</td>
                    <td>${miembro.nohijos || ''}</td>
                </tr>`;
        });
        document.getElementById("tableBody_miembros").innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});