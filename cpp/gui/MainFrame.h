//
// Created by josh on 1/3/26.
//

#ifndef REFERENCES_MAINFRAME_H
#define REFERENCES_MAINFRAME_H
#pragma once
#include <wx/wx.h>

class MainFrame : public wxFrame
{
  public:
    MainFrame(const wxString &title);

  private:
    void OnAnyButtonClicked(wxCommandEvent &evt);
    void OnButton1Clicked(wxCommandEvent &evt);
    void OnButton2Clicked(wxCommandEvent &evt);
    void OnClose(wxCloseEvent &evt);
    // void OnSliderChanged(wxCommandEvent &evt);
    // void OnTextChanged(wxCommandEvent &evt);
};

#endif //REFERENCES_MAINFRAME_H
