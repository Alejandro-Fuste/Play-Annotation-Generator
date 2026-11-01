# Play-Annotation-Generator Annotation Review — InsideZoneRead_345

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_345`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 95
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
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Keep` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `17` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 8 | START | 8 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `11` | 11 | START | 11 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `15` | 11 | START | 11 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 11 | START | 26 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `22` | `21` | 11 | START | 11 | 96 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `3` | 11 | START | 11 | 104 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 25 | END | 8 | 25 |
| ✅ EXACT | `Action_ReadDefender` | QB | `14` | `13` | 29 | START | 29 | 35 |
| ✅ EXACT | `Action_Keep` | QB | `14` | `13` | 36 | START | 36 | 59 |
| ✅ EXACT | `Action_BallCarry` | QB | `14` | `13` | 60 | START | 60 | 210 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 104 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 8 | 25 | 18 | inferred_complete_timeline |
| `Action_None` | 26 | 28 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 29 | 35 | 7 | inferred_complete_timeline |
| `Action_Keep` | 36 | 59 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 60 | 210 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 189 | 182 | inferred_complete_timeline |
| `Action_None` | 193 | 210 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 137 | 130 | inferred_complete_timeline |
| `Action_None` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_None` | 145 | 148 | 4 | inferred_complete_timeline |
| `Action_None` | 150 | 210 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 96 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_None` | 105 | 136 | 32 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_None` | 150 | 190 | 41 | inferred_complete_timeline |
| `Action_None` | 193 | 195 | 3 | inferred_complete_timeline |
| `Action_None` | 198 | 210 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 32 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 39 | 46 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 50 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 8 | 25 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 81 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 104 | 18 | inferred_complete_timeline |
| `Action_None` | 105 | 190 | 86 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 31 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 104 | 70 | inferred_complete_timeline |
| `Action_None` | 105 | 136 | 32 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 162 | 210 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 11 | 104 | 94 | inferred_complete_timeline |
| `Action_None` | 105 | 139 | 35 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_None` | 163 | 210 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 136 | 129 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 150 | 159 | 10 | inferred_complete_timeline |
| `Action_None` | 161 | 210 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 136 | 129 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 149 | 190 | 42 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 113 | 106 | inferred_complete_timeline |
| `Action_None` | 117 | 127 | 11 | inferred_complete_timeline |
| `Action_None` | 132 | 136 | 5 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_None` | 150 | 183 | 34 | inferred_complete_timeline |
| `Action_None` | 185 | 191 | 7 | inferred_complete_timeline |
| `Action_None` | 193 | 209 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 136 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 99 | 92 | inferred_complete_timeline |
| `Action_None` | 107 | 141 | 35 | inferred_complete_timeline |
| `Action_None` | 146 | 210 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 172 | 165 | inferred_complete_timeline |
| `Action_None` | 176 | 210 | 35 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 57–65 | 4 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 57–59 | 3 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 67–210 | 103 | 8 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 73–76 | 4 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 168–210 | 39 | 3 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (RT) duration 94 frames exceeds threshold 90 frames [start=11, end=104].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (RG) duration 94 frames exceeds threshold 90 frames [start=11, end=104].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (C) duration 94 frames exceeds threshold 90 frames [start=11, end=104].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [8–25], lower_priority='Action_ZoneBlock' annotated_start=11, effective_Action_ZoneBlock_start=26.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LT) duration 94 frames exceeds threshold 90 frames [start=11, end=104].
- ⚠️ Action 'Action_None' range [8-136] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-190] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-137] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-104] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-139] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-159] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-210] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-99] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-141] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-113] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-127] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-183] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-209] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-136] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-189] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-32] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [39-46] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-50] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [60-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-31] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-136] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-210] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-172] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-81] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [83-84] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-190] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [11-96] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-136] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-190] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-77] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-188] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-199] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-76] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '27' has 1 frames without a visible bounding box.
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

</details>