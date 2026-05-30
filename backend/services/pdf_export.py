from fpdf import FPDF


def generate_combined_pdf(data) -> bytes:
    pdf = FPDF()
    pdf.add_page()

    score = round(data.get("score", 0))
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 20, "ATS Resume Score Report", align="C")
    pdf.ln(20)

    pdf.set_font("Helvetica", "B", 48)
    # pdf.cell(0, 30, f"{score}/100", align="C")
    pdf.ln(20)

    pdf.set_font("Helvetica", "", 14)
    pdf.multi_cell(
        0,
        10,
        f"Your ATS Resume Score is {score}/100."
    )

    return bytes(pdf.output())