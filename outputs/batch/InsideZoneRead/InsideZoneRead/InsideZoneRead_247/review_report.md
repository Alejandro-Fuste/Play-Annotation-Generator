# Play-Annotation-Generator Annotation Review — InsideZoneRead_247

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_247`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 134
- **Validation Warnings:** 138
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | WR2 | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | WR3 | offense | `11` | `10` |
| ✅ EXACT | `Action_ReadDefender` | WR3 | offense | `11` | `10` |
| ✅ EXACT | `Action_Keep` | WR3 | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `11` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 22 |
| ✅ EXACT | `Action_BallSnap` | WR2 | `9` | `8` | 23 | START | 23 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `17` | `16` | 26 | START | 26 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `18` | `17` | 26 | START | 26 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 26 | START | 26 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 26 | START | 26 | 30 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `6` | 26 | START | 26 | 96 |
| ✅ EXACT | `Action_SnapReceive` | WR3 | `11` | `10` | 39 | END | 23 | 39 |
| ✅ EXACT | `Action_ReadDefender` | WR3 | `11` | `10` | 42 | START | 42 | 48 |
| ✅ EXACT | `Action_Keep` | WR3 | `11` | `10` | 49 | START | 49 | 78 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `11` | `10` | 79 | START | 79 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 96 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 37 | 15 | inferred_complete_timeline |
| `Action_None` | 47 | 159 | 113 | inferred_complete_timeline |
| `Action_None` | 162 | 172 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 49 | 27 | inferred_complete_timeline |
| `Action_None` | 51 | 81 | 31 | inferred_complete_timeline |
| `Action_None` | 83 | 119 | 37 | inferred_complete_timeline |
| `Action_None` | 131 | 210 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 210 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 23 | 39 | 17 | inferred_complete_timeline |
| `Action_None` | 40 | 182 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 23 | 39 | 17 | inferred_complete_timeline |
| `Action_None` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 42 | 48 | 7 | inferred_complete_timeline |
| `Action_Keep` | 49 | 78 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 79 | 210 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 97 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 96 | 71 | inferred_complete_timeline |
| `Action_None` | 97 | 210 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 25 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 96 | 71 | inferred_complete_timeline |
| `Action_None` | 97 | 122 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 25 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 30 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 71 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 96 | 21 | inferred_complete_timeline |
| `Action_None` | 97 | 123 | 27 | inferred_complete_timeline |
| `Action_None` | 126 | 210 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 19 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 25 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 64 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 89 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 96 | 1 | inferred_complete_timeline |
| `Action_None` | 97 | 97 | 1 | inferred_complete_timeline |
| `Action_None` | 101 | 115 | 15 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 138 | 4 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_None` | 146 | 159 | 14 | inferred_complete_timeline |
| `Action_None` | 162 | 177 | 16 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 210 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 96 | 71 | inferred_complete_timeline |
| `Action_None` | 97 | 117 | 21 | inferred_complete_timeline |
| `Action_None` | 131 | 210 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 22 | 6 | inferred_complete_timeline |
| `Action_None` | 23 | 68 | 46 | inferred_complete_timeline |
| `Action_None` | 76 | 82 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 190 | 168 | inferred_complete_timeline |
| `Action_None` | 193 | 195 | 3 | inferred_complete_timeline |
| `Action_None` | 198 | 210 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 41 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_None` | 40 | 171 | 132 | inferred_complete_timeline |
| `Action_None` | 173 | 180 | 8 | inferred_complete_timeline |
| `Action_None` | 184 | 186 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 85 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 65 | 43 | inferred_complete_timeline |
| `Action_None` | 72 | 93 | 22 | inferred_complete_timeline |
| `Action_None` | 96 | 100 | 5 | inferred_complete_timeline |
| `Action_None` | 115 | 121 | 7 | inferred_complete_timeline |
| `Action_None` | 137 | 141 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 122 | 100 | inferred_complete_timeline |
| `Action_None` | 124 | 129 | 6 | inferred_complete_timeline |
| `Action_None` | 131 | 136 | 6 | inferred_complete_timeline |
| `Action_None` | 142 | 146 | 5 | inferred_complete_timeline |
| `Action_None` | 148 | 167 | 20 | inferred_complete_timeline |
| `Action_None` | 170 | 210 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 210 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 186 | 164 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 203 | 6 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 139 | 117 | inferred_complete_timeline |
| `Action_None` | 144 | 210 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 97 | 75 | inferred_complete_timeline |
| `Action_None` | 99 | 158 | 60 | inferred_complete_timeline |
| `Action_None` | 160 | 162 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 68–146 | 64 | 5 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 90–209 | 108 | 6 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 94–97 | 4 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 108–210 | 94 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 114–195 | 78 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 124–159 | 28 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 137–210 | 9 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 147–210 | 56 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 156–210 | 55 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 169–210 | 23 | 4 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 175–210 | 36 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 201–210 | 10 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 207–210 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 108 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [23-186] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-203] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-97] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-158] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-65] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-93] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-210] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-182] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-37] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-159] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [79-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-49] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-119] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-171] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-19] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-64] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 97, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [97-97] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-30] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-71] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-96] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-41] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-68] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-72] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-93] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-100] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-146] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-189] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-209] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-121] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-138] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-187] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-195] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-144] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-160] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '35' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_247'; source metadata written as null.

</details>