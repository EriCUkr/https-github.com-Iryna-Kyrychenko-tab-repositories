import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl'

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.dashboard_url) == self.expected_title


    '''
    button_players_count_xpath="//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-md-3'][1]"
    button_matches_count_xpath="//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-md-3'][2]"
    button_reports_count_xpath="//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-md-3'][3]"
    button_events_count_xpath="//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-md-3'][4]"
    button_scouts_panel_xpath="//h2[contains(@class,'m')][1]"
    last_updated_player_xpath="//h6[contains(@class,'m')][1]"
    last_updated_report_xpath="//h6[contains(@class,'m')][2]"
    window_scouts_panel_xpath="//div[contains(@class,'12')][1]"
    window_shortcuts_xpath="//div[contains(@class,'12')][2]"
    window_activity_xpath="//div[contains(@class,'12')][3]"
    pass
    '''
