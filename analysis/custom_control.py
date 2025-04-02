from branca.element import MacroElement, Template

class CustomControl(MacroElement):
    _template = Template("""
        {% macro script(this, kwargs) %}
        L.Control.CustomControl = L.Control.extend({
            onAdd: function(map) {
                var div = L.DomUtil.create('div');
                div.innerHTML = `{{ this.html }}`;
                return div;
            },
            onRemove: function(map) {
                // Nothing required here.
            }
        });
        L.control.customControl = function(opts) {
            return new L.Control.CustomControl(opts);
        }
        L.control.customControl({ position: "{{ this.position }}" }).addTo({{ this._parent.get_name() }});
        {% endmacro %}
    """)

    def __init__(self, html, position='bottomleft'):
        super().__init__()
        self.html = html.replace('\n', ' ')
        self.position = position