# Play-Annotation-Generator Annotation Review — SplitZone_93

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_93`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `24` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `16` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 25 | START | 26 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 25 | START | 26 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `13` | `Group` | 25 | START | 26 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 25 | START | 26 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 25 | START | 26 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 25 | START | 26 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 25 | START | 26 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `24` | `Group` | 25 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 25 | START | 26 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 25 | START | 26 | 85 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | Position_Unknown | `21` | `21` | 83 | START | 83 | 87 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `18` | `18` | 86 | START | 86 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 86 | START | 86 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `24` | `22` | 86 | START | 121 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `8` | 86 | START | 86 | 107 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `13` | `13` | 88 | START | 88 | 134 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 92 | END | 83 | 92 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `19` | 99 | START | 99 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `16` | `16` | 112 | START | 112 | 137 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 174 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 26–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 82 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 83 | 92 | 10 | inferred_complete_timeline |
| `Action_None` | 93 | 98 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 99 | 111 | 13 | inferred_complete_timeline |
| `Action_None` | 112 | 239 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 26–239
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 111 | 86 | inferred_complete_timeline |
| `Action_BallCarry` | 112 | 137 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 139 | 200 | 62 | inferred_complete_timeline |
| `Action_BallCarry` | 208 | 231 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 233 | 239 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 26–239
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 87 | 62 | inferred_complete_timeline |
| `Action_SplitBlock` | 88 | 134 | 47 | inferred_complete_timeline |
| `Action_SplitBlock` | 137 | 140 | 4 | inferred_complete_timeline |
| `Action_SplitBlock` | 143 | 174 | 32 | inferred_complete_timeline |
| `Action_None` | 175 | 239 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 26–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 82 | 57 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 26–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 82 | 57 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 26–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 82 | 57 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 26–92
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 85 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 92 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `24`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 121–191
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 121 | 122 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 135 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 174 | 38 | inferred_complete_timeline |
| `Action_None` | 175 | 191 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 26–239
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 85 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 108 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 124 | 8 | inferred_complete_timeline |
| `Action_None` | 200 | 239 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 26–239
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 85 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 107 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 155 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 174 | 10 | inferred_complete_timeline |
| `Action_None` | 175 | 184 | 10 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 195 | 239 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 26–117
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 82 | 57 | inferred_complete_timeline |
| `Action_None` | 83 | 117 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 26–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 82 | 57 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 26–125
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 82 | 57 | inferred_complete_timeline |
| `Action_None` | 83 | 105 | 23 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 26–239
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 82 | 57 | inferred_complete_timeline |
| `Action_None` | 83 | 115 | 33 | inferred_complete_timeline |
| `Action_None` | 121 | 165 | 45 | inferred_complete_timeline |
| `Action_None` | 173 | 239 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 26–239
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 82 | 57 | inferred_complete_timeline |
| `Action_None` | 83 | 142 | 60 | inferred_complete_timeline |
| `Action_None` | 161 | 239 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 26–239
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 82 | 57 | inferred_complete_timeline |
| `Action_None` | 83 | 121 | 39 | inferred_complete_timeline |
| `Action_None` | 131 | 147 | 17 | inferred_complete_timeline |
| `Action_None` | 225 | 239 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 26–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 82 | 57 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 26–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 82 | 57 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 26–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 82 | 57 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 26–218
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 82 | 57 | inferred_complete_timeline |
| `Action_None` | 83 | 218 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 26–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 82 | 57 | inferred_complete_timeline |
| `Action_None` | 83 | 239 | 157 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 26–225 | 182 | 6 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 26–239 | 166 | 9 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 157–239 | 82 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 183–239 | 57 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 193–238 | 44 | 2 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 201–239 | 39 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 205–238 | 13 | 3 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 215–216 | 2 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 218–239 | 22 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `24` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (4 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 188: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [83-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-121] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-147] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-107] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [157-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-184] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-115] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-165] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [88-134] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [137-140] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [143-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-128] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-189] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-225] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [139-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [208-231] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-218] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-239] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-108] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-124] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-34] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [83-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-196] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-122] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-135] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-191] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-208] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-212] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-238] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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