Following the First Link on Wikipedia
=====================================

> Wikipedia trivia: if you take any article, click on the first link in the
> article text not in parentheses or italics, and then repeat, you will
> eventually end up at "Philosophy".
> [xkcd: Extended Mind](http://xkcd.com/903/)

This is from sometime in 2011.

A few tests of going to a random page wikipedia and applying the rule mentioned
in XKCD show that you really do end up at Philosophy most of the time. Using a
[complete dump](http://en.wikipedia.org/wiki/Wikipedia:Database_download) to
generate stats on where most pages lead, which is here as the percentage of
pages which reach the given page, tied pages form a loop:

| Percentage | Destination |
|:------------------------------:|:-----------:|
| 93.39% | Sense |
| 93.39% | Philosophy |
| 93.39% | Perception |
| 93.39% | Panpsychism |
| 93.39% | Mind |
| 93.39% | Existence |
| 93.39% | Consciousness |
| 93.39% | Awareness |
| 89.60% | Modern philosophy |
| 89.60% | Property (philosophy) |
| 89.17% | Quantity |
| 89.15% | Mathematics |
| 84.78% | Sequence |
| 84.78% | Information |
| 83.72% | Fact |
| 83.72% | Knowledge |
| 78.66% | Science |
| 62.09% | Natural science |
| 32.73% | Physics |
| 28.74% | Biology |
| 23.98% | Extant taxon |
| 23.97% | Human |
| 19.05% | Observable |
| 19.05% | Event |
| 19.05% | Causality |
| 19.05% | Interaction |
| 19.05% | Community |
| 18.93% | Academia |
| 18.82% | List of academic disciplines |
| 17.72% | Social sciences |
| 15.18% | State (polity) |
| 10.08% | Language |

The pages listed are reached, not necessarily dead ends or cycles, so one could
actually lead to another, e.g., Mathematics leads to Philosophy.

On average it took 20 pages to reach Philosophy from any page that eventually
reached it, although the furthest page was 727 clicks away: [List of state
leaders in 1707](http://en.wikipedia.org/wiki/List_of_state_leaders_in_1707).

There are a bunch of heurstics here to solve some problems I found:
* Detecting nested blocks at the start of the page which show up on the right
  of the page
* Rules for capitalization, e.g., 'GNOME' and 'Gnome' are different pages, but
  'gnome' goes to 'Gnome' 
* Links to subsections within a page, e.g., 'Mind#Etymology' is really a link
  to the page 'Mind',
