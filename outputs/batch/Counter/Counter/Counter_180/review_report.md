# Play-Annotation-Generator Annotation Review — Counter_180

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_180`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DE1 | defense | `11` | `10` |
| ✅ EXACT | `Action_DownBlock` | DE1 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | WR4 | offense | `8` | `7` |
| ✅ EXACT | `Action_PullLeadBlock` | WR1 | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | DT2 | defense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | DT3 | defense | `3` | `2` |
| ✅ EXACT | `Action_Handoff` | DT3 | defense | `3` | `2` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DT2 | defense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 94 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `8` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 104 |
| ✅ EXACT | `Action_BallSnap` | DE1 | `11` | `10` | 105 | START | 105 | 106 |
| ✅ EXACT | `Action_DownBlock` | DE1 | `11` | `10` | 107 | START | 107 | 185 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `13` | `12` | 107 | START | 107 | 181 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | WR4 | `8` | `7` | 107 | START | 107 | 123 |
| ✅ EXACT | `Action_PullLeadBlock` | WR1 | `2` | `1` | 107 | START | 107 | 183 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | DT2 | `4` | `3` | 112 | START | 112 | 121 |
| ✅ EXACT | `Action_SnapReceive` | DT3 | `3` | `2` | 119 | END | 105 | 119 |
| ✅ EXACT | `Action_Handoff` | DT3 | `3` | `2` | 129 | START | 129 | 140 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DT2 | `4` | `3` | 148 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 185 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 94–127
- **Visible Samples:** 15

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 101 | 5 | inferred_complete_timeline |
| `Action_None` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_None` | 124 | 127 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 131 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 107 | 183 | 77 | inferred_complete_timeline |
| `Action_None` | 186 | 299 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 161 | 57 | inferred_complete_timeline |
| `Action_None` | 164 | 177 | 14 | inferred_complete_timeline |
| `Action_None` | 179 | 299 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 254 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 106 | 65 | inferred_complete_timeline |
| `Action_PullBlock` | 107 | 123 | 17 | inferred_complete_timeline |
| `Action_PullBlock` | 129 | 144 | 16 | inferred_complete_timeline |
| `Action_PullBlock` | 147 | 171 | 25 | inferred_complete_timeline |
| `Action_PullBlock` | 174 | 185 | 12 | inferred_complete_timeline |
| `Action_None` | 186 | 269 | 84 | inferred_complete_timeline |
| `Action_None` | 272 | 286 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 181 | 75 | inferred_complete_timeline |
| `Action_DownBlock` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_None` | 186 | 263 | 78 | inferred_complete_timeline |
| `Action_None` | 265 | 299 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 161–167
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 161 | 167 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_BallSnap` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 107 | 185 | 79 | inferred_complete_timeline |
| `Action_None` | 186 | 299 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 112 | 121 | 10 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 125 | 140 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_SnapReceive` | 105 | 119 | 15 | inferred_complete_timeline |
| `Action_None` | 120 | 128 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 129 | 140 | 12 | inferred_complete_timeline |
| `Action_None` | 148 | 151 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 299 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 299 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 93 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_None` | 105 | 299 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 168 | 64 | inferred_complete_timeline |
| `Action_None` | 172 | 209 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_None` | 105 | 173 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `19` | Position_Unknown | Team_Unknown | 140–190 | 43 | 3 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 165–299 | 88 | 2 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 170–299 | 124 | 3 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 174–299 | 126 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 185–299 | 115 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 202–299 | 97 | 2 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 211–299 | 89 | 1 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 238–299 | 61 | 2 | Undefined position; Undefined team |
| `24` | `38` | Position_Unknown | Team_Unknown | 268–289 | 12 | 3 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 268–273 | 6 | 1 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 270–299 | 30 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 272–299 | 28 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 274–299 | 26 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 282–299 | 18 | 1 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `8` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `4` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `4` (DT2)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 362: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Track ID '22' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '20' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '3' has invalid range: start=148, end=140. Clamping end to start.
- ⚠️ Action 'Action_None' range [105-161] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-177] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-299] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [107-183] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [129-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [112-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [125-140] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-173] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [107-123] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [129-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [147-171] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [174-185] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-286] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-254] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-209] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-299] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-131] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [107-181] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [183-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-263] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-93] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-156] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-183] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-167] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-248] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-273] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-289] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-273] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-299] for track '31' has 1 frames without a visible bounding box.
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