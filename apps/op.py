import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

def app():
    df = pd.read_excel("data.xlsx")

    # ---- SIDEBAR ----
    st.header("Please Filter Here:")
    machine = st.multiselect(
        "Select the machine type:",
        options=df["Machine"].unique(),
        default=df["Machine"].unique()
    )

    failure_type = st.multiselect(
        "Select the Failure Type:",
        options=df["naturedepanne"].unique(),
        default=df["naturedepanne"].unique(),
    )

 

    df_selection = df.query(
        "Machine == @machine  & naturedepanne == @failure_type"
    )

    # ---- MAINPAGE ----
 

    # TOP KPI's
    total_interventions = int(df_selection["TempsIntervention"].sum())
    average_intervention = round(df_selection["TempsIntervention"].mean(), 1)
   

  

    # SALES BY PRODUCT LINE [BAR CHART]
    sales_by_product_line = (
        df_selection.groupby(by=["Intervenant"]).sum()[["TempsIntervention"]].sort_values(by="TempsIntervention")
    )
    fig_product_sales = px.bar(
        sales_by_product_line,
        x=sales_by_product_line.index,
        y="TempsIntervention",
        orientation="v",
        title="<b>Sales by Product Line</b>",
        color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
        template="plotly_white",
    )
    fig_product_sales.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )



    st.plotly_chart(fig_product_sales, use_container_width=True)







