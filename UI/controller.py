import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._sel_country = None

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        sel_year = self._view._txtAnno.value
        try:
            int_year = int(sel_year)
        except ValueError:
            self._view._txt_result.controls.append(ft.Text("The selected year is not written correctly"))
            self._view._page.update()

        if 1816 <= int_year <= 2016:
            self._model.build_graph(year=int_year)
            self._view._txt_result.controls.append(ft.Text("Graph buildt successfully"))
            num_conn_components = self._model.number_conn_comp()
            self._view._txt_result.controls.append(ft.Text(f"The number of connected components is: {num_conn_components}"))
            to_print = self._model.printable_graph()
            for row in to_print:
                self._view._txt_result.controls.append(ft.Text(f"{row[0]} -- {row[1]} adjacents"))

        else:
            self._view._txt_result.controls.append(ft.Text("Choose an year between 1816 and 2016"))
        self._view._btnCalcolaRaggiungibili.disabled = False
        self._view._page.update()

    def handleCalcolaRaggiungibili(self,e):
        #  to handle non-existing country prob
        visited = self._model.get_BFS_nodes(self._sel_country)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(
            ft.Text(f"from {self._sel_country} you can reach "
                    f"{len(visited)} countries.")
        )
        for v in visited:
            self._view._txt_result.controls.append(ft.Text(v))
        self._view._page.update()

    def handleCalcolaRaggiungibiliRicorsione(self,e):
        self._view._txt_result.controls.clear()
        if self._sel_country not in list(self._model._sol_graph.nodes):
            self._view._txt_result.controls.append(ft.Text("this country didn't exist in till the sel year"))
        else:
            visited = self._model.get_reachable_recursion(self._sel_country)
            self._view._txt_result.controls.append(
                ft.Text(f"from {self._sel_country} you can reach "
                        f"{len(visited)} countries.")
            )
            for v in visited:
                self._view._txt_result.controls.append(ft.Text(v))
        self._view._page.update()

    def fill_dd_country(self):
        countries = self._model.get_countries()
        for country in countries:
            self._view._ddCountry.options.append(ft.dropdown.Option(text=country.StateNme,
                                                                     data=country,
                                                                     on_click=self.read_country))
        self._view.update_page()
    def read_country(self,e):
        if e.control.data is None:
            self._sel_country = None
        else:
            self._sel_country = e.control.data


