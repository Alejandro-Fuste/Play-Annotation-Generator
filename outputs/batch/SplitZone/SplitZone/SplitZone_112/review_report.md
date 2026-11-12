# Play-Annotation-Generator Annotation Review — SplitZone_112

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_112`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `11` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 8 | START | 9 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 8 | START | 9 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 8 | START | 9 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `13` | `Group` | 8 | START | 9 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 8 | START | 9 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 8 | START | 9 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 8 | START | 9 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 8 | START | 9 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 8 | START | 9 | 27 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 83 | START | 83 | 99 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `1` | 86 | START | 86 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `12` | 86 | START | 86 | 100 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `14` | 86 | START | 100 | 191 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `4` | 86 | START | 86 | 136 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `9` | 86 | START | 86 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `13` | `13` | 89 | START | 89 | 127 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 99 | END | 83 | 99 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 103 | START | 103 | 115 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `1` | `1` | 115 | START | 115 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `11` | `11` | 116 | START | 116 | 123 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 227 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 9–222
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 82 | 74 | inferred_complete_timeline |
| `Action_SnapReceive` | 83 | 99 | 17 | inferred_complete_timeline |
| `Action_None` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 103 | 115 | 13 | inferred_complete_timeline |
| `Action_None` | 116 | 124 | 9 | inferred_complete_timeline |
| `Action_None` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_None` | 131 | 133 | 3 | inferred_complete_timeline |
| `Action_None` | 135 | 222 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 9–170
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 115 | 107 | inferred_complete_timeline |
| `Action_BallCarry` | 116 | 123 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 129 | 143 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 145 | 162 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 170 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 9–101
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 13 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 82 | 40 | inferred_complete_timeline |
| `Action_None` | 83 | 101 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 9–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 88 | 80 | inferred_complete_timeline |
| `Action_SplitBlock` | 89 | 127 | 39 | inferred_complete_timeline |
| `Action_SplitBlock` | 133 | 151 | 19 | inferred_complete_timeline |
| `Action_SplitBlock` | 157 | 227 | 71 | inferred_complete_timeline |
| `Action_None` | 228 | 269 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 9–201
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 85 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 114 | 29 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 115 | 201 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 9–201
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 85 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 100 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 109 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 122 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 127 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 201 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 9–191
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 82 | 74 | inferred_complete_timeline |
| `Action_BallSnap` | 83 | 99 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 191 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 9–172
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 27 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 85 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 172 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 9–136
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 85 | 77 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 136 | 51 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 9–155
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 41 | 33 | inferred_complete_timeline |
| `Action_None` | 90 | 155 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 9–183
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 27 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 82 | 49 | inferred_complete_timeline |
| `Action_None` | 83 | 144 | 62 | inferred_complete_timeline |
| `Action_None` | 158 | 183 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 46–146
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 46 | 82 | 37 | inferred_complete_timeline |
| `Action_None` | 83 | 103 | 21 | inferred_complete_timeline |
| `Action_None` | 108 | 146 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–169
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 82 | 74 | inferred_complete_timeline |
| `Action_None` | 83 | 169 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 9–196
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 68 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 82 | 10 | inferred_complete_timeline |
| `Action_None` | 83 | 94 | 12 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 151 | 34 | inferred_complete_timeline |
| `Action_None` | 158 | 196 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 9–187
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 82 | 74 | inferred_complete_timeline |
| `Action_None` | 83 | 187 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 9–254
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 82 | 74 | inferred_complete_timeline |
| `Action_None` | 83 | 254 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 9–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 31 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 82 | 50 | inferred_complete_timeline |
| `Action_None` | 83 | 269 | 187 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 9–21 | 13 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 132–174 | 38 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 136–217 | 82 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 154–168 | 15 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 158–269 | 112 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 158–191 | 34 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 160–250 | 91 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 166–189 | 24 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 172–205 | 34 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 180–269 | 90 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 186–269 | 84 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 188–202 | 15 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 189–233 | 45 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 253–255 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (5 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 86 != Inferred start 100
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (LG) duration 116 frames exceeds threshold 90 frames [start=86, end=201].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 106 frames exceeds threshold 90 frames [start=86, end=191].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [83–99], lower_priority='Action_ZoneBlock' annotated_start=86, effective_Action_ZoneBlock_start=100.
- ⚠️ Action 'Action_None' range [83-254] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [115-201] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-187] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-68] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-82] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-94] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-151] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-196] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-27] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-82] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-144] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-183] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-41] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-155] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-31] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-269] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-124] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-222] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-27] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [116-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [129-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [145-162] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-85] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-100] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [102-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [111-122] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [89-127] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [133-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [157-227] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-191] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-13] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-21] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-146] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-167] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-217] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-168] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-191] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-250] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-189] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-205] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-269] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-202] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-233] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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