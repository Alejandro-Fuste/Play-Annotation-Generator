# Play-Annotation-Generator Annotation Review — SplitZone_104

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_104`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 110
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_BlockSecondLevel` | OLB1 | defense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `0` | `Group` | 5 | START | 6 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 5 | START | 6 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 5 | START | 6 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 5 | START | 11 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 5 | START | 6 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 5 | START | 6 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `5` | `Group` | 5 | START | 6 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 5 | START | 6 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 5 | START | 6 | 91 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 89 | START | 89 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `11` | `11` | 92 | START | 92 | 101 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `17` | `16` | 92 | START | 104 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `3` | 92 | START | 92 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `4` | 92 | START | 92 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `9` | `9` | 92 | START | 92 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `5` | `5` | 96 | START | 96 | 126 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 103 | END | 89 | 103 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 105 | START | 105 | 115 |
| ✅ EXACT | `Action_BlockSecondLevel` | OLB1 | `6` | `6` | 109 | START | 109 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `7` | 116 | START | 116 | 168 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 200 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 6–173
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 88 | 83 | inferred_complete_timeline |
| `Action_SnapReceive` | 89 | 103 | 15 | inferred_complete_timeline |
| `Action_None` | 104 | 104 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 105 | 115 | 11 | inferred_complete_timeline |
| `Action_None` | 116 | 125 | 10 | inferred_complete_timeline |
| `Action_None` | 131 | 173 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 115 | 110 | inferred_complete_timeline |
| `Action_BallCarry` | 116 | 168 | 53 | inferred_complete_timeline |
| `Action_BallCarry` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 186 | 188 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 193 | 244 | 52 | inferred_complete_timeline |
| `Action_BallCarry` | 249 | 299 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 6–136
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 88 | 83 | inferred_complete_timeline |
| `Action_None` | 89 | 136 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 95 | 90 | inferred_complete_timeline |
| `Action_SplitBlock` | 96 | 126 | 31 | inferred_complete_timeline |
| `Action_SplitBlock` | 137 | 145 | 9 | inferred_complete_timeline |
| `Action_SplitBlock` | 148 | 200 | 53 | inferred_complete_timeline |
| `Action_None` | 201 | 299 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 91 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 101 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 166 | 63 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 200 | 24 | inferred_complete_timeline |
| `Action_None` | 201 | 299 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 6–286
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 91 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 115 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 130 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 200 | 54 | inferred_complete_timeline |
| `Action_None` | 201 | 222 | 22 | inferred_complete_timeline |
| `Action_None` | 227 | 286 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 11–143
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 12 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 89 | 103 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 143 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 6–135
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 91 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 119 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 125 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 135 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 6–229
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 91 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 137 | 46 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 200 | 59 | inferred_complete_timeline |
| `Action_None` | 201 | 229 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 88 | 83 | inferred_complete_timeline |
| `Action_None` | 89 | 101 | 13 | inferred_complete_timeline |
| `Action_None` | 117 | 276 | 160 | inferred_complete_timeline |
| `Action_None` | 286 | 299 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 6–155
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 88 | 83 | inferred_complete_timeline |
| `Action_None` | 89 | 155 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 6–124
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 88 | 83 | inferred_complete_timeline |
| `Action_None` | 89 | 124 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 108 | 103 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 109 | 200 | 92 | inferred_complete_timeline |
| `Action_None` | 201 | 223 | 23 | inferred_complete_timeline |
| `Action_None` | 227 | 299 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 6–152
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 88 | 83 | inferred_complete_timeline |
| `Action_None` | 89 | 152 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 6–212
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 88 | 83 | inferred_complete_timeline |
| `Action_None` | 89 | 160 | 72 | inferred_complete_timeline |
| `Action_None` | 169 | 184 | 16 | inferred_complete_timeline |
| `Action_None` | 198 | 212 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 88 | 83 | inferred_complete_timeline |
| `Action_None` | 89 | 167 | 79 | inferred_complete_timeline |
| `Action_None` | 170 | 192 | 23 | inferred_complete_timeline |
| `Action_None` | 206 | 266 | 61 | inferred_complete_timeline |
| `Action_None` | 269 | 297 | 29 | inferred_complete_timeline |
| `Action_None` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 6–90 | 16 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 132–194 | 50 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 167–198 | 28 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 169–191 | 23 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 179–299 | 119 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 184–264 | 60 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 185–206 | 22 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 185–269 | 65 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 186–299 | 114 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 196–299 | 103 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 201–221 | 21 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 202–257 | 56 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 222–265 | 44 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 224–299 | 58 | 3 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 246–299 | 54 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `17` (C): Annotated start 92 != Inferred start 104
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 210: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LG) duration 109 frames exceeds threshold 90 frames [start=92, end=200].
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '6' (OLB1) duration 92 frames exceeds threshold 90 frames [start=109, end=200].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 109 frames exceeds threshold 90 frames [start=92, end=200].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (LT) duration 109 frames exceeds threshold 90 frames [start=92, end=200].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [89–103], lower_priority='Action_ZoneBlock' annotated_start=92, effective_Action_ZoneBlock_start=104.
- ⚠️ Action 'Action_None' range [89-136] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-160] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-184] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-212] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-130] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-134] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [143-144] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-200] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-286] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-119] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-125] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [127-135] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [96-126] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [137-145] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [148-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-223] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [116-168] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [176-177] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [186-188] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [193-244] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-101] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-276] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-137] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-229] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-166] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-124] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-167] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-192] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-266] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-297] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-155] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-12] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-55] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-12] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-143] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-176] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-198] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-191] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-216] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-260] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-249] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-264] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-206] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-194] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-215] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-243] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-223] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-221] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-257] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-265] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-254] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>