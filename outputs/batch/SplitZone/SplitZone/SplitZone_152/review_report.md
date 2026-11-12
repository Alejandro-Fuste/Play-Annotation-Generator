# Play-Annotation-Generator Annotation Review — SplitZone_152

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_152`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | DT1 | defense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 20 | START | 21 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 20 | START | 21 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 20 | START | 21 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 20 | START | 21 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 20 | START | 21 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 20 | START | 21 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 20 | START | 21 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 20 | START | 21 | 63 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 61 | START | 61 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `11` | 64 | START | 76 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `13` | `13` | 64 | START | 64 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `15` | `15` | 64 | START | 64 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `3` | `3` | 64 | START | 64 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `9` | 64 | START | 64 | 80 |
| ✅ EXACT | `Action_SplitBlock` | DT1 | `2` | `2` | 67 | START | 67 | 119 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 75 | END | 61 | 75 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `5` | 77 | START | 77 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `4` | 91 | START | 91 | 99 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 167 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 21–359
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 60 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 61 | 75 | 15 | inferred_complete_timeline |
| `Action_None` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 77 | 90 | 14 | inferred_complete_timeline |
| `Action_None` | 91 | 201 | 111 | inferred_complete_timeline |
| `Action_None` | 203 | 235 | 33 | inferred_complete_timeline |
| `Action_None` | 240 | 255 | 16 | inferred_complete_timeline |
| `Action_None` | 257 | 274 | 18 | inferred_complete_timeline |
| `Action_None` | 281 | 302 | 22 | inferred_complete_timeline |
| `Action_None` | 304 | 306 | 3 | inferred_complete_timeline |
| `Action_None` | 308 | 359 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 21–359
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 90 | 70 | inferred_complete_timeline |
| `Action_BallCarry` | 91 | 99 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 104 | 359 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 21–190
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 60 | 40 | inferred_complete_timeline |
| `Action_None` | 61 | 190 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 21–155
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 63 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 121 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 155 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 21–209
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 63 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 142 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_None` | 168 | 191 | 24 | inferred_complete_timeline |
| `Action_None` | 193 | 209 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 21–197
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 60 | 40 | inferred_complete_timeline |
| `Action_BallSnap` | 61 | 75 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 98 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 167 | 68 | inferred_complete_timeline |
| `Action_None` | 168 | 197 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 21–201
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 63 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 86 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 145 | 58 | inferred_complete_timeline |
| `Action_None` | 171 | 201 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 21–198
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 63 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 80 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 167 | 83 | inferred_complete_timeline |
| `Action_None` | 168 | 171 | 4 | inferred_complete_timeline |
| `Action_None` | 197 | 198 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 21–205
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 60 | 40 | inferred_complete_timeline |
| `Action_None` | 61 | 71 | 11 | inferred_complete_timeline |
| `Action_None` | 124 | 139 | 16 | inferred_complete_timeline |
| `Action_None` | 149 | 163 | 15 | inferred_complete_timeline |
| `Action_None` | 168 | 196 | 29 | inferred_complete_timeline |
| `Action_None` | 204 | 205 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 21–195
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 60 | 40 | inferred_complete_timeline |
| `Action_None` | 61 | 87 | 27 | inferred_complete_timeline |
| `Action_None` | 99 | 139 | 41 | inferred_complete_timeline |
| `Action_None` | 148 | 156 | 9 | inferred_complete_timeline |
| `Action_None` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 171 | 195 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 21–119
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 66 | 46 | inferred_complete_timeline |
| `Action_SplitBlock` | 67 | 119 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 21–74
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 60 | 40 | inferred_complete_timeline |
| `Action_None` | 61 | 74 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 21–122
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 60 | 40 | inferred_complete_timeline |
| `Action_None` | 61 | 117 | 57 | inferred_complete_timeline |
| `Action_None` | 119 | 122 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 21–96
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 60 | 40 | inferred_complete_timeline |
| `Action_None` | 61 | 96 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 21–112
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 60 | 40 | inferred_complete_timeline |
| `Action_None` | 61 | 112 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 21–143
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 60 | 40 | inferred_complete_timeline |
| `Action_None` | 61 | 137 | 77 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 21–237
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 60 | 40 | inferred_complete_timeline |
| `Action_None` | 61 | 194 | 134 | inferred_complete_timeline |
| `Action_None` | 198 | 229 | 32 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 237 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 122–359 | 237 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 136–359 | 222 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 138–213 | 71 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 139–202 | 64 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 140–266 | 126 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 153–161 | 9 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 156–359 | 204 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 157–207 | 27 | 4 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 159–169 | 7 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 179–359 | 175 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 185–204 | 20 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 196–359 | 164 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 199–359 | 146 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 226–359 | 132 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 255–359 | 100 | 3 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 292–359 | 56 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 72 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 306: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (RG) duration 104 frames exceeds threshold 90 frames [start=64, end=167].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 104 frames exceeds threshold 90 frames [start=64, end=167].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (C) duration 104 frames exceeds threshold 90 frames [start=64, end=167].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [61–75], lower_priority='Action_ZoneBlock' annotated_start=64, effective_Action_ZoneBlock_start=76.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (LG) duration 104 frames exceeds threshold 90 frames [start=64, end=167].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (LT) duration 92 frames exceeds threshold 90 frames [start=64, end=155].
- ⚠️ Action 'Action_None' range [61-117] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-87] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-139] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-156] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-195] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [67-119] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-86] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-145] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-201] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [91-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-201] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-235] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-255] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-274] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-302] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-306] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-112] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-80] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [85-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-197] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-194] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [161-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-191] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-209] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-121] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-71] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-163] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-196] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-137] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-359] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-359] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-213] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-202] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-149] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-266] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-161] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-193] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-207] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-163] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-258] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-204] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-359] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-221] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-245] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-359] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-353] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.

</details>