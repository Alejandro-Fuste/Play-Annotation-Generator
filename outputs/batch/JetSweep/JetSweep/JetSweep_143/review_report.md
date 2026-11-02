# Play-Annotation-Generator Annotation Review — JetSweep_143

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_143`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_JetMotion` | WR3 | offense | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | SAF2 | defense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_Toss` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_JetMotion` | WR3 | `20` | `19` | 0 | START | 0 | 63 |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | SAF2 | `20` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 34 | START | 34 | 45 |
| ✅ EXACT | `Action_LeadBlock` | RB | `13` | `12` | 36 | START | 36 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 36 | START | 46 | 89 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `12` | `11` | 36 | START | 36 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 36 | START | 36 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 36 | START | 36 | 47 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 45 | END | 34 | 45 |
| ✅ EXACT | `Action_Toss` | QB | `17` | `16` | 52 | START | 52 | 63 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `20` | `19` | 64 | START | 64 | 175 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 118 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_SnapReceive` | 34 | 45 | 12 | inferred_complete_timeline |
| `Action_None` | 46 | 51 | 6 | inferred_complete_timeline |
| `Action_Toss` | 52 | 63 | 12 | inferred_complete_timeline |
| `Action_None` | 64 | 210 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_LeadBlock` | 36 | 118 | 83 | inferred_complete_timeline |
| `Action_None` | 119 | 210 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 127 | 94 | inferred_complete_timeline |
| `Action_None` | 131 | 134 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 99 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_BallCarry` | 64 | 175 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 148 | 115 | inferred_complete_timeline |
| `Action_None` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_None` | 163 | 210 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 118 | 83 | inferred_complete_timeline |
| `Action_None` | 119 | 210 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_BallSnap` | 34 | 45 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 89 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 98 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 107 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 118 | 9 | inferred_complete_timeline |
| `Action_None` | 119 | 154 | 36 | inferred_complete_timeline |
| `Action_None` | 169 | 210 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 47 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 52 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 36 | 59 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 78 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 118 | 37 | inferred_complete_timeline |
| `Action_None` | 119 | 119 | 1 | inferred_complete_timeline |
| `Action_None` | 122 | 210 | 89 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 82 | 49 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 141 | 108 | inferred_complete_timeline |
| `Action_None` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_None` | 154 | 185 | 32 | inferred_complete_timeline |
| `Action_None` | 202 | 205 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 105 | 72 | inferred_complete_timeline |
| `Action_None` | 107 | 127 | 21 | inferred_complete_timeline |
| `Action_None` | 130 | 210 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 201 | 168 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–92 | 93 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 44–210 | 160 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 58–67 | 8 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 99–210 | 108 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 113–114 | 2 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 119–210 | 74 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 126–210 | 83 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 149–210 | 60 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 166–203 | 24 | 3 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 166–168 | 3 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 174–189 | 8 | 2 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 188–210 | 23 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `21`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 288: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [34–45], lower_priority='Action_ZoneBlock' annotated_start=36, effective_Action_ZoneBlock_start=46.
- ⚠️ Action 'Action_None' range [34-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-99] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-105] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-127] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-141] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-82] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-89] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-98] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-107] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-59] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [70-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 119, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [119-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [64-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-201] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [36-47] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-52] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-46] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-54] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-67] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-191] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-125] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-177] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-190] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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

</details>