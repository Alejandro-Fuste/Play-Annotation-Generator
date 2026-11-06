# Play-Annotation-Generator Annotation Review — OutsideZoneRead_137

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_137`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 113
- **Validation Warnings:** 87
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
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Keep` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `9` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 12 | START | 12 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `9` | 15 | START | 46 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `14` | `13` | 15 | START | 15 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `16` | 15 | START | 15 | 29 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 15 | START | 15 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 15 | START | 15 | 47 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 28 | END | 12 | 28 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `12` | `11` | 31 | START | 31 | 37 |
| ✅ EXACT | `Action_Keep` | QB | `12` | `11` | 38 | START | 38 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `12` | `11` | 63 | START | 63 | 99 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 111 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_SnapReceive` | 12 | 28 | 17 | inferred_complete_timeline |
| `Action_None` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 31 | 37 | 7 | inferred_complete_timeline |
| `Action_Keep` | 38 | 62 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 63 | 99 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 185 | 85 | inferred_complete_timeline |
| `Action_BallCarry` | 198 | 224 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 56 | 45 | inferred_complete_timeline |
| `Action_None` | 58 | 239 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 239 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 239 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 239 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 86 | 75 | inferred_complete_timeline |
| `Action_None` | 89 | 102 | 14 | inferred_complete_timeline |
| `Action_None` | 105 | 108 | 4 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 130 | 13 | inferred_complete_timeline |
| `Action_None` | 132 | 225 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 15 | 66 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 84 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 104 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_None` | 112 | 185 | 74 | inferred_complete_timeline |
| `Action_None` | 198 | 206 | 9 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |
| `Action_None` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 223 | 4 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 15 | 29 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 62 | 111 | 50 | inferred_complete_timeline |
| `Action_None` | 112 | 185 | 74 | inferred_complete_timeline |
| `Action_None` | 188 | 239 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 12 | 24 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 87 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 101 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 15 | 47 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 51 | 55 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 111 | 36 | inferred_complete_timeline |
| `Action_None` | 112 | 239 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 15 | 111 | 97 | inferred_complete_timeline |
| `Action_None` | 112 | 236 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 239 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 60 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 173 | 162 | inferred_complete_timeline |
| `Action_None` | 176 | 185 | 10 | inferred_complete_timeline |
| `Action_None` | 188 | 194 | 7 | inferred_complete_timeline |
| `Action_None` | 196 | 239 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 75 | 64 | inferred_complete_timeline |
| `Action_None` | 107 | 184 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 65 | 54 | inferred_complete_timeline |
| `Action_None` | 67 | 160 | 94 | inferred_complete_timeline |
| `Action_None` | 163 | 168 | 6 | inferred_complete_timeline |
| `Action_None` | 180 | 186 | 7 | inferred_complete_timeline |
| `Action_None` | 188 | 213 | 26 | inferred_complete_timeline |
| `Action_None` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_None` | 225 | 239 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 186 | 175 | inferred_complete_timeline |
| `Action_None` | 188 | 228 | 41 | inferred_complete_timeline |
| `Action_None` | 231 | 239 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 194 | 183 | inferred_complete_timeline |
| `Action_None` | 196 | 204 | 9 | inferred_complete_timeline |
| `Action_None` | 206 | 213 | 8 | inferred_complete_timeline |
| `Action_None` | 216 | 224 | 9 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 229 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 193 | 182 | inferred_complete_timeline |
| `Action_None` | 198 | 239 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 239 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 133 | 122 | inferred_complete_timeline |
| `Action_None` | 135 | 137 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 78–239 | 160 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 80–239 | 160 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 95–184 | 63 | 8 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 146–239 | 72 | 5 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 202–239 | 35 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF3` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [12–28], lower_priority='Action_ZoneBlock' annotated_start=15, effective_Action_ZoneBlock_start=29.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (LT) duration 97 frames exceeds threshold 90 frames [start=15, end=111].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (LG) duration 97 frames exceeds threshold 90 frames [start=15, end=111].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RT) duration 97 frames exceeds threshold 90 frames [start=15, end=111].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 97 frames exceeds threshold 90 frames [start=15, end=111].
- ⚠️ Action 'Action_None' range [12-194] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-204] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-213] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-224] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-239] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-193] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-229] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-133] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-86] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-130] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-225] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [12-24] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-101] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [63-99] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-185] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [198-224] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-160] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-186] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-213] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [15-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-84] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-89] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-239] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-186] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-228] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [15-29] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-185] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-173] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-185] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-194] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-75] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-184] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-60] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-236] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [15-47] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [51-55] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-107] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-239] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-107] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-143] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-152] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-177] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-183] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-212] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-223] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '26' has 1 frames without a visible bounding box.
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

</details>