# Play-Annotation-Generator Annotation Review — InsideZoneRead_325

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_325`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 129
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 104
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Keep` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `2` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 14 | START | 14 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `16` | 17 | START | 17 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 17 | START | 27 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `19` | `18` | 17 | START | 17 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 17 | START | 17 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `22` | `21` | 17 | START | 17 | 43 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 26 | END | 14 | 26 |
| ✅ EXACT | `Action_ReadDefender` | QB | `7` | `6` | 31 | START | 31 | 38 |
| ✅ EXACT | `Action_Keep` | QB | `7` | `6` | 39 | START | 39 | 57 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `19` | `18` | 49 | START | 49 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `7` | `6` | 58 | START | 58 | 190 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 87 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_SnapReceive` | 14 | 26 | 13 | inferred_complete_timeline |
| `Action_None` | 27 | 30 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 31 | 38 | 8 | inferred_complete_timeline |
| `Action_Keep` | 39 | 57 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 58 | 190 | 133 | inferred_complete_timeline |
| `Action_BallCarry` | 193 | 196 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 39 | 26 | inferred_complete_timeline |
| `Action_None` | 44 | 130 | 87 | inferred_complete_timeline |
| `Action_None` | 133 | 137 | 5 | inferred_complete_timeline |
| `Action_None` | 144 | 146 | 3 | inferred_complete_timeline |
| `Action_None` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_None` | 158 | 173 | 16 | inferred_complete_timeline |
| `Action_None` | 177 | 210 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 139 | 126 | inferred_complete_timeline |
| `Action_None` | 141 | 210 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 41 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 48 | 48 | 1 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 49 | 69 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 76 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_None` | 88 | 97 | 10 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 106 | 210 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_BallSnap` | 14 | 26 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 27 | 32 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 87 | 71 | inferred_complete_timeline |
| `Action_None` | 88 | 121 | 34 | inferred_complete_timeline |
| `Action_None` | 126 | 130 | 5 | inferred_complete_timeline |
| `Action_None` | 132 | 136 | 5 | inferred_complete_timeline |
| `Action_None` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_None` | 151 | 154 | 4 | inferred_complete_timeline |
| `Action_None` | 156 | 159 | 4 | inferred_complete_timeline |
| `Action_None` | 161 | 173 | 13 | inferred_complete_timeline |
| `Action_None` | 177 | 210 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 43 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 60 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 87 | 24 | inferred_complete_timeline |
| `Action_None` | 88 | 137 | 50 | inferred_complete_timeline |
| `Action_None` | 143 | 147 | 5 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 157 | 171 | 15 | inferred_complete_timeline |
| `Action_None` | 177 | 210 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 137 | 124 | inferred_complete_timeline |
| `Action_None` | 141 | 173 | 33 | inferred_complete_timeline |
| `Action_None` | 175 | 210 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 140 | 127 | inferred_complete_timeline |
| `Action_None` | 143 | 210 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 45 | 32 | inferred_complete_timeline |
| `Action_None` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_None` | 57 | 58 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 79 | 66 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 102 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 87 | 74 | inferred_complete_timeline |
| `Action_None` | 91 | 107 | 17 | inferred_complete_timeline |
| `Action_None` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_None` | 127 | 196 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 107 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 109 | 96 | inferred_complete_timeline |
| `Action_None` | 113 | 137 | 25 | inferred_complete_timeline |
| `Action_None` | 140 | 210 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 193 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 100 | 87 | inferred_complete_timeline |
| `Action_None` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_None` | 106 | 138 | 33 | inferred_complete_timeline |
| `Action_None` | 142 | 155 | 14 | inferred_complete_timeline |
| `Action_None` | 157 | 210 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–108 | 19 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 78–210 | 94 | 8 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 101–210 | 98 | 5 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 113–210 | 85 | 4 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 127–210 | 67 | 6 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 133–136 | 4 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 147–210 | 63 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 177–179 | 3 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 184–205 | 18 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 199–200 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 100 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [14–26], lower_priority='Action_ZoneBlock' annotated_start=17, effective_Action_ZoneBlock_start=27.
- ⚠️ Action 'Action_None' range [14-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-107] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-87] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-196] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [58-190] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [193-196] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-45] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-51] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-137] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-173] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-140] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-109] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-210] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-79] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-138] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-155] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-193] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-76] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-97] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [27-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-41] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [49-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-130] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-173] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-87] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-121] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-43] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-60] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-137] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-171] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-108] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-94] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-119] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-130] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-173] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-137] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-147] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-193] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-205] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '31' has 1 frames without a visible bounding box.
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

</details>