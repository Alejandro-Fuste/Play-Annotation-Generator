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
- **Action Segments:** 144
- **Validation Warnings:** 133
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 116
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
| ❌ MISSING SEGMENT | `Action_BallSnap` | RT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `15` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | CB1 | defense | `8` | `7` |
| ✅ EXACT | `Action_ReadDefender` | CB1 | defense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | CB1 | defense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT1 | defense | `15` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 85 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | RT | `7` | `6` | 83 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `15` | 86 | START | 92 | 94 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `20` | `19` | 86 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 86 | START | 92 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `6` | 86 | START | 92 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `8` | 86 | START | 92 | 94 |
| ✅ EXACT | `Action_SnapReceive` | CB1 | `8` | `7` | 100 | END | 83 | 100 |
| ✅ EXACT | `Action_ReadDefender` | CB1 | `8` | `7` | 106 | START | 106 | 117 |
| ✅ EXACT | `Action_Handoff` | CB1 | `8` | `7` | 118 | START | 118 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LT | `9` | `8` | 133 | START | 133 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT1 | `15` | `14` | 142 | START | 148 | 158 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 174 | BOUNDARY | N/A | N/A |

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
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 82 | 9 | inferred_complete_timeline |
| `Action_None` | 83 | 87 | 5 | inferred_complete_timeline |
| `Action_None` | 92 | 239 | 148 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 137 | 55 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 181 | 99 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 129 | 47 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 211 | 129 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 132 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 133 | 137 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 139 | 159 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 213 | 48 | inferred_complete_timeline |
| `Action_BallCarry` | 224 | 239 | 16 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 85 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 106 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 146 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 152 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 162 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 172 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 174 | 174 | 1 | inferred_complete_timeline |
| `Action_None` | 175 | 239 | 65 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |

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
| `Action_PreSnap` | 65 | 70 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 84 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 129 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 162 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 174 | 9 | inferred_complete_timeline |
| `Action_None` | 175 | 239 | 65 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 121 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 131 | 136 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 174 | 36 | inferred_complete_timeline |
| `Action_None` | 175 | 239 | 65 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 94 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 113 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 148 | 158 | 11 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 160 | 174 | 15 | inferred_complete_timeline |
| `Action_None` | 175 | 239 | 65 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 94 | 12 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 129 | 47 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_SnapReceive` | 83 | 100 | 18 | inferred_complete_timeline |
| `Action_None` | 101 | 105 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 106 | 117 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 118 | 132 | 15 | inferred_complete_timeline |
| `Action_None` | 133 | 210 | 78 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 129 | 47 | inferred_complete_timeline |
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
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 202 | 120 | inferred_complete_timeline |
| `Action_None` | 206 | 219 | 14 | inferred_complete_timeline |
| `Action_None` | 222 | 239 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–124 | 111 | 3 | Undefined position; Undefined team |
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

- ❌ Missing segment for action `Action_BallSnap` on target `7` (RT)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (9 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `20` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 113 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 436: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '19' has invalid range: start=86, end=78. Clamping end to start.
- ⚠️ Action 'Action_None' range [83-129] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-151] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-239] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-211] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-232] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-137] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-192] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-228] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-217] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-94] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [131-136] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [133-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [139-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-213] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-105] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-202] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-230] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-162] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-113] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [148-158] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-85] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-113] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-120] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-146] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [148-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 175, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [175-239] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-80] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-124] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-202] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-219] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-82] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-87] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-70] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-84] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [133-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [139-162] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-174] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '21' starts at frame 175, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [175-239] for track '21' has 2 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_218'; source metadata written as null.

</details>