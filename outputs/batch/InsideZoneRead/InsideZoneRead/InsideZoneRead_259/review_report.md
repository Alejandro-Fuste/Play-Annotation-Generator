# Play-Annotation-Generator Annotation Review — InsideZoneRead_259

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_259`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 158
- **Validation Warnings:** 153
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 132
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `20` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 5 | START | 5 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 8 | START | 8 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `13` | `12` | 8 | START | 8 | 38 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 8 | START | 21 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 8 | START | 8 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 8 | START | 8 | 25 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 20 | END | 5 | 20 |
| ✅ EXACT | `Action_ReadDefender` | QB | `15` | `14` | 22 | START | 22 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `15` | `14` | 32 | START | 32 | 36 |
| ✅ EXACT | `Action_BallCarry` | QB | `15` | `14` | 58 | START | 58 | 91 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 90 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 5 | 20 | 16 | inferred_complete_timeline |
| `Action_None` | 21 | 21 | 1 | inferred_complete_timeline |
| `Action_ReadDefender` | 22 | 31 | 10 | inferred_complete_timeline |
| `Action_Keep` | 32 | 36 | 5 | inferred_complete_timeline |
| `Action_Keep` | 38 | 57 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 58 | 91 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 38 | 34 | inferred_complete_timeline |
| `Action_None` | 48 | 109 | 62 | inferred_complete_timeline |
| `Action_None` | 116 | 137 | 22 | inferred_complete_timeline |
| `Action_None` | 139 | 146 | 8 | inferred_complete_timeline |
| `Action_None` | 152 | 154 | 3 | inferred_complete_timeline |
| `Action_None` | 166 | 172 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 121 | 117 | inferred_complete_timeline |
| `Action_None` | 125 | 202 | 78 | inferred_complete_timeline |
| `Action_None` | 211 | 239 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 65 | 61 | inferred_complete_timeline |
| `Action_None` | 72 | 78 | 7 | inferred_complete_timeline |
| `Action_None` | 88 | 90 | 3 | inferred_complete_timeline |
| `Action_None` | 95 | 106 | 12 | inferred_complete_timeline |
| `Action_None` | 109 | 239 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 105 | 101 | inferred_complete_timeline |
| `Action_None` | 110 | 116 | 7 | inferred_complete_timeline |
| `Action_None` | 119 | 239 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 239 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 38 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 90 | 50 | inferred_complete_timeline |
| `Action_None` | 91 | 95 | 5 | inferred_complete_timeline |
| `Action_None` | 124 | 129 | 6 | inferred_complete_timeline |
| `Action_None` | 172 | 175 | 4 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 184 | 188 | 5 | inferred_complete_timeline |
| `Action_None` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 211 | 5 | inferred_complete_timeline |
| `Action_None` | 224 | 227 | 4 | inferred_complete_timeline |
| `Action_None` | 232 | 239 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 69 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 90 | 17 | inferred_complete_timeline |
| `Action_None` | 91 | 153 | 63 | inferred_complete_timeline |
| `Action_None` | 163 | 239 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–95
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 5 | 20 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 35 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 65 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 90 | 1 | inferred_complete_timeline |
| `Action_None` | 91 | 91 | 1 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 25 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 65 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 69 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 85 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 90 | 1 | inferred_complete_timeline |
| `Action_None` | 91 | 110 | 20 | inferred_complete_timeline |
| `Action_None` | 112 | 151 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 91 | 87 | inferred_complete_timeline |
| `Action_None` | 96 | 101 | 6 | inferred_complete_timeline |
| `Action_None` | 103 | 129 | 27 | inferred_complete_timeline |
| `Action_None` | 131 | 239 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 60 | 56 | inferred_complete_timeline |
| `Action_None` | 74 | 77 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 37 | 33 | inferred_complete_timeline |
| `Action_None` | 58 | 67 | 10 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 97 | 19 | inferred_complete_timeline |
| `Action_None` | 102 | 104 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 27 | 23 | inferred_complete_timeline |
| `Action_None` | 31 | 70 | 40 | inferred_complete_timeline |
| `Action_None` | 72 | 77 | 6 | inferred_complete_timeline |
| `Action_None` | 85 | 87 | 3 | inferred_complete_timeline |
| `Action_None` | 105 | 127 | 23 | inferred_complete_timeline |
| `Action_None` | 132 | 171 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 69 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 70 | 66 | inferred_complete_timeline |
| `Action_None` | 79 | 95 | 17 | inferred_complete_timeline |
| `Action_None` | 110 | 144 | 35 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 195 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 107 | 103 | inferred_complete_timeline |
| `Action_None` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_None` | 119 | 239 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 137 | 133 | inferred_complete_timeline |
| `Action_None` | 148 | 239 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 96 | 92 | inferred_complete_timeline |
| `Action_None` | 105 | 208 | 104 | inferred_complete_timeline |
| `Action_None` | 212 | 214 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 187 | 183 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 239 | 235 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 6–8 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 13–34 | 16 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 51–139 | 88 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 54–56 | 3 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 70–239 | 104 | 7 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 93–239 | 105 | 10 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 99–138 | 35 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 108–212 | 100 | 3 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 117–141 | 15 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 127–141 | 15 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 135–239 | 97 | 5 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 153–239 | 87 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 201–202 | 2 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 206–220 | 12 | 2 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 211–239 | 28 | 2 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 213–227 | 8 | 2 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 218–239 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 115 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [5–20], lower_priority='Action_ZoneBlock' annotated_start=8, effective_Action_ZoneBlock_start=21.
- ⚠️ Action 'Action_None' range [5-60] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-77] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-105] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-116] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-27] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-70] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-77] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-127] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-171] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-101] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-129] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-96] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-208] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-202] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-37] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-67] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-97] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-69] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-85] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-110] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-151] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-38] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [41-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-35] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [37-65] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 91, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [91-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [32-36] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [58-91] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-70] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-95] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-144] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-195] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-187] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-153] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-65] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-106] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-38] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-109] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-137] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-25] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [37-65] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-8] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-18] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-26] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-34] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-135] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-56] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-90] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-97] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-107] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-176] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-125] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-172] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-207] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-233] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-131] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-117] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-209] for track '29' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-129] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-141] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-214] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-234] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-215] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-216] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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

</details>