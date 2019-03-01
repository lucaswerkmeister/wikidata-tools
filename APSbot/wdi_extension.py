import wikidataintegrator
from wikidataintegrator import wdi_core, wdi_helpers

class MyRelease(wdi_helpers.Release):
    def __init__(self, title, description, edition, edition_of=None, edition_of_wdid=None, archive_url=None,
                 pub_date=None, date_precision=11, url=None, doi=None):
        """
        :param title: title of release item
        :type title: str
        :param description: description of release item
        :type description: str
        :param edition: edition number or unique identifier for the release
        :type edition: str
        :param edition_of: name of database. database wdid will automatically be looked up. Must pass either edition_of or edition_of_wdid
        :type edition_of: str
        :param edition_of_wdid: wikidata id of database
        :type edition_of_wdid: str
        :param archive_url: (optional)
        :type archive_url: str
        :param pub_date: (optional) Datetime will be converted to str
        :type pub_date: str or datetime
        :param date_precision: (optional) passed to PBB_Core.WDTime as is. default is 11 (day)
        :type date_precision: int
        :param url: (optional) standard URL for the release
        :type url: str
        :param doi: (optional) DOI for the release
        :type doi: str
        """
        super().__init__(title, description, edition, edition_of_wdid, archive_url,
                         pub_date, date_precision)
        self.url = url
        self.doi = doi


    def make_statements(self):
        super().make_statements()
        if self.url:
            is_download_url = wdi_core.WDItemID('Q7126717', 'P642', is_qualifier=True)
            self.statements.append(wdi_core.WDUrl(self.url, 'P2699', qualifiers=[is_download_url]))
        if self.doi:
            self.statements.append(wdi_core.WDExternalID(self.doi, 'P356'))
