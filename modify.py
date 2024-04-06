import os

def find_and_replace_method(file_path, method_signature, replacement_text):
    temp_file_path = file_path + '.temp'
    method_started = False
    found_method = False

    with open(file_path, 'r') as input_file, open(temp_file_path, 'w') as output_file:
        for line in input_file:
            if method_signature in line:
                method_started = True
                found_method = True
                output_file.write(replacement_text)
            elif method_started and '.end method' in line:
                method_started = False
            elif not method_started:
                output_file.write(line)

    os.replace(temp_file_path, file_path)

    if found_method:
        print("Method replaced successfully.")
    else:
        print("Method not found.")

target_smali = os.path.join('decompiled_apk', 'smali', 'com', 'jamworks', 'dynamicspot', 'SettingsHome.smali')

find_and_replace_method(target_smali, '.method public r(Ljava/util/List;)V', '''.method public r(Ljava/util/List;)V
    .locals 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/util/List<",
            "Lcom/android/billingclient/api/Purchase;",
            ">;)V"
        }
    .end annotation

    .line 1
    const/4 v0, 0x1

    .line 2
    iput-boolean v0, p0, Lcom/jamworks/dynamicspot/SettingsHome;->V:Z

    .line 3
    .line 4
    iput-boolean v0, p0, Lcom/jamworks/dynamicspot/SettingsHome;->L:Z

    .line 5
    .line 6
    if-eqz p1, :cond_4

    .line 7
    .line 8
    invoke-interface {p1}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    .line 9
    .line 10
    .line 11
    move-result-object p1

    .line 12
    :cond_0
    :goto_0
    invoke-interface {p1}, Ljava/util/Iterator;->hasNext()Z

    .line 13
    .line 14
    .line 15
    move-result v0

    .line 16
    if-eqz v0, :cond_4

    .line 17
    .line 18
    invoke-interface {p1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    .line 19
    .line 20
    .line 21
    move-result-object v0

    .line 22
    check-cast v0, Lcom/android/billingclient/api/Purchase;

    .line 23
    .line 24
    invoke-virtual {v0}, Lcom/android/billingclient/api/Purchase;->b()Ljava/util/List;

    .line 25
    .line 26
    .line 27
    move-result-object v1

    .line 28
    const-string v2, "aod_coffee"

    .line 29
    .line 30
    invoke-interface {v1, v2}, Ljava/util/List;->contains(Ljava/lang/Object;)Z

    .line 31
    .line 32
    .line 33
    move-result v1

    .line 34
    if-nez v1, :cond_1

    .line 35
    .line 36
    invoke-virtual {v0}, Lcom/android/billingclient/api/Purchase;->b()Ljava/util/List;

    .line 37
    .line 38
    .line 39
    move-result-object v1

    .line 40
    const-string v2, "aod_coffee_big"

    .line 41
    .line 42
    invoke-interface {v1, v2}, Ljava/util/List;->contains(Ljava/lang/Object;)Z

    .line 43
    .line 44
    .line 45
    move-result v1

    .line 46
    if-nez v1, :cond_1

    .line 47
    .line 48
    invoke-virtual {v0}, Lcom/android/billingclient/api/Purchase;->b()Ljava/util/List;

    .line 49
    .line 50
    .line 51
    move-result-object v1

    .line 52
    const-string v2, "aod_coffee_small"

    .line 53
    .line 54
    invoke-interface {v1, v2}, Ljava/util/List;->contains(Ljava/lang/Object;)Z

    .line 55
    .line 56
    .line 57
    move-result v1

    .line 58
    if-eqz v1, :cond_0

    .line 59
    .line 60
    :cond_1
    invoke-virtual {v0}, Lcom/android/billingclient/api/Purchase;->c()I

    .line 61
    .line 62
    .line 63
    move-result v1

    .line 64
    const/4 v2, 0x1

    .line 65
    if-ne v1, v2, :cond_3

    .line 66
    .line 67
    iput-boolean v2, p0, Lcom/jamworks/dynamicspot/SettingsHome;->V:Z

    .line 68
    .line 69
    invoke-virtual {v0}, Lcom/android/billingclient/api/Purchase;->f()Z

    .line 70
    .line 71
    .line 72
    move-result v1

    .line 73
    if-nez v1, :cond_2

    .line 74
    .line 75
    invoke-static {}, Li1/a;->b()Li1/a$a;

    .line 76
    .line 77
    .line 78
    move-result-object v1

    .line 79
    invoke-virtual {v0}, Lcom/android/billingclient/api/Purchase;->d()Ljava/lang/String;

    .line 80
    .line 81
    .line 82
    move-result-object v0

    .line 83
    invoke-virtual {v1, v0}, Li1/a$a;->b(Ljava/lang/String;)Li1/a$a;

    .line 84
    .line 85
    .line 86
    move-result-object v0

    .line 87
    invoke-virtual {v0}, Li1/a$a;->a()Li1/a;

    .line 88
    .line 89
    .line 90
    move-result-object v0

    .line 91
    iget-object v1, p0, Lcom/jamworks/dynamicspot/SettingsHome;->D:Lcom/android/billingclient/api/a;

    .line 92
    .line 93
    new-instance v3, Lcom/jamworks/dynamicspot/SettingsHome$u;

    .line 94
    .line 95
    invoke-direct {v3, p0}, Lcom/jamworks/dynamicspot/SettingsHome$u;-><init>(Lcom/jamworks/dynamicspot/SettingsHome;)V

    .line 96
    .line 97
    .line 98
    invoke-virtual {v1, v0, v3}, Lcom/android/billingclient/api/a;->a(Li1/a;Li1/b;)V

    .line 99
    .line 100
    .line 101
    :cond_2
    iput-boolean v2, p0, Lcom/jamworks/dynamicspot/SettingsHome;->L:Z

    .line 102
    .line 103
    goto :goto_0

    .line 104
    :cond_3
    invoke-virtual {v0}, Lcom/android/billingclient/api/Purchase;->c()I

    .line 105
    .line 106
    .line 107
    goto :goto_0

    .line 108
    :cond_4
    iget-object p1, p0, Lcom/jamworks/dynamicspot/SettingsHome;->f:Landroid/os/Handler;

    .line 109
    .line 110
    new-instance v0, Lcom/jamworks/dynamicspot/SettingsHome$b;

    .line 111
    .line 112
    invoke-direct {v0, p0}, Lcom/jamworks/dynamicspot/SettingsHome$b;-><init>(Lcom/jamworks/dynamicspot/SettingsHome;)V

    .line 113
    .line 114
    .line 115
    invoke-virtual {p1, v0}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    .line 116
    .line 117
    .line 118
    return-void
.end method
''')
