//
// Created by josh on 1/3/26.
//

#include "App.h"
#include "MainFrame.h"
#include <wx/wx.h>

wxIMPLEMENT_APP(App);

bool App::OnInit()
{
    MainFrame* mainFrame = new MainFrame("C++ GUI");
    // Window sizing etc options
    mainFrame->SetClientSize(800, 600);
    mainFrame->Center();
    mainFrame->Show();
    return true;
}
