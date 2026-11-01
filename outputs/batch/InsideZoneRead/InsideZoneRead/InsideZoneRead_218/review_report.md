# Play-Annotation-Generator Annotation Review — InsideZoneRead_218

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_218`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 148
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 3
- **Inferred Coverage Segments (Action_None):** 123
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ℹ️ GLOBAL EVENT | `Action_ReadDefender` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `15` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `21` | `20` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `21` | `20` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 62 |
| ℹ️ GLOBAL EVENT | `Action_ReadDefender` | N/A | N/A | N/A | 0 | START | N/A | N/A |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 60 | START | 60 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `15` | 63 | START | 63 | 75 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `20` | `19` | 63 | START | 73 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 63 | START | 65 | 70 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `6` | 63 | START | 63 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `8` | 63 | START | 63 | 85 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `21` | `20` | 72 | END | 60 | 69 |
| ✅ EXACT | `Action_Handoff` | QB | `21` | `20` | 93 | START | 93 | 104 |
| ✅ EXACT | `Action_BallCarry` | QB | `21` | `20` | 105 | START | 105 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `16` | `15` | 107 | START | 110 | 113 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 151 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_SnapReceive` | 60 | 69 | 10 | inferred_complete_timeline |
| `Action_None` | 74 | 87 | 14 | inferred_complete_timeline |
| `Action_None` | 92 | 92 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 93 | 104 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 105 | 239 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 137 | 78 | inferred_complete_timeline |
| `Action_None` | 139 | 192 | 54 | inferred_complete_timeline |
| `Action_None` | 213 | 228 | 16 | inferred_complete_timeline |
| `Action_None` | 234 | 236 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 181 | 122 | inferred_complete_timeline |
| `Action_None` | 183 | 217 | 35 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 129 | 70 | inferred_complete_timeline |
| `Action_None` | 131 | 135 | 5 | inferred_complete_timeline |
| `Action_None` | 139 | 151 | 13 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 239 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 211 | 152 | inferred_complete_timeline |
| `Action_None` | 228 | 232 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 85 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 137 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 151 | 13 | inferred_complete_timeline |
| `Action_None` | 152 | 159 | 8 | inferred_complete_timeline |
| `Action_None` | 166 | 213 | 48 | inferred_complete_timeline |
| `Action_None` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 75 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 85 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 106 | 10 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 142 | 146 | 5 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 148 | 151 | 4 | inferred_complete_timeline |
| `Action_None` | 152 | 152 | 1 | inferred_complete_timeline |
| `Action_None` | 156 | 162 | 7 | inferred_complete_timeline |
| `Action_None` | 168 | 172 | 5 | inferred_complete_timeline |
| `Action_None` | 174 | 239 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_BallSnap` | 60 | 72 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 78 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 70 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 78 | 84 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 129 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 151 | 13 | inferred_complete_timeline |
| `Action_None` | 152 | 162 | 11 | inferred_complete_timeline |
| `Action_None` | 166 | 239 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 79 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 121 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 131 | 136 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 151 | 13 | inferred_complete_timeline |
| `Action_None` | 152 | 239 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 85 | 26 | inferred_complete_timeline |
| `Action_None` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_None` | 97 | 129 | 33 | inferred_complete_timeline |
| `Action_None` | 131 | 136 | 6 | inferred_complete_timeline |
| `Action_None` | 139 | 162 | 24 | inferred_complete_timeline |
| `Action_None` | 165 | 239 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 84 | 25 | inferred_complete_timeline |
| `Action_None` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_None` | 97 | 113 | 17 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_None` | 148 | 158 | 11 | inferred_complete_timeline |
| `Action_None` | 160 | 239 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 85 | 26 | inferred_complete_timeline |
| `Action_None` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_None` | 97 | 105 | 9 | inferred_complete_timeline |
| `Action_None` | 124 | 129 | 6 | inferred_complete_timeline |
| `Action_None` | 131 | 136 | 6 | inferred_complete_timeline |
| `Action_None` | 139 | 162 | 24 | inferred_complete_timeline |
| `Action_None` | 166 | 171 | 6 | inferred_complete_timeline |
| `Action_None` | 182 | 202 | 21 | inferred_complete_timeline |
| `Action_None` | 204 | 230 | 27 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 94 | 35 | inferred_complete_timeline |
| `Action_None` | 97 | 129 | 33 | inferred_complete_timeline |
| `Action_None` | 131 | 136 | 6 | inferred_complete_timeline |
| `Action_None` | 140 | 162 | 23 | inferred_complete_timeline |
| `Action_None` | 166 | 239 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 129 | 70 | inferred_complete_timeline |
| `Action_None` | 131 | 136 | 6 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 142 | 162 | 21 | inferred_complete_timeline |
| `Action_None` | 166 | 239 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 210 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 129 | 70 | inferred_complete_timeline |
| `Action_None` | 131 | 136 | 6 | inferred_complete_timeline |
| `Action_None` | 139 | 162 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 202 | 143 | inferred_complete_timeline |
| `Action_None` | 206 | 219 | 14 | inferred_complete_timeline |
| `Action_None` | 222 | 239 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–124 | 111 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 98–135 | 32 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 123–239 | 98 | 10 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 157–239 | 80 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 157–224 | 22 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 171–181 | 6 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 190–239 | 48 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (4 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `20` (C): Annotated start 63 != Inferred start 73
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `16` (4 segments found)

### Track Identity Issues

- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 108 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 436: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [60–72], lower_priority='Action_ZoneBlock' annotated_start=63, effective_Action_ZoneBlock_start=73.
- ⚠️ Action 'Action_None' range [60-129] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-151] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-239] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-211] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-239] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-137] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-192] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-228] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-217] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-79] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-94] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [131-136] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-85] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-213] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-85] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-105] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-202] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-230] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-85] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-162] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-84] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-113] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-158] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-85] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [110-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [115-120] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [142-146] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 152, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [152-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-239] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-80] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-124] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-202] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-219] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-78] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [60-69] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-87] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [78-84] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-239] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-115] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-128] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-129] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-154] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-179] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-219] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-231] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-163] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-179] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-166] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-224] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-224] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>