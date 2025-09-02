from django_prose_editor.fields import ProseEditorField
from django_prose_editor.widgets import ProseEditorWidget


class TallProseEditorWidget(ProseEditorWidget):
    """Widget personalizado para ProseEditorField con altura aumentada"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configurar altura personalizada
        self.config = self.config or {}
        self.config.update({
            'height': '250px',
            'minHeight': '200px',
            'editorProps': {
                'style': {
                    'height': '250px',
                    'minHeight': '200px'
                }
            }
        })


class TallProseEditorField(ProseEditorField):
    """Campo ProseEditorField personalizado con altura aumentada"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = TallProseEditorWidget()
