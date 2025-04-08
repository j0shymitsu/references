package exercises;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class HelloWorld
{
    private JPanel rootPanel;
    private JLabel helloLabel;
    private JButton helloButton;
    private JTextField nameTextField;
    private JTextField greetingLabel;

    public HelloWorld()
    {
        helloButton.addActionListener(new ActionListener()
        {
            @Override
            public void actionPerformed(ActionEvent actionEvent)
            {
                greetingLabel.setText("Hello " + nameTextField.getText());
            }
        });
    }

    /* Code > generate > 'Form.main()' */
    public static void main(String[] args)
    {
        JFrame frame = new JFrame("HelloWorld");
        frame.setContentPane(new HelloWorld().rootPanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }

}
