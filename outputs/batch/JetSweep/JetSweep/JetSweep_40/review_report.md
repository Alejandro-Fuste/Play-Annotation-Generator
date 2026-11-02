# Play-Annotation-Generator Annotation Review — JetSweep_40

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_40`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 159
- **Validation Warnings:** 170
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 26
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 4
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 132
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-Y | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-F | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | LT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE-F | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_Toss` | QB | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | offense | `17` | `16` |
| ✅ EXACT | `Action_BallCarry` | WR | offense | `2` | `1` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `10` | `9` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `17` | `16` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `17` | `16` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `22` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `2` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-Y | `23` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE-F | `8` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_JetMotion` | WR | `2` | `1` | 20 | START | 20 | 73 |
| ✅ EXACT | `Action_BallSnap` | LT | `17` | `16` | 48 | START | 48 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE-F | `8` | `7` | 50 | START | 50 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 50 | START | 50 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `15` | 50 | START | 50 | 72 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `17` | `16` | 50 | START | 50 | 71 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 50 | START | 50 | 72 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 59 | END | 48 | 59 |
| ✅ EXACT | `Action_Toss` | QB | `20` | `19` | 67 | START | 67 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | `17` | `16` | 72 | START | 72 | 72 |
| ✅ EXACT | `Action_BallCarry` | WR | `2` | `1` | 74 | START | 74 | 112 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `10` | `9` | 116 | BOUNDARY | 116 | 116 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `17` | `16` | 116 | BOUNDARY | 104 | 116 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `17` | `16` | 116 | BOUNDARY | 104 | 116 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `22` | `21` | 116 | BOUNDARY | N/A | 116 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SnapReceive` | 48 | 59 | 12 | inferred_complete_timeline |
| `Action_None` | 60 | 66 | 7 | inferred_complete_timeline |
| `Action_Toss` | 67 | 73 | 7 | inferred_complete_timeline |
| `Action_None` | 74 | 84 | 11 | inferred_complete_timeline |
| `Action_None` | 86 | 192 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 88 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 249 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_JetMotion` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_BallCarry` | 74 | 112 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>TE-F — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_LeadBlock` | 50 | 103 | 54 | inferred_complete_timeline |
| `Action_LeadBlock` | 105 | 115 | 11 | inferred_complete_timeline |
| `Action_None` | 117 | 120 | 4 | inferred_complete_timeline |
| `Action_None` | 122 | 139 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE-Y — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 73 | 26 | inferred_complete_timeline |
| `Action_None` | 81 | 94 | 14 | inferred_complete_timeline |
| `Action_None` | 97 | 100 | 4 | inferred_complete_timeline |
| `Action_None` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_None` | 121 | 184 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_BallSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 71 | 22 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 72 | 72 | 1 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 104 | 116 | 13 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_None` | 134 | 170 | 37 | inferred_complete_timeline |
| `Action_None` | 173 | 186 | 14 | inferred_complete_timeline |
| `Action_None` | 195 | 197 | 3 | inferred_complete_timeline |
| `Action_None` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 211 | 4 | inferred_complete_timeline |
| `Action_None` | 213 | 233 | 21 | inferred_complete_timeline |
| `Action_None` | 235 | 246 | 12 | inferred_complete_timeline |
| `Action_None` | 248 | 251 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 72 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 72 | 23 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 172 | 40 | inferred_complete_timeline |
| `Action_None` | 176 | 184 | 9 | inferred_complete_timeline |
| `Action_None` | 186 | 188 | 3 | inferred_complete_timeline |
| `Action_None` | 195 | 197 | 3 | inferred_complete_timeline |
| `Action_None` | 201 | 205 | 5 | inferred_complete_timeline |
| `Action_None` | 219 | 223 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 72 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 116 | 1 | inferred_complete_timeline |
| `Action_None` | 117 | 155 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 72 | 25 | inferred_complete_timeline |
| `Action_None` | 75 | 204 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 71 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 71 | 24 | inferred_complete_timeline |
| `Action_None` | 91 | 98 | 8 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 71 | 24 | inferred_complete_timeline |
| `Action_None` | 88 | 92 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 77 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 94 | 47 | inferred_complete_timeline |
| `Action_None` | 96 | 193 | 98 | inferred_complete_timeline |
| `Action_None` | 196 | 199 | 4 | inferred_complete_timeline |
| `Action_None` | 202 | 224 | 23 | inferred_complete_timeline |
| `Action_None` | 226 | 279 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>FS — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 136 | 89 | inferred_complete_timeline |
| `Action_None` | 139 | 299 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 74 | 27 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 299 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 190 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 71 | 24 | inferred_complete_timeline |
| `Action_None` | 78 | 85 | 8 | inferred_complete_timeline |
| `Action_None` | 93 | 144 | 52 | inferred_complete_timeline |
| `Action_None` | 170 | 188 | 19 | inferred_complete_timeline |
| `Action_None` | 193 | 199 | 7 | inferred_complete_timeline |
| `Action_None` | 201 | 223 | 23 | inferred_complete_timeline |
| `Action_None` | 226 | 255 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–299 | 263 | 7 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–126 | 62 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 90–168 | 52 | 8 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 99–139 | 36 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 108–228 | 118 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 118–119 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 119–129 | 11 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 119–156 | 25 | 5 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 133–259 | 125 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 135–227 | 73 | 8 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 140–299 | 160 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 146–147 | 2 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 151–230 | 66 | 8 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 167–173 | 6 | 2 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 171–189 | 14 | 2 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 185–299 | 115 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 185–253 | 68 | 2 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 202–242 | 41 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 211–238 | 24 | 3 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 220–231 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `17` (4 segments found)

### Track Identity Issues

- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 128 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 81: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [48-249] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [74-112] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-72] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-204] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-77] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-71] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-94] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-193] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-224] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-279] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [50-103] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [105-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-139] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-88] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-72] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-155] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-190] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-136] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-299] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-71] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-71] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-85] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-144] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-188] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-223] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-255] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-71] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-72] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' for track '16' starts at frame 72, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BlockSecondLevel' range [72-72] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [92-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [96-97] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [104-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-186] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-233] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-246] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-72] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-99] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-84] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-192] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-51] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-122] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-184] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-73] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-94] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-184] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-124] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-147] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-223] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-129] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-140] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-149] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-156] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-249] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-259] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-156] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-193] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-299] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-193] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-214] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-179] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-299] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-253] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-242] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-223] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-238] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>