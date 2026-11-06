# Play-Annotation-Generator Annotation Review — OutsideZoneRead_109

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_109`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 88
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `20` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Keep` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 8 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `17` | `16` | 9 | START | 9 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 12 | START | 12 | 15 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `17` | `16` | 12 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `18` | 12 | START | 12 | 13 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `20` | 12 | START | 12 | 12 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | LG | `22` | `21` | 12 | START | 21 | 87 |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | C | `17` | `16` | 20 | START | 27 | 87 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 26 | END | 9 | 26 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `5` | `4` | 30 | START | 30 | 32 |
| ✅ EXACT | `Action_Keep` | QB | `5` | `4` | 33 | START | 33 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `5` | `4` | 50 | START | 50 | 74 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 87 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_SnapReceive` | 9 | 26 | 18 | inferred_complete_timeline |
| `Action_None` | 27 | 29 | 3 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 30 | 32 | 3 | inferred_complete_timeline |
| `Action_Keep` | 33 | 49 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 50 | 74 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 78 | 210 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 105 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 189 | 181 | inferred_complete_timeline |
| `Action_None` | 192 | 210 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 16 | 8 | inferred_complete_timeline |
| `Action_None` | 20 | 44 | 25 | inferred_complete_timeline |
| `Action_None` | 49 | 60 | 12 | inferred_complete_timeline |
| `Action_None` | 63 | 146 | 84 | inferred_complete_timeline |
| `Action_None` | 148 | 210 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 12 | 12 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 46 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 50 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 87 | 67 | inferred_complete_timeline |
| `Action_None` | 90 | 201 | 112 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_BallSnap` | 9 | 20 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 22 | 24 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 27 | 87 | 61 | inferred_complete_timeline |
| `Action_None` | 88 | 210 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–30
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 30 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–40
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 12 | 15 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 40 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 13 | 5 | inferred_complete_timeline |
| `Action_None` | 21 | 61 | 41 | inferred_complete_timeline |
| `Action_None` | 70 | 82 | 13 | inferred_complete_timeline |
| `Action_None` | 87 | 90 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 61 | 53 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 77 | 160 | 84 | inferred_complete_timeline |
| `Action_None` | 174 | 210 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 13 | 5 | inferred_complete_timeline |
| `Action_None` | 21 | 26 | 6 | inferred_complete_timeline |
| `Action_None` | 28 | 202 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 13 | 5 | inferred_complete_timeline |
| `Action_None` | 21 | 63 | 43 | inferred_complete_timeline |
| `Action_None` | 65 | 84 | 20 | inferred_complete_timeline |
| `Action_None` | 88 | 129 | 42 | inferred_complete_timeline |
| `Action_None` | 131 | 210 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 102 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 210 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 97 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 159 | 151 | inferred_complete_timeline |
| `Action_None` | 167 | 210 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 161 | 153 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 190 | 17 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 210 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 207 | 199 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 35–210 | 174 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 53–210 | 144 | 4 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 76–210 | 134 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 90–105 | 16 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 109–210 | 102 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 116–210 | 95 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 119–210 | 89 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 141–210 | 70 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `17` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `22` (LG): Annotated start 12 != Inferred start 21
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `17` (C): Annotated start 20 != Inferred start 27
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [9–26], lower_priority='Action_ZoneBlock' annotated_start=12, effective_Action_ZoneBlock_start=27.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [9–26], lower_priority='Action_BlockSecondLevel' annotated_start=20, effective_Action_BlockSecondLevel_start=27.
- ⚠️ Action 'Action_None' range [9-189] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-105] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-207] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-159] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [50-74] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [78-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-161] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-190] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [12-15] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-40] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-61] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-160] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-97] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-13] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-13] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-202] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [9-20] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [22-24] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-16] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-60] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-146] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [12-13] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-30] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-13] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-82] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '20' starts at frame 12, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [12-12] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-46] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-50] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-201] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-36] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-80] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-93] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-126] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-106] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-105] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-126] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '29' has 1 frames without a visible bounding box.
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

</details>