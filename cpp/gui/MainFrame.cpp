//
// Created by josh on 1/3/26.
//

#include "MainFrame.h"
#include <wx/wx.h>
#include <wx/spinctrl.h>

// Macros (static event handling)
// enum IDs
// {
//     // ID must be positive, not 0 or 1
//     BUTTON_ID = 2,
//     SLIDER_ID = 3,
//     TEXT_ID = 4
// };

// wxBEGIN_EVENT_TABLE(MainFrame, wxFrame)
//     EVT_BUTTON(BUTTON_ID, MainFrame::OnButtonClicked)
//     EVT_SLIDER(SLIDER_ID, MainFrame::OnSliderChanged)
//     EVT_TEXT(TEXT_ID, MainFrame::OnTextChanged)
// wxEND_EVENT_TABLE()

MainFrame::MainFrame(const wxString& title) : wxFrame(nullptr, wxID_ANY, title)
{
    // Entry point in a wx window program: Class that represents application
    wxPanel* panel = new wxPanel(this);

    // Controls - all controls need a parent, ID, pos, and size
    // wxButton* button = new wxButton(
    //     panel, wxID_ANY, "Button",
    //     wxPoint(150, 50),
    //     wxSize(100, 35),
    //     wxBU_LEFT);     // Left-align text
    //
    // wxCheckBox* checkBox = new wxCheckBox(
    //     panel, wxID_ANY, "CheckBox",
    //     wxPoint(550, 55),
    //     wxDefaultSize,
    //     wxCHK_3STATE | wxCHK_ALLOW_3RD_STATE_FOR_USER);     // Add undetermined state
    //
    // wxStaticText* staticText = new wxStaticText(
    //     panel, wxID_ANY, "StaticText - NOT editable",
    //     wxPoint(0, 150),
    //     wxSize(400, -1),
    //     wxALIGN_CENTER_HORIZONTAL);
    // staticText->SetBackgroundColour(*wxLIGHT_GREY);
    //
    // wxTextCtrl* textCtrl = new wxTextCtrl(
    //     panel, wxID_ANY, "TextCtrl - editable",
    //     wxPoint(500, 145),
    //     wxSize(200, -1),
    //     wxTE_PASSWORD);                                     // Password style text input
    //
    // wxSlider* slider = new wxSlider(
    //     panel, wxID_ANY, 25, 0, 100,
    //     wxPoint(100, 250),
    //     wxSize(200, -1),
    //     wxSL_VALUE_LABEL);                                  // Slider will display current value
    //
    // // Not interactable, set from code
    // wxGauge* gauge = new wxGauge(
    //     panel, wxID_ANY, 100,
    //     wxPoint(590, 205),
    //     wxSize(-1, 125),
    //     wxGA_VERTICAL);
    // gauge->SetValue(50);
    //
    // wxArrayString choices;
    // choices.Add("Item C");
    // choices.Add("Item A");
    // choices.Add("Item B");
    //
    // wxChoice* choice = new wxChoice(
    //     panel, wxID_ANY,
    //     wxPoint(150, 375),
    //     wxSize(100, -1),
    //     choices, wxCB_SORT);                              // Sorts the choices into alphabetical(?) order
    // choice->Select(0);                                      // Set default
    //
    // wxSpinCtrl* spinCtrl = new wxSpinCtrl(
    //     panel, wxID_ANY, "",
    //     wxPoint(550, 375),
    //     wxSize(120, -1),
    //     wxSP_WRAP);
    //
    //
    // wxListBox* listBox = new wxListBox(
    //     panel, wxID_ANY,
    //     wxPoint(150, 475),
    //     wxSize(100, -1),
    //     choices, wxLB_MULTIPLE);
    //
    // wxRadioBox* radioBox = new wxRadioBox(
    //     panel, wxID_ANY, "Radio Box",
    //     wxPoint(555, 450),
    //     wxDefaultSize,
    //     choices, 3,                                             // Number of columns or rows
    //     wxRA_SPECIFY_ROWS);

    // IMPORTANT: wxWidgets takes care of deallocating memory for these controls

    wxButton* button = new wxButton(
        panel, wxID_ANY, "Button",
        wxPoint(300, 275),
        wxSize(200,50));

    wxSlider* slider = new wxSlider(
        panel, wxID_ANY, 0, 0, 100,
        wxPoint(300, 200),
        wxSize(200, -1));

    wxTextCtrl* text = new wxTextCtrl(
        panel, wxID_ANY, "",
        wxPoint(300, 375),
        wxSize(200, -1));

    // Dynamic event handling (use this!)
    button->Bind(wxEVT_BUTTON, &MainFrame::OnButtonClicked, this);
    slider->Bind(wxEVT_SLIDER, &MainFrame::OnSliderChanged, this);
    text->Bind(wxEVT_TEXT, &MainFrame::OnTextChanged, this);

    button->Unbind(wxEVT_BUTTON, &MainFrame::OnButtonClicked, this);

    CreateStatusBar();
}

void MainFrame::OnButtonClicked(wxCommandEvent& evt)
{
    wxLogStatus("Button Clicked!");
}

void MainFrame::OnSliderChanged(wxCommandEvent& evt)
{
    wxString str = wxString::Format("Slider Value: %d", evt.GetInt());
    wxLogStatus(str);
}

void MainFrame::OnTextChanged(wxCommandEvent& evt)
{
    wxString str = wxString::Format("Text: %s", evt.GetString());
    wxLogStatus(str);
}