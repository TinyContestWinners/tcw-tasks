
TEXT_TEMPLATE = """
CONTEST EXPIRED:
  - {{ contest.title }}

STATISTICS:
  - max_entrants: {{ contest.max_entrants }}
  - number of winners: {{ winners | length }}
  - sign ups: {{ contest.entrants | length }}
  - expired: {{ contest.expires.strftime('%Y-%m-%d %H:%M:%S') }} UTC

{% if winners | length -%}
WINNERS:
  {% for winner in winners -%}
  {{ loop.index }}. {{ winner }}
  {% endfor %}

Please remember, it is your responsibilty to contact the winners.
Thank You!
{%- else %}
Sorry. There were no winners selected, because no one signed up.
{% endif %}
"""

HTML_TEMPLATE = """
<html>
  <head>
  </head>
  <body>
    <h3>Contest Expired</h3>
    Contest Name: {{ contest.name }}
    <h3>Statistics</h3>
    <table>
        <tr><td>max entrants</td><td>{{ contest.max }}</td></tr>
        <tr><td>number of winners</td><td>{{ winners | length }}</td></tr>
        <tr><td>sign ups</td><td>{{ contest.entrants | length }}</td></tr>
        <tr><td>expired</td><td>{{ contest.expires.strftime('%Y-%m-%d %H:%M:%S') }} UTC</td></tr>
    </table>
    {% if winners | length -%}
    <h3>Winners</h3>
    <ol>
        {% for winner in winners -%}
        <li>{{ winner }}</li>
        {% endfor %}
    </ol>
    <p>Please remember, it is your responsibilty to contact the winners.</p>
    <p>Thank You!</p>
    {%- else %}
    <p>Sorry. There were no winners selected, because no one signed up.</p>
    {% endif %}
  </body>
</html>
"""
