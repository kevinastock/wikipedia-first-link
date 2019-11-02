import unittest
from wikigraph.parser import LinkSearch

class TestLinkSearch(unittest.TestCase):
    def test_simple(self):
        s = "[[hello world]]"
        ls = LinkSearch(s)
        fl = ls.first_link()
        self.assertEqual("Hello world",fl)

    def test_complex(self):
        s = """{{Dablink|This article is about the United States of America. For other uses of terms redirecting here, see [[US (disambiguation)]], [[USA (disambiguation)]], and [[United States (disambiguation)]].}}
        {{pp-semi|small=yes}}{{pp-move-indef}}
        {{Infobox country
        |conventional_long_name = United States of America
        |common_name            = the United States
        |image_flag             = Flag_of_the_United_States_(Pantone).svg‎
        |image_coat             = US-GreatSeal-Obverse.svg
        |length                 = 1776–Present
        |symbol_type            = Great Seal
        |national_motto         = <!--Please read the talk page before editing these mottos:-->[[In God We Trust]]{{spaces|2}}<small>(official)</small><br />{{lang|la|''[[E pluribus unum|E Pluribus Unum]]''}}{{spaces|2}}<small>(traditional)</small><br /><small>([[Latin]]: Out of Many, One)</small>
        |image_map              = United States (orthographic projection).svg
        |map_width              = 220px
        |national_anthem        = "[[The Star-Spangled Banner]]"
        |official_languages     = None at federal level{{Ref label|engoffbox|a|}}
        |languages_type         = [[National language]]
        |languages              = [[English language|English]] (''[[de facto]]''){{Ref label|engfactobox|b|}}
        |capital                = [[Washington, D.C.]]
        |largest_city           = [[New York City]]
        |latd                   = 38|latm=53|latNS=N|longd=77|longm=01|longEW=W
        |government_type        = [[Federalism|Federal]] [[Presidential system|presidential]] [[constitutional republic]]
        |leader_title1          = [[President of the United States|President]]
        |leader_name1           = [[Barack Obama]] ([[Democratic Party (United States)|D]])
        |leader_title2          = [[Vice President of the United States|Vice President]]
        |leader_name2           = [[Joe Biden]] ([[Democratic Party (United States)|D]])
        |leader_title3          = {{nowrap|[[Speaker of the United States House of Representatives|Speaker of the House]]}}
        |leader_name3           = [[John Boehner]] ([[Republican Party (United States)|R]])
        |leader_title4          = [[Chief Justice of the United States|Chief Justice]]
        |leader_name4           = [[John Roberts]]
        |legislature            = [[United States Congress|Congress]]
        |upper_house            = [[United States Senate|Senate]]
        |lower_house            = [[United States House of Representatives|House of Representatives]]
        |sovereignty_type       = [[American Revolutionary War|Independence]] {{nobold|from the [[Kingdom of Great Britain]]}}
        |established_event1     = [[United States Declaration of Independence|Declared]]
        |established_date1      = July 4, 1776
        |established_event2     = [[Treaty of Paris (1783)|Recognized]]
        |established_date2      = September 3, 1783
        |established_event3     = [[United States Constitution|Current constitution]]
        |established_date3      = June 21, 1788
        |area_footnote          = <ref name="WF"/>{{Ref label|areabox|c|}}
        |area_sq_mi             = 3794101
        |area_km2               = 9826675
        |area_rank              = 3rd/4th
        |area_magnitude         = 1 E12
        |percent_water          = 6.76
        |population_census        = 308,745,538<ref name="2010.census.gov">{{cite web|url=http://2010.census.gov/2010census/data/apportionment-dens-text.php|title=Resident Population Data – 2010|publisher=U.S. Census Bureau|accessdate=2010-12-22|year=2010}}</ref>
        |population_census_year   = 2010
        |population_density_km2   = 33.7
        |population_density_sq_mi = 87.4
        |population_density_rank  = <!-- 178th (unknown source, commented for now) -->
        |GDP_PPP_year             = 2010
        |GDP_PPP                  = $14.624 trillion<ref name=IMF_GDP>{{cite web|url=http://www.imf.org/external/pubs/ft/weo/2010/01/weodata/weorept.aspx?sy=2007&ey=2010&scsm=1&ssd=1&sort=country&ds=.&br=1&c=111&s=NGDPD%2CNGDPDPC%2CPPPGDP%2CPPPPC%2CLP&grp=0&a=&pr.x=40&pr.y=10|title=United States|publisher=International Monetary Fund|accessdate=2010-04-21}}</ref>
        |GDP_PPP_rank             = 1st
        |GDP_PPP_per_capita       = $47,123<ref name="IMF_GDP"/>
        |GDP_PPP_per_capita_rank  = 6th
        |GDP_nominal              = $14.624 trillion<ref name="IMF GDP"/>
        |GDP_nominal_rank         = 1st
        |GDP_nominal_year         = 2010
        |GDP_nominal_per_capita   = $47,132<ref name="IMF_GDP"/>
        |GDP_nominal_per_capita_rank = 9th
        |HDI_year                 = 2010
        |HDI                      = {{increase}} 0.902<ref name="HDI">{{cite web|url=http://hdr.undp.org/en/media/HDR_2010_EN_Tables_reprint.pdf|title=Human Development Report 2010|year=2010|publisher=United Nations|accessdate=4 November 2010}}</ref>
        |HDI_rank                 = 4th
        |HDI_category             = <span style="color:#006000;">very high</span>
        |Gini                     = 45.0<ref name="WF"/>
        |Gini_rank                = 44th
        |Gini_year                = 2007
        |currency                 = [[United States dollar]] ($)
        |currency_code            = USD
        |country_code             = USA
        |utc_offset               = −5 to −10
        |utc_offset_DST           = −4 to −10
        |cctld                    = [[.us]] [[.gov]] [[.mil]] [[.edu]]
        |calling_code             = [[North American Numbering Plan|+1]]
        |date_format              = m/d/yy ([[Anno Domini|AD]])
        |drives_on                = right
        |demonym                  = [[Names for United States citizens|American]]
        |footnotes                =
        {{note|engoffbox}}a. English is the official language of at least 28 states—some sources give a higher figure, based on differing definitions of "official".<ref name=ILW/> English and [[Hawaiian language|Hawaiian]] are both official languages in the state of Hawaii.

        {{note|engfactobox}}b. English is the ''de facto'' language of American government and the sole language spoken at home by 80% of Americans age five and older. Spanish is the [[Spanish language in the United States|second most commonly spoken language]].

        {{note|areabox}}c. Whether the United States or the [[People's Republic of China]] is larger is [[List of countries and outlying territories by total area|disputed]]. The figure given is from the U.S. [[Central Intelligence Agency]]'s ''[[World Factbook]]''. Other sources give smaller figures. All authoritative calculations of the country's size include only the 50 states and the District of Columbia, not the territories.

        {{note|popbox}}d. The population estimate includes people whose usual residence is in the fifty states and the District of Columbia, including noncitizens. It does not include either those living in the territories, amounting to more than 4&nbsp;million U.S. citizens (most in [[Puerto Rico]]), or U.S. citizens living outside the United States.
        }}<!--
        The following opening paragraphs on this subject are a topic of great debate. Check the discussion page before editing. In particular, do ''not'' add mention of the territories to the first sentence: they are possessions of the United States, not part of it.
        -->

        The '''United States of America''' (also referred to as the '''United States''', the '''U.S.''', the '''USA''', or '''[[Americas#Terminology|America]]''') is a [[federalism|federal]] [[constitutional republic]] comprising [[U.S. state|fifty states]] and a [[federal district]]. The country is situated mostly in central [[North America]], where its [[Contiguous United States|forty-eight contiguous states]] and [[Washington, D.C.|Washington,&nbsp;D.C.]], the [[capital districts and territories|capital district]], lie between the [[Pacific Ocean|Pacific]] and [[Atlantic Ocean]]s, bordered by [[Canada]] to the north and [[Mexico]] to the south. The state of [[Alaska]] is in the northwest of the continent, with Canada to the east and [[Russia]] to the west across the [[Bering Strait]]. The state of [[Hawaii]] is an [[archipelago]] in the mid-Pacific. The country also possesses [[Territories of the United States|several territories]] in the [[Caribbean]] and Pacific.
        """
        ls = LinkSearch(s)
        fl = ls.first_link()
        self.assertEqual("Federalism",fl)

    def test_close(self):
        s = """{{about|the river in France, Luxembourg, and Germany|the river in England|River Moselle (London)}}
{{Infobox River | river_name = Moselle
  | image_name = Mosel-einzugsgebiet.jpg
  | caption = The Moselle River
  | origin = [[Vosges mountains]] 
  | mouth = [[Rhine]] &lt;br&gt;{{coord|50|21|58|N|7|36|25|E|name=Rhine-Moselle|display=inline,title}}
  | basin_countries = [[France]], [[Germany]], [[Luxembourg]]
  | length = {{km to mi|545|abbr=yes|precision=2}} 
  | elevation = {{m to ft|715|abbr=yes}} 
  | discharge = 290 m³/s
  | watershed = {{km2 to mi2|num=28286|abbr=yes|spell=Commonwealth|precision=2|wiki=yes}} 
}}

The '''Moselle River''' ({{lang-de|Mosel}}  is a river which flows through  [[France]] and [[Luxembourg]], then becomes part of the [[Rhine River]] after it flows into [[Germany]]. It is {{km to mi|num=545|abbr=no|spell=Commonwealth|precision=2|wiki=yes}} long.

Important cities at the Moselle river are [[Metz]], [[Thionville]], [[Trier]], [[Bernkastel-Kues]] and [[Koblenz]].

The valley of the Moselle river is famous for the wine of [[Elbling]], [[Riesling]], and [[Müller-Thurgau]] - grapes in the wine growing region [[Moselle-Saar-Ruwer]]."""

        ls = LinkSearch(s)
        fl = ls.first_link()
        self.assertEqual("France",fl)

    def test_math(self):
        s = """{{Dablink|&quot;Maths&quot; and &quot;Math&quot; redirect here. For other uses of &quot;Mathematics&quot; or &quot;Math&quot;, see [[Mathematics (disambiguation)]] and [[Math (disambiguation)]].}}
{{semiprotected|small=yes}}

[[File:Euclid.jpg|thumb |[[Euclid]], Greek mathematician, 3rd century BC, as imagined by [[Raphael]] in this detail from ''[[The School of Athens]]''.&lt;ref&gt;No likeness or description of Euclid's physical appearance made during his lifetime survived antiquity. Therefore, Euclid's depiction in works of art depends on the artist's imagination (''see [[Euclid]]'').&lt;/ref&gt;]]

'''Mathematics''' is the study of [[quantity]], [[structure]], [[space]], and [[calculus|change]]. &lt;!-- &lt;&lt;&lt; Please do NOT change the opening sentence without discussion; much time and discussion has been invested in its current form. --&gt; [[Mathematician]]s seek out [[patterns]],&lt;ref&gt;[[Lynn Steen|Steen, L.A.]] (April 29, 1988). ''The Science of Patterns'' [[Science (journal)|Science]], 240: 611–616. and summarized at [http://www.ascd.org/publications/curriculum-handbook/409/chapters/The-Future-of-Mathematics-Education.aspx Association for Supervision and Curriculum Development], ascd.org&lt;/ref&gt;&lt;ref&gt;[[Keith Devlin|Devlin, Keith]], """

        ls = LinkSearch(s)
        fl = ls.first_link()
        self.assertEqual("Quantity",fl)

#class TestSequenceFunctions(unittest.TestCase):
#
#    def setUp(self):
#        self.seq = list(range(10))
#
#    def test_shuffle(self):
#        # make sure the shuffled sequence does not lose any elements
#        random.shuffle(self.seq)
#        self.seq.sort()
#        self.assertEqual(self.seq, list(range(10)))
#
#        # should raise an exception for an immutable sequence
#        self.assertRaises(TypeError, random.shuffle, (1,2,3))
#
#    def test_choice(self):
#        element = random.choice(self.seq)
#        self.assertTrue(element in self.seq)
#
#    def test_sample(self):
#        with self.assertRaises(ValueError):
#            random.sample(self.seq, 20)
#        for element in random.sample(self.seq, 5):
#            self.assertTrue(element in self.seq)

#if __name__ == '__main__':
#    unittest.main()
