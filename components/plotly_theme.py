import plotly.graph_objects as go
import streamlit as st

# Marka renk paleti: mavi / mor / yesil
BRAND_COLORWAY = ["#0ea5e9", "#8b5cf6", "#10b981", "#38bdf8", "#a78bfa", "#34d399"]


def _detect_theme_mode() -> str:
    """Streamlit'in aktif temasini (acik/koyu) guvenli bicimde tespit eder."""
    try:
        # Streamlit >= 1.35: st.context.theme.type -> 'light' | 'dark'
        theme_type = st.context.theme.type
        if theme_type in ("light", "dark"):
            return theme_type
    except Exception:
        pass
    try:
        base = st.get_option("theme.base")
        if base in ("light", "dark"):
            return base
    except Exception:
        pass
    return "dark"


def apply_plotly_theme(fig):
    is_light = _detect_theme_mode() == "light"

    text_color = "#334155" if is_light else "#94a3b8"
    legend_color = "#0f172a" if is_light else "#f8fafc"
    grid_color = "rgba(15, 23, 42, 0.08)" if is_light else "rgba(255, 255, 255, 0.06)"
    hover_bg = "#ffffff" if is_light else "#1e293b"
    hover_font = "#0f172a" if is_light else "#f8fafc"

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color=text_color, family='Outfit, sans-serif'),
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(font=dict(color=legend_color)),
        colorway=BRAND_COLORWAY,
        transition=dict(duration=400, easing='cubic-in-out'),
        hoverlabel=dict(
            bgcolor=hover_bg,
            font_size=13,
            font_family="Outfit",
            font_color=hover_font,
            bordercolor="rgba(14, 165, 233, 0.35)"
        )
    )
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor=grid_color, color=text_color, zerolinecolor=grid_color)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor=grid_color, color=text_color, zerolinecolor=grid_color)
    return fig
