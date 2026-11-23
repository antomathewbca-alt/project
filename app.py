with tab_benchmarks:
    st.subheader("🧪 Machine Learning Benchmarking & Accuracy Metrics")
    st.caption("Rigorous multi-model evaluation on held-out test data (80/20 train-test split).")
    
    bench_records = []
    for m_name, metrics in engine.benchmarks.items():
        bench_records.append({
            "Algorithm": m_name,
            "R² Score (Goodness of Fit)": f"{metrics['R2_Score']:.4f}",
            "MAE (Mean Absolute Error)": f"₹{metrics['MAE_Lakhs']:.2f} L",
            "RMSE (Root Mean Sq Error)": f"₹{metrics['RMSE_Lakhs']:.2f} L",
            "MAPE (% Error)": f"{metrics['MAPE_Pct']:.2f}%",
            "Rank": "🏆 Champion" if m_name == engine.best_model_name else "Candidate"
        })
    st.dataframe(pd.DataFrame(bench_records), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("##### Verified Listing Dataset Explorer")
    st.caption(f"Showing sample data from the {len(df_data)} verified Indian metro property listings:")
    
    filter_city = st.selectbox("Explore Listings in City", ["All"] + list(CITY_DATA.keys()), key="explorer_city")
    if filter_city == "All":
        preview_df = df_data.head(50)
    else:
        preview_df = df_data[df_data["City"] == filter_city].head(50)
        
    st.dataframe(preview_df[["City", "Locality", "BHK", "Property_Type", "Area_SqFt", "Furnishing", "Age_Years", "Price_Lakhs", "Price_Per_SqFt"]], use_container_width=True)
# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94A3B8; font-size: 0.85rem;">
    PropValuer AI • Real Estate Price & Valuation Predictor • Powered by Scikit-Learn & Streamlit
</div>
""", unsafe_allow_html=True)
