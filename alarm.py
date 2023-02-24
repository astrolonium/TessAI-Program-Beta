import tkinter as tk
import time
import winsound

class AlarmClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Alarm Clock")
        self.alarms = []
        self.alarm_labels = []

        # Create widgets
        self.label_time = tk.Label(self.master, font=('calibri', 40, 'bold'), bg='black', fg='white', width=10, anchor='center')
        self.label_time.pack(padx=10, pady=10)

        self.label_alarm = tk.Label(self.master, text='Set Alarm', font=('calibri', 20, 'bold'), anchor='w')
        self.label_alarm.pack(padx=10, pady=10)

        self.frame_alarms = tk.Frame(self.master)
        self.frame_alarms.pack()

        self.button_set_alarm = tk.Button(self.master, text='Add Alarm', font=('calibri', 16), command=self.add_alarm)
        self.button_set_alarm.pack(padx=10, pady=10)

        # Create a timer to update the time label every second
        self.update_time()
        self.timer = self.master.after(1000, self.update_time)

    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.label_time.config(text=current_time)
        self.check_alarms()
        self.timer = self.master.after(1000, self.update_time)

    def add_alarm(self):
        if len(self.alarms) >= 5:
            tk.messagebox.showinfo("Error", "Maximum number of alarms reached")
            return

        alarm = tk.Toplevel(self.master)
        alarm.title("Add Alarm")
        alarm.geometry('300x150')

        label_time = tk.Label(alarm, text='Time (HH:MM:SS)', font=('calibri', 12))
        label_time.pack(padx=10, pady=10)
        entry_time = tk.Entry(alarm, font=('calibri', 12))
        entry_time.pack(padx=10, pady=10)

        label_ringtone = tk.Label(alarm, text='Ringtone', font=('calibri', 12))
        label_ringtone.pack(padx=10, pady=10)
        entry_ringtone = tk.Entry(alarm, font=('calibri', 12))
        entry_ringtone.pack(padx=10, pady=10)

        button_save = tk.Button(alarm, text='Save', font=('calibri', 12), command=lambda: self.save_alarm(entry_time.get(), entry_ringtone.get(), alarm))
        button_save.pack(padx=10, pady=10)

    def save_alarm(self, time_str, ringtone, alarm):
        try:
            time_obj = time.strptime(time_str, '%H:%M:%S')
            alarm_time = time.strftime('%H:%M:%S', time_obj)
        except ValueError:
            tk.messagebox.showinfo("Error", "Invalid time format")
            return

        if alarm_time in self.alarms:
            tk.messagebox.showinfo("Error", "Alarm already exists")
            return

        self.alarms.append(alarm_time)
        self.alarm_labels.append((alarm_time, ringtone))

        label_alarm = tk.Label(self.frame_alarms, text=f'{alarm_time} ({ringtone})', font=('calibri', 12))
        label_alarm.pack(padx=10, pady=5)

        alarm.destroy()

    def check_alarms(self):
        current_time = time.strftime('%H:%M:%S')
        for i, alarm in enumerate(self.alarms):
            if current_time == alarm:
                    ringtone = self.alarm_labels[i][1]
            if ringtone:
                try:
                    winsound.PlaySound(ringtone, winsound.SND_FILENAME)
                except:
                    pass
            else:
                try:
                    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
                except:
                    pass

            # Remove the alarm
            self.alarms.pop(i)
            self.alarm_labels.pop(i)
            self.label_alarm.config(text='Alarm triggered', fg='red')
            self.master.after(3000, lambda: self.label_alarm.config(text='Set Alarm', fg='black'))
            self.frame_alarms.destroy()
            self.frame_alarms = tk.Frame(self.master)
            self.frame_alarms.pack()
            for alarm in self.alarm_labels:
                label_alarm = tk.Label(self.frame_alarms, text=f'{alarm[0]} ({alarm[1]})', font=('calibri', 12))
                label_alarm.pack(padx=10, pady=5)


root = tk.Tk()
app = AlarmClock(root)
root.mainloop()
