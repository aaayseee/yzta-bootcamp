import plotly.graph_objects as go

def apply_plotly_theme(fig):
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#94a3b8', family='Outfit, sans-serif'),
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(font=dict(color='#f8fafc')),
        hoverlabel=dict(
            bgcolor="#1e293b",
            font_size=13,
            font_family="Outfit"
        )
    )
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255, 255, 255, 0.05)', color='#94a3b8')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255, 255, 255, 0.05)', color='#94a3b8')
    return fig
