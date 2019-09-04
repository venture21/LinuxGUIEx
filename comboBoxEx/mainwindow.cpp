#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->cb1->addItem("Option1");
    ui->cb1->addItem("Option2");
    ui->cb1->addItem("Option3");
    ui->cb1->addItem("Option4");
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_cb1_activated(const QString &arg1)
{
    ui->lbl->setText(arg1);
    ui->lbl->adjustSize();
}
